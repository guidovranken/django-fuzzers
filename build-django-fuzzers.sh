#!/bin/bash

set -e

export CC=clang
export CXX=clang++
export COMPILE_FLAGS="-fsanitize=fuzzer-no-link"
export CFLAGS=$COMPILE_FLAGS
export CXXFLAGS=$COMPILE_FLAGS
export LDFLAGS=$COMPILE_FLAGS
export LIB_FUZZING_ENGINE="-fsanitize=fuzzer"

# Get Django
git clone --depth 1 https://github.com/django/django.git

# Get Django fuzzers
git clone --depth 1 git@github.com:guidovranken/django-fuzzers.git

# Get CPython
wget https://github.com/python/cpython/archive/v3.8.0b2.tar.gz
tar zxf v3.8.0b2.tar.gz

mkdir cpython-install
export CPYTHON_INSTALL_PATH=`realpath cpython-install`

cd cpython-3.8.0b2/

# Patch CPython
cp ../django-fuzzers/python_coverage.h Python/
sed -i '1 s/^.*$/#include "python_coverage.h"/g' Python/ceval.c
sed -i 's/case TARGET\(.*\): {/\0\nfuzzer_record_code_coverage(f->f_code, f->f_lasti);/g' Python/ceval.c

# Compile and install CPython
./configure --prefix=$CPYTHON_INSTALL_PATH && make -j $(nproc) && make install

rm -rf $CPYTHON_INSTALL_PATH/lib/python3.8/lib-dynload/_tkinter*.so

# Django dependencies
mkdir ../django-dependencies
$CPYTHON_INSTALL_PATH/bin/pip3 install asgiref pytz sqlparse -t ../django-dependencies

cd ../django-fuzzers
export OUT=$(realpath .)
mv ../django/* .
mv ../django-dependencies/ .
make
