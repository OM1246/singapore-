with open('c:/Users/Om/Documents/Demo_singpour/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Verify we're targeting the right block
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<div class="why-grid">' in line:
        start_idx = i
        break

if start_idx != -1:
    for i in range(start_idx, len(lines)):
        # find the end of the why-grid (it's the second closing div from the start of the container, but since it's exactly where we saw it...)
        if '<!-- Card 6 -->' in lines[i - 10] if i >= 10 else False:
            if '</div>' in lines[i] and '</div>' in lines[i-1] and '</div>' in lines[i-2]:
                # find the closing div of why-grid, it's at indentation of why-grid
                if lines[i].strip() == '</div>' and len(lines[i]) - len(lines[i].lstrip()) == 12:
                    end_idx = i
                    break

new_content = """            <style>
                .property-images-grid {
                    display: grid;
                    grid-template-columns: repeat(3, 1fr);
                    gap: 2rem;
                    margin-top: 3rem;
                }
                .prop-img-box {
                    position: relative;
                    border-radius: 20px;
                    overflow: hidden;
                    cursor: pointer;
                    box-shadow: 0 15px 35px rgba(15, 23, 42, 0.08);
                    aspect-ratio: 4/3;
                }
                .prop-img-box img {
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                    transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
                }
                .prop-img-box:hover img {
                    transform: scale(1.08);
                }
                .prop-img-box::after {
                    content: 'Click to view details';
                    position: absolute;
                    bottom: 0; left: 0; right: 0;
                    background: linear-gradient(0deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%);
                    color: white;
                    padding: 30px 20px 20px;
                    text-align: center;
                    font-family: var(--font-body);
                    font-weight: 600;
                    opacity: 0;
                    transition: opacity 0.3s;
                }
                .prop-img-box:hover::after {
                    opacity: 1;
                }
                @media(max-width: 900px) {
                    .property-images-grid { grid-template-columns: 1fr; }
                }
                
                /* Modal Styles */
                .why-modal-overlay {
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
                .why-modal-content {
                    background: white;
                    padding: 3rem;
                    border-radius: 24px;
                    max-width: 800px;
                    width: 100%;
                    max-height: 85vh;
                    overflow-y: auto;
                    position: relative;
                    box-shadow: 0 25px 50px rgba(0,0,0,0.2);
                    animation: modalScaleIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
                }
                @keyframes modalScaleIn {
                    from { transform: scale(0.95); opacity: 0; }
                    to { transform: scale(1); opacity: 1; }
                }
                .why-modal-close {
                    position: absolute;
                    top: 20px;
                    right: 25px;
                    font-size: 28px;
                    color: var(--text-secondary);
                    cursor: pointer;
                    transition: color 0.3s;
                }
                .why-modal-close:hover {
                    color: var(--accent-red);
                }
                .why-modal-title {
                    color: var(--text-primary);
                    font-family: var(--font-heading);
                    font-size: 2.2rem;
                    margin-bottom: 2rem;
                    line-height: 1.2;
                }
                .why-modal-list {
                    list-style: none;
                    padding: 0;
                    margin: 0;
                }
                .why-modal-list li {
                    position: relative;
                    padding-left: 35px;
                    margin-bottom: 1.2rem;
                    font-family: var(--font-body);
                    font-size: 1.1rem;
                    color: var(--text-secondary);
                    line-height: 1.6;
                }
                .why-modal-list li i {
                    position: absolute;
                    left: 0;
                    top: 4px;
                    color: var(--accent-red);
                    font-size: 1.2rem;
                }
            </style>

            <div class="property-images-grid">
                <div class="prop-img-box" onclick="document.getElementById('whyAttendModal').style.display='flex'">
                    <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80" alt="Premium Residential">
                </div>
                <div class="prop-img-box" onclick="document.getElementById('whyAttendModal').style.display='flex'">
                    <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80" alt="Investment Projects">
                </div>
                <div class="prop-img-box" onclick="document.getElementById('whyAttendModal').style.display='flex'">
                    <img src="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80" alt="Luxury Real Estate">
                </div>
            </div>

            <div id="whyAttendModal" class="why-modal-overlay" onclick="if(event.target === this) this.style.display='none'">
                <div class="why-modal-content">
                    <span class="why-modal-close" onclick="document.getElementById('whyAttendModal').style.display='none'"><i class="fa-solid fa-xmark"></i></span>
                    <h3 class="why-modal-title">Why Attend the Indian Property Show in Singapore?</h3>
                    <ul class="why-modal-list">
                        <li><i class="fa-solid fa-check-circle"></i> Explore premium residential and investment projects from Hyderabad, Vizag, Chennai, and Bangalore under one roof.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Meet leading and trusted Indian developers directly and get your questions answered.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Compare multiple projects, locations, pricing, and amenities in a single visit.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Discover exclusive event-only offers, discounts, and flexible payment plans.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Learn about high-growth real estate markets with strong appreciation potential.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Find properties suited for investment, retirement, or future relocation.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Get expert guidance on NRI property purchases, legal procedures, taxation, and home loans.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Understand the latest market trends and investment opportunities in South India's fastest-growing cities.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Save time by evaluating multiple options without traveling to India.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Book your preferred property with confidence after interacting directly with developers and experts.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Receive personalized investment advice based on your budget and goals.</li>
                        <li><i class="fa-solid fa-check-circle"></i> Network with real estate professionals and industry experts to make informed decisions</li>
                    </ul>
                </div>
            </div>\n"""

print(f"Found block from {start_idx} to {end_idx}")
if start_idx != -1 and end_idx != -1:
    lines[start_idx:end_idx+1] = [new_content]
    with open('c:/Users/Om/Documents/Demo_singpour/index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Replaced successfully!")
else:
    print("Could not find exact bounds!")
