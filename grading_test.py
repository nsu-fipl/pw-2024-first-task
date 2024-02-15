import sys
import hashlib

expected = '''437c569c85798f09571f9673446712bee75b7be56f3fbdc058949652eaa5ee25
9da2e5b928d286f2c57caec344e81266bacd6f24bc2f91394954f74d2cb7cf6e
c9f95f149c7b42490467bacb3a03aa60c290437cebd82025c22711fd1f9ccb1b
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
b8ff72cc22dc047cf4e64ccdeaf7c239c1b8f65bb8cfee438591b3cf71bc9701
2e2769ca1c2bb0c7e3a2cde5cb7b722f7f7f80e8d28f44a9d8a5504f2f8c0e80
4bc2dfef049c354b41f9b526981a8429b9ec30cd39c7ec0ce2193a1e7adece9e
0c926af1a64df0e374257e923ad14eb2441ccf824f426d678ec9444b8eac2462
c36c7c80d2a1fe37b687a983d47d8e2269f964badfd3076efa370651c37ef04c
7a8a0c322cc4ec639f1e7d5eb3bd190aebdf9347a0f6bbcf84b7065313413c36
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
3bd5d91bfe70a5b1fac5780f6a451a9fddb28a35787918fc15d88bc0d52096d1
182645a6314d5e8ba74d3e3f0b0ca54188d5a2a2dd82b3bd67bbeb5e000d62b9
b8ff72cc22dc047cf4e64ccdeaf7c239c1b8f65bb8cfee438591b3cf71bc9701
181c7d6cdd5cdeedf3fff5ecc12044112d9aeee99435d47600d39e6027cc29ba
c32f2b1a66f8a79deadb74f533f3075c60a629df343b89e8c4477d40fa960ba8
7194580d58b191e864dff63fff01c9ddb9f0034abb19d886611e7013c0d0ab4e
bcc16eea570e9d454d27c6a0b031c99f25ce6998f4030eb30f8ad6ac51999c0e
53178aa96a6bea1967e625bec8deb01428473de8c3288ccb97399da76b70b5f4
b8ff72cc22dc047cf4e64ccdeaf7c239c1b8f65bb8cfee438591b3cf71bc9701
befa82f711039a5cdd7c45d2425c0afaf39695389810bbb64699787520db106f
'''

def normalize(cmd):
    return " ".join(cmd.rstrip('\n').split())

def hex(cmd):
    return hashlib.sha256(cmd.encode('utf-8')).hexdigest()

def correct_git_clone():
    import subprocess
    cmd = ['git', 'config', '--get', 'remote.origin.url']
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
    output = output.decode('utf-8').rstrip('\n')
    repo_name_prefix = "nsu-fipl/pw-2024-first-task-"
    start = output.find(repo_name_prefix)
    assert start > 0, f"Expected repo name to contain '{repo_name_prefix}'"
    user_name = output[len(repo_name_prefix) + start:].split()[0]
    return f"{repo_name_prefix}{user_name}"

def test_git():
    n_line = 1
    with open("commands.txt") as f:
        cmd = f.readline()
        assert cmd
        cmd = cmd.rstrip('\n')
        assert correct_git_clone() in cmd, f"Incorrect git clone line"
        hashes = expected.strip('\n').split('\n')
        for cmd in f:
            n_line += 1
            cmd_hex = hex(normalize(cmd))
            h = hashes[n_line - 2]
            assert cmd_hex == h, f"Incorrect git command at line: {n_line}"