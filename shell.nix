with import <nixpkgs> {};
pkgs.mkShell {
  name = "pyshell";

  # Here is where you will add all the libraries required by your native modules
  # You can use the following one-liner to find out which ones you need.
  # Just make sure you have `gcc` installed.
  # `find .venv/ -type f -name "*.so" | xargs ldd | grep "not found" | sort | uniq`
  NIX_LD_LIBRARY_PATH = lib.makeLibraryPath [
    stdenv.cc.cc # libstdc++
    # zlib # libz (for numpy)
  ];

  NIX_LD = lib.fileContents "${stdenv.cc}/nix-support/dynamic-linker";

  packages = with pkgs; [
    poetry
    uv
    python314
  ];

  # Uncomment if you're using Poetry - since we're using a Nix-provided `python`
  # as opposed to an unpatched one, we need to explicitly inform it of the
  # dynamic library path.
  #
  shellHook = ''
    export LD_LIBRARY_PATH=$NIX_LD_LIBRARY_PATH
  '';
}
