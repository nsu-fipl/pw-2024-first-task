import sys
import hashlib

expected = '''437c569c85798f09571f9673446712bee75b7be56f3fbdc058949652eaa5ee25
05071330a14e57d19e6fd26a71e9dcca82a796020e726acbc97eb37dd9f5863f
4c0fe4b6b3186f24c3056c55e341ab825b680274e06dd93d307a840177d7dc23
9f4ddbdc6b6ff86a6b9c43e2d1c115e18b1fa6fb14a53301f041fe757c4bfed1
0bfab9444575bcf30b39757a51e9626051690b37073167a2233b59b52e01593a
86742d54b5d8a35591e82ef454ebfcf5549c51fb5e67a661640d575643828c19
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
b8ff72cc22dc047cf4e64ccdeaf7c239c1b8f65bb8cfee438591b3cf71bc9701
2e2769ca1c2bb0c7e3a2cde5cb7b722f7f7f80e8d28f44a9d8a5504f2f8c0e80
0bfab9444575bcf30b39757a51e9626051690b37073167a2233b59b52e01593a
0c926af1a64df0e374257e923ad14eb2441ccf824f426d678ec9444b8eac2462
c36c7c80d2a1fe37b687a983d47d8e2269f964badfd3076efa370651c37ef04c
95b1e5dea5b40cae6fa6d19807bd2722b89b12f47caa6e76ceb457d9997e6840
c7b7736261bf33fd8bf6eaf3e2be98eca6fd7b1d119dbc280e8e155b5882be88
3bd5d91bfe70a5b1fac5780f6a451a9fddb28a35787918fc15d88bc0d52096d1
182645a6314d5e8ba74d3e3f0b0ca54188d5a2a2dd82b3bd67bbeb5e000d62b9
b8ff72cc22dc047cf4e64ccdeaf7c239c1b8f65bb8cfee438591b3cf71bc9701
181c7d6cdd5cdeedf3fff5ecc12044112d9aeee99435d47600d39e6027cc29ba
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
7194580d58b191e864dff63fff01c9ddb9f0034abb19d886611e7013c0d0ab4e
bcc16eea570e9d454d27c6a0b031c99f25ce6998f4030eb30f8ad6ac51999c0e
0bfab9444575bcf30b39757a51e9626051690b37073167a2233b59b52e01593a
c8471010f1bc07ee6a7419b56c669b4cc583ddb6f1c6d4dbe1021665852628c5
182645a6314d5e8ba74d3e3f0b0ca54188d5a2a2dd82b3bd67bbeb5e000d62b9
b8ff72cc22dc047cf4e64ccdeaf7c239c1b8f65bb8cfee438591b3cf71bc9701
10a0f33c588dfc9cc0be468db9e076410486eb01e220f032875bfb092737cbd4
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
'''

def normalize(cmd):
    return " ".join(cmd.rstrip('\n').split())

def hex(cmd):
    return hashlib.sha256(cmd.encode('utf-8')).hexdigest()

def test_git():
    n_line = 1
    with open("commands.txt") as f:
        cmd = f.readline()
        assert cmd
        cmd = cmd.rstrip('\n')
        assert 'clone' in cmd, f"Incorrect git clone line"
        hashes = expected.strip('\n').split('\n')
        total_line = 1
        for cmd in f:
            total_line += 1
            if cmd.isspace():
                continue
            n_line += 1
            cmd_hex = hex(normalize(cmd))
            h = hashes[n_line - 2]
            assert cmd_hex == h, f"Incorrect git command at line: {total_line}"
        assert (n_line - 1) >= len(hashes), f"Not enough commands, expected {len(hashes) + 1}"
