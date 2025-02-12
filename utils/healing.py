# Auto-Healing using Healenium
def auto_heal(driver, locator):
    try:
        return driver.find_element(*locator)
    except Exception:
        logger.warning("Auto-healing required for: %s", locator)
        healenium = Healenium(driver)
        return healenium.find_element(locator)