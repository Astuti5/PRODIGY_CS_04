# Educational Keylogger — Lab Exercise

> **Disclaimer:** This tool was built strictly for educational purposes in an isolated 
> virtual machine environment. It should NEVER be deployed on systems you do not own or 
> have explicit written authorization to test. Unauthorized use is illegal under the 
> IT Act, 2000 (India) and equivalent laws globally.

## Purpose
Understanding how keyloggers work is essential for a SOC analyst or VAPT professional.
This project helped me understand how attackers capture credentials silently, which 
directly informs detection strategies.

## What it does
- Captures keystrokes within a defined test window
- Timestamps each keystroke
- Saves output to a local log file

## How attackers use this technique (and how defenders catch it)
- Persistence mechanisms: Registry run keys, scheduled tasks
- Detection: Endpoint EDR tools flag pynput/keyboard library behavior
- Mitigation: Application allowlisting, keyboard encryption (Secure Input on macOS)

## Environment
Tested exclusively on an isolated Windows VM with no network access.
Never tested on live systems.

## Detection signatures
This tool would be flagged by:
- Windows Defender (heuristic behavioral detection)
- Any EDR with process injection monitoring
