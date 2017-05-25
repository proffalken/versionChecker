from checkVersion import checkVersion

versions = ["1.1", "1.2", "1.1.1", "1.0"]

for version in versions:
    result = checkVersion(version)
    print("Checking %s - result was %s" % (
            version,
            result
        )
    )
