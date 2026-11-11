/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    ignoreDuringBuilds: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    unoptimized: true,
  },
  serverExternalPackages: ["@prisma/client", ".prisma/client"],
  env: {
    DATABASE_URL: process.env.DATABASE_URL || "postgresql://dummy:dummy@localhost:5432/dummy",
  },
};

module.exports = nextConfig;
