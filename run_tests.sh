source ./.venv/bin/activate
echo "Running tests..."
timeout 2h pytest -W ignore::DeprecationWarning --disable-pytest-warnings --cov=. --cov-context=test --timeout=300 --continue-on-collection-errors -ra | tee coverage_output.txt
echo "Forming spectrum..."
coverage-sbfl -e coverage_output.txt
echo "Done!"
deactivate
