import React from "react";

const Navbar = () => {
    const user = false
  return (
    <nav className="bg-gray-800 p-4 shadow-lg text-white w-full fixed top-0 left-0">
      <div className="flex justify-between items-center w-full px-4">
        {/* Logo and Company Name */}
        <div className="flex items-center space-x-4">
          <span className="text-xl font-bold">Company</span><span className="text-xl font-bold text-red-400">Name</span>
        </div>

        {/* Navigation Links */}
        <div className="hidden md:flex space-x-8">
          <a href="#" className="hover:text-gray-400 transition duration-300">
            Home
          </a>
          <a href="#" className="hover:text-gray-400 transition duration-300">
            Portfolio Management
          </a>
          <a href="#" className="hover:text-gray-400 transition duration-300">
            Contact Us
          </a>
          <a href="#" className="hover:text-gray-400 transition duration-300">
            About Us
          </a>
          {
  user ? (
    <div className="flex items-center space-x-4">
      {/* First Button */}
      <button className="bg-gray-700 hover:bg-gray-600 transition duration-300 p-2 rounded-full">
        <i className="fas fa-user"></i>
      </button>
      {/* Second Button */}
      <button className="bg-gray-700 hover:bg-gray-600 transition duration-300 p-2 rounded-full">
        <i className="fas fa-cog"></i>
      </button>
    </div>
  ) : (
    <div>
      {/* User Profile or Alternative Content */}
      <div className="bg-gray-700 text-white p-4 rounded-lg space-x-4 ">
        <button>

        </button>
        <button>

        </button>
      </div>
    </div>
  )
}

        </div>
        
        
      </div>
    </nav>
  );
};

export default Navbar;
