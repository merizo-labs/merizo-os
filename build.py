#!/usr/bin/env python3
import os
import sys

def build_bootloader(r: bool):
    if not r:
        process = os.popen("cd bootloader && cargo build")
    else: 
        process = os.popen("cd bootloader && cargo build --release")
    output = process.read()
    process.close()
    if r:
        os.system("mv target/x86_64-unknown-uefi/release/merizo-bootloader.efi images/merizo-bootloader.efi")
    else:
        os.system("mv target/x86_64-unknown-uefi/debug/merizo-bootloader.efi images/merizo-bootloader.efi")
    print(output)

def build_kernel(r: bool):
    if r:
        process = os.popen("cd kernel && just rbuild")
    else:
        process = os.popen("cd kernel && just build")
    output = process.read()
    process.close()
    print(output)

def prepare_iso_dir():
    os.system("mkdir -p iso/EFI/BOOT")
    os.system("cp images/merizo-bootloader.efi iso/EFI/BOOT/BOOTX64.EFI")
    os.system("cp images/merizo-kernel.elf iso/merizo-kernel.elf")
def form_iso():
    os.system("mkdir -p images/iso")
    process = os.popen("xorriso -as mkisofs -R \
  -J \
  -V 'MERIZO_OS' \
  -b EFI/BOOT/BOOTX64.EFI \
  -no-emul-boot \
  -append_partition 2 0xef iso/EFI/BOOT/BOOTX64.EFI \
  -o images/iso/merizo.iso \
  iso/")
    output = process.read()
    process.close()
    print(output)
def clear_iso_support_files():
    os.system("rm -rf iso")

def build(r: bool):
    build_bootloader(r)
    build_kernel(r)

    
release_flag = "--release" in sys.argv
build(release_flag)

create_iso = "--iso" in sys.argv
if create_iso:
    prepare_iso_dir()
    form_iso()
    clear_iso_support_files()
print("Build complete")