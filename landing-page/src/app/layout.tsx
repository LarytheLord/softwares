import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Trae File Manager - Organize, Clean & Secure Your Digital Life",
  description: "Discover Trae File Manager, the ultimate desktop application for effortless file organization, intelligent cleaning, and enhanced digital security. Streamline your workflow and take control of your digital space.",
  keywords: "file manager, file organizer, desktop application, digital organization, file cleaning, secure files, productivity software, Windows file manager",
  openGraph: {
    title: "Trae File Manager - Organize, Clean & Secure Your Digital Life",
    description: "Discover Trae File Manager, the ultimate desktop application for effortless file organization, intelligent cleaning, and enhanced digital security. Streamline your workflow and take control of your digital space.",
    url: "https://yourwebsite.com", // Replace with your actual website URL
    siteName: "Trae File Manager",
    images: [
      {
        url: "https://yourwebsite.com/og-image.jpg", // Replace with your actual OG image
        width: 1200,
        height: 630,
        alt: "Trae File Manager Software",
      },
    ],
    locale: "en_US",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Trae File Manager - Organize, Clean & Secure Your Digital Life",
    description: "Discover Trae File Manager, the ultimate desktop application for effortless file organization, intelligent cleaning, and enhanced digital security. Streamline your workflow and take control of your digital space.",
    images: ["https://yourwebsite.com/twitter-image.jpg"], // Replace with your actual Twitter image
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
