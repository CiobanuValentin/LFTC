from model.St import SymbolTable

if __name__ == "__main__":
    st = SymbolTable()
    st.add("if")
    st.add("else")
    st.add("ion")
    assert (st.add("marcel") == 3)
    assert (st.get("marcel") == 3)
    assert (st.get("if") == 0)
    assert (st.add('"if"') == 4)
    st.add(1)
    st.add(3)
    st.add(2)
    st.inorder()
