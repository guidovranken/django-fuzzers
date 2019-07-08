#pragma once
#include <stdint.h>
#include <stddef.h>

#define COVERAGE_ARRAY_SIZE 65536

__attribute__((section("__libfuzzer_extra_counters")))
uint8_t coverage_counter[COVERAGE_ARRAY_SIZE];

void fuzzer_record_code_coverage(void* codeptr, int lasti)
{
    coverage_counter[ ((size_t)(codeptr) ^ (size_t)(lasti)) % COVERAGE_ARRAY_SIZE ] = 1;
}
