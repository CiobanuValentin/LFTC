from model.St import SymbolTable

if __name__ == "__main__":
    st = SymbolTable()
    st.add("if")
    st.add("else")
    st.add("ion")
    assert (st.add("marcel") == 3)
    assert (st.get("marcel") == 3)
    assert (st.get("if") == 1)
    assert (st.add('"if"') == 4)
    st.inorder()
