"use client";
import { useEffect } from 'react';

export default function ErrorReporter() {
  useEffect(() => {
    const handleError = (event: ErrorEvent) => {
      const el = document.createElement('div');
      el.style.cssText = "position:fixed; top:0; left:0; width:100%; height:100%; background:white; color:red; z-index:99999; padding:20px; overflow:auto; font-family:monospace; font-size: 14px;";
      el.innerHTML = `<h1>ERRO NO NAVEGADOR:</h1><p>${event.message}</p><pre>${event.error?.stack || ''}</pre>`;
      document.body.appendChild(el);
    };
    const handleRejection = (event: PromiseRejectionEvent) => {
      const el = document.createElement('div');
      el.style.cssText = "position:fixed; top:0; left:0; width:100%; height:100%; background:white; color:red; z-index:99999; padding:20px; overflow:auto; font-family:monospace; font-size: 14px;";
      el.innerHTML = `<h1>PROMISE REJECTION:</h1><p>${event.reason}</p>`;
      document.body.appendChild(el);
    };
    window.addEventListener('error', handleError);
    window.addEventListener('unhandledrejection', handleRejection);
    return () => {
      window.removeEventListener('error', handleError);
      window.removeEventListener('unhandledrejection', handleRejection);
    };
  }, []);
  return null;
}
