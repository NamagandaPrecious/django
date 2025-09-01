<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Precious Wakabi | Portfolio</title>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            primary: '#6D28D9',  // Purple
            secondary: '#10B981', // Green
            darkBg: '#121212',
            darkCard: '#1E1E1E',
            darkText: '#F3F4F6',
            lightBg: '#F9FAFB',
            lightCard: '#FFFFFF',
            lightText: '#1F2937',
          },
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
            display: ['Poppins', 'sans-serif'],
          }
        },
      }
    }
  </script>
  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <!-- AOS Animation -->
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <style id="app-style">
    .timeline-item::before {
      content: '';
      position: absolute;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      left: -8px;
      top: 8px;
      background-color: #6D28D9;
      border: 2px solid #F3F4F6;
    }
    
    .timeline-line {
      position: absolute;
      left: 0;
      top: 16px;
      bottom: -16px;
      width: 1px;
      background-color: #6D28D9;
    }
    
    .timeline-item:last-child .timeline-line {
      display: none;
    }

    .skill-badge {
      transition: all 0.3s ease;
    }
    
    .skill-badge:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 15px -3px rgba(109, 40, 217, 0.3);
    }

    .project-card {
      transition: all 0.3s ease;
    }
    
    .project-card:hover {
      transform: translateY(-8px);
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
    }
    
    .dark ::-webkit-scrollbar-track {
      background: #1E1E1E;
    }
    
    .dark ::-webkit-scrollbar-thumb {
      background: #6D28D9;
      border-radius: 4px;
    }
    
    ::-webkit-scrollbar-track {
      background: #F3F4F6;
    }
    
    ::-webkit-scrollbar-thumb {
      background: #6D28D9;
      border-radius: 4px;
    }
  </style>
