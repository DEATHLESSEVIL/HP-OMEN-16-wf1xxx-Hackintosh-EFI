#!/usr/bin/env python3
from pathlib import Path
import plistlib
import tempfile,zipfile,sys
repo=Path(__file__).resolve().parent
archive=Path(sys.argv[1]) if len(sys.argv)>1 else repo/"EFI.zip"
stage=tempfile.TemporaryDirectory()
with zipfile.ZipFile(archive) as z:z.extractall(stage.name)
root=Path(stage.name)/"EFI/OC"
d=plistlib.loads((root/"config.plist").read_bytes())
g=d["PlatformInfo"]["Generic"]
assert all(not g[k] for k in ["SystemSerialNumber","MLB","SystemUUID"]),"Private machine identity must not be published"
assert not any(g["ROM"]),"ROM must stay cleared in the public snapshot"
for item in d["Kernel"]["Add"]:
 if item["Enabled"]:
  base=root/"Kexts"/item["BundlePath"]
  assert (base/item["PlistPath"]).is_file(),str(base)
  if item["ExecutablePath"]:assert (base/item["ExecutablePath"]).is_file(),str(base)
for item in d["UEFI"]["Drivers"]:
 if item["Enabled"]:assert (root/"Drivers"/item["Path"]).is_file(),item["Path"]
for item in d["ACPI"]["Add"]:
 if item["Enabled"]:assert (root/"ACPI"/item["Path"]).is_file(),item["Path"]
print("Public identity is blank; enabled ACPI, drivers and kext paths exist.")
