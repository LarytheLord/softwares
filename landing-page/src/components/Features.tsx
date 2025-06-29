
const Features = () => {
  return (
    <section id="features" className="py-20 px-4 bg-gray-800">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-4xl font-bold text-center mb-12">Key Features</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
          <div className="bg-gray-700 p-8 rounded-lg shadow-xl transform hover:scale-105 transition duration-300 ease-in-out">
            <h3 className="text-2xl font-semibold mb-4">Intelligent Organization</h3>
            <p className="text-gray-300">Automatically sort and categorize your files based on type, date, or custom rules. Say goodbye to clutter.</p>
          </div>
          <div className="bg-gray-700 p-8 rounded-lg shadow-xl transform hover:scale-105 transition duration-300 ease-in-out">
            <h3 className="text-2xl font-semibold mb-4">Powerful Cleaning Tools</h3>
            <p className="text-gray-300">Identify and remove duplicate files, temporary files, and other digital junk to free up valuable space.</p>
          </div>
          <div className="bg-gray-700 p-8 rounded-lg shadow-xl transform hover:scale-105 transition duration-300 ease-in-out">
            <h3 className="text-2xl font-semibold mb-4">Enhanced Security</h3>
            <p className="text-gray-300">Protect your sensitive data with encryption and secure deletion options, ensuring your privacy.</p>
          </div>
          <div className="bg-gray-700 p-8 rounded-lg shadow-xl transform hover:scale-105 transition duration-300 ease-in-out">
            <h3 className="text-2xl font-semibold mb-4">Intuitive User Interface</h3>
            <p className="text-gray-300">A clean and easy-to-navigate interface makes file management a breeze for everyone.</p>
          </div>
          <div className="bg-gray-700 p-8 rounded-lg shadow-xl transform hover:scale-105 transition duration-300 ease-in-out">
            <h3 className="text-2xl font-semibold mb-4">Cross-Platform Compatibility</h3>
            <p className="text-gray-300">Seamlessly manage your files across different operating systems (Windows, macOS, Linux).</p>
          </div>
          <div className="bg-gray-700 p-8 rounded-lg shadow-xl transform hover:scale-105 transition duration-300 ease-in-out">
            <h3 className="text-2xl font-semibold mb-4">Customizable Workflows</h3>
            <p className="text-gray-300">Tailor the software to your specific needs with customizable rules and automation options.</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Features;
