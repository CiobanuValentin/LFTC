from model.St import SymbolTable

if __name__ == "__main__":

    st = SymbolTable()
    st.add("if")
    st.add("else")
    st.add("ion")
    print(st.add("marcel"))
    print(st.get("marcel"))
