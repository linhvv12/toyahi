#region debai
"""
--- ma debai / id
hi(name)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hi

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/uYheiLdfy6K8LVQj6

--- debai / problem
Khi chay voi input           | Ketqua output
---------------------------- | -----------------
hi(name='Mom')               | Hi Mom!
hi('Mom')                    | Hi Mom!
hi('')                       | Hi!
hi()                         | Hi!
hi(None)                     | Hi!

------------------- mucdo: kho -----------------
hi('Mom', 'Dad')             | Hi Mom, and Dad!
hi('A', 'B', 'C')            | Hi A, B, and C!
hi('1', '22', '333', '4444') | Hi 1, 22, 333, and 4444!
"""
#endregion debai

#region bailam
def hi(*args, name=None):
    if name:  # Nếu có tham số name
        return f"Hi {name}!"

    args = [arg for arg in args if arg]  # Loại bỏ giá trị rỗng hoặc None

    if not args:  # Nếu không có số hợp lệ
        return "Hi!"

    if len(args) == 1:  # Nếu chỉ có 1 tham số
        return f"Hi {args[0]}!"

    if len(args) == 2:  # Nếu có 2 tham số
        return f"Hi {args[0]}, and {args[1]}!"

    # Nếu có nhiều hơn 2 tham số
    return f"Hi {', '.join(args[:-1])}, and {args[-1]}!"
   #endregion bailam

#endregion bailam
