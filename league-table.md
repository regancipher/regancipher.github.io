---
layout: default
title: Audio League Table
permalink: /league-table/
---

# Audio League Table

## Dynamic Rankings Based on Measurements & Performance

This league table updates as I test new products. Rankings are based on objective measurements combined with real-world performance. Scores adjust relative to new competitors - a product that scored 8.5/10 might shift as better (or worse) options enter the market.

<div class="league-table-wrapper">
    <!-- Filter Controls -->
    <div class="table-controls">
        <div class="control-group">
            <label>Type:</label>
            <select id="filter-type">
                <option value="all">All Types</option>
                <option value="headphones">Headphones</option>
                <option value="iems">IEMs</option>
                <option value="dacs">DACs</option>
            </select>
        </div>
        
        <div class="control-group">
            <label>Price:</label>
            <select id="filter-price">
                <option value="all">All Prices</option>
                <option value="budget">Budget (< $100)</option>
                <option value="midfi">Mid-Fi ($100-500)</option>
                <option value="highend">High-End ($500-1000)</option>
                <option value="summitfi">Summit-Fi ($1000+)</option>
            </select>
        </div>
        
        <div class="control-group">
            <label>Sort:</label>
            <select id="sort-by">
                <option value="score">Overall Score</option>
                <option value="price">Price</option>
                <option value="name">Name</option>
            </select>
        </div>
    </div>

    <!-- The Table -->
    <div class="table-scroll">
        <table class="league-table">
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>Product</th>
                    <th>Type</th>
                    <th>Price</th>
                    <th>Score</th>
                    <th>Sound</th>
                    <th>Tech</th>
                    <th>Build</th>
                    <th>Value</th>
                    <th>Review</th>
                </tr>
            </thead>
            <tbody id="league-table-body">
                <!-- Example rows - you'll add more -->
                <tr class="rank-gold" data-type="headphones" data-price="budget" data-score="8.2">
                    <td>1</td>
                    <td><strong>QCY H3</strong></td>
                    <td>Headphones</td>
                    <td>$44.99</td>
                    <td class="score">8.2</td>
                    <td>8.0</td>
                    <td>7.5</td>
                    <td>7.0</td>
                    <td>9.5</td>
                    <td><a href="/reviews/2025/10/qcy-h3-review/">View</a></td>
                </tr>
                
                <!-- Add more rows here as you add reviews -->
                <!-- Template:
                <tr class="rank-silver" data-type="TYPE" data-price="BRACKET" data-score="X.X">
                    <td>RANK</td>
                    <td><strong>PRODUCT NAME</strong></td>
                    <td>TYPE</td>
                    <td>$XX.XX</td>
                    <td class="score">X.X</td>
                    <td>X.X</td>
                    <td>X.X</td>
                    <td>X.X</td>
                    <td>X.X</td>
                    <td><a href="/reviews/YYYY/MM/slug/">View</a></td>
                </tr>
                -->
            </tbody>
        </table>
    </div>
    
    <div class="table-note">
        <p><strong>Note:</strong> This table is manually curated and updated with each new review. Rankings may shift as new products enter the market.</p>
        <p><em>Last updated: November 3, 2025</em></p>
    </div>
</div>

## How the Rankings Work

### Scoring Categories

Each product is evaluated across multiple dimensions:

- **Sound Quality (40%)** - Frequency response accuracy, distortion, detail retrieval
- **Technical Performance (30%)** - Measurements, power output, noise floor
- **Build Quality (15%)** - Materials, durability, design
- **Value (15%)** - Price-to-performance ratio

### Dynamic Adjustments

Unlike static reviews, this table evolves:

- **New Competition**: When a better product launches at the same price, older products may see score adjustments
- **Price Changes**: Sales and discounts can boost value scores
- **Long-term Testing**: Extended use sometimes reveals issues (or strengths) not apparent in initial testing
- **Firmware Updates**: Improvements via software updates can increase scores

### Color Coding

- 🥇 **Gold** (9.0-10.0) - Exceptional, class-leading
- 🥈 **Silver** (8.0-8.9) - Excellent, highly recommended
- 🥉 **Bronze** (7.0-7.9) - Good, solid choice
- ⚪ **White** (6.0-6.9) - Decent, niche appeal
- 🔴 **Red** (Below 6.0) - Not recommended

---

## Updating This Table

**For you (when editing):**

To add a new product, copy this template and paste into the `<tbody>`:

```html
<tr class="rank-silver" data-type="iems" data-price="midfi" data-score="8.7">
    <td>2</td>
    <td><strong>Moondrop Blessing 3</strong></td>
    <td>IEMs</td>
    <td>$319.99</td>
    <td class="score">8.7</td>
    <td>9.0</td>
    <td>8.5</td>
    <td>8.0</td>
    <td>8.5</td>
    <td><a href="/reviews/2025/10/blessing-3-review/">View</a></td>
</tr>
```

**Change these values:**
- `class="rank-XXX"` - gold/silver/bronze/white/red based on score
- `data-type` - headphones/iems/dacs
- `data-price` - budget/midfi/highend/summitfi
- `data-score` - overall score for sorting
- All the table cells with your data

<style>
.league-table-wrapper {
    margin: 2rem 0;
}

.table-controls {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
    background: var(--secondary-bg);
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid var(--border-color);
}

.control-group {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.control-group label {
    font-weight: 600;
    color: var(--accent-color);
}

.control-group select {
    background: var(--tertiary-bg);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    padding: 0.5rem 1rem;
    border-radius: 4px;
    font-family: inherit;
}

.table-scroll {
    overflow-x: auto;
    background: var(--secondary-bg);
    border: 1px solid var(--border-color);
    border-radius: 8px;
}

.league-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
}

.league-table thead {
    background: var(--tertiary-bg);
    border-bottom: 2px solid var(--accent-color);
}

.league-table th {
    padding: 1rem;
    text-align: left;
    font-weight: 600;
    color: var(--accent-color);
    white-space: nowrap;
}

.league-table td {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--border-color);
}

.league-table tbody tr {
    transition: background 0.2s;
}

.league-table tbody tr:hover {
    background: var(--tertiary-bg);
}

.league-table .score {
    font-weight: 700;
    font-size: 1.1rem;
}

/* Rank color coding */
.rank-gold { background: rgba(212, 175, 55, 0.1); }
.rank-gold .score { color: #d4af37; }

.rank-silver { background: rgba(192, 192, 192, 0.1); }
.rank-silver .score { color: #c0c0c0; }

.rank-bronze { background: rgba(205, 127, 50, 0.1); }
.rank-bronze .score { color: #cd7f32; }

.rank-white .score { color: var(--text-primary); }

.rank-red { background: rgba(248, 81, 73, 0.1); }
.rank-red .score { color: #f85149; }

.table-note {
    margin-top: 1rem;
    padding: 1rem;
    background: var(--tertiary-bg);
    border-radius: 4px;
    font-size: 0.875rem;
    color: var(--text-secondary);
}

@media (max-width: 768px) {
    .table-controls {
        flex-direction: column;
    }
    
    .control-group {
        width: 100%;
        justify-content: space-between;
    }
}
</style>

<script>
// Simple filtering and sorting (no external dependencies)
document.addEventListener('DOMContentLoaded', function() {
    const table = document.getElementById('league-table-body');
    const typeFilter = document.getElementById('filter-type');
    const priceFilter = document.getElementById('filter-price');
    const sortBy = document.getElementById('sort-by');
    
    function filterAndSort() {
        const rows = Array.from(table.querySelectorAll('tr'));
        const type = typeFilter.value;
        const price = priceFilter.value;
        const sort = sortBy.value;
        
        // Filter
        rows.forEach(row => {
            const matchType = type === 'all' || row.dataset.type === type;
            const matchPrice = price === 'all' || row.dataset.price === price;
            row.style.display = (matchType && matchPrice) ? '' : 'none';
        });
        
        // Sort visible rows
        const visibleRows = rows.filter(row => row.style.display !== 'none');
        visibleRows.sort((a, b) => {
            if (sort === 'score') {
                return parseFloat(b.dataset.score) - parseFloat(a.dataset.score);
            } else if (sort === 'price') {
                const priceA = parseFloat(a.cells[3].textContent.replace('$', ''));
                const priceB = parseFloat(b.cells[3].textContent.replace('$', ''));
                return priceA - priceB;
            } else { // name
                return a.cells[1].textContent.localeCompare(b.cells[1].textContent);
            }
        });
        
        // Re-append in sorted order
        visibleRows.forEach(row => table.appendChild(row));
        
        // Update rank numbers
        let rank = 1;
        visibleRows.forEach(row => {
            row.cells[0].textContent = rank++;
        });
    }
    
    typeFilter.addEventListener('change', filterAndSort);
    priceFilter.addEventListener('change', filterAndSort);
    sortBy.addEventListener('change', filterAndSort);
});
</script>
