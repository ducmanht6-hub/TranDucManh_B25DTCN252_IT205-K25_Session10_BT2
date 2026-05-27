while True:
    choice = input("""
                        HỆ THÔNG QUAN LÝ NỘI DUNG SAN PHÂM SHOPPEE

                        1. Nhập dữ liệu sản phầm và xem báo cáo thông kê
                        2. Chuân hóa tên shop
                        3. Kiêm tra mã giảm giá hợp lệ
                        4. Tìm kiểm và thay thể từ khóa trong mô tả sản phâm
                        5. Thoát chương trình

                        > Mời bạn chọn chức năng (1-5):
                        """)
    if choice.isdigit():
        choice = int(choice)
        match choice:
            case 1:
                while True:
                    shop_name = input("Tên shop: ")
                    if shop_name.strip() == "":
                        print("Tên shop không được để trống")
                    else:
                        break
                
                product_name = input("Tên sản phẩm: ")
                
                while True:
                    description = input("Mô tả sản phẩm: ")
                    if description.strip() == "":
                        print("Mô tả sản phẩm không được để trống")
                    break
                
                category_name = input("Danh mục sản phẩm: ")
                key_search = input("Danh mục từ khóa tìm kiếm: ")
                sale_id = input("Mã giảm giá")
                
            case 2:
                print(f"Tên shop ban đầu:  {shop_name}")
                shop_name_v2 = "shop-" + shop_name.strip().lower().replace(" ", "-")
                print(f"Tên shop sau khi được chuẩn hóa: {shop_name_v2}")

            case 3:
                search_sale_id = input("Hãy nhập mã giảm giá: ")
                if search_sale_id.strip() == "":
                    print("Mã giảm giá không được để trống")
                elif " " in search_sale_id:
                    print("Mã giảm giá không được chứa khoảng trắng")
                elif len(search_sale_id) < 6 or len(search_sale_id) > 12:
                    print("Mã giảm giá phải có độ dài từ 6-12 ký tự")
                elif search_sale_id != search_sale_id.upper():
                    print("Mã giảm giá phải viết hoa toàn bộ")
                elif not search_sale_id.isalnum():
                    print("Mã giảm giá chỉ chứa số và chữ")
                elif search_sale_id[0:4] != "SALE":
                    print("Mã giảm giá phải bắt đầu bằng chuỗi SALE")
                else:
                    print("Mã giảm giá hợp lệ")
                    print(search_sale_id)
                
            case 4: 
                key_search_input = input("Hãy nhập từ khóa tìm kiếm: ")
                key_search_output = input("Hãy nhập từ khóa thay thế: ")
                if f"{key_search_input}" in description:
                    print(f"Số lần xuất hiện của từ khóa: {description.count(key_search_input)}")
                    print(f"Mô tả thay thế: {description.replace(key_search_input, key_search_output)}")
                else:
                    print("Từ khóa bạn nhập ko có trong mô tả")

            case 5:
                print("Chương trình kết thúc")
                break
            case _:
                print("Hãy nhập số từ (1-5)")
    else:
        print("Hãy nhập số nguyên")