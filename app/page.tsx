export const dynamic = "force-dynamic";

import { CategoryMenu, Hero, Incentives, IntroducingSection, Newsletter, ProductsSection } from "@/components";

export default function Home() {
  return (
    <>
    <Hero />
    <IntroducingSection />
    <CategoryMenu />
    <ProductsSection />
    </>
  );
}
