-- ============================================================
-- Inventário de Ativos de TI - Script de Inicialização
-- ============================================================

-- Extensões úteis
CREATE EXTENSION IF NOT EXISTS "unaccent";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Índices de texto completo (trigram) para buscas rápidas
-- Criados após o Alembic rodar as migrations
-- CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_assets_name_trgm ON assets USING GIN (name gin_trgm_ops);
-- CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_assets_tag_trgm ON assets USING GIN (tag gin_trgm_ops);
