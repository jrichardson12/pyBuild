def dependency_file():
    text = """
# Don't forget to be in ven

python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

"""
    return text
