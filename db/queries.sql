-- 1. Insert into tai_khoan
INSERT INTO tai_khoan (id_nhan_vien, ten_nhan_vien, mat_khau, chuc_vu, email, trang_thai, gioi_tinh)
VALUES
('NV001', 'Lê Thị Huyền Trang', 'pass123', 'Sale Staff', 'a@example.com', 'Hoạt động', 'Male'),
('NV002', 'Thái Bình', 'pass456', 'Warehouse Staff', 'b@example.com', 'Hoạt động', 'Female'),
('NV003', 'Hữu Xuân', 'pass789', 'admin', 'c@example.com', 'Tạm khóa', 'Male'),
('NV004', 'Minh Tài', 'pass111', 'Sale Staff', 'd@example.com', 'Hoạt động', 'Female'),
('NV005', 'Trà Giang', 'pass222', 'Warehouse Staff', 'e@example.com', 'Hoạt động', 'Male'),
('NV006', 'Nguyễn Ngọc Tú Anh', 'pass333', 'Sale Staff', 'f@example.com', 'Hoạt động', 'Female'),
('NV007', 'Huyền Trang 1', 'pass444', 'Warehouse Manager', 'nvql@example.com', 'Hoạt động', 'Female');



-- 2. Insert into san_pham
INSERT INTO san_pham (id_san_pham, id_danh_muc, ten_san_pham, so_luong, mo_ta, trang_thai, hinh_anh, don_vi_tinh)
VALUES
('SP001', 'DM01', 'Laptop Dell XPS 13', 31, 'Mô tả sản phẩm Laptop Dell XPS 13', 'Không hỏng', 'link_hinh.jpg', 'Cái'),
('SP002', 'DM01', 'Chuột Logitech M185', 80, 'Mô tả sản phẩm Chuột Logitech M185', 'Không hỏng', 'link_hinh.jpg', 'Cái'),
('SP003', 'DM01', 'Bàn phím cơ Keychron K6', 15, 'Mô tả sản phẩm Bàn phím cơ Keychron K6', 'Không hỏng', 'link_hinh.jpg', 'Cái'),
('SP004', 'DM01', 'Màn hình Samsung 24 inch', 52, 'Mô tả sản phẩm Màn hình Samsung 24 inch', 'Không hỏng', 'link_hinh.jpg', 'Cái'),
('SP005', 'DM01', 'Ổ cứng SSD Samsung 1TB', 81, 'Mô tả sản phẩm Ổ cứng SSD Samsung 1TB', 'Không hỏng', 'link_hinh.jpg', 'Cái');

