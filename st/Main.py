from model.St import SymbolTable

st = SymbolTable()
st.add("if")
st.add("else")
st.add("ion")
print(st.add("marcel"))
print(st.get("marcel"))
