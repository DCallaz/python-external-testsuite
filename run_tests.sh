source ./.venv/bin/activate
pip install pytest-cov
pip install coverage-sbfl
timeout 2h pytest -W ignore::DeprecationWarning --disable-pytest-warnings --cov=. --cov-context=test --timeout=300 --continue-on-collection-errors -ra > coverage_output.txt
coverage-sbfl -e coverage_output.txt
deactivate