-- 3. Insert into ds_yeu_cau_xuat_kho with id_nhan_vien_yc
INSERT INTO ds_yeu_cau_xuat_kho (
    id_yeu_cau_xuat, id_nhan_vien_yc, id_nhan_vien_duyet,
    thoi_gian, thoi_gian_duyet, thoi_gian_xuat,
    ghi_chu, trang_thai, loai
) VALUES
('YC001', 'NV001', NULL, '2025-06-04 08:00:00', NULL, NULL, 'Xuất sản phẩm cho đơn hàng A', 'Chờ duyệt', 'Hàng để bán'),
('YC002', 'NV001', NULL, '2025-06-04 09:30:00', NULL, NULL, 'Xuất trưng bày showroom', 'Chờ duyệt', 'Hàng để bán'),
('YC003', 'NV001', NULL, '2025-06-04 10:45:00', NULL, NULL, 'Xuất sản phẩm lỗi cần xử lý', 'Chờ duyệt', 'Xuất hàng hỏng'),
('YC004', 'NV001', NULL, '2025-06-04 11:15:00', NULL, NULL, 'Xuất nội bộ cho nhóm kỹ thuật', 'Chờ duyệt', 'Hàng để bán'),
('YC005', 'NV001', NULL, '2025-06-04 13:00:00', NULL, NULL, 'Xuất đơn hàng online', 'Chờ duyệt', 'Hàng để bán'),
('YC006', 'NV004', NULL, '2025-06-05 08:00:00', NULL, NULL, 'Xuất cho đối tác 1', 'Chờ duyệt', 'Hàng để bán'),
('YC007', 'NV004', 'NV002', '2025-06-05 09:00:00', '2025-06-05 09:30:00', NULL, 'Xuất hội thảo', 'Đã duyệt', 'Hàng để bán'),
('YC008', 'NV005', 'NV002', '2025-06-05 10:00:00', '2025-06-05 10:15:00', '2025-06-05 11:00:00', 'Xuất demo', 'Đã xuất', 'Hàng để bán'),
('YC009', 'NV004', NULL, '2025-06-05 11:30:00', NULL, NULL, 'Hỏng cần xử lý', 'Chờ duyệt', 'Xuất hàng hỏng'),
('YC010', 'NV005', 'NV003', '2025-06-05 13:00:00', '2025-06-05 13:30:00', NULL, 'Xuất trả hàng', 'Đã duyệt', 'Hàng để bán'),
('YC011', 'NV005', 'NV003', '2025-06-05 14:15:00', '2025-06-05 14:30:00', '2025-06-05 15:00:00', 'Xuất bảo hành', 'Đã xuất', 'Xuất hàng hỏng'),
('YC012', 'NV006', NULL, '2025-06-05 15:15:00', NULL, NULL, 'Xuất kiểm thử', 'Chờ duyệt', 'Hàng để bán'),
('YC013', 'NV006', NULL, '2025-06-05 15:45:00', NULL, NULL, 'Hủy đơn lỗi', 'Từ chối', 'Hàng để bán'),
('YC014', 'NV004', 'NV005', '2025-06-05 16:00:00', '2025-06-05 16:30:00', NULL, 'Xuất gấp', 'Đã duyệt', 'Hàng để bán'),
('YC015', 'NV005', 'NV005', '2025-06-05 17:00:00', '2025-06-05 17:30:00', '2025-06-05 18:00:00', 'Xuất tạm', 'Đã xuất', 'Hàng để bán'),
('YC016', 'NV006', NULL, '2025-06-05 18:15:00', NULL, NULL, 'Dự phòng', 'Chờ duyệt', 'Hàng để bán'),
('YC017', 'NV006', NULL, '2025-06-05 18:45:00', NULL, NULL, 'Thử nghiệm sản phẩm', 'Từ chối', 'Xuất hàng hỏng'),
('YC018', 'NV005', 'NV002', '2025-06-05 19:15:00', '2025-06-05 19:30:00', NULL, 'Xuất nội bộ', 'Đã duyệt', 'Hàng để bán'),
('YC019', 'NV004', 'NV002', '2025-06-05 20:00:00', '2025-06-05 20:30:00', NULL, 'Trưng bày hội nghị', 'Đã duyệt', 'Hàng để bán'),
('YC020', 'NV006', NULL, '2025-06-05 21:00:00', NULL, NULL, 'Đơn khách hàng mới', 'Chờ duyệt', 'Hàng để bán'),
('YC021', 'NV001', 'NV002', '2025-06-06 09:00:00', '2025-06-06 09:15:00', NULL, 'Test mismatch 1', 'Đã duyệt', 'Hàng để bán'),
('YC022', 'NV004', 'NV003', '2025-06-06 10:00:00', '2025-06-06 10:30:00', NULL, 'Test mismatch 2', 'Đã duyệt', 'Hàng để bán'),
('YC023', 'NV006', 'NV005', '2025-06-06 11:00:00', '2025-06-06 11:30:00', NULL, 'Test mismatch 3', 'Đã duyệt', 'Hàng để bán');

