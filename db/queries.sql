-- 1. Insert into tai_khoan
INSERT INTO tai_khoan (id_nhan_vien, ten_nhan_vien, mat_khau, chuc_vu, email, trang_thai, gioi_tinh)
VALUES
('NV001', 'Nguyễn Văn A', 'pass123', 'Sale Staff', 'a@example.com', 'Hoạt động', 'Male'),
('NV002', 'Trần Thị B', 'pass456', 'Warehouse Staff', 'b@example.com', 'Hoạt động', 'Female'),
('NV003', 'Lê Văn C', 'pass789', 'Admin', 'c@example.com', 'Tạm khóa', 'Male');

-- 2. Insert into san_pham
INSERT INTO san_pham (id_san_pham, id_danh_muc, ten_san_pham, so_luong, mo_ta, trang_thai, hinh_anh, don_vi_tinh)
VALUES
('SP001', 'DM01', 'Laptop Dell XPS 13', 31, 'Mô tả sản phẩm Laptop Dell XPS 13', 'Không hỏng', 'link_hinh.jpg', 'Cái'),
('SP002', 'DM01', 'Chuột Logitech M185', 80, 'Mô tả sản phẩm Chuột Logitech M185', 'Không hỏng', 'link_hinh.jpg', 'Cái'),
('SP003', 'DM01', 'Bàn phím cơ Keychron K6', 15, 'Mô tả sản phẩm Bàn phím cơ Keychron K6', 'Không hỏng', 'link_hinh.jpg', 'Cái'),
('SP004', 'DM01', 'Màn hình Samsung 24 inch', 52, 'Mô tả sản phẩm Màn hình Samsung 24 inch', 'Không hỏng', 'link_hinh.jpg', 'Cái'),
('SP005', 'DM01', 'Ổ cứng SSD Samsung 1TB', 81, 'Mô tả sản phẩm Ổ cứng SSD Samsung 1TB', 'Không hỏng', 'link_hinh.jpg', 'Cái');

-- 3. Insert into ds_yeu_cau_xuat_kho with id_nhan_vien_yc
INSERT INTO ds_yeu_cau_xuat_kho (id_yeu_cau_xuat, id_nhan_vien_yc_id, thoi_gian, ghi_chu, trang_thai, loai)
VALUES
('YC001', 'NV001', '2025-06-04 08:00:00', 'Xuất sản phẩm cho đơn hàng A', 'Chờ duyệt', 'Hàng để bán'),
('YC002', 'NV001', '2025-06-04 09:30:00', 'Xuất trưng bày showroom', 'Chờ duyệt', 'Hàng để bán'),
('YC003', 'NV001', '2025-06-04 10:45:00', 'Xuất sản phẩm lỗi cần xử lý', 'Chờ duyệt', 'Xuất hàng hỏng'),
('YC004', 'NV001', '2025-06-04 11:15:00', 'Xuất nội bộ cho nhóm kỹ thuật', 'Chờ duyệt', 'Hàng để bán'),
('YC005', 'NV001', '2025-06-04 13:00:00', 'Xuất đơn hàng online', 'Chờ duyệt', 'Hàng để bán');

-- 4. Insert into chi_tiet_yeu_cau_xuat
INSERT INTO chi_tiet_yeu_cau_xuat (id_yeu_cau_xuat, id_san_pham_id, so_luong, ghi_chu)
VALUES
('YC001', 'SP001', 3, 'Đơn hàng A laptop'),
('YC001', 'SP002', 5, 'Chuột kèm theo'),
('YC002', 'SP003', 2, 'Trưng bày bàn phím'),
('YC002', 'SP004', 1, 'Trưng bày màn hình'),
('YC003', 'SP005', 2, 'Hỏng cần xử lý'),
('YC003', 'SP001', 1, 'Laptop lỗi bàn phím'),
('YC004', 'SP002', 3, 'Dùng nội bộ'),
('YC004', 'SP005', 2, 'Lắp ráp thử nghiệm'),
('YC005', 'SP004', 1, 'Chuẩn bị giao hàng'),
('YC005', 'SP003', 1, 'Giao đơn online');

-- 5. Insert into hang_xuat_kho
INSERT INTO hang_xuat_kho (id_yeu_cau_xuat, id_nhan_vien_xuat_id, id_san_pham_id, so_luong, ghi_chu, thoi_gian_xuat)
VALUES
('YC001', 'NV002', 'SP001', 3, 'Xuất từ kho NV002', '2025-06-05 14:00:00'),
('YC001', 'NV002', 'SP002', 5, 'Xuất từ kho NV002', '2025-06-05 14:00:00');