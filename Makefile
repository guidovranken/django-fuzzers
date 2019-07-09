all : fuzzer-utils

CPYTHON_LIB_PATH=$(CPYTHON_INSTALL_PATH)/lib/python3.8
CPYTHON_LIB_DYNLOAD_PATH=$(CPYTHON_LIB_PATH)/lib-dynload

PYTHON_LD_FLAGS=$(CPYTHON_INSTALL_PATH)/lib/libpython3.8.a -lutil -lpthread $(CPYTHON_LIB_DYNLOAD_PATH)/*.so

fuzzer-utils:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 -I $(CPYTHON_INSTALL_PATH)/include/python3.8/ fuzzer.cpp -DPYTHON_HARNESS_PATH="\"$(OUT)/utils.py\"" $(PYTHON_LD_FLAGS) -ldl -o fuzzer-utils
