document.addEventListener('DOMContentLoaded', function () {
    const userMenu = document.querySelector('.user-menu');
    const dropDown = userMenu.querySelector('.drop-down');

    // Toggle dropdown
    userMenu.addEventListener('click', function (e) {
        e.stopPropagation();
        dropDown.classList.toggle('show');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function () {
        dropDown.classList.remove('show');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const submenuToggles = document.querySelectorAll('.submenu-toggle');

    submenuToggles.forEach(toggle => {
        const parentItem = toggle.closest('.has-submenu');

        toggle.addEventListener('click', function (e) {
            e.stopPropagation();
            const isOpen = parentItem.classList.contains('open');
            parentItem.classList.toggle('open');
            localStorage.setItem('exportMenuOpen', !isOpen); // Lưu trạng thái
        });

        const submenu = parentItem.querySelector('.sub-menu');
        submenu.addEventListener('click', e => e.stopPropagation());
        submenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', e => e.stopPropagation());
        });
    });

    document.addEventListener('click', function (e) {
        if (!e.target.closest('.has-submenu')) {
            document.querySelectorAll('.has-submenu.open').forEach(item => {
                item.classList.remove('open');
                localStorage.setItem('exportMenuOpen', false); // Reset nếu click ngoài
            });
        }
    });
});

// ✅ Quan trọng: chỉ mở lại menu sau khi trang và DOM đã load xong
window.addEventListener('load', function () {
    const exportMenu = document.querySelector('.has-submenu');
    if (localStorage.getItem('exportMenuOpen') === 'true' && exportMenu) {
        exportMenu.classList.add('open');
    }
});
