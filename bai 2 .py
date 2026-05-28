music_list = []

while True:
    print("\n=========== MENU QUẢN LÝ DANH SÁCH BÀI HÁT ==========")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa danh sách bài hát")
    print("4. Sắp xếp và trích xuất danh sách")
    print("5. Thoát chương trình")
    print("=====================================================")
    choice = input("Nhập lựa chọn của bạn: ").strip()

    match choice:
        case '1':
            while True:
                print("\n--- THÊM BÀI HÁT ---")
                print("1. Thêm vào cuối danh sách")
                print("2. Chèn vào vị trí cụ thể")
                # input: Người dùng chọn cách thêm bài hát
                # output: Xử lý thêm bài hát theo lựa chọn
                option = input("Nhập lựa chọn: ")
                # input: Người dùng nhập tên bài hát
                # output: Lưu tên bài hát vào playlist
                music_name = input("Nhập tên bài hát: ")

                if option == '1':
                    music_list.append(music_name)
                    amount = len(music_list)

                    print(f"Thêm bài hát {music_name} thành công!")
                    print(f"Số lượng bài hát hiện tại trong playlist: {amount}")
                    break

                elif option == '2':
                    placed = input("Nhập vị trí muốn thêm vào: ")

                    if placed < 0 or placed > len(music_list):
                        print("Vị trí không hợp lệ.")
                    else:
                        music_list.insert(placed, music_name)
                        amount = len(music_list)

                        print(f"Thêm bài hát {music_name} thành công!")
                        print(f"Số lượng bài hát hiện tại trong playlist: {amount}")
                        break
                else:
                    print("Lựa chọn không hợp lệ!")
                    
        case '2':

            if len(music_list) == 0:
                print("Danh sách phát hiện đang trống!")
                continue
            print("\n--- DANH SÁCH PHÁT ---")
            for i, song in enumerate(music_list, start=1):
                print(f"{i}. {song}")
            total = len(music_list)
            print(f"\nTổng số bài hát: {total}")
            
        case '3':

            if len(music_list) == 0:
                print("Danh sách phát hiện đang trống!")
                continue
            print("\n--- XÓA BÀI HÁT ---")
            print("1. Xóa theo tên bài hát")
            print("2. Xóa theo số thứ tự")

            option = input("Nhập lựa chọn: ")

            if option == '1':
                delete_name = input("Nhập tên bài hát muốn xóa: ")

                if delete_name in music_list:
                    music_list.remove(delete_name)
                    print(f"Đã xóa bài hát {delete_name} khỏi danh sách")
                else:
                    print("Không tìm thấy bài hát trong danh sách phát.")

            elif option == '2':
                delete_index = int(input("Nhập số thứ tự muốn xóa: "))
                if not delete_index.isdigit():
                    print("Vị trí không hợp lệ.")
                    continue
                real_index = delete_index - 1

                if real_index < 0 or real_index >= len(music_list):
                    print("Vị trí không hợp lệ.")

                else:
                    removed_song = music_list.pop(real_index)
                    print(f"Đã xóa bài hát {removed_song} khỏi danh sách")

        case '4':

            if len(music_list) == 0:
                print("Danh sách phát hiện đang trống!")
                continue
            print("\n--- SẮP XẾP VÀ TRÍCH XUẤT ---")
            print("1. Sắp xếp A-Z")
            print("2. Lấy 3 bài hát đầu tiên")

            option = input("Nhập lựa chọn: ")

            if option == '1':
                sorted_list = sorted(music_list)
                print("\nDanh sách sau khi sắp xếp:")
                for song in sorted_list:
                    print(song)

            elif option == '2':
                first_three = music_list[:3]
                print("\n3 bài hát đầu tiên:")

                for song in first_three:
                    print(song)
            else:
                print("Lựa chọn không hợp lệ!")

        case 5:
            # output: Thoát chương trình
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")