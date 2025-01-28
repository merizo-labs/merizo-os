#!/usr/bin/env python3
import os
import sys

def build_bootloader(r: bool):
    if not r:
        process = os.popen("cd bootloader && cargo clean")
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

def build(r: bool):
    build_bootloader(r)
    build_kernel(r)

    
release_flag = "--release" in sys.argv
build(release_flag)
