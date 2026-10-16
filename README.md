# HP OMEN 16-wf1xxx — macOS Tahoe EFI

This is the EFI from my HP OMEN 16-wf1xxx with an i7-14650HX and RTX 4060 Laptop GPU. It boots macOS Tahoe 26.7.1. It is a record of this laptop’s setup, not a universal OMEN EFI.

Download **EFI.zip** from this repository’s Releases page and extract it to get the EFI folder. `config.example.plist` is the same sanitized config, available separately for review. The serial number, MLB, UUID and ROM have been removed. Fill in your own before using it.

## Hardware

| Part | Hardware |
| --- | --- |
| Laptop / board | HP OMEN 16-wf1xxx / 103C:8C78 |
| BIOS | F.15 |
| CPU | Intel Core i7-14650HX, 16 cores |
| GPU | NVIDIA GeForce RTX 4060 Laptop GPU, 8 GB |
| Memory | 16 GB DDR5-5600 |
| Wi-Fi | Intel AX211 |
| Bluetooth | Intel USB Bluetooth, 8087:0033 |
| Ethernet | Realtek RTL8168/8111 family |
| Audio | Realtek ALC245 / Intel SST controller |
| Trackpad | ELAN07C6, I2C HID |
| Keyboard | PS/2 |
| SMBIOS | MacBookPro16,4 |
| OpenCore | 1.0.9 DEBUG, build 2026-10-10 |

## What works

These results are from this laptop, last checked on 16 October 2026.

| Feature | Notes |
| --- | --- |
| Booting macOS | Tahoe 26.7.1, build 25G241 |
| NVIDIA graphics acceleration | Working with the separately installed NullMoth driver setup. See the graphics note below. |
| Internal speakers | Working. Audio still has a stability issue noted below. |
| iMessage | Working with this machine’s own SMBIOS identity. Ethernet is preferred for the initial sign-in; after activation, Wi-Fi can be used. |
| Wired headphones | Output through the 3.5 mm jack works. |
| Ethernet | Working through the onboard Realtek controller. |
| USB | All USB ports work for USB devices. Thunderbolt and external display support are separate. |
| Battery indicator | Working. Battery runtime has not been measured. |
| OMEN button | Mapped to open Omen Control. Requires the app to be installed with its background service running. |
| AirPlay audio | Audio can be sent from a real Mac to this laptop and from this laptop to a real Mac. This does not establish AirPlay display support. |
| Wi-Fi | Built-in AX211; AirportItlwm is enabled, itlwm is disabled. |
| Bluetooth | Working. AirDrop does not work. |
| Trackpad | Working through VoodooI2C/VoodooI2CHID and the 7A4C matching injector. Individual gestures have not been listed separately. |
| Brightness controls | Working on the internal display. |
| Keyboard | Normal typing and navigation keys work with the current PS/2 mapping. |
| Manual fan control | CPU and GPU readback/control through OmenFanBridge 0.4.0 and Omen Control Alpha 1.0V. |

## What does not work

| Feature | Current state |
| --- | --- |
| External displays | Not working. Individual HDMI/USB-C outputs have not been recorded separately. |
| AirDrop | Not working. |
| Handoff | Not working. |
| Thunderbolt 4 | Drivers are not loaded; Thunderbolt functionality is not enabled or verified. |
| Webcam | Not working. |
| Sleep / wake | Not working reliably. Do not rely on lid-close sleep. |

### Audio stability

Speaker output working does not mean the audio stack is stable. A captured panic occurred in `coreaudiod`, through `IOAudioFamily`, `AppleHDA` and `DspFuncLib`, ending in `vecLib`’s `_vDSP_conv_AVX2` during input processing. The cause has not been isolated. Microphone/input use still needs testing; the panic has not been shown to come from the fan driver.

### Not tested separately

Battery runtime, USB-C alternate modes, DRM playback, FaceTime and Continuity features not listed above have not been verified for this export. A loaded kext is not treated as proof that a device works.

## Graphics dependency

The RTX 4060 is using a separate NullMoth graphics setup on this machine. Those system-installed drivers and patches are **not** included here. Copying this EFI alone does not install NVIDIA acceleration, and this is not a claim of stock macOS support for the GPU. Keep the driver versions and installation details with your own recovery notes before changing macOS or graphics settings.

## Boot picker

OpenCanopy is enabled with `Acidanthera\GoldenGate`. Kernel verbose boot is off. OpenCore file logging remains enabled, but console logging is disabled. These picker changes were applied and validated; their next-boot appearance has not yet been confirmed separately.

## Before using the EFI

1. Keep a bootable recovery USB and a copy of your working EFI.
2. Compare your board, BIOS and devices with the hardware table. A similar OMEN model name does not establish compatibility.
3. Generate your own MacBookPro16,4 serial, MLB and UUID, and set your own six-byte ROM under `PlatformInfo → Generic`. Do not copy identifiers from a real Mac or publish your filled-in config.
4. Review the ACPI tables, CPU patches, graphics arguments, USB setup and audio layout. This export retains the working machine’s DSDT and board-specific patches; they are not generic SSDTs for every OMEN.
5. Validate the edited config with the matching OpenCore 1.0.9 `ocvalidate`. Start from USB before replacing your normal boot EFI.

The public config passes `ocvalidate` with its identity fields blank, but it is deliberately not ready for Apple services until you provide your own values.

## Configuration notes

- AppleALC is loaded before SimpleHDA; the current HDA layout is 11.
- The keyboard map changes some unprefixed keypad scan codes to navigation keys. Check your own keyboard before carrying that map over.
- `UTBDefault.kext` is present. This is not a documented, per-port USB map.
- `OmenI2C-7A4C.kext` supplies the controller match used on this laptop. `-vi2c-force-polling` remains enabled.
- `OmenWMIProbe.kext` is a diagnostic component. It is retained in this snapshot; do not publish its collected hardware dumps.
- `OmenFanBridge.kext` is specific to the tested board/firmware. 0% returns a fan to firmware Auto; it does not stop the fan. Performance means full fans, not a CPU/GPU power-limit change.
- SecureBootModel is disabled, SIP is reduced and AMFI-related bypass arguments are present. This is the existing patched installation’s configuration, not a security-hardened setup.

## Files and credits

`EFI.zip` in Releases contains the sanitized boot files. [COMPONENTS.md](COMPONENTS.md) lists the included kext versions. After downloading the archive, run `python3 check-config.py /path/to/EFI.zip` to check that the public identity fields remain blank and enabled file paths exist.

OpenCore/OpenCanopy and the bundled extensions belong to their respective authors. Upstream references and licensing notes are in [THIRD-PARTY.md](THIRD-PARTY.md). No blanket license is being applied to the compiled third-party binaries. Personal EFI backups, older configs, boot logs, hardware reports and the system-installed graphics/audio components are excluded.
