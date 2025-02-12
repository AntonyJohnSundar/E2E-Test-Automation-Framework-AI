# Function to run tests based on category
def run_tests():
    category = select_test_category()
    pytest_args = ["-v", "--tb=short", "--capture=sys", "--alluredir=reports/allure"]
    
    if category != "all":
        pytest_args.append(f"-m {category}")  # Run only selected marker
    
    pytest.main(pytest_args)
    generate_report()
