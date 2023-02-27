import os

if os.name == "nt":
    # Windows
    import msvcrt

    def portable_lock(fp):
        msvcrt.locking(fp.fileno(), msvcrt.LK_LOCK, 1)

    def portable_unlock(fp):
        msvcrt.locking(fp.fileno(), msvcrt.LK_UNLCK, 1)

else:
    # *nix
    import fcntl

    def portable_lock(fp):
        fcntl.flock(fp.fileno(), fcntl.LOCK_EX)

    def portable_unlock(fp):
        fcntl.flock(fp.fileno(), fcntl.LOCK_UN)


class GlobalLock:
    """Global mutex implementation.

    Ensures only one process can access a block of code. Use:

    with Locker():
        # do something

    See https://stackoverflow.com/a/60214222/6419909 for details.

    """

    def __enter__(self):
        self.fp = open("./lockfile.lock", "wb")
        portable_lock(self.fp)

    def __exit__(self, _type, value, tb):
        portable_unlock(self.fp)
        self.fp.close()
        os.remove("./lockfile.lock")
