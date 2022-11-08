#!/bin/bash
echo test
rm -rf install/scripts/airflowfile
#pytest -k "swap" --html=BCT_TestReport.html --self-contained-html

pytest --html=E_TestReport.html --self-contained-html