</head>
<body class="bg-lightBg text-lightText dark:bg-darkBg dark:text-darkText font-sans">
  <!-- Header -->
  <header class="fixed top-0 left-0 right-0 z-50 bg-white/80 dark:bg-darkBg/80 backdrop-blur-md shadow-sm">
    <div class="container mx-auto px-4 py-4 flex justify-between items-center">
      <a href="javascript:void(0)" class="text-xl font-bold font-display flex items-center gap-2">
        <span class="text-primary">Precious</span>
        <span class="hidden sm:inline">Wakabi</span>
      </a>
      
      <div class="hidden md:flex items-center space-x-6">
        <a href="#hero" class="hover:text-primary transition-colors">Home</a>
        <a href="#skills" class="hover:text-primary transition-colors">Skills</a>
        <a href="#education" class="hover:text-primary transition-colors">Education</a>
        <a href="#projects" class="hover:text-primary transition-colors">Projects</a>
        <a href="#leadership" class="hover:text-primary transition-colors">Leadership</a>
        <a href="#contact" class="hover:text-primary transition-colors">Contact</a>
      </div>
      
      <div class="flex items-center gap-4">
        <button id="darkModeToggle" class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-darkCard transition">
          <i class="fas fa-sun hidden dark:inline-block text-yellow-400"></i>
          <i class="fas fa-moon inline-block dark:hidden text-slate-700"></i>
        </button>
        
        <button id="mobileMenuToggle" class="md:hidden p-2 rounded-md hover:bg-gray-100 dark:hover:bg-darkCard transition">
          <i class="fas fa-bars"></i>
        </button>
      </div>
    </div>
    
    <!-- Mobile menu -->
    <div id="mobileMenu" class="md:hidden hidden bg-white dark:bg-darkBg shadow-md">
      <div class="container mx-auto px-4 py-3 flex flex-col space-y-3">
        <a href="#hero" class="py-2 hover:text-primary transition-colors">Home</a>
        <a href="#skills" class="py-2 hover:text-primary transition-colors">Skills</a>
        <a href="#education" class="py-2 hover:text-primary transition-colors">Education</a>
        <a href="#projects" class="py-2 hover:text-primary transition-colors">Projects</a>
        <a href="#leadership" class="py-2 hover:text-primary transition-colors">Leadership</a>
        <a href="#contact" class="py-2 hover:text-primary transition-colors">Contact</a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section id="hero" class="min-h-screen flex items-center pt-24 pb-12">
    <div class="container mx-auto px-4">
      <div class="flex flex-col md:flex-row items-center gap-8 md:gap-12">
        <div class="w-full md:w-1/2" data-aos="fade-right">
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold font-display mb-4">
            Hi, I'm <span class="text-primary">Precious Wakabi</span>
          </h1>
          <h2 class="text-xl md:text-2xl font-medium mb-6">Computer Science Student & Tech Enthusiast</h2>
          <p class="text-gray-600 dark:text-gray-300 mb-8 text-lg leading-relaxed">
            Adaptive, hardworking, and self-motivated Computer Science student with strong analytical and problem-solving skills. 
            Passionate about data analytics, software development, and networking. 
            Enthusiastic about AI and data-driven projects.
          </p>
          <div class="flex flex-wrap gap-4">
            <a href="javascript:void(0)" id="downloadCV" class="px-6 py-3 bg-primary text-white rounded-md hover:bg-purple-700 transition font-medium flex items-center gap-2">
              <i class="fas fa-download"></i>
              Download CV
            </a>
            <a href="#contact" class="px-6 py-3 border-2 border-primary text-primary dark:text-white rounded-md hover:bg-primary hover:text-white transition font-medium flex items-center gap-2">
              <i class="fas fa-envelope"></i>
              Contact Me
            </a>
          </div>
          <div class="mt-8 flex gap-5">
            <a href="https://github.com/WakabiPrecious" target="_blank" class="text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary text-xl transition">
              <i class="fab fa-github"></i>
            </a>
            <a href="mailto:preciouswakabi@gmail.com" class="text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary text-xl transition">
              <i class="fas fa-envelope"></i>
            </a>
            <a href="tel:+256756989388" class="text-gray-600 dark:text-gray-300 hover:text-primary dark:hover:text-primary text-xl transition">
              <i class="fas fa-phone"></i>
            </a>
          </div>
        </div>
        <div class="w-full md:w-1/2" data-aos="fade-left">
          <img src="https://cdn.pixabay.com/photo/2018/11/08/23/52/developer-3803901_1280.png" alt="Illustration of developer" class="w-full h-auto max-w-lg mx-auto" />
        </div>
      </div>
    </div>
  </section>

  <!-- Skills Section -->
  <section id="skills" class="py-16 bg-gray-50 dark:bg-darkCard">
    <div class="container mx-auto px-4">
      <div class="text-center mb-12" data-aos="fade-up">
        <h2 class="text-3xl font-bold font-display mb-2">Technical Skills</h2>
        <p class="text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
          A collection of technologies, tools, and frameworks I've worked with throughout my academic and personal projects.
        </p>
      </div>
      
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4" data-aos="fade-up" data-aos-delay="100">
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fab fa-python text-3xl text-primary mb-2"></i>
          <span>Python</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fas fa-code text-3xl text-primary mb-2"></i>
          <span>C</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fab fa-js text-3xl text-primary mb-2"></i>
          <span>JavaScript</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fab fa-html5 text-3xl text-primary mb-2"></i>
          <span>HTML</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fab fa-css3-alt text-3xl text-primary mb-2"></i>
          <span>CSS</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fab fa-figma text-3xl text-primary mb-2"></i>
          <span>Figma</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fas fa-database text-3xl text-primary mb-2"></i>
          <span>MySQL</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fas fa-chart-bar text-3xl text-primary mb-2"></i>
          <span>Pandas</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fas fa-calculator text-3xl text-primary mb-2"></i>
          <span>NumPy</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fas fa-chart-line text-3xl text-primary mb-2"></i>
          <span>Matplotlib</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fab fa-git-alt text-3xl text-primary mb-2"></i>
          <span>Git/GitHub</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fas fa-code-branch text-3xl text-primary mb-2"></i>
          <span>Visual Studio</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fab fa-microsoft text-3xl text-primary mb-2"></i>
          <span>Microsoft Office</span>
        </div>
        <div class="skill-badge bg-white dark:bg-darkBg p-4 rounded-lg shadow-md flex flex-col items-center">
          <i class="fab fa-flutter text-3xl text-primary mb-2"></i>
          <span>Flutter</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Education Section -->
  <section id="education" class="py-16">
    <div class="container mx-auto px-4">
      <div class="text-center mb-12" data-aos="fade-up">
        <h2 class="text-3xl font-bold font-display mb-2">Education & Certifications</h2>
        <p class="text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
          My academic background and professional certifications.
        </p>
      </div>
      
      <div class="max-w-3xl mx-auto relative pl-8 mt-12">
        <!-- Timeline Line -->
        <div class="absolute left-0 top-0 bottom-0 w-0.5 bg-gray-200 dark:bg-gray-700"></div>
        
        <!-- Timeline Items -->
        <div class="timeline-item relative mb-12 pl-8" data-aos="fade-up">
          <div class="timeline-line"></div>
          <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md">
            <div class="flex justify-between items-start mb-2 flex-wrap">
              <h3 class="text-xl font-bold text-primary">BSc. Computer Science</h3>
              <span class="text-gray-500 dark:text-gray-400">Current</span>
            </div>
            <p class="text-gray-600 dark:text-gray-300 mb-1">Uganda Christian University</p>
          </div>
        </div>
        
        <div class="timeline-item relative mb-12 pl-8" data-aos="fade-up" data-aos-delay="100">
          <div class="timeline-line"></div>
          <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md">
            <div class="flex justify-between items-start mb-2 flex-wrap">
              <h3 class="text-xl font-bold text-primary">UACE</h3>
              <span class="text-gray-500 dark:text-gray-400">Completed</span>
            </div>
            <p class="text-gray-600 dark:text-gray-300 mb-1">London College of St. Lawrence, Maya</p>
          </div>
        </div>
        
        <div class="timeline-item relative mb-12 pl-8" data-aos="fade-up" data-aos-delay="200">
          <div class="timeline-line"></div>
          <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md">
            <div class="flex justify-between items-start mb-2 flex-wrap">
              <h3 class="text-xl font-bold text-primary">UCE</h3>
              <span class="text-gray-500 dark:text-gray-400">Completed</span>
            </div>
            <p class="text-gray-600 dark:text-gray-300 mb-1">London College of St. Lawrence</p>
          </div>
        </div>

        <!-- Certifications -->
        <h3 class="text-2xl font-bold font-display mb-6 mt-16" data-aos="fade-up">Certifications</h3>
        
        <div class="timeline-item relative mb-12 pl-8" data-aos="fade-up" data-aos-delay="300">
          <div class="timeline-line"></div>
          <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md">
            <h3 class="text-xl font-bold text-primary mb-2">Introduction to Web Programming</h3>
            <p class="text-gray-600 dark:text-gray-300 mb-1">Equals Tech for Girls</p>
          </div>
        </div>
        
        <div class="timeline-item relative mb-12 pl-8" data-aos="fade-up" data-aos-delay="400">
          <div class="timeline-line"></div>
          <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md">
            <h3 class="text-xl font-bold text-primary mb-2">Distinguished Mentorship Masterclass</h3>
          </div>
        </div>
        
        <div class="timeline-item relative mb-12 pl-8" data-aos="fade-up" data-aos-delay="500">
          <div class="timeline-line"></div>
          <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md">
            <h3 class="text-xl font-bold text-primary mb-2">UCU Workshop Practice</h3>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Experience & Projects Section -->
  <section id="projects" class="py-16 bg-gray-50 dark:bg-darkCard">
    <div class="container mx-auto px-4">
      <div class="text-center mb-12" data-aos="fade-up">
        <h2 class="text-3xl font-bold font-display mb-2">Experience & Projects</h2>
        <p class="text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
          A collection of my professional experience and projects.
        </p>
      </div>

      <!-- Experience -->
      <div class="max-w-5xl mx-auto mb-16">
        <h3 class="text-2xl font-bold font-display mb-6" data-aos="fade-up">Experience</h3>
        
        <div class="bg-white dark:bg-darkBg p-6 rounded-lg shadow-md mb-6" data-aos="fade-up">
          <h4 class="text-xl font-bold text-primary mb-3">Figma Design Development</h4>
          <p class="text-gray-600 dark:text-gray-300 mb-4">
            Created UI/UX designs for various projects including Justice Chap Chap, DmarkVault, PPDA, and Russo App.
          </p>
        </div>
        
        <div class="bg-white dark:bg-darkBg p-6 rounded-lg shadow-md mb-6" data-aos="fade-up" data-aos-delay="100">
          <h4 class="text-xl font-bold text-primary mb-3">Database Programming</h4>
          <p class="text-gray-600 dark:text-gray-300 mb-4">
            Developed a comprehensive Farming Machinery Rental System, implementing database design, normalization, and SQL queries.
          </p>
        </div>
        
        <div class="bg-white dark:bg-darkBg p-6 rounded-lg shadow-md mb-6" data-aos="fade-up" data-aos-delay="200">
          <h4 class="text-xl font-bold text-primary mb-3">Algorithms</h4>
          <p class="text-gray-600 dark:text-gray-300 mb-4">
            Built a Python-based Personal Scheduling Assistant that uses algorithmic approaches to optimize time management.
          </p>
        </div>
        
        <div class="bg-white dark:bg-darkBg p-6 rounded-lg shadow-md" data-aos="fade-up" data-aos-delay="300">
          <h4 class="text-xl font-bold text-primary mb-3">Object-Oriented Programming</h4>
          <p class="text-gray-600 dark:text-gray-300 mb-4">
            Created a Vehicle Rental System in Python, implementing OOP principles like inheritance, polymorphism, and encapsulation.
          </p>
        </div>
      </div>
      
      <!-- Add Project Form -->
      <div class="max-w-5xl mx-auto">
        <div class="flex justify-between items-center mb-8">
          <h3 class="text-2xl font-bold font-display" data-aos="fade-up">My Projects</h3>
          <button id="addProjectBtn" class="px-4 py-2 bg-primary text-white rounded-md hover:bg-purple-700 transition font-medium flex items-center gap-2" data-aos="fade-up">
            <i class="fas fa-plus"></i>
            Add Project
          </button>
        </div>

        <!-- Add Project Form (hidden by default) -->
        <div id="addProjectForm" class="bg-white dark:bg-darkBg p-6 rounded-lg shadow-md mb-8 hidden">
          <h4 class="text-xl font-bold mb-4">Add New Project</h4>
          <form id="projectForm">
            <div class="mb-4">
              <label class="block text-gray-700 dark:text-gray-300 mb-2" for="projectTitle">Project Title</label>
              <input type="text" id="projectTitle" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary dark:bg-darkCard dark:border-gray-700" required>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 dark:text-gray-300 mb-2" for="projectDescription">Description</label>
              <textarea id="projectDescription" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary dark:bg-darkCard dark:border-gray-700" rows="3" required></textarea>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 dark:text-gray-300 mb-2" for="projectTechnologies">Technologies (comma separated)</label>
              <input type="text" id="projectTechnologies" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary dark:bg-darkCard dark:border-gray-700" placeholder="e.g. Python, MySQL, Flask" required>
            </div>
            <div class="mb-4">
              <label class="block text-gray-700 dark:text-gray-300 mb-2" for="projectImageUrl">Image URL</label>
              <input type="url" id="projectImageUrl" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary dark:bg-darkCard dark:border-gray-700" placeholder="https://example.com/image.jpg">
            </div>
            <div class="flex justify-end gap-4">
              <button type="button" id="cancelAddProject" class="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md hover:bg-gray-100 dark:hover:bg-darkCard transition">
                Cancel
              </button>
              <button type="submit" class="px-4 py-2 bg-primary text-white rounded-md hover:bg-purple-700 transition">
                Add Project
              </button>
            </div>
          </form>
        </div>
        
        <!-- Projects Container -->
        <div id="projectsContainer" class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Project cards will be added here dynamically -->
          <div class="project-card bg-white dark:bg-darkBg rounded-lg shadow-md overflow-hidden flex flex-col" data-aos="fade-up">
            <img src="https://cdn.pixabay.com/photo/2018/05/08/08/44/artificial-intelligence-3382507_1280.jpg" alt="Personal Scheduling Assistant" class="w-full h-48 object-cover">
            <div class="p-6 flex flex-col flex-grow">
              <h4 class="text-xl font-bold text-primary mb-3">Personal Scheduling Assistant</h4>
              <p class="text-gray-600 dark:text-gray-300 mb-4 flex-grow">
                Python-based assistant that uses algorithms to optimize time management and scheduling tasks.
              </p>
              <div class="mb-4 flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">Python</span>
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">Algorithms</span>
              </div>
              <a href="javascript:void(0)" class="text-primary hover:underline inline-flex items-center gap-1">
                <i class="fab fa-github"></i> View Repository
              </a>
            </div>
          </div>
          
          <div class="project-card bg-white dark:bg-darkBg rounded-lg shadow-md overflow-hidden flex flex-col" data-aos="fade-up" data-aos-delay="100">
            <img src="https://cdn.pixabay.com/photo/2017/06/10/07/22/farm-2389025_1280.jpg" alt="Farming Machinery Rental System" class="w-full h-48 object-cover">
            <div class="p-6 flex flex-col flex-grow">
              <h4 class="text-xl font-bold text-primary mb-3">Farming Machinery Rental System</h4>
              <p class="text-gray-600 dark:text-gray-300 mb-4 flex-grow">
                Database system for managing farm equipment rentals, scheduling, and maintenance tracking.
              </p>
              <div class="mb-4 flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">MySQL</span>
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">Python</span>
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">Database Design</span>
              </div>
              <a href="javascript:void(0)" class="text-primary hover:underline inline-flex items-center gap-1">
                <i class="fab fa-github"></i> View Repository
              </a>
            </div>
          </div>
          
          <div class="project-card bg-white dark:bg-darkBg rounded-lg shadow-md overflow-hidden flex flex-col" data-aos="fade-up" data-aos-delay="200">
            <img src="https://cdn.pixabay.com/photo/2016/03/01/07/36/car-1230125_1280.jpg" alt="Vehicle Rental System" class="w-full h-48 object-cover">
            <div class="p-6 flex flex-col flex-grow">
              <h4 class="text-xl font-bold text-primary mb-3">Vehicle Rental System</h4>
              <p class="text-gray-600 dark:text-gray-300 mb-4 flex-grow">
                Object-oriented application for managing a vehicle rental business, including bookings, vehicle inventory, and customer management.
              </p>
              <div class="mb-4 flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">Python</span>
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">OOP</span>
              </div>
              <a href="javascript:void(0)" class="text-primary hover:underline inline-flex items-center gap-1">
                <i class="fab fa-github"></i> View Repository
              </a>
            </div>
          </div>
          
          <div class="project-card bg-white dark:bg-darkBg rounded-lg shadow-md overflow-hidden flex flex-col" data-aos="fade-up" data-aos-delay="300">
            <img src="https://cdn.pixabay.com/photo/2022/01/18/20/33/figma-6948283_1280.jpg" alt="UI/UX Design Projects" class="w-full h-48 object-cover">
            <div class="p-6 flex flex-col flex-grow">
              <h4 class="text-xl font-bold text-primary mb-3">UI/UX Design Projects</h4>
              <p class="text-gray-600 dark:text-gray-300 mb-4 flex-grow">
                Collection of UI/UX designs for Justice Chap Chap, DmarkVault, PPDA, and Russo App.
              </p>
              <div class="mb-4 flex flex-wrap gap-2">
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">Figma</span>
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">UI/UX</span>
                <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">Design</span>
              </div>
              <a href="javascript:void(0)" class="text-primary hover:underline inline-flex items-center gap-1">
                <i class="fab fa-github"></i> View Repository
              </a>
            </div>
          </div>
        </div>
        
        <!-- GitHub Projects -->
        <div class="mt-12">
          <h3 class="text-2xl font-bold font-display mb-6" data-aos="fade-up">GitHub Projects</h3>
          
          <div id="githubProjectsContainer" class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="text-center p-8" id="githubProjectsLoading">
              <div class="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-primary"></div>
              <p class="mt-4 text-gray-600 dark:text-gray-300">Loading projects from GitHub...</p>
            </div>
            <!-- GitHub projects will be added here -->
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Leadership & Community Section -->
  <section id="leadership" class="py-16">
    <div class="container mx-auto px-4">
      <div class="text-center mb-12" data-aos="fade-up">
        <h2 class="text-3xl font-bold font-display mb-2">Leadership & Community</h2>
        <p class="text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
          My involvement in communities and leadership roles.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
        <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md" data-aos="fade-up">
          <div class="flex items-center justify-center h-16 w-16 rounded-full bg-purple-100 dark:bg-purple-900/30 text-primary mx-auto mb-4">
            <i class="fas fa-chart-bar text-xl"></i>
          </div>
          <h3 class="text-xl font-bold text-center mb-3">Data Analytics Chapter</h3>
          <p class="text-gray-600 dark:text-gray-300 text-center">
            Active member at Uganda Christian University's Data Analytics Chapter, participating in workshops and data projects.
          </p>
        </div>
        
        <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md" data-aos="fade-up" data-aos-delay="100">
          <div class="flex items-center justify-center h-16 w-16 rounded-full bg-purple-100 dark:bg-purple-900/30 text-primary mx-auto mb-4">
            <i class="fas fa-laptop-code text-xl"></i>
          </div>
          <h3 class="text-xl font-bold text-center mb-3">Code Buddy Chapter</h3>
          <p class="text-gray-600 dark:text-gray-300 text-center">
            Member of UCU's Code Buddy Chapter, collaborating on coding projects and peer programming sessions.
          </p>
        </div>
        
        <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md" data-aos="fade-up" data-aos-delay="200">
          <div class="flex items-center justify-center h-16 w-16 rounded-full bg-purple-100 dark:bg-purple-900/30 text-primary mx-auto mb-4">
            <i class="fas fa-users text-xl"></i>
          </div>
          <h3 class="text-xl font-bold text-center mb-3">Equals Tech for Girls</h3>
          <p class="text-gray-600 dark:text-gray-300 text-center">
            Mentee in the Equals Tech for Girls Mentorship Program, developing skills and networking with industry professionals.
          </p>
        </div>
      </div>

      <!-- Languages -->
      <div class="mt-16 max-w-3xl mx-auto">
        <h3 class="text-2xl font-bold font-display mb-6 text-center" data-aos="fade-up">Languages</h3>
        
        <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md" data-aos="fade-up">
          <div class="flex flex-col md:flex-row justify-around">
            <div class="text-center mb-4 md:mb-0">
              <div class="inline-block h-16 w-16 rounded-full bg-purple-100 dark:bg-purple-900/30 text-primary flex items-center justify-center mb-2">
                <i class="fas fa-language text-2xl"></i>
              </div>
              <h4 class="font-bold">English</h4>
              <p class="text-gray-600 dark:text-gray-400">Fluent</p>
            </div>
            
            <div class="text-center mb-4 md:mb-0">
              <div class="inline-block h-16 w-16 rounded-full bg-purple-100 dark:bg-purple-900/30 text-primary flex items-center justify-center mb-2">
                <i class="fas fa-language text-2xl"></i>
              </div>
              <h4 class="font-bold">Luganda</h4>
              <p class="text-gray-600 dark:text-gray-400">Fluent</p>
            </div>
            
            <div class="text-center">
              <div class="inline-block h-16 w-16 rounded-full bg-purple-100 dark:bg-purple-900/30 text-primary flex items-center justify-center mb-2">
                <i class="fas fa-language text-2xl"></i>
              </div>
              <h4 class="font-bold">Lusoga</h4>
              <p class="text-gray-600 dark:text-gray-400">Fluent</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Referees -->
      <div class="mt-16 max-w-4xl mx-auto">
        <h3 class="text-2xl font-bold font-display mb-6 text-center" data-aos="fade-up">Referees</h3>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md" data-aos="fade-up">
            <h4 class="text-lg font-bold mb-2">Nassimbwa Jalia</h4>
            <p class="text-gray-600 dark:text-gray-400 mb-1">Branch Manager</p>
            <p class="text-gray-600 dark:text-gray-400 mb-3">Kaluna Microfinance Ltd</p>
            <p class="flex items-center gap-2 text-primary">
              <i class="fas fa-phone"></i>
              <a href="tel:+256751051726">+256 751 051726</a>
            </p>
          </div>
          
          <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md" data-aos="fade-up" data-aos-delay="100">
            <h4 class="text-lg font-bold mb-2">Ochwo Jude</h4>
            <p class="text-gray-600 dark:text-gray-400 mb-1">Deputy Academics</p>
            <p class="text-gray-600 dark:text-gray-400 mb-3">Kingstone High School</p>
            <p class="flex items-center gap-2 text-primary">
              <i class="fas fa-phone"></i>
              <a href="tel:+256702960363">+256 702 960363</a>
            </p>
          </div>
          
          <div class="bg-white dark:bg-darkCard p-6 rounded-lg shadow-md" data-aos="fade-up" data-aos-delay="200">
            <h4 class="text-lg font-bold mb-2">Ogwok Kenneth</h4>
            <p class="text-gray-600 dark:text-gray-400 mb-1">Patron Data Analytics Chapter</p>
            <p class="text-gray-600 dark:text-gray-400 mb-3">UCU</p>
            <p class="flex items-center gap-2 text-primary">
              <i class="fas fa-phone"></i>
              <a href="tel:+256701372673">+256 701 372673</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="py-16 bg-gray-50 dark:bg-darkCard">
    <div class="container mx-auto px-4">
      <div class="text-center mb-12" data-aos="fade-up">
        <h2 class="text-3xl font-bold font-display mb-2">Get In Touch</h2>
        <p class="text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
          Feel free to reach out if you'd like to collaborate on a project or have any questions.
        </p>
      </div>
      
      <div class="flex flex-col md:flex-row gap-8 max-w-5xl mx-auto">
        <div class="w-full md:w-2/5" data-aos="fade-right">
          <div class="bg-white dark:bg-darkBg p-6 rounded-lg shadow-md">
            <h3 class="text-xl font-bold mb-6">Contact Information</h3>
            
            <div class="mb-6">
              <div class="flex items-center gap-4 mb-4">
                <div class="h-10 w-10 rounded-full bg-purple-100 dark:bg-purple-900/30 flex items-center justify-center text-primary">
                  <i class="fas fa-envelope"></i>
                </div>
                <div>
                  <p class="text-gray-500 dark:text-gray-400 text-sm">Email</p>
                  <a href="mailto:preciouswakabi@gmail.com" class="hover:text-primary transition">preciouswakabi@gmail.com</a>
                </div>
              </div>
              
              <div class="flex items-center gap-4 mb-4">
                <div class="h-10 w-10 rounded-full bg-purple-100 dark:bg-purple-900/30 flex items-center justify-center text-primary">
                  <i class="fas fa-phone"></i>
                </div>
                <div>
                  <p class="text-gray-500 dark:text-gray-400 text-sm">Phone</p>
                  <p>+256 756 989388 / +256 764 113614</p>
                </div>
              </div>
              
              <div class="flex items-center gap-4">
                <div class="h-10 w-10 rounded-full bg-purple-100 dark:bg-purple-900/30 flex items-center justify-center text-primary">
                  <i class="fab fa-github"></i>
                </div>
                <div>
                  <p class="text-gray-500 dark:text-gray-400 text-sm">GitHub</p>
                  <a href="https://github.com/WakabiPrecious" target="_blank" class="hover:text-primary transition">github.com/WakabiPrecious</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="w-full md:w-3/5" data-aos="fade-left">
          <div class="bg-white dark:bg-darkBg p-6 rounded-lg shadow-md">
            <h3 class="text-xl font-bold mb-6">Send Me a Message</h3>
            
            <form id="contactForm">
              <div class="mb-4">
                <label class="block text-gray-700 dark:text-gray-300 mb-2" for="name">Your Name</label>
                <input type="text" id="name" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary dark:bg-darkCard dark:border-gray-700" required>
              </div>
              
              <div class="mb-4">
                <label class="block text-gray-700 dark:text-gray-300 mb-2" for="email">Your Email</label>
                <input type="email" id="email" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary dark:bg-darkCard dark:border-gray-700" required>
              </div>
              
              <div class="mb-4">
                <label class="block text-gray-700 dark:text-gray-300 mb-2" for="subject">Subject</label>
                <input type="text" id="subject" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary dark:bg-darkCard dark:border-gray-700" required>
              </div>
              
              <div class="mb-6">
                <label class="block text-gray-700 dark:text-gray-300 mb-2" for="message">Message</label>
                <textarea id="message" rows="4" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-primary dark:bg-darkCard dark:border-gray-700" required></textarea>
              </div>
              
              <button type="submit" id="submitContactForm" class="w-full px-6 py-3 bg-primary text-white rounded-md hover:bg-purple-700 transition font-medium">
                Send Message
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="py-8 bg-gray-800 dark:bg-darkBg text-white">
    <div class="container mx-auto px-4">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <div class="mb-4 md:mb-0">
          <p>&copy; 2025 Precious Wakabi. All rights reserved.</p>
        </div>
        
        <div class="flex items-center gap-4">
          <a href="mailto:preciouswakabi@gmail.com" class="text-white hover:text-primary text-xl transition">
            <i class="fas fa-envelope"></i>
          </a>
          <a href="https://github.com/WakabiPrecious" target="_blank" class="text-white hover:text-primary text-xl transition">
            <i class="fab fa-github"></i>
          </a>
          <a href="tel:+256756989388" class="text-white hover:text-primary text-xl transition">
            <i class="fas fa-phone"></i>
          </a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Modals -->
  <div id="messageModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 hidden backdrop-blur-sm">
    <div class="bg-white dark:bg-darkCard rounded-lg p-6 shadow-xl max-w-md w-full mx-4">
      <div class="flex justify-between items-start mb-4">
        <h3 class="text-xl font-bold" id="modalTitle">Message Sent</h3>
        <button id="closeModal" class="text-gray-500 hover:text-gray-700 dark:text-gray-300 dark:hover:text-gray-100">
          <i class="fas fa-times"></i>
        </button>
      </div>
      <div class="mb-6">
        <p id="modalMessage">Thank you for your message. I will get back to you as soon as possible!</p>
      </div>
      <div class="flex justify-end">
        <button id="modalButton" class="px-4 py-2 bg-primary text-white rounded-md hover:bg-purple-700 transition">
          OK
        </button>
      </div>
    </div>
  </div>

  <!-- AOS Animation Library -->
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  
  <script id="app-script">
    // Initialize AOS animation
    document.addEventListener('DOMContentLoaded', () => {
      AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true
      });
      
      // Check for dark mode preference
      if (localStorage.getItem('darkMode') === 'true' || 
          (!localStorage.getItem('darkMode') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
      }

      // Load projects from localStorage
      loadProjects();

      // Simulate loading GitHub projects
      setTimeout(() => {
        document.getElementById('githubProjectsLoading').style.display = 'none';
        loadGitHubProjects();
      }, 1500);
    });

    // Dark mode toggle
    document.getElementById('darkModeToggle').addEventListener('click', () => {
      document.documentElement.classList.toggle('dark');
      localStorage.setItem('darkMode', document.documentElement.classList.contains('dark'));
    });

    // Mobile menu toggle
    document.getElementById('mobileMenuToggle').addEventListener('click', () => {
      document.getElementById('mobileMenu').classList.toggle('hidden');
    });

    // Close mobile menu when clicking on a link
    document.querySelectorAll('#mobileMenu a').forEach(link => {
      link.addEventListener('click', () => {
        document.getElementById('mobileMenu').classList.add('hidden');
      });
    });

    // Download CV button
    document.getElementById('downloadCV').addEventListener('click', () => {
      showModal('CV Download', 'This is a prototype. In the full version, this would download the CV.', 'OK');
    });

    // Add Project form
    document.getElementById('addProjectBtn').addEventListener('click', () => {
      document.getElementById('addProjectForm').classList.remove('hidden');
    });

    document.getElementById('cancelAddProject').addEventListener('click', () => {
      document.getElementById('addProjectForm').classList.add('hidden');
      document.getElementById('projectForm').reset();
    });

    // Handle project form submission
    document.getElementById('projectForm').addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Get form values
      const project = {
        id: Date.now(),
        title: document.getElementById('projectTitle').value,
        description: document.getElementById('projectDescription').value,
        technologies: document.getElementById('projectTechnologies').value.split(',').map(tech => tech.trim()),
        imageUrl: document.getElementById('projectImageUrl').value || 'https://cdn.pixabay.com/photo/2016/11/23/14/45/coding-1853305_1280.jpg'
      };
      
      // Save project to localStorage
      saveProject(project);
      
      // Hide form and reset
      document.getElementById('addProjectForm').classList.add('hidden');
      document.getElementById('projectForm').reset();
      
      // Show success message
      showModal('Project Added', 'Your project has been successfully added to your portfolio.', 'OK');
    });

    // Contact form submission
    document.getElementById('contactForm').addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Get form values
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const subject = document.getElementById('subject').value;
      const message = document.getElementById('message').value;
      
      // Show loading state
      const submitButton = document.getElementById('submitContactForm');
      const originalText = submitButton.innerHTML;
      submitButton.disabled = true;
      submitButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
      
      // Simulate API call
      setTimeout(() => {
        // Reset form
        document.getElementById('contactForm').reset();
        
        // Reset button
        submitButton.disabled = false;
        submitButton.innerHTML = originalText;
        
        // Show success message
        showModal('Message Sent', 'Thank you for your message. I will get back to you as soon as possible!', 'OK');
      }, 1500);
    });

    // Modal handling
    function showModal(title, message, buttonText) {
      document.getElementById('modalTitle').textContent = title;
      document.getElementById('modalMessage').textContent = message;
      document.getElementById('modalButton').textContent = buttonText;
      document.getElementById('messageModal').classList.remove('hidden');
    }

    document.getElementById('closeModal').addEventListener('click', () => {
      document.getElementById('messageModal').classList.add('hidden');
    });

    document.getElementById('modalButton').addEventListener('click', () => {
      document.getElementById('messageModal').classList.add('hidden');
    });

    // Project storage functions
    function saveProject(project) {
      let projects = JSON.parse(localStorage.getItem('portfolioProjects') || '[]');
      projects.push(project);
      localStorage.setItem('portfolioProjects', JSON.stringify(projects));
      
      // Add new project to DOM
      addProjectToDOM(project);
    }

    function loadProjects() {
      const projects = JSON.parse(localStorage.getItem('portfolioProjects') || '[]');
      projects.forEach(project => {
        addProjectToDOM(project);
      });
    }

    function addProjectToDOM(project) {
      const projectsContainer = document.getElementById('projectsContainer');
      
      const projectCard = document.createElement('div');
      projectCard.className = 'project-card bg-white dark:bg-darkBg rounded-lg shadow-md overflow-hidden flex flex-col';
      projectCard.dataset.id = project.id;
      projectCard.dataset.aos = 'fade-up';
      
      const techBadges = project.technologies.map(tech => 
        `<span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">${tech}</span>`
      ).join('');
      
      projectCard.innerHTML = `
        <img src="${project.imageUrl}" alt="${project.title}" class="w-full h-48 object-cover">
        <div class="p-6 flex flex-col flex-grow">
          <h4 class="text-xl font-bold text-primary mb-3">${project.title}</h4>
          <p class="text-gray-600 dark:text-gray-300 mb-4 flex-grow">${project.description}</p>
          <div class="mb-4 flex flex-wrap gap-2">${techBadges}</div>
          <div class="flex justify-between items-center">
            <a href="javascript:void(0)" class="text-primary hover:underline inline-flex items-center gap-1">
              <i class="fab fa-github"></i> View Repository
            </a>
            <button class="text-red-500 hover:text-red-700 delete-project" data-id="${project.id}">
              <i class="fas fa-trash"></i>
            </button>
          </div>
        </div>
      `;
      
      // Add delete functionality
      projectCard.querySelector('.delete-project').addEventListener('click', function() {
        const projectId = parseInt(this.dataset.id);
        deleteProject(projectId);
      });
      
      projectsContainer.prepend(projectCard);
    }

    function deleteProject(id) {
      let projects = JSON.parse(localStorage.getItem('portfolioProjects') || '[]');
      projects = projects.filter(project => project.id !== id);
      localStorage.setItem('portfolioProjects', JSON.stringify(projects));
      
      // Remove from DOM
      document.querySelector(`.project-card[data-id="${id}"]`).remove();
      
      showModal('Project Deleted', 'The project has been removed from your portfolio.', 'OK');
    }

    // GitHub Projects simulation
    function loadGitHubProjects() {
      const githubProjects = [
        {
          name: "Data Analysis Portfolio",
          description: "Collection of data analysis projects using Python, Pandas, and visualization libraries.",
          language: "Python",
          stars: 12
        },
        {
          name: "Web Dev Experiments",
          description: "Experiments with modern web development frameworks and libraries.",
          language: "JavaScript",
          stars: 8
        },
        {
          name: "ML Algorithms Implementation",
          description: "Implementation of various machine learning algorithms from scratch.",
          language: "Python",
          stars: 15
        }
      ];
      
      const container = document.getElementById('githubProjectsContainer');
      
      githubProjects.forEach((project, index) => {
        const projectElement = document.createElement('div');
        projectElement.className = 'bg-white dark:bg-darkBg p-5 rounded-lg shadow-md flex flex-col';
        projectElement.dataset.aos = 'fade-up';
        projectElement.dataset.aosDelay = (index * 100).toString();
        
        projectElement.innerHTML = `
          <div class="flex justify-between items-start mb-3">
            <h4 class="text-lg font-bold">${project.name}</h4>
            <span class="flex items-center text-yellow-500 text-sm">
              <i class="fas fa-star mr-1"></i> ${project.stars}
            </span>
          </div>
          <p class="text-gray-600 dark:text-gray-300 mb-4 flex-grow">${project.description}</p>
          <div class="flex justify-between items-center">
            <span class="px-3 py-1 bg-purple-100 text-primary dark:bg-purple-900/30 dark:text-purple-300 rounded-full text-sm">
              ${project.language}
            </span>
            <a href="javascript:void(0)" class="text-primary hover:underline inline-flex items-center gap-1">
              <i class="fab fa-github"></i> View Repo
            </a>
          </div>
        `;
        
        container.appendChild(projectElement);
      });
    }
  </script>
</body>
</html>