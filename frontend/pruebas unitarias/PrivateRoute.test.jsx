import { render, screen } from '@testing-library/react';
import { MemoryRouter, Routes, Route } from 'react-router-dom';
import { describe, it, expect, beforeEach, vi } from 'vitest';
import PrivateRoute from '../src/components/PrivateRoute';

describe('PrivateRoute Component', () => {
    beforeEach(() => {
        localStorage.clear();
        vi.clearAllMocks();
    });

    it('debe redirigir al login si no hay token', () => {
        render(
            <MemoryRouter initialEntries={['/protected']}>
                <Routes>
                    <Route path="/login" element={<div>Pagina de Login</div>} />
                    <Route 
                        path="/protected" 
                        element={
                            <PrivateRoute>
                                <div>Contenido Protegido</div>
                            </PrivateRoute>
                        } 
                    />
                </Routes>
            </MemoryRouter>
        );

        expect(screen.getByText(/Pagina de Login/i)).toBeInTheDocument();
        expect(screen.queryByText(/Contenido Protegido/i)).not.toBeInTheDocument();
    });

    it('debe mostrar el contenido si hay un token presente', () => {
        localStorage.setItem('token', 'fake-token');
        render(
            <MemoryRouter initialEntries={['/protected']}>
                <Routes>
                    <Route path="/login" element={<div>Pagina de Login</div>} />
                    <Route 
                        path="/protected" 
                        element={
                            <PrivateRoute>
                                <div>Contenido Protegido</div>
                            </PrivateRoute>
                        } 
                    />
                </Routes>
            </MemoryRouter>
        );

        expect(screen.getByText(/Contenido Protegido/i)).toBeInTheDocument();
        expect(screen.queryByText(/Pagina de Login/i)).not.toBeInTheDocument();
    });
});
