import os
import pytest
from utils.reporting import generate_report

def run_tests():
    # Run Pytest with options
    pytest.main([
        "-v", "--tb=short", "--capture=sys", "--alluredir=reports/allure"
    ])
    
    # Generate Test Report
    generate_report()

if __name__ == "__main__":
    run_tests()
