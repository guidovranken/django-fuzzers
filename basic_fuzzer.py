import atheris

with atheris.instrument_imports():
    import fuzzers

def TestOneInput(data):
  fuzzers.test_base36_to_int(data)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()