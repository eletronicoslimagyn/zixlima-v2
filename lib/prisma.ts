import { PrismaClient } from '@prisma/client';
import { PrismaNeon } from '@prisma/adapter-neon';
import { Pool } from '@neondatabase/serverless';

let prismaInstance: PrismaClient | null = null;

function getPrismaInstance(): PrismaClient {
  if (!prismaInstance) {
    // Usa a URL real se existir; senão, uma URL dummy apenas para o build não travar
    const connectionString = process.env.DATABASE_URL || "postgresql://dummy:dummy@localhost:5432/dummy";
    const neon = new Pool({ connectionString });
    const adapter = new PrismaNeon(neon);
    prismaInstance = new PrismaClient({ adapter });
  }
  return prismaInstance;
}

// Proxy que adia a criação do PrismaClient até o primeiro uso real
const prisma = new Proxy({} as PrismaClient, {
  get: (target, prop) => {
    const instance = getPrismaInstance();
    return Reflect.get(instance, prop);
  },
});

export default prisma;
