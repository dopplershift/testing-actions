import json
from pathlib import Path
from packaging import version

# Get all paths that are versions
vers = sorted(version.parse(str(p)) for p in Path().glob('v[0-9]*'))

# Set up our version dictionary
versions = dict(versions=['latest', 'dev'],
                latest=f'v{vers[-1].major}.{vers[-1].minor}', prereleases=[])
versions['versions'].extend(f'{v.major}.{v.minor}' for v in vers[-4:])

# Write to JSON file
with open('versions.json', 'wt') as verfile:
    json.dump(versions, verfile)

# Update the 'latest' symlink
latest = Path('latest')
latest.unlink(missing_ok=True)
latest.symlink_to(versions['latest'], target_is_directory=True)