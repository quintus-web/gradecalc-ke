const coursesData = [
  {
    name: "Bachelor of Arts",
    universities: [
      { name: "Chuka University", cutoff: 28.566 },
      { name: "Kisii University", cutoff: 26.315 },
      { name: "Rongo University", cutoff: 27.808 },
      { name: "Egerton University", cutoff: 26.783 },
      { name: "Multimedia University of Kenya", cutoff: 26.207 },
      { name: "Bomet University College", cutoff: 22.916 },
      { name: "Tharaka University", cutoff: 22.916 },
      { name: "University of Nairobi", cutoff: 26.506 },
      { name: "Moi University", cutoff: 26.127 },
      { name: "Machakos University", cutoff: 25.340 },
      { name: "South Eastern Kenya University", cutoff: 24.460 },
      { name: "Kenyatta University", cutoff: 28.578 }
    ]
  },
  {
    name: "Bachelor of Arts (with IT)",
    universities: [
      { name: "Tom Mboya University", cutoff: 22.916 },
      { name: "Maseno University", cutoff: 26.259 }
    ]
  },
  {
    name: "Bachelor of Architectural Studies / Architecture",
    universities: [
      { name: "Technical University of Mombasa", cutoff: 40.571 },
      { name: "Kenyatta University", cutoff: 42.407 },
      { name: "University of Nairobi", cutoff: 43.794 },
      { name: "JKUAT", cutoff: 42.528 },
      { name: "Technical University of Kenya", cutoff: 41.962 }
    ]
  },
  {
    name: "Bachelor of Quantity Surveying",
    universities: [
      { name: "University of Nairobi", cutoff: 40.993 },
      { name: "JKUAT", cutoff: 41.641 },
      { name: "Technical University of Kenya", cutoff: 40.533 }
    ]
  },
  {
    name: "Bachelor of Actuarial Science",
    universities: [
      { name: "Egerton University", cutoff: 28.868 },
      { name: "Chuka University", cutoff: 22.714 },
      { name: "Co-operative University of Kenya", cutoff: 24.735 },
      { name: "University of Nairobi", cutoff: 39.271 },
      { name: "Kenyatta University", cutoff: 31.842 },
      { name: "JKUAT", cutoff: 31.441 },
      { name: "Maseno University", cutoff: 24.601 },
      { name: "Dedan Kimathi University of Technology", cutoff: 24.342 },
      { name: "Multimedia University of Kenya", cutoff: 25.777 }
    ]
  },
  {
    name: "Bachelor of Medicine & Bachelor of Surgery (MBChB)",
    universities: [
      { name: "Kenya Methodist University", cutoff: 38.040 },
      { name: "Egerton University", cutoff: 44.079 },
      { name: "Kisii University", cutoff: 44.012 },
      { name: "Masinde Muliro University", cutoff: 44.026 },
      { name: "Kenyatta University", cutoff: 44.914 },
      { name: "Maseno University", cutoff: 44.463 },
      { name: "Mount Kenya University", cutoff: 43.486 },
      { name: "University of Nairobi", cutoff: 45.034 },
      { name: "JKUAT", cutoff: 44.611 },
      { name: "Moi University", cutoff: 44.492 }
    ]
  },
  {
    name: "Bachelor of Pharmacy",
    universities: [
      { name: "Kisii University", cutoff: 43.003 },
      { name: "Kenya Methodist University", cutoff: 34.150 },
      { name: "Kabarak University", cutoff: 38.341 },
      { name: "Maseno University", cutoff: 43.126 },
      { name: "Mount Kenya University", cutoff: 39.982 },
      { name: "University of Nairobi", cutoff: 43.885 },
      { name: "JKUAT", cutoff: 43.483 },
      { name: "Kenyatta University", cutoff: 43.541 }
    ]
  },
  {
    name: "Bachelor of Dental Surgery",
    universities: [
      { name: "University of Nairobi", cutoff: 44.334 },
      { name: "Moi University", cutoff: 44.070 }
    ]
  },
  {
    name: "Bachelor of Science (Nursing)",
    universities: [
      { name: "Chuka University", cutoff: 41.319 },
      { name: "University of Embu", cutoff: 40.621 },
      { name: "Masinde Muliro University", cutoff: 41.939 },
      { name: "Kirinyaga University", cutoff: 39.509 },
      { name: "Kisii University", cutoff: 41.825 },
      { name: "Egerton University", cutoff: 41.947 },
      { name: "Maseno University", cutoff: 42.357 },
      { name: "Kenyatta University", cutoff: 42.773 },
      { name: "University of Nairobi", cutoff: 43.297 },
      { name: "Moi University", cutoff: 42.216 },
      { name: "Mount Kenya University", cutoff: 41.098 },
      { name: "JKUAT", cutoff: 42.730 }
    ]
  },
  {
    name: "Bachelor of Laws (LL.B.)",
    universities: [
      { name: "Chuka University", cutoff: 39.904 },
      { name: "University of Embu", cutoff: 38.819 },
      { name: "Kisii University", cutoff: 39.448 },
      { name: "Kabarak University", cutoff: 35.922 },
      { name: "Egerton University", cutoff: 39.860 },
      { name: "Moi University", cutoff: 40.788 },
      { name: "University of Nairobi", cutoff: 41.758 },
      { name: "JKUAT", cutoff: 41.254 },
      { name: "Kenyatta University", cutoff: 41.278 },
      { name: "Mount Kenya University", cutoff: 39.748 }
    ]
  },
  {
    name: "Bachelor of Science (Computer Science)",
    universities: [
      { name: "Chuka University", cutoff: 35.626 },
      { name: "Egerton University", cutoff: 37.746 },
      { name: "Co-operative University of Kenya", cutoff: 38.257 },
      { name: "JKUAT", cutoff: 43.809 },
      { name: "Dedan Kimathi University of Technology", cutoff: 39.405 },
      { name: "Multimedia University of Kenya", cutoff: 41.440 },
      { name: "University of Nairobi", cutoff: 44.122 },
      { name: "Moi University", cutoff: 37.892 },
      { name: "Maseno University", cutoff: 37.840 },
      { name: "Kenyatta University", cutoff: 43.230 }
    ]
  },
  {
    name: "Bachelor of Science (Civil Engineering)",
    universities: [
      { name: "Technical University of Mombasa", cutoff: 38.702 },
      { name: "JKUAT", cutoff: 42.178 },
      { name: "Dedan Kimathi University of Technology", cutoff: 39.769 },
      { name: "Multimedia University of Kenya", cutoff: 38.924 },
      { name: "Technical University of Kenya", cutoff: 41.524 },
      { name: "University of Nairobi", cutoff: 43.091 },
      { name: "Kenyatta University", cutoff: 42.148 }
    ]
  },
  {
    name: "Bachelor of Science (Electrical & Electronic Engineering)",
    universities: [
      { name: "Technical University of Mombasa", cutoff: 37.437 },
      { name: "JKUAT", cutoff: 42.291 },
      { name: "Dedan Kimathi University of Technology", cutoff: 39.454 },
      { name: "University of Nairobi", cutoff: 42.776 },
      { name: "Kenyatta University", cutoff: 42.125 }
    ]
  },
  {
    name: "Bachelor of Science (Mechanical Engineering)",
    universities: [
      { name: "University of Nairobi", cutoff: 41.321 },
      { name: "Kenyatta University", cutoff: 41.033 },
      { name: "JKUAT", cutoff: 41.449 },
      { name: "Dedan Kimathi University of Technology", cutoff: 37.987 },
      { name: "Technical University of Kenya", cutoff: 40.186 }
    ]
  },
  {
    name: "Bachelor of Commerce",
    universities: [
      { name: "Chuka University", cutoff: 23.266 },
      { name: "Egerton University", cutoff: 26.655 },
      { name: "JKUAT", cutoff: 30.346 },
      { name: "University of Nairobi", cutoff: 33.556 },
      { name: "Kenyatta University", cutoff: 30.779 },
      { name: "Technical University of Kenya", cutoff: 29.070 }
    ]
  },
  {
    name: "Bachelor of Education (Arts)",
    universities: [
      { name: "Chuka University", cutoff: 32.845 },
      { name: "Kisii University", cutoff: 30.144 },
      { name: "Egerton University", cutoff: 32.486 },
      { name: "University of Nairobi", cutoff: 33.663 },
      { name: "Moi University", cutoff: 30.707 },
      { name: "Kenyatta University", cutoff: 34.725 },
      { name: "Maseno University", cutoff: 32.556 }
    ]
  },
  {
    name: "Bachelor of Education (Science)",
    universities: [
      { name: "Chuka University", cutoff: 35.446 },
      { name: "Kisii University", cutoff: 32.322 },
      { name: "Egerton University", cutoff: 35.282 },
      { name: "Maseno University", cutoff: 36.459 },
      { name: "University of Nairobi", cutoff: 37.073 },
      { name: "Moi University", cutoff: 35.434 },
      { name: "Kenyatta University", cutoff: 37.778 }
    ]
  },
  {
    name: "Bachelor of Science (Mathematics)",
    universities: [
      { name: "University of Nairobi", cutoff: 32.487 },
      { name: "Technical University of Kenya", cutoff: 26.695 }
    ]
  },
  {
    name: "Bachelor of Science (Biochemistry)",
    universities: [
      { name: "University of Nairobi", cutoff: 31.056 },
      { name: "Kenyatta University", cutoff: 31.582 },
      { name: "Technical University of Kenya", cutoff: 32.890 },
      { name: "Maseno University", cutoff: 16.974 }
    ]
  },
  {
    name: "Bachelor of Science (Industrial Chemistry)",
    universities: [
      { name: "University of Nairobi", cutoff: 31.980 }
    ]
  },
  {
    name: "Bachelor of Science (Statistics)",
    universities: [
      { name: "University of Nairobi", cutoff: 33.673 },
      { name: "JKUAT", cutoff: 27.899 }
    ]
  },
  {
    name: "Bachelor of Economics",
    universities: [
      { name: "University of Nairobi", cutoff: 30.453 },
      { name: "JKUAT", cutoff: 22.977 },
      { name: "Kenyatta University", cutoff: 24.100 },
      { name: "Technical University of Kenya", cutoff: 24.780 }
    ]
  },
  {
    name: "Bachelor of Science (Medical Laboratory Sciences)",
    universities: [
      { name: "University of Nairobi", cutoff: 41.139 },
      { name: "JKUAT", cutoff: 40.680 },
      { name: "Kenyatta University", cutoff: 41.000 },
      { name: "Masinde Muliro University", cutoff: 38.739 },
      { name: "Kisii University", cutoff: 38.700 }
    ]
  },
  {
    name: "Bachelor of Science (Public Health)",
    universities: [
      { name: "JKUAT", cutoff: 37.235 },
      { name: "Maseno University", cutoff: 34.339 },
      { name: "Kisii University", cutoff: 32.151 }
    ]
  },
  {
    name: "Bachelor of Science (Information Technology)",
    universities: [
      { name: "JKUAT", cutoff: 40.270 },
      { name: "Multimedia University of Kenya", cutoff: 35.394 },
      { name: "Technical University of Kenya", cutoff: 38.039 }
    ]
  },
  {
    name: "Bachelor of Science (Software Engineering)",
    universities: [
      { name: "JKUAT", cutoff: 42.892 },
      { name: "Co-operative University of Kenya", cutoff: 39.959 },
      { name: "Multimedia University of Kenya", cutoff: 41.420 },
      { name: "Murang'a University of Technology", cutoff: 37.792 }
    ]
  },
  {
    name: "Bachelor of Science (Biomedical Engineering)",
    universities: [
      { name: "Kenyatta University", cutoff: 41.807 }
    ]
  },
  {
    name: "Bachelor of Science (Mechatronic Engineering)",
    universities: [
      { name: "JKUAT", cutoff: 42.892 },
      { name: "Dedan Kimathi University of Technology", cutoff: 39.852 }
    ]
  },
  {
    name: "Bachelor of Science (Petroleum Engineering)",
    universities: [
      { name: "Kenyatta University", cutoff: 37.463 }
    ]
  },
  {
    name: "Bachelor of Science (Aerospace Engineering)",
    universities: [
      { name: "JKUAT", cutoff: 38.971 },
      { name: "Kenyatta University", cutoff: 40.538 }
    ]
  },
  {
    name: "Bachelor of Engineering (Aeronautical Engineering)",
    universities: [
      { name: "Technical University of Kenya", cutoff: 43.028 }
    ]
  },
  {
    name: "Bachelor of Science Clinical Medicine",
    universities: [
      { name: "Egerton University", cutoff: 41.983 },
      { name: "JKUAT", cutoff: 42.365 },
      { name: "Masinde Muliro University", cutoff: 42.023 },
      { name: "Kisii University", cutoff: 41.571 }
    ]
  },
  {
    name: "Bachelor of Radiography",
    universities: [
      { name: "JKUAT", cutoff: 43.127 }
    ]
  },
  {
    name: "Bachelor of Science (Physiotherapy)",
    universities: [
      { name: "JKUAT", cutoff: 38.116 },
      { name: "Masinde Muliro University", cutoff: 35.876 },
      { name: "Moi University", cutoff: 36.954 }
    ]
  },
  {
    name: "Bachelor of Science (Optometry and Vision Sciences)",
    universities: [
      { name: "Masinde Muliro University", cutoff: 38.166 },
      { name: "Kaimosi Friends University", cutoff: 36.009 }
    ]
  },
  {
    name: "Bachelor of Veterinary Medicine and Surgery",
    universities: [
      { name: "Egerton University", cutoff: 38.443 },
      { name: "University of Nairobi", cutoff: 39.091 }
    ]
  },
  {
    name: "Bachelor of Science (Food Science & Technology)",
    universities: [
      { name: "JKUAT", cutoff: 33.076 },
      { name: "University of Nairobi", cutoff: 32.155 }
    ]
  },
  {
    name: "Bachelor of Science (Agriculture)",
    universities: [
      { name: "JKUAT", cutoff: 32.284 }
    ]
  },
  {
    name: "Bachelor of Science (Microbiology)",
    universities: [
      { name: "JKUAT", cutoff: 26.199 },
      { name: "Kenyatta University", cutoff: 25.937 }
    ]
  },
  {
    name: "Bachelor of Science (Biomedical Science and Technology)",
    universities: [
      { name: "Egerton University", cutoff: 36.066 },
      { name: "Technical University of Kenya", cutoff: 37.022 }
    ]
  },
  {
    name: "Bachelor of Human Resource Management",
    universities: [
      { name: "Kenyatta University", cutoff: 32.725 },
      { name: "JKUAT", cutoff: 30.688 }
    ]
  },
  {
    name: "Bachelor of Real Estate",
    universities: [
      { name: "University of Nairobi", cutoff: 36.881 },
      { name: "JKUAT", cutoff: 35.982 },
      { name: "Kenyatta University", cutoff: 34.531 }
    ]
  },
  {
    name: "Bachelor of Construction Management",
    universities: [
      { name: "University of Nairobi", cutoff: 37.326 },
      { name: "JKUAT", cutoff: 37.780 }
    ]
  },
  {
    name: "Bachelor of Engineering (Geospatial Engineering)",
    universities: [
      { name: "Technical University of Kenya", cutoff: 37.616 },
      { name: "University of Nairobi", cutoff: 38.483 }
    ]
  },
  {
    name: "Bachelor of Science (Marine Engineering)",
    universities: [
      { name: "JKUAT", cutoff: 37.795 }
    ]
  },
  {
    name: "Bachelor of Landscape Architecture",
    universities: [
      { name: "JKUAT", cutoff: 36.138 }
    ]
  },
  {
    name: "Bachelor of Arts in International Relations and Diplomacy",
    universities: [
      { name: "University of Nairobi", cutoff: 34.361 },
      { name: "Technical University of Kenya", cutoff: 34.267 }
    ]
  },
  {
    name: "Bachelor of Economics and Statistics",
    universities: [
      { name: "University of Nairobi", cutoff: 33.223 },
      { name: "Kenyatta University", cutoff: 28.213 }
    ]
  },
  {
    name: "Bachelor of Science in Data Science and Analytics",
    universities: [
      { name: "JKUAT", cutoff: 36.902 }
    ]
  },
  {
    name: "Bachelor of Science (Telecommunication and Information Engineering)",
    universities: [
      { name: "JKUAT", cutoff: 39.652 }
    ]
  },
  {
    name: "Bachelor of Science (Environmental Health)",
    universities: [
      { name: "Kenyatta University", cutoff: 29.014 }
    ]
  },
  {
    name: "Bachelor of Science (Forensic Science)",
    universities: [
      { name: "Kenyatta University", cutoff: 35.032 }
    ]
  },
  {
    name: "Bachelor of Information Technology",
    universities: [
      { name: "Kenyatta University", cutoff: 39.905 }
    ]
  },
  {
    name: "Bachelor of Communication and Media Studies",
    universities: [
      { name: "Kenyatta University", cutoff: 34.635 }
    ]
  },
  {
    name: "Bachelor of Journalism",
    universities: [
      { name: "JKUAT", cutoff: 33.837 },
      { name: "Multimedia University of Kenya", cutoff: 33.246 }
    ]
  },
  {
    name: "Bachelor of Science (Civil and Structural Engineering)",
    universities: [
      { name: "Masinde Muliro University", cutoff: 38.536 },
      { name: "Moi University", cutoff: 39.792 }
    ]
  },
  {
    name: "Bachelor of Engineering (Chemical Engineering)",
    universities: [
      { name: "Technical University of Kenya", cutoff: 38.404 },
      { name: "Dedan Kimathi University of Technology", cutoff: 31.644 }
    ]
  },
  {
    name: "Bachelor of Science in Oral Health",
    universities: [
      { name: "Mount Kenya University", cutoff: 34.284 }
    ]
  },
  {
    name: "Bachelor of Science in Dental Technology",
    universities: [
      { name: "Mount Kenya University", cutoff: 35.151 }
    ]
  },
  {
    name: "Bachelor of Public Policy and Administration",
    universities: [
      { name: "Kenyatta University", cutoff: 32.940 }
    ]
  },
  {
    name: "Bachelor of Science (Accounting)",
    universities: [
      { name: "Technical University of Kenya", cutoff: 36.475 },
      { name: "Co-operative University of Kenya", cutoff: 28.031 }
    ]
  },
  {
    name: "Bachelor of Science (Health Records & Information Management)",
    universities: [
      { name: "Kenyatta University", cutoff: 32.695 },
      { name: "JKUAT", cutoff: 30.985 }
    ]
  },
  {
    name: "Bachelor of Journalism & Mass Communication",
    universities: [
      { name: "University of Nairobi", cutoff: 34.056 },
      { name: "Technical University of Mombasa", cutoff: 32.201 },
      { name: "Masinde Muliro University", cutoff: 30.615 }
    ]
  },
  {
    name: "Bachelor of Science (Medical Biochemistry)",
    universities: [
      { name: "JKUAT", cutoff: 31.234 }
    ]
  },
  {
    name: "Bachelor of Science (Physics)",
    universities: [
      { name: "Maseno University", cutoff: 22.631 }
    ]
  },
  {
    name: "Bachelor of Science (Analytical Chemistry)",
    universities: [
      { name: "University of Nairobi", cutoff: 31.513 }
    ]
  },
  {
    name: "Bachelor of Arts (Psychology)",
    universities: [
      { name: "Kenyatta University", cutoff: 34.531 }
    ]
  },
  {
    name: "Bachelor of Arts (Criminology & Security Studies)",
    universities: [
      { name: "Egerton University", cutoff: 30.426 },
      { name: "Maseno University", cutoff: 30.192 }
    ]
  }
];