INSERT INTO chi_tiet_yeu_cau_xuat (id_yeu_cau_xuat, id_san_pham, so_luong, so_luong_thuc, ghi_chu)
VALUES
('YC001', 'SP002', 5, 5, 'Chuột kèm theo'),
('YC002', 'SP003', 2, 2, 'Trưng bày bàn phím'),
('YC002', 'SP004', 1, 1, 'Trưng bày màn hình'),
('YC003', 'SP005', 2, 1, 'Hỏng cần xử lý'),                -- mismatch
('YC003', 'SP001', 1, 1, 'Laptop lỗi bàn phím'),
('YC004', 'SP002', 3, 3, 'Dùng nội bộ'),
('YC004', 'SP005', 2, 2, 'Lắp ráp thử nghiệm'),
('YC005', 'SP004', 1, 1, 'Chuẩn bị giao hàng'),
('YC005', 'SP003', 1, 0, 'Giao đơn online'),              -- mismatch
('YC006', 'SP001', 2, 2, 'Demo laptop'),
('YC006', 'SP002', 5, 4, 'Chuột không dây'),              -- mismatch
('YC007', 'SP003', 1, 1, 'Xuất bàn phím cơ'),
('YC007', 'SP004', 2, 2, 'Màn hình hội thảo'),
('YC008', 'SP005', 3, 3, 'Ổ cứng demo'),
('YC008', 'SP001', 1, 1, 'Laptop kiểm thử'),
('YC009', 'SP002', 4, 3, 'Chuột lỗi cần đổi'),            -- mismatch
('YC009', 'SP003', 2, 2, 'Xuất lỗi kỹ thuật'),
('YC010', 'SP004', 1, 1, 'Màn hình hoàn trả'),
('YC010', 'SP005', 1, 1, 'Ổ cứng hoàn trả'),
('YC011', 'SP001', 2, 2, 'Laptop bảo hành'),
('YC011', 'SP002', 3, 3, 'Chuột bảo hành'),
('YC012', 'SP003', 2, 2, 'Kiểm thử layout'),
('YC012', 'SP004', 1, 1, 'Màn hình kiểm tra'),
('YC013', 'SP005', 2, 2, 'Bị từ chối đơn lỗi'),
('YC013', 'SP001', 1, 1, 'Sai sản phẩm'),
('YC014', 'SP002', 5, 5, 'Xuất gấp cho dự án'),
('YC014', 'SP003', 2, 2, 'Bàn phím dự án'),
('YC015', 'SP004', 1, 1, 'Tạm xuất thử nghiệm'),
('YC015', 'SP005', 3, 3, 'Ổ cứng cho QA'),
('YC016', 'SP001', 2, 2, 'Dự phòng hệ thống'),
('YC016', 'SP002', 1, 1, 'Chuột dự phòng'),
('YC017', 'SP003', 2, 2, 'Không đạt kiểm thử'),
('YC017', 'SP004', 1, 1, 'Hỏng màn hình'),
('YC018', 'SP005', 2, 2, 'Xuất nội bộ thử'),
('YC018', 'SP001', 1, 1, 'Kiểm tra vận hành'),
('YC019', 'SP002', 4, 4, 'Trưng bày sản phẩm'),
('YC019', 'SP003', 2, 2, 'Dùng hội nghị'),
('YC020', 'SP004', 1, 1, 'Giao khách mới'),
('YC020', 'SP005', 2, 2, 'Ổ cứng khách mới'),
('YC021', 'SP001', 3, 2, 'Laptop thiếu 1'),
('YC022', 'SP002', 5, 4, 'Chuột thiếu 1'),
('YC023', 'SP003', 2, 0, 'Không xuất được');


INSERT INTO hang_xuat_kho (id_yeu_cau_xuat, id_nhan_vien_xuat, id_san_pham, so_luong, ghi_chu, thoi_gian_xuat)
VALUES
('YC008', 'NV002', 'SP005', 3, 'Ổ cứng demo', '2025-06-05 11:00:00'),
('YC008', 'NV002', 'SP001', 1, 'Laptop kiểm thử', '2025-06-05 11:00:00'),
('YC011', 'NV004', 'SP001', 2, 'Laptop bảo hành', '2025-06-05 15:00:00'),
('YC011', 'NV004', 'SP002', 3, 'Chuột bảo hành', '2025-06-05 15:00:00'),
('YC015', 'NV003', 'SP004', 1, 'Tạm xuất thử nghiệm', '2025-06-05 18:00:00'),
('YC015', 'NV003', 'SP005', 3, 'Ổ cứng cho QA', '2025-06-05 18:00:00');
