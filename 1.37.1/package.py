
name = "materialx"

version = "1.37.1"

variants = [
    ["arch-*", "os-*", "release-1"],
    ["arch-*", "os-*", "release-0"],
]

build_requires = [
    "rezutil-1+",
    "cmake-3.2+",
]
build_command = "python {root}/rezbuild.py {install}"


def commands():
    env = globals()["env"]

    env.PATH.append("{root}/lib")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/share/pkgconfig")

    env.MATERIALX_ROOT.set("{root}")

