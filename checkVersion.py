import semver

def checkVersion(new_version):
    version_parts = new_version.split('.')
    version_length = len(version_parts)
    padded_version = ""

    if version_length < 3:
        padded_version = "%s.%s.0" % (
                version_parts[0],
                version_parts[1])
    else:
        padded_version = new_version

    result = semver.match(padded_version, ">=1.1.0")

    return result
