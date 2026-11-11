"use client";
import Image from "next/image";
import Link from "next/link";
import { FaPesquisar, FaHeart, FaShoppingCart, FaUser, FaEnvelope } from "react-icons/fa";

export default function Header() {
  return (
    <header className="w-full flex flex-col shadow-sm">
      
      {/* BARRA SUPERIOR (Contatos e Login/Cadastro) */}
      <div className="bg-blue-800 text-white text-xs md:text-sm py-2">
        <div className="max-w-7xl mx-auto px-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <FaEnvelope />
            <span>suporte@zixlima.com.br</span>
          </div>
          <div className="flex items-center gap-4 font-semibold">
            <Link href="/login" className="hover:text-blue-200 transition flex items-center gap-1">
              <FaUser size={12} /> Entrar
            </Link>
            <Link href="/register" className="hover:text-blue-200 transition">
              Cadastrar
            </Link>
          </div>
        </div>
      </div>

      {/* CABEÇALHO PRINCIPAL (Logo, Busca, Ícones) */}
      <div className="bg-white py-3 border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4">
          
          {/* Logo (Tamanho controlado) */}
          <Link href="/" className="flex-shrink-0">
            <img 
              src="/logo.png" 
              alt="Zixlima Eletrônicos" 
              className="w-32 md:w-40 h-auto object-contain"
            />
          </Link>

          {/* Barra de Busca */}
          <div className="w-full md:w-1/2 flex-grow mx-0 md:mx-8">
            <div className="relative flex w-full">
              <input 
                type="text" 
                placeholder="O que você está procurando?" 
                className="w-full border-2 border-blue-600 rounded-l-lg py-2 px-4 focus:outline-none text-sm"
              />
              <button className="bg-blue-600 text-white px-6 py-2 rounded-r-lg hover:bg-blue-700 transition flex items-center justify-center">
                <FaPesquisar />
              </button>
            </div>
          </div>

          {/* Ícones da Direita (Coração e Carrinho) */}
          <div className="flex items-center gap-6">
            <Link href="/wishlist" className="relative flex flex-col items-center text-gray-700 hover:text-blue-600 transition">
              <FaHeart size={22} />
              <span className="absolute -top-2 -right-3 bg-blue-600 text-white text-[10px] font-bold rounded-full h-5 w-5 flex items-center justify-center border-2 border-white">0</span>
            </Link>
            <Link href="/cart" className="relative flex flex-col items-center text-gray-700 hover:text-blue-600 transition">
              <FaShoppingCart size={22} />
              <span className="absolute -top-2 -right-3 bg-blue-600 text-white text-[10px] font-bold rounded-full h-5 w-5 flex items-center justify-center border-2 border-white">0</span>
            </Link>
          </div>

        </div>
      </div>
    </header>
  );
}
