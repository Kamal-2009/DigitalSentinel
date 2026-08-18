import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ToastProvider } from './components/common/Toast';
import { AppShell } from './components/shell/AppShell';

// Pages
import { Dashboard } from './pages/Dashboard';
import { MyCases } from './pages/MyCases';
import { CaseWorkspace } from './pages/CaseWorkspace';
import { UploadEvidence } from './pages/UploadEvidence';
import { Timeline } from './pages/Timeline';
import { EntityGraph } from './pages/EntityGraph';
import { GeospatialMap } from './pages/GeospatialMap';
import { CriminalFlow } from './pages/CriminalFlow';
import { EvidenceReport } from './pages/EvidenceReport';
import { UniversalSearch } from './pages/UniversalSearch';
import { SentinelWatch } from './pages/SentinelWatch';
import { UserManagement } from './pages/UserManagement';
import { AuditLog } from './pages/AuditLog';

export const App: React.FC = () => {
  return (
    <ToastProvider>
      <BrowserRouter>
        <Routes>
          <Route element={<AppShell />}>
            {/* Global Dashboard & Cases */}
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/cases" element={<MyCases />} />

            {/* Case #2847 Contextual Analysis Routes */}
            <Route path="/cases/2847" element={<CaseWorkspace />} />
            <Route path="/cases/2847/upload-evidence" element={<UploadEvidence />} />
            <Route path="/cases/2847/timeline" element={<Timeline />} />
            <Route path="/cases/2847/entity-graph" element={<EntityGraph />} />
            <Route path="/cases/2847/geospatial" element={<GeospatialMap />} />
            <Route path="/cases/2847/criminal-flow" element={<CriminalFlow />} />
            <Route path="/cases/2847/evidence-report" element={<EvidenceReport />} />

            {/* Global Intelligence & Administration */}
            <Route path="/search" element={<UniversalSearch />} />
            <Route path="/sentinelwatch" element={<SentinelWatch />} />
            <Route path="/admin/users" element={<UserManagement />} />
            <Route path="/admin/audit-log" element={<AuditLog />} />

            {/* Catch-all fallback */}
            <Route path="*" element={<Navigate to="/dashboard" replace />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </ToastProvider>
  );
};

export default App;
