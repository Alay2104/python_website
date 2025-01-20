function filterPortfolio(categoryId) {
  const grid = document.getElementById('portfolio-grid');
  const items = grid.children;

  for (let item of items) {
    const itemCategory = item.getAttribute('data-category');
    if (categoryId === 'all' || itemCategory === categoryId) {
      item.style.display = 'block';
    } else {
      item.style.display = 'none';
    }
  }
}
