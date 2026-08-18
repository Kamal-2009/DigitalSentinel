import React from 'react';
import { Outlet } from 'react-router-dom';
import { Header } from './Header';
import { Sidebar } from './Sidebar';

export const AppShell: React.FC = () => {
  return (
    <div className="min-h-screen bg-[#F5F7FA] text-[#172B4D] flex flex-col font-sans">
      {/* Global Header */}
      <Header />

      {/* Global Sidebar */}
      <Sidebar />

      {/* Main Page Workspace Content */}
      <main className="fixed left-60 right-0 top-16 bottom-0 overflow-y-auto bg-[#F5F7FA] custom-scrollbar">
        <div className="min-h-full p-5 lg:p-6 pb-12 max-w-[1700px] mx-auto">
          <Outlet />
        </div>
      </main>
    </div>
  );
};
