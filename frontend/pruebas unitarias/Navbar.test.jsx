import { render, screen, fireEvent } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import Navbar from '../src/components/Navbar';

// Mock de useNavigate
const mockedUsedNavigate = vi.fn();
vi.mock('react-router-dom', async () => {
    const actual = await vi.importActual('react-router-dom');
    return {
        ...actual,
        useNavigate: () => mockedUsedNavigate,
    };
});

describe('Navbar Component', () => {
    beforeEach(() => {
        vi.clearAllMocks();
        localStorage.clear();
    });

    it('debe renderizar el título del sistema', () => {
        render(
            <BrowserRouter>
                <Navbar />
            </BrowserRouter>
        );
        expect(screen.getByText(/Sistema de Votación/i)).toBeInTheDocument();
    });

    it('debe mostrar el nombre de usuario de localStorage', () => {
        localStorage.setItem('username', 'Juan Perez');
        render(
            <BrowserRouter>
                <Navbar />
            </BrowserRouter>
        );
        expect(screen.getByText('Juan Perez')).toBeInTheDocument();
    });

    it('debe llamar a handleLogout al hacer clic en Salir', () => {
        localStorage.setItem('token', 'fake-token');
        render(
            <BrowserRouter>
                <Navbar />
            </BrowserRouter>
        );

        const logoutButton = screen.getByText(/Salir/i);
        fireEvent.click(logoutButton);

        expect(localStorage.getItem('token')).toBeNull();
        expect(mockedUsedNavigate).toHaveBeenCalledWith('/login');
    });
});
