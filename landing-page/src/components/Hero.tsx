
import Image from 'next/image';

const Hero = () => {
  return (
    <section className="relative flex flex-col items-center justify-center h-screen text-center px-4">
      <div className="absolute inset-0 z-0">
        <Image
          src="/window.svg"
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
          href="/FileManagementSoftware_Installer.exe"
          download
          className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-10 rounded-full text-lg transition duration-300 ease-in-out transform hover:scale-105 shadow-lg animate-fade-in-up animation-delay-400"
        >
          Download Now
        </a>
      </div>
    </section>
  );
};

export default Hero;
