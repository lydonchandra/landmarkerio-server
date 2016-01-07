from enum import Enum


class FileExt(Enum):
    lm = '.ljson'
    template = '.yml'
    old_template = '.txt'
    collection = '.txt'


class CacheFile(Enum):
    texture = 'texture.jpg'
    image = 'image.json'
    thumbnail = 'thumbnail.jpg'
    mesh_tmp = 'mesh.raw.tmp'
    mesh = 'mesh.raw.gz'


class Server(Enum):
    allowed_origins = ['https://www.landmarker.io',      # secure client
                       'http://localhost:4000',          # client development
                       'http://insecure.landmarker.io']  # legacy client
    endpoint = '/api/v2/'


class Endpoints(Enum):
    mode = 'mode'
    images = 'images'
    collections = 'collections'
    landmarks = 'landmarks'
    meshes = 'meshes'
    templates = 'templates'
    points = 'points'
    trilist = 'trilist'
    tcoords = 'tcoords'
    normals = 'normals'
    textures = 'textures'
    thumbnail = 'thumbnails'
    fit = 'fit'


class Mimetype(Enum):
    json = 'application/json'
    jpeg = 'image/jpeg'
    binary = 'application/octet-stream'


LM_DIRNAME = 'lmiolandmarks'
TEMPLATE_DINAME = '.lmiotemplates'

ALL_COLLECTION_ID = 'all'

dirs_in_dir = lambda (path): sorted([p for p in path.iterdir() if p.is_dir()])

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
