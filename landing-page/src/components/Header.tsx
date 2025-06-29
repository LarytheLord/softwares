
import Link from 'next/link';

const Header = () => {
  return (
    <header className="bg-transparent text-white py-4 px-6 flex justify-between items-center">
      <div className="text-2xl font-bold">
        <Link href="/">Trae</Link>
      </div>
      <nav>
        <ul className="flex space-x-6">
          <li><Link href="#features" className="hover:text-gray-300">Features</Link></li>
          <li><Link href="#benefits" className="hover:text-gray-300">Benefits</Link></li>
          <li><Link href="#cta" className="hover:text-gray-300">Download</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
