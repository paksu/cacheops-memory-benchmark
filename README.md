# cacheops-memory-benchmark
Example project with lots of models to demonstrate memory consumption for django 1.8.5 with django-cacheops

## setup
```
pip install -r requirements.txt
```

## Test memory footprint
without cacheops:
```
/usr/bin/time -l python manage.py test 
```
with cacheops:
```
/usr/bin/time -l python manage.py test --settings=benchmark.with_cacheops
```

### Example benchmarks with 2015 macbook pro

**Django 1.8.5 without cacheops**
```
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
       17.13 real        13.55 user         0.24 sys
 131768320  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
     34333  page reclaims
         0  page faults
         0  swaps
         0  block input operations
         0  block output operations
      1769  messages sent
      1763  messages received
         0  signals received
        25  voluntary context switches
     12077  involuntary context switches
```

**Django 1.8.5 with cacheops**
```
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
       22.38 real        15.47 user         0.43 sys
 270540800  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
     68334  page reclaims
         0  page faults
         0  swaps
         0  block input operations
         0  block output operations
      2151  messages sent
      2143  messages received
         0  signals received
       381  voluntary context switches
     41548  involuntary context switches
```

**Django 1.9.b1 without cacheops**
```
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
       14.90 real         6.25 user         0.29 sys
  60317696  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
     17221  page reclaims
         0  page faults
         0  swaps
         0  block input operations
         0  block output operations
      1704  messages sent
      1702  messages received
         0  signals received
        13  voluntary context switches
     37473  involuntary context switches
```

**Django 1.9.b1 with cacheops**
```
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
        8.97 real         5.58 user         0.23 sys
 133828608  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
     35247  page reclaims
         0  page faults
         0  swaps
         0  block input operations
         0  block output operations
      2058  messages sent
      2056  messages received
         0  signals received
       366  voluntary context switches
      8699  involuntary context switches
```
