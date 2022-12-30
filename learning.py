#!/usr/bin/env python3
import pandas
visitors=[1234,3445,5365,2354]
errors=[23,45,33,47]
df=pandas.DataFrame({"visitors":visitors, "errors":errors},index=["mon","tue","wed","thu"])

print(df)
print(df["errors"].mean())