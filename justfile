build-bootloader:
    cd bootloader && cargo build
    mv target/x86_64-unknown-uefi/debug/merizo-bootloader.efi images/merizo-bootloader.efi
build-kernel:
    cd kernel && just build
    