build:
    just build-kernel
    just build-bootloader
    mv target/x86_64-unknown-uefi/debug/merizo-bootloader.efi images/merizo-bootloader.efi

build-kernel:
    @cd kernel && just build

build-bootloader:
    @cd bootloader && cargo build
