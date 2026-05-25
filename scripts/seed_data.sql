-- ============================================================
-- Inventário de Ativos de TI - Dados Iniciais (Seed)
-- ============================================================
-- ATENÇÃO: Execute APÓS o Alembic aplicar as migrations
-- ============================================================

-- Categorias padrão
INSERT INTO categories (name, description) VALUES
  ('Computador Desktop', 'Desktops e workstations'),
  ('Notebook', 'Laptops e ultrabooks'),
  ('Monitor', 'Monitores e displays'),
  ('Impressora', 'Impressoras e multifuncionais'),
  ('Servidor', 'Servidores físicos e virtuais'),
  ('Switch / Roteador', 'Equipamentos de rede'),
  ('Telefone / VoIP', 'Telefones IP e fixos'),
  ('Tablet', 'Tablets e iPads'),
  ('Teclado / Mouse', 'Periféricos de entrada'),
  ('Nobreak / UPS', 'Fontes de energia e nobreaks'),
  ('Projetor', 'Projetores e data shows'),
  ('Outros', 'Demais equipamentos')
ON CONFLICT (name) DO NOTHING;

-- Usuários de exemplo (senha: Admin@123)
-- Hash bcrypt para "Admin@123"
INSERT INTO users (name, email, hashed_password, department, is_admin, is_active) VALUES
  (
    'Administrador TI',
    'admin@empresa.com',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj4tbQR.Nq5a',
    'TI',
    true,
    true
  )
ON CONFLICT (email) DO NOTHING;
