import sys
sys.path.insert(0, "/home/user/Teste/boost-falstad")
from lzstring import compress_to_encoded_uri_component as cz
print("https://www.falstad.com/circuit/circuitjs.html?ctz=" + cz(open(sys.argv[1]).read()))
