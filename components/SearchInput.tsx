// *********************
// Role of the component: Pesquisar input element located in the header but it can be used anywhere in your application
// Name of the component: PesquisarInput.tsx
// Developer: Aleksandar Kuzmanovic
// Version: 1.0
// Component call: <PesquisarInput />
// Input parameters: no input parameters
// Output: form with search input and button
// *********************

"use client";
import { useRouter } from "next/navigation";
import React, { useState } from "react";
import { sanitize } from "@/lib/sanitize";

const PesquisarInput = () => {
  const [searchInput, setPesquisarInput] = useState<string>("");
  const router = useRouter();

  // function for modifying URL for searching products
  const searchProducts = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Sanitize the search input before using it in URL
    const sanitizedPesquisar = sanitize(searchInput);
    router.push(`/search?search=${encodeURIComponent(sanitizedPesquisar)}`);
    setPesquisarInput("");
  };

  return (
    <form className="flex w-full justify-center" onSubmit={searchProducts}>
      <input
        type="text"
        value={searchInput}
        onChange={(e) => setPesquisarInput(e.target.value)}
        placeholder="O que você procura?"
        className="bg-gray-50 input input-bordered w-[70%] rounded-r-none outline-none focus:outline-none max-sm:w-full"
      />
      <button type="submit" className="btn bg-blue-500 text-white rounded-l-none rounded-r-xl hover:bg-blue-600">
        Pesquisar
      </button>
    </form>
  );
};

export default PesquisarInput;
