import Image from "next/image";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black text-white">
      {/* Hero Section */}
      <section className="relative flex flex-col items-center justify-center h-screen text-center px-4">
        <div className="absolute inset-0 z-0">
          <Image
            src="/window.svg" // Using an existing SVG as a placeholder for a background image
            alt="Background"
            layout="fill"
            objectFit="cover"
            className="opacity-10"
          />
        </div>
        <div className="z-10 max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-7xl font-extrabold leading-tight mb-6 animate-fade-in-up">
            Trae File Manager: Organize, Clean & Secure Your Digital Life
          </h1>
          <p className="text-xl md:text-2xl mb-10 opacity-90 animate-fade-in-up animation-delay-200">
            Effortlessly manage your files with intelligent organization, powerful cleaning tools, and robust security features.
          </p>
          <a
            href="#" // Placeholder for download link
            className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-10 rounded-full text-lg transition duration-300 ease-in-out transform hover:scale-105 shadow-lg animate-fade-in-up animation-delay-400"
          >
            Download Now
          </a>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-4 bg-gray-800">
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

      {/* Benefits Section */}
      <section className="py-20 px-4 bg-gray-900">
        <div className="max-w-6xl mx-auto text-center">
          <h2 className="text-4xl font-bold mb-12">Why Choose Trae File Manager?</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
            <div className="bg-gray-800 p-8 rounded-lg shadow-xl">
              <h3 className="text-2xl font-semibold mb-4">Boost Your Productivity</h3>
              <p className="text-gray-300">Spend less time searching for files and more time on what matters. Trae File Manager streamlines your digital workflow.</p>
            </div>
            <div className="bg-gray-800 p-8 rounded-lg shadow-xl">
              <h3 className="text-2xl font-semibold mb-4">Reclaim Disk Space</h3>
              <p className="text-gray-300">Our powerful cleaning tools help you eliminate unnecessary files, giving you more room for important data.</p>
            </div>
            <div className="bg-gray-800 p-8 rounded-lg shadow-xl">
              <h3 className="text-2xl font-semibold mb-4">Peace of Mind</h3>
              <p className="text-gray-300">With robust security features, you can rest assured that your sensitive information is protected.</p>
            </div>
            <div className="bg-gray-800 p-8 rounded-lg shadow-xl">
              <h3 className="text-2xl font-semibold mb-4">Simple & Effective</h3>
              <p className="text-gray-300">Designed for ease of use, Trae File Manager makes complex tasks simple, even for beginners.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Call to Action Section */}
      <section className="py-20 px-4 bg-black text-center">
        <h2 className="text-4xl font-bold mb-8">Ready to Take Control of Your Files?</h2>
        <a
          href="#" // Placeholder for download link
          className="bg-green-600 hover:bg-green-700 text-white font-bold py-4 px-12 rounded-full text-xl transition duration-300 ease-in-out transform hover:scale-105 shadow-lg"
        >
          Download Trae File Manager Today!
        </a>
      </section>

      {/* Footer */}
      <footer className="bg-gray-950 py-8 text-center text-gray-500 text-sm">
        <p>&copy; {new Date().getFullYear()} Trae File Manager. All rights reserved.</p>
      </footer>
    </div>
  );
}