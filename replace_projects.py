with open('c:/Users/Om/Documents/Demo_singpour/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# We want to replace everything from <style> (line 2178) all the way down to the closing </script> at line 2355.
# Let's find the position of:
# <h3 style="text-align: center; margin-top: 2rem; font-size: 2.5rem; color: var(--text-primary); font-family: var(--font-heading);">Our Projects</h3>
#             </div>

pattern = r'(<h3[^>]*>Our Projects</h3>\s*</div>\s*)<style>.*?</script>'

match = re.search(pattern, text, re.DOTALL)

if match:
    new_content = """<style>
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.5rem;
        margin-top: 3rem;
    }
    .project-card {
        border-radius: 20px;
        overflow: hidden;
        position: relative;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        aspect-ratio: 3/4;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    .project-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.6s ease;
    }
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(194, 24, 50, 0.2);
    }
    .project-card:hover img {
        transform: scale(1.1);
    }
    .project-card-overlay {
        position: absolute;
        bottom: 0; left: 0; right: 0;
        background: linear-gradient(to top, rgba(15,23,42,0.95), transparent);
        padding: 40px 20px 20px;
        color: white;
    }
    .project-card-title {
        font-family: var(--font-heading);
        font-size: 1.5rem;
        margin-bottom: 5px;
    }
    .project-card-location {
        font-family: var(--font-body);
        font-size: 0.9rem;
        color: #ddd;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    @media(max-width: 1024px) {
        .projects-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media(max-width: 600px) {
        .projects-grid { grid-template-columns: 1fr; }
    }
    
    /* Project Modal Styles */
    .project-modal-overlay {
        display: none;
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(15, 23, 42, 0.85);
        z-index: 9999;
        justify-content: center;
        align-items: center;
        padding: 20px;
        backdrop-filter: blur(5px);
    }
    .project-modal-content {
        background: white;
        padding: 3rem;
        border-radius: 24px;
        max-width: 500px;
        width: 100%;
        max-height: 85vh;
        overflow-y: auto;
        position: relative;
        box-shadow: 0 30px 60px rgba(0,0,0,0.25), 0 0 0 1px rgba(0,0,0,0.05);
        animation: modalScaleIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes modalScaleIn {
        from { transform: scale(0.95) translateY(20px); opacity: 0; }
        to { transform: scale(1) translateY(0); opacity: 1; }
    }
    .project-modal-close {
        position: absolute;
        top: 20px;
        right: 25px;
        font-size: 28px;
        color: var(--text-secondary);
        cursor: pointer;
        transition: transform 0.3s, color 0.3s;
    }
    .project-modal-close:hover {
        color: var(--accent-red);
        transform: rotate(90deg);
    }
    .project-modal-title {
        color: var(--text-primary);
        font-family: var(--font-heading);
        font-size: 2rem;
        margin-bottom: 1.5rem;
        line-height: 1.2;
    }
    .project-modal-details {
        display: flex;
        flex-direction: column;
        gap: 1.2rem;
    }
    .project-detail-item {
        display: flex;
        justify-content: space-between;
        padding-bottom: 0.8rem;
        border-bottom: 1px solid rgba(0,0,0,0.05);
        font-family: var(--font-body);
    }
    .project-detail-label {
        font-weight: 600;
        color: var(--text-secondary);
    }
    .project-detail-value {
        font-weight: 700;
        color: var(--text-primary);
        text-align: right;
    }
    .project-modal-extra {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 10px;
        font-size: 0.9rem;
        color: var(--accent-red);
        font-weight: 600;
        text-align: center;
        margin-top: 1rem;
    }
</style>

<div class="projects-grid">
    <div class="project-card" onclick="openProjectModal('Lumina', 'Miyapur', '3BHK', '1550 - 2550 Sqft', '1.31cr ++', 'Dec 2028', 'G+13 Storey', 'Each floor 16 units with one single tower')">
        <img src="1.jpeg" alt="Lumina">
        <div class="project-card-overlay">
            <h4 class="project-card-title">Lumina</h4>
            <div class="project-card-location"><i class="fa-solid fa-location-dot"></i> Miyapur</div>
        </div>
    </div>
    
    <div class="project-card" onclick="openProjectModal('Botanika', 'Gachibowli', '3BHK', '2252 - 2660 Sqft', '3.5cr ++', 'Ready to move', '', '')">
        <img src="2.jpeg" alt="Botanika">
        <div class="project-card-overlay">
            <h4 class="project-card-title">Botanika</h4>
            <div class="project-card-location"><i class="fa-solid fa-location-dot"></i> Gachibowli</div>
        </div>
    </div>
    
    <div class="project-card" onclick="openProjectModal('Parkview', 'Gachibowli', '3BHK', '1725 2168 Sqft', '2cr ++', 'March 2027', 'G+ 21 storey', '')">
        <img src="3.jpeg" alt="Parkview">
        <div class="project-card-overlay">
            <h4 class="project-card-title">Parkview</h4>
            <div class="project-card-location"><i class="fa-solid fa-location-dot"></i> Gachibowli</div>
        </div>
    </div>
    
    <div class="project-card" onclick="openProjectModal('Beaumomde', 'Kokapet', '3BHK', '1860 - 2350 Sqft', '2.20cr ++', 'March 2028', 'G+14 Storey', 'EACH FLOOR 10 UNITS WITH SIX LIFTS')">
        <img src="4.jpeg" alt="Beaumomde">
        <div class="project-card-overlay">
            <h4 class="project-card-title">Beaumomde</h4>
            <div class="project-card-location"><i class="fa-solid fa-location-dot"></i> Kokapet</div>
        </div>
    </div>
</div>

<div id="projectModal" class="project-modal-overlay" onclick="if(event.target === this) document.getElementById('projectModal').style.display='none'">
    <div class="project-modal-content">
        <span class="project-modal-close" onclick="document.getElementById('projectModal').style.display='none'"><i class="fa-solid fa-xmark"></i></span>
        <h3 class="project-modal-title" id="pm-title">Project Name</h3>
        
        <div class="project-modal-details">
            <div class="project-detail-item">
                <span class="project-detail-label">Location</span>
                <span class="project-detail-value" id="pm-location">-</span>
            </div>
            <div class="project-detail-item">
                <span class="project-detail-label">Configuration</span>
                <span class="project-detail-value" id="pm-config">-</span>
            </div>
            <div class="project-detail-item" id="pm-storey-container">
                <span class="project-detail-label">Storey</span>
                <span class="project-detail-value" id="pm-storey">-</span>
            </div>
            <div class="project-detail-item">
                <span class="project-detail-label">Carpet Area</span>
                <span class="project-detail-value" id="pm-carpet">-</span>
            </div>
            <div class="project-detail-item">
                <span class="project-detail-label">Pricing</span>
                <span class="project-detail-value" id="pm-pricing">-</span>
            </div>
            <div class="project-detail-item">
                <span class="project-detail-label">Possession</span>
                <span class="project-detail-value" id="pm-possession">-</span>
            </div>
        </div>
        
        <div id="pm-extra" class="project-modal-extra"></div>
    </div>
</div>

<script>
    function openProjectModal(name, loc, config, carpet, price, pos, storey, extra) {
        document.getElementById('pm-title').innerText = name;
        document.getElementById('pm-location').innerText = loc;
        document.getElementById('pm-config').innerText = config;
        document.getElementById('pm-carpet').innerText = carpet;
        document.getElementById('pm-pricing').innerText = price;
        document.getElementById('pm-possession').innerText = pos;
        
        if (storey) {
            document.getElementById('pm-storey-container').style.display = 'flex';
            document.getElementById('pm-storey').innerText = storey;
        } else {
            document.getElementById('pm-storey-container').style.display = 'none';
        }
        
        const extraEl = document.getElementById('pm-extra');
        if (extra) {
            extraEl.style.display = 'block';
            extraEl.innerText = extra;
        } else {
            extraEl.style.display = 'none';
        }
        
        document.getElementById('projectModal').style.display = 'flex';
    }
    
    // Move modal to body to fix stacking context issues
    setTimeout(() => {
        const modal = document.getElementById('projectModal');
        if (modal) document.body.appendChild(modal);
    }, 100);
</script>"""

    new_text = text[:match.start()] + match.group(1) + new_content + text[match.end():]
    with open('c:/Users/Om/Documents/Demo_singpour/index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced successfully!")
else:
    print("Match not found!")
