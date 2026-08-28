{ ... }:

{
  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    version = "3.14.6";

    uv = {
      enable = true;
      sync.enable = true;
    };

    venv.enable = true;
  };

  processes = {
    uv-sync = {
      exec = ''
        uv sync
      '';
      restart.on = "never";

      watch = {
        paths = [
          ./pyproject.toml
          ./uv.lock
        ];
      };
    };
  };

  tasks = {
    "env:MAKEFLAGS" = {
      exec = ''
        cpus=$(nproc)
        export MAKEFLAGS="--jobs=$cpus --load-average=$cpus --output-sync=target"
      '';
      exports = [ "MAKEFLAGS" ];
      before = [ "devenv:enterShell" ];
    };
  };
}
