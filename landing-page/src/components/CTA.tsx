
const CTA = () => {
  return (
    <section id="cta" className="py-20 px-4 bg-black text-center">
      <h2 className="text-4xl font-bold mb-8">Ready to Take Control of Your Files?</h2>
      <a
        href="/FileManagementSoftware_Installer.exe"
        download
        className="bg-green-600 hover:bg-green-700 text-white font-bold py-4 px-12 rounded-full text-xl transition duration-300 ease-in-out transform hover:scale-105 shadow-lg"
      >
        Download Trae File Manager Today!
      </a>
    </section>
  );
};

export default CTA;
