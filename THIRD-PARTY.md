# Components and licensing

This repository collects a machine-specific configuration and compiled components. It does not claim ownership of the bundled bootloader, extensions, firmware or artwork. Retain their original notices and follow each component’s license. Configuration changes do not relicense those components.

- OpenCore, OpenCanopy and related tools: https://github.com/acidanthera/OpenCorePkg
- Picker resources: https://github.com/acidanthera/OcBinaryData
- Lilu, AppleALC, WhateverGreen, RestrictEvents, VirtualSMC, NVMeFix, BrightnessKeys and VoodooPS2: https://github.com/acidanthera
- Intel Wi-Fi/Bluetooth projects: https://github.com/OpenIntelWireless
- Installed AirportItlwm fork referenced during setup: https://github.com/jzrodriguez98/itlwm
- VoodooI2C and VoodooI2CHID: https://github.com/VoodooI2C
- USBToolBox: https://github.com/USBToolBox
- RealtekRTL8111: https://github.com/Mieze/RTL8111_driver_for_OS_X

Some supplied binaries are modified, historical or locally built. The inventory records installed version strings, not proof of a particular upstream commit. Exact source/license provenance for SimpleHDA, AMFIPass, CpuTopologyRebuild, XHCI-unsupported and NullMothSafe.efi has not been established by this export; do not represent them as original MIT-licensed project code. Their inclusion in the existing machine setup is not a license grant.

OmenI2C-7A4C is a local controller-matching injector. OmenWMIProbe and OmenFanBridge are local experimental drivers; the fan-control project contains their maintained source and documentation. The full graphics driver installation is outside this repository.
