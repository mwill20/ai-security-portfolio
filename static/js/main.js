// Main JavaScript for the portfolio website
document.addEventListener('DOMContentLoaded', function() {
    // Enhanced smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            e.preventDefault();
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const headerOffset = 80; // Height of fixed header
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
                
                // Update URL without page jump
                if (history.pushState) {
                    history.pushState(null, null, targetId);
                } else {
                    window.location.hash = targetId;
                }
            }
        });
    });

    // Back to top button functionality
    const backToTopButton = document.querySelector('.back-to-top');
    if (backToTopButton) {
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.add('visible');
            } else {
                backToTopButton.classList.remove('visible');
            }
        });
        
        backToTopButton.addEventListener('click', (e) => {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Add active class to current navigation item based on scroll position
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a, .footer-links a[href^="#"]');
    
    const makeActive = (link) => {
        navLinks.forEach(link => link.classList.remove('active'));
        link.classList.add('active');
    };
    
    const sectionMargin = 200;
    let currentActive = '';
    
    const checkSectionInView = () => {
        sections.forEach(section => {
            const sectionTop = section.offsetTop - sectionMargin;
            const sectionBottom = sectionTop + section.offsetHeight;
            
            if (window.scrollY >= sectionTop && window.scrollY < sectionBottom) {
                const id = '#' + section.getAttribute('id');
                if (currentActive !== id) {
                    currentActive = id;
                    navLinks.forEach(link => {
                        if (link.getAttribute('href') === id) {
                            makeActive(link);
                        }
                    });
                }
            }
        });
    };
    
    // Initial check
    checkSectionInView();
    
    // Check on scroll
    window.addEventListener('scroll', checkSectionInView);
    
    // Form submission feedback
    const messageForm = document.querySelector('.message-form');
    if (messageForm) {
        messageForm.addEventListener('submit', function(e) {
            const submitButton = this.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.textContent = 'Sending...';
                submitButton.classList.add('sending');
            }
        });
    }
    
    // Add animation to elements on scroll
    const animateOnScroll = () => {
        const animatedElements = document.querySelectorAll('.project-card, .timeline-content, .skills-card');
        animatedElements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.3;
            
            if (elementPosition < screenPosition) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };

    // Initial check
    animateOnScroll();
    
    // Check on scroll
    window.addEventListener('scroll', animateOnScroll);
    
    // Component Detail View
    const detailView = document.getElementById('component-detail-view');
    const closeDetailBtn = document.getElementById('close-detail-view');
    const detailContent = document.getElementById('detail-view-content');
    
    if (closeDetailBtn) {
        closeDetailBtn.addEventListener('click', hideComponentDetail);
    }
    
    // Close detail view when clicking outside content
    if (detailView) {
        detailView.addEventListener('click', (e) => {
            if (e.target === detailView) {
                hideComponentDetail();
            }
        });
    }
    
    // Handle escape key to close detail view
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && detailView && detailView.classList.contains('active')) {
            hideComponentDetail();
        }
    });
    
    function showComponentDetail(componentId) {
        const detailElement = document.getElementById(`${componentId}-detail`);
        if (detailElement && detailContent) {
            detailContent.innerHTML = '';
            detailContent.appendChild(detailElement.cloneNode(true));
            document.body.style.overflow = 'hidden';
            detailView.classList.add('active');
            
            // Focus the close button for better keyboard navigation
            setTimeout(() => {
                const closeBtn = detailView.querySelector('.close-btn');
                if (closeBtn) closeBtn.focus();
            }, 100);
        }
    }
    
    function hideComponentDetail() {
        if (detailView) {
            detailView.classList.remove('active');
            document.body.style.overflow = '';
            
            // Return focus to the button that opened the detail view
            const activeComponent = document.querySelector('.mcp-component.active');
            if (activeComponent) {
                const viewDetailsBtn = activeComponent.querySelector('.btn-view-details');
                if (viewDetailsBtn) viewDetailsBtn.focus();
            }
        }
    }

    // MCP Component Toggle Functionality
    const mcpComponents = document.querySelectorAll('.mcp-component');
    
    mcpComponents.forEach(component => {
        const header = component.querySelector('.mcp-component-header');
        const content = component.querySelector('.mcp-component-content');
        const toggleIcon = component.querySelector('.toggle-icon');
        const viewDetailsBtn = component.querySelector('.btn-view-details');
        const componentId = component.getAttribute('data-component');
        
        // Toggle component content on header click
        if (header && content) {
            header.addEventListener('click', (e) => {
                // Don't toggle if clicking on a link inside the header
                if (e.target.tagName === 'A' || e.target.closest('a')) {
                    return;
                }
                
                const isActive = component.classList.contains('active');
                
                // Close all other open components
                mcpComponents.forEach(comp => {
                    if (comp !== component && comp.classList.contains('active')) {
                        comp.classList.remove('active');
                        const otherContent = comp.querySelector('.mcp-component-content');
                        if (otherContent) {
                            otherContent.style.maxHeight = '0';
                            otherContent.style.paddingTop = '0';
                            otherContent.style.paddingBottom = '0';
                        }
                    }
                });
                
                // Toggle current component
                if (!isActive) {
                    component.classList.add('active');
                    content.style.maxHeight = content.scrollHeight + 'px';
                    content.style.paddingTop = '1rem';
                    content.style.paddingBottom = '1.5rem';
                    
                    // Scroll to the component if it's not fully in view
                    component.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                } else {
                    component.classList.remove('active');
                    content.style.maxHeight = '0';
                    content.style.paddingTop = '0';
                    content.style.paddingBottom = '0';
                }
            });
            
            // Handle view details button click
            if (viewDetailsBtn) {
                viewDetailsBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    // Add your view details functionality here
                    console.log('View details for:', componentId);
                });
            }
        }
    });
    
    // Highlight current year in footer
    const currentYear = new Date().getFullYear();
    const yearElement = document.getElementById('current-year');
    if (yearElement) {
        yearElement.textContent = currentYear;
    }

    // Project Filtering Logic
    const filterContainer = document.querySelector('#project-filters');
    if (filterContainer) {
        const filterButtons = filterContainer.querySelectorAll('.filter-btn');
        const projectGroups = document.querySelectorAll('.project-group');

        filterContainer.addEventListener('click', (e) => {
            if (!e.target.matches('.filter-btn')) return;

            const selectedFilter = e.target.dataset.filter;

            // Update active button state
            filterButtons.forEach(btn => btn.classList.remove('active'));
            e.target.classList.add('active');

            // Filter project groups
            projectGroups.forEach(group => {
                const groupCategory = group.dataset.category;
                if (selectedFilter === 'all' || selectedFilter === groupCategory) {
                    group.style.display = 'block';
                } else {
                    group.style.display = 'none';
                }
            });
        });
    }
});

// Simple console greeting
console.log("%c👋%c Hello there! Thanks for checking out my portfolio.", 
            "color: #2ecc71; font-size: 14px; font-weight: bold; margin-right: 5px;",
            "color: #2ecc71; font-size: 14px; font-weight: normal;");
console.log("%c🔍%c Curious about how this site works? Check out the source code on GitHub!", 
            "color: #2ecc71; font-size: 14px; margin-right: 5px;",
            "color: #2ecc71; font-size: 12px; font-weight: normal;");
