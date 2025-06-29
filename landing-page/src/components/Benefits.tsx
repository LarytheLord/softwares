
const Benefits = () => {
  return (
    <section id="benefits" className="py-20 px-4 bg-gray-900">
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
  );
};

export default Benefits;
