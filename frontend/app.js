/* ─── State ──────────────────────────────────────────────────── */
const S = {
  token: localStorage.getItem('ti_token') || null,
  user:  JSON.parse(localStorage.getItem('ti_user') || 'null'),
  page:  'dashboard',
  assetPage: 1,
  assetFilters: {},
};

/* ─── Icons ──────────────────────────────────────────────────── */
const I = {
  cpu:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="2" x2="9" y2="4"/><line x1="15" y1="2" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="22"/><line x1="15" y1="20" x2="15" y2="22"/><line x1="2" y1="9" x2="4" y2="9"/><line x1="2" y1="15" x2="4" y2="15"/><line x1="20" y1="9" x2="22" y2="9"/><line x1="20" y1="15" x2="22" y2="15"/></svg>`,
  grid:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>`,
  box:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>`,
  tag:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>`,
  users:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>`,
  move:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><polyline points="5 9 2 12 5 15"/><polyline points="9 5 12 2 15 5"/><line x1="2" y1="12" x2="22" y2="12"/><polyline points="15 19 12 22 9 19"/><polyline points="19 9 22 12 19 15"/></svg>`,
  logout:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>`,
  plus:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>`,
  edit:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>`,
  trash:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M9 6V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2"/></svg>`,
  search:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>`,
  download: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>`,
  x:        `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>`,
  image:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>`,
  check:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>`,
  info:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>`,
  alert:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>`,
  arrow:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>`,
  activity: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>`,
  dollar:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>`,
  shield:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
  settings: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>`,
};

/* ─── API ──────────────────────────────────────────────────── */
const BASE = '/api/v1';

async function api(method, path, body, isForm = false) {
  const headers = {};
  if (S.token) headers['Authorization'] = `Bearer ${S.token}`;
  if (body && !isForm) headers['Content-Type'] = 'application/json';

  const res = await fetch(BASE + path, {
    method,
    headers,
    body: isForm ? body : (body ? JSON.stringify(body) : undefined),
  });

  if (res.status === 401) { logout(); return null; }

  const ct = res.headers.get('content-type') || '';
  if (ct.includes('application/json')) {
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || 'Erro na requisição');
    return data;
  }
  if (!res.ok) throw new Error('Erro na requisição');
  return res;
}

const get    = (p)    => api('GET',    p);
const post   = (p, b) => api('POST',   p, b);
const put    = (p, b) => api('PUT',    p, b);
const patch  = (p, b) => api('PATCH',  p, b);
const del    = (p)    => api('DELETE', p);
const upload = (p, f) => api('POST',   p, f, true);

/* ─── Auth ──────────────────────────────────────────────────── */
async function login(email, password) {
  const form = new URLSearchParams({ username: email, password });
  const res  = await fetch(`${BASE}/auth/token`, {
    method:  'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body:    form,
  });
  if (!res.ok) throw new Error('E-mail ou senha incorretos.');
  const data = await res.json();
  S.token = data.access_token;
  localStorage.setItem('ti_token', S.token);
  S.user  = await get('/auth/me');
  localStorage.setItem('ti_user', JSON.stringify(S.user));
  navigate('dashboard');
}

function logout() {
  S.token = null; S.user = null;
  localStorage.removeItem('ti_token');
  localStorage.removeItem('ti_user');
  renderLogin();
}

/* ─── Router ──────────────────────────────────────────────── */
function navigate(page, params = {}) {
  S.page = page;
  S.params = params;
  if (page === 'assets') { S.assetPage = 1; S.assetFilters = {}; }
  renderApp();
}

function renderApp() {
  if (!S.token) { renderLogin(); return; }
  const app = document.getElementById('app');
  app.innerHTML = `
    <div class="layout">
      ${renderSidebar()}
      <div class="main">
        <div id="page-content"></div>
      </div>
    </div>
  `;
  bindNav();

  const pages = {
    dashboard:   loadDashboard,
    assets:      loadAssets,
    categories:  loadCategories,
    users:       loadUsers,
    movements:   loadMovements,
  };
  (pages[S.page] || loadDashboard)();
}

/* ─── Sidebar ──────────────────────────────────────────────── */
function renderSidebar() {
  const nav = [
    { id: 'dashboard',  label: 'Dashboard',      icon: I.grid },
    { id: 'assets',     label: 'Ativos',          icon: I.box },
    { id: 'categories', label: 'Categorias',      icon: I.tag },
    { id: 'movements',  label: 'Movimentações',   icon: I.move },
    { id: 'users',      label: 'Usuários',        icon: I.users },
  ];
  const initial = (S.user?.name || 'A').charAt(0).toUpperCase();
  return `
    <aside class="sidebar">
      <div class="sidebar-logo">
        <div class="sidebar-logo-mark">
          <div class="logo-icon">${I.cpu}</div>
          <div>
            <div class="logo-name">Inventário TI</div>
            <div class="logo-sub">Gestão de Ativos</div>
          </div>
        </div>
      </div>
      <nav class="sidebar-nav">
        <div class="nav-section-label">Menu</div>
        ${nav.map(n => `
          <div class="nav-item ${S.page === n.id ? 'active' : ''}" data-nav="${n.id}">
            ${n.icon}<span>${n.label}</span>
          </div>
        `).join('')}
      </nav>
      <div class="sidebar-footer">
        <div class="user-card">
          <div class="avatar">${initial}</div>
          <div class="user-info">
            <div class="user-name">${S.user?.name || ''}</div>
            <div class="user-role">${S.user?.is_admin ? 'Administrador' : 'Usuário'}</div>
          </div>
          <button class="btn-logout" onclick="logout()" title="Sair">${I.logout}</button>
        </div>
      </div>
    </aside>
  `;
}

function bindNav() {
  document.querySelectorAll('[data-nav]').forEach(el => {
    el.addEventListener('click', () => navigate(el.dataset.nav));
  });
}

function setContent(html) {
  document.getElementById('page-content').innerHTML = html;
}

/* ─── Login Page ──────────────────────────────────────────── */
function renderLogin() {
  document.getElementById('app').innerHTML = `
    <div class="login-wrap">
      <div class="login-card">
        <div class="login-logo">
          <div class="login-logo-icon">${I.cpu}</div>
          <span class="login-logo-text">Inventário TI</span>
        </div>
        <p class="login-sub">Acesse sua conta para continuar</p>
        <div id="login-error" class="login-error"></div>
        <div class="form-group">
          <label>E-mail</label>
          <input id="l-email" class="input" type="email" placeholder="admin@empresa.com" autocomplete="email" />
        </div>
        <div class="form-group">
          <label>Senha</label>
          <input id="l-pass" class="input" type="password" placeholder="••••••••" autocomplete="current-password" />
        </div>
        <button id="btn-login" class="btn btn-primary" style="width:100%;justify-content:center;margin-top:8px">
          Entrar
        </button>
      </div>
    </div>
  `;
  const doLogin = async () => {
    const btn = document.getElementById('btn-login');
    const errEl = document.getElementById('login-error');
    errEl.style.display = 'none';
    btn.disabled = true;
    btn.innerHTML = `<span class="spinner"></span> Entrando...`;
    try {
      await login(
        document.getElementById('l-email').value,
        document.getElementById('l-pass').value,
      );
    } catch(e) {
      errEl.textContent = e.message;
      errEl.style.display = 'block';
      btn.disabled = false;
      btn.innerHTML = 'Entrar';
    }
  };
  document.getElementById('btn-login').addEventListener('click', doLogin);
  document.getElementById('l-pass').addEventListener('keydown', e => e.key === 'Enter' && doLogin());
  document.getElementById('l-email').addEventListener('keydown', e => e.key === 'Enter' && doLogin());
}

/* ─── Dashboard ──────────────────────────────────────────── */
async function loadDashboard() {
  setContent(`
    <div class="page">
      <div class="page-header">
        <div><div class="page-title">Dashboard</div><div class="page-subtitle">Visão geral do inventário</div></div>
      </div>
      <div id="dash-content"><div style="text-align:center;padding:60px;color:var(--text-3)"><span class="spinner"></span></div></div>
    </div>
  `);
  try {
    const d = await get('/dashboard/');
    renderDashboardData(d);
  } catch(e) { toast(e.message, 'error'); }
}

function renderDashboardData(d) {
  const currency = v => v > 0 ? `R$ ${v.toLocaleString('pt-BR', {minimumFractionDigits:2})}` : '—';
  const statusColors = {
    'ativo': '#6366F1', 'inativo': '#94A3B8', 'manutencao': '#F59E0B',
    'descartado': '#EF4444', 'perdido': '#8B5CF6', 'reservado': '#3B82F6',
  };
  const maxCat = Math.max(...d.assets_by_category.map(c => c.count), 1);

  document.getElementById('dash-content').innerHTML = `
    <div class="stats-grid">
      ${statCard('Total de Ativos', d.total_assets, 'var(--primary-light)', 'var(--primary)', I.box, `Valor total: ${currency(d.total_value)}`)}
      ${statCard('Ativos em Uso', d.active_assets, 'var(--success-bg)', 'var(--success)', I.check)}
      ${statCard('Em Manutenção', d.maintenance_assets, 'var(--warning-bg)', 'var(--warning)', I.settings)}
      ${statCard('Sem Responsável', d.assets_without_responsible, 'var(--danger-bg)', 'var(--danger)', I.users, d.warranty_expiring_soon > 0 ? `${d.warranty_expiring_soon} garantia(s) vencendo` : '')}
    </div>

    ${d.warranty_expiring_soon > 0 ? `
      <div class="card mb-16" style="margin-bottom:20px;border-color:var(--warning);background:var(--warning-bg)">
        <div class="card-body" style="padding:14px 20px;display:flex;align-items:center;gap:12px">
          <span style="color:var(--warning)">${I.alert}</span>
          <span style="font-size:13.5px;color:var(--warning-text);font-weight:500">
            ${d.warranty_expiring_soon} ativo(s) com garantia vencendo nos próximos 30 dias.
          </span>
          <button class="btn btn-sm btn-secondary" style="margin-left:auto" onclick="navigate('assets')">Ver ativos</button>
        </div>
      </div>` : ''}

    <div class="grid-2" style="gap:20px">
      <div class="card">
        <div class="card-header"><span class="card-title">Ativos por Status</span></div>
        <div class="card-body">
          <div class="bar-list">
            ${d.assets_by_status.filter(s => s.count > 0).map(s => `
              <div class="bar-item">
                <div class="bar-label">
                  <span class="bar-label-name">${statusLabel(s.status)}</span>
                  <span class="bar-label-value">${s.count}</span>
                </div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:${d.total_assets ? (s.count/d.total_assets*100) : 0}%;background:${statusColors[s.status]||'var(--primary)'}"></div>
                </div>
              </div>
            `).join('')}
            ${d.assets_by_status.every(s => s.count === 0) ? '<div class="text-muted text-small" style="text-align:center;padding:20px">Nenhum ativo cadastrado</div>' : ''}
          </div>
        </div>
      </div>

      <div class="card">
        <div class="card-header"><span class="card-title">Ativos por Categoria</span></div>
        <div class="card-body">
          <div class="bar-list">
            ${d.assets_by_category.slice(0,8).map(c => `
              <div class="bar-item">
                <div class="bar-label">
                  <span class="bar-label-name">${c.category}</span>
                  <span class="bar-label-value">${c.count}</span>
                </div>
                <div class="bar-track">
                  <div class="bar-fill" style="width:${(c.count/maxCat*100)}%;background:var(--primary)"></div>
                </div>
              </div>
            `).join('')}
            ${d.assets_by_category.length === 0 ? '<div class="text-muted text-small" style="text-align:center;padding:20px">Nenhum dado</div>' : ''}
          </div>
        </div>
      </div>
    </div>

    <div class="card" style="margin-top:20px">
      <div class="card-header">
        <span class="card-title">Movimentações Recentes</span>
        <button class="btn btn-sm btn-ghost" onclick="navigate('movements')">${I.arrow} Ver todas</button>
      </div>
      <div class="table-wrap">
        ${d.recent_movements.length > 0 ? `
          <table>
            <thead><tr>
              <th>Tag</th><th>Ativo</th><th>Tipo</th><th>Data</th><th>Por</th>
            </tr></thead>
            <tbody>
              ${d.recent_movements.map(m => `
                <tr>
                  <td class="td-mono">${m.asset_tag}</td>
                  <td>${m.asset_name}</td>
                  <td>${movBadge(m.movement_type)}</td>
                  <td class="td-muted text-small">${m.created_at}</td>
                  <td class="td-muted">${m.created_by}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>` : `<div class="empty"><div class="empty-title">Nenhuma movimentação</div></div>`}
      </div>
    </div>
  `;
}

function statCard(label, value, bgColor, iconColor, icon, sub = '') {
  return `
    <div class="stat-card">
      <div class="stat-icon" style="background:${bgColor};color:${iconColor}">${icon}</div>
      <div class="stat-body">
        <div class="stat-value">${value}</div>
        <div class="stat-label">${label}</div>
        ${sub ? `<div class="stat-sub">${sub}</div>` : ''}
      </div>
    </div>`;
}

/* ─── Assets ──────────────────────────────────────────────── */
async function loadAssets() {
  setContent(`
    <div class="page">
      <div class="page-header">
        <div><div class="page-title">Ativos de TI</div><div class="page-subtitle">Gerencie todos os equipamentos</div></div>
        <div class="page-actions">
          <button class="btn btn-secondary btn-sm" id="btn-export-csv">${I.download} CSV</button>
          <button class="btn btn-secondary btn-sm" id="btn-export-xlsx">${I.download} Excel</button>
          <button class="btn btn-primary" id="btn-new-asset">${I.plus} Novo Ativo</button>
        </div>
      </div>
      <div class="search-bar">
        <div class="search-input-wrap">${I.search}<input id="asset-search" class="input" placeholder="Buscar por tag, nome, série, marca..." /></div>
        <select id="f-status" class="select filter-select"><option value="">Todos os status</option>${statusOptions()}</select>
        <select id="f-category" class="select filter-select"><option value="">Todas as categorias</option></select>
      </div>
      <div class="card"><div id="assets-table-wrap"><div class="loading-row"><table><tbody><tr><td><span class="spinner"></span></td></tr></tbody></table></div></div></div>
    </div>
  `);

  // Load categories for filter
  try {
    const cats = await get('/categories/');
    const sel = document.getElementById('f-category');
    cats.forEach(c => { const o = document.createElement('option'); o.value = c.id; o.textContent = c.name; sel.appendChild(o); });
  } catch(_) {}

  document.getElementById('btn-new-asset').addEventListener('click', () => showAssetModal());
  document.getElementById('btn-export-csv').addEventListener('click', () => exportFile('/assets/export/csv', 'ativos_ti.csv'));
  document.getElementById('btn-export-xlsx').addEventListener('click', () => exportFile('/assets/export/excel', 'ativos_ti.xlsx'));

  let searchTimer;
  const doSearch = () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => { S.assetPage = 1; fetchAssets(); }, 350);
  };
  document.getElementById('asset-search').addEventListener('input', doSearch);
  document.getElementById('f-status').addEventListener('change', () => { S.assetPage = 1; fetchAssets(); });
  document.getElementById('f-category').addEventListener('change', () => { S.assetPage = 1; fetchAssets(); });

  fetchAssets();
}

async function fetchAssets() {
  const search   = document.getElementById('asset-search')?.value || '';
  const status   = document.getElementById('f-status')?.value || '';
  const category = document.getElementById('f-category')?.value || '';

  const params = new URLSearchParams({ page: S.assetPage, page_size: 15 });
  if (search)   params.append('search', search);
  if (status)   params.append('status', status);
  if (category) params.append('category_id', category);

  try {
    const data = await get(`/assets/?${params}`);
    renderAssetsTable(data);
  } catch(e) { toast(e.message, 'error'); }
}

function renderAssetsTable(data) {
  const { items, total, page, pages } = data;
  const wrap = document.getElementById('assets-table-wrap');
  if (items.length === 0) {
    wrap.innerHTML = `<div class="empty">${I.box}<div class="empty-title">Nenhum ativo encontrado</div><div class="empty-sub">Tente ajustar os filtros ou cadastre um novo ativo.</div></div>`;
    return;
  }
  wrap.innerHTML = `
    <div class="table-wrap">
      <table>
        <thead><tr>
          <th>Ativo</th><th>Status</th><th>Categoria</th><th>Responsável</th><th>Localização</th><th></th>
        </tr></thead>
        <tbody>
          ${items.map(a => `
            <tr>
              <td>
                <div class="asset-name-cell">
                  <div class="asset-img">${a.image_path ? `<img src="/uploads/${a.image_path}" alt="">` : `<div class="asset-img-placeholder">${I.image}</div>`}</div>
                  <div>
                    <div class="asset-name-text">${a.name}</div>
                    <div class="asset-tag-text">${a.tag}${a.brand ? ' · ' + a.brand : ''}${a.model ? ' ' + a.model : ''}</div>
                  </div>
                </div>
              </td>
              <td>${statusBadge(a.status)}</td>
              <td class="td-muted">${a.category?.name || '—'}</td>
              <td class="td-muted">${a.responsible_user?.name || '—'}</td>
              <td class="td-muted">${a.location || '—'}</td>
              <td>
                <div style="display:flex;gap:4px">
                  <button class="btn-icon" title="Editar" onclick="showAssetModal(${a.id})">${I.edit}</button>
                  <button class="btn-icon" title="Movimentação" onclick="showMovementModal(${a.id})">${I.move}</button>
                  <button class="btn-icon" title="Upload imagem" onclick="showImageModal(${a.id})">${I.image}</button>
                </div>
              </td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    </div>
    <div class="pagination">
      <span>${total} ativo${total !== 1 ? 's' : ''} encontrado${total !== 1 ? 's' : ''}</span>
      <div class="pagination-pages">
        ${Array.from({length: pages}, (_, i) => i + 1).map(p => `
          <button class="page-btn ${p === page ? 'active' : ''}" onclick="goToPage(${p})">${p}</button>
        `).join('')}
      </div>
    </div>
  `;
}

function goToPage(p) { S.assetPage = p; fetchAssets(); }

/* ─── Asset Modal ──────────────────────────────────────────── */
async function showAssetModal(id = null) {
  let asset = null;
  let cats = [], users = [];
  try {
    [cats, users] = await Promise.all([get('/categories/'), get('/users/')]);
    if (id) asset = await get(`/assets/${id}`);
  } catch(e) { toast(e.message, 'error'); return; }

  const v = (field, def = '') => asset?.[field] ?? def;
  const selOpt = (arr, val, label, valField = 'id') => arr.map(x =>
    `<option value="${x[valField]}" ${x[valField] == val ? 'selected' : ''}>${x[label]}</option>`
  ).join('');

  openModal(`${id ? 'Editar' : 'Novo'} Ativo`, `
    <div class="form-row">
      <div class="form-group">
        <label>Tag *</label>
        <input id="f-tag" class="input" placeholder="TI-001" value="${v('tag')}" ${id ? 'readonly style="background:var(--bg)"' : ''}>
      </div>
      <div class="form-group">
        <label>Nome *</label>
        <input id="f-name" class="input" placeholder="Notebook Dell Latitude" value="${v('name')}">
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label>Marca</label>
        <input id="f-brand" class="input" placeholder="Dell, Apple, HP..." value="${v('brand')}">
      </div>
      <div class="form-group">
        <label>Modelo</label>
        <input id="f-model" class="input" placeholder="Latitude 5420" value="${v('model')}">
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label>Número de Série</label>
        <input id="f-serial" class="input" placeholder="SN123456" value="${v('serial_number')}">
      </div>
      <div class="form-group">
        <label>Status</label>
        <select id="f-status-field" class="select">
          ${statusOptions(v('status', 'ativo'))}
        </select>
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label>Categoria</label>
        <select id="f-cat" class="select">
          <option value="">Sem categoria</option>
          ${selOpt(cats, v('category_id'), 'name')}
        </select>
      </div>
      <div class="form-group">
        <label>Responsável</label>
        <select id="f-user" class="select">
          <option value="">Sem responsável</option>
          ${selOpt(users, v('responsible_user_id'), 'name')}
        </select>
      </div>
    </div>
    <div class="form-group">
      <label>Localização</label>
      <input id="f-loc" class="input" placeholder="Sala TI, 2° andar..." value="${v('location')}">
    </div>
    <div class="form-row-3">
      <div class="form-group">
        <label>Data de Compra</label>
        <input id="f-pdate" class="input" type="date" value="${v('purchase_date')}">
      </div>
      <div class="form-group">
        <label>Valor (R$)</label>
        <input id="f-pval" class="input" type="number" step="0.01" placeholder="0.00" value="${v('purchase_value')}">
      </div>
      <div class="form-group">
        <label>Garantia até</label>
        <input id="f-warranty" class="input" type="date" value="${v('warranty_expires')}">
      </div>
    </div>
    <div class="form-group">
      <label>Observações</label>
      <textarea id="f-notes" class="textarea" placeholder="Informações adicionais...">${v('notes')}</textarea>
    </div>
  `, async () => {
    const body = {
      tag:                document.getElementById('f-tag').value.trim(),
      name:               document.getElementById('f-name').value.trim(),
      brand:              document.getElementById('f-brand').value.trim() || null,
      model:              document.getElementById('f-model').value.trim() || null,
      serial_number:      document.getElementById('f-serial').value.trim() || null,
      status:             document.getElementById('f-status-field').value,
      category_id:        document.getElementById('f-cat').value || null,
      responsible_user_id:document.getElementById('f-user').value || null,
      location:           document.getElementById('f-loc').value.trim() || null,
      purchase_date:      document.getElementById('f-pdate').value || null,
      purchase_value:     parseFloat(document.getElementById('f-pval').value) || null,
      warranty_expires:   document.getElementById('f-warranty').value || null,
      notes:              document.getElementById('f-notes').value.trim() || null,
    };
    if (!body.tag || !body.name) { toast('Tag e nome são obrigatórios.', 'error'); return false; }
    if (id) await put(`/assets/${id}`, body);
    else    await post('/assets/', body);
    toast(id ? 'Ativo atualizado.' : 'Ativo cadastrado.', 'success');
    fetchAssets();
  }, 'modal-lg');
}

/* ─── Movement Modal ──────────────────────────────────────── */
async function showMovementModal(assetId) {
  let users = [];
  try { users = await get('/users/'); } catch(_) {}

  const movTypes = [
    ['atribuicao','Atribuição'], ['devolucao','Devolução'], ['transferencia','Transferência'],
    ['entrada_manutencao','Entrada Manutenção'], ['saida_manutencao','Saída Manutenção'],
    ['descarte','Descarte'], ['aquisicao','Aquisição'],
  ];
  const selOpt = (arr, val, lbl, vf = 'id') => arr.map(x =>
    `<option value="${x[vf]}" ${x[vf] == val ? 'selected' : ''}>${x[lbl]}</option>`
  ).join('');

  openModal('Registrar Movimentação', `
    <div class="form-group">
      <label>Tipo de Movimentação *</label>
      <select id="mv-type" class="select">
        ${movTypes.map(([v,l]) => `<option value="${v}">${l}</option>`).join('')}
      </select>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label>De (Localização)</label>
        <input id="mv-from-loc" class="input" placeholder="Origem...">
      </div>
      <div class="form-group">
        <label>Para (Localização)</label>
        <input id="mv-to-loc" class="input" placeholder="Destino...">
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label>De (Usuário)</label>
        <select id="mv-from-user" class="select">
          <option value="">Nenhum</option>
          ${selOpt(users, '', 'name')}
        </select>
      </div>
      <div class="form-group">
        <label>Para (Usuário)</label>
        <select id="mv-to-user" class="select">
          <option value="">Nenhum</option>
          ${selOpt(users, '', 'name')}
        </select>
      </div>
    </div>
    <div class="form-group">
      <label>Observações</label>
      <textarea id="mv-notes" class="textarea" placeholder="Detalhes sobre a movimentação..."></textarea>
    </div>
  `, async () => {
    const body = {
      asset_id:      assetId,
      movement_type: document.getElementById('mv-type').value,
      from_location: document.getElementById('mv-from-loc').value || null,
      to_location:   document.getElementById('mv-to-loc').value || null,
      from_user_id:  document.getElementById('mv-from-user').value || null,
      to_user_id:    document.getElementById('mv-to-user').value || null,
      notes:         document.getElementById('mv-notes').value || null,
    };
    await post('/movements/', body);
    toast('Movimentação registrada.', 'success');
    fetchAssets();
  });
}

/* ─── Image Modal ──────────────────────────────────────────── */
function showImageModal(assetId) {
  openModal('Upload de Imagem', `
    <div class="form-group">
      <label>Selecione uma imagem (JPG, PNG, GIF, WebP — máx. 5MB)</label>
      <input id="img-file" class="input" type="file" accept="image/*" style="padding:7px">
    </div>
  `, async () => {
    const file = document.getElementById('img-file').files[0];
    if (!file) { toast('Selecione um arquivo.', 'error'); return false; }
    const form = new FormData();
    form.append('file', file);
    await upload(`/assets/${assetId}/image`, form);
    toast('Imagem atualizada.', 'success');
    fetchAssets();
  }, 'modal-sm');
}

/* ─── Categories ──────────────────────────────────────────── */
async function loadCategories() {
  setContent(`
    <div class="page">
      <div class="page-header">
        <div><div class="page-title">Categorias</div><div class="page-subtitle">Organize os tipos de equipamento</div></div>
        <div class="page-actions">
          <button class="btn btn-primary" id="btn-new-cat">${I.plus} Nova Categoria</button>
        </div>
      </div>
      <div id="cat-content"><div style="text-align:center;padding:60px;color:var(--text-3)"><span class="spinner"></span></div></div>
    </div>
  `);
  document.getElementById('btn-new-cat').addEventListener('click', () => showCategoryModal());
  fetchCategories();
}

async function fetchCategories() {
  try {
    const cats = await get('/categories/');
    const el = document.getElementById('cat-content');
    if (cats.length === 0) {
      el.innerHTML = `<div class="empty">${I.tag}<div class="empty-title">Nenhuma categoria</div><div class="empty-sub">Crie a primeira categoria para organizar os ativos.</div></div>`;
      return;
    }
    el.innerHTML = `<div class="category-grid">${cats.map(c => `
      <div class="category-card">
        <div class="cat-info">
          <div class="cat-name">${c.name}</div>
          ${c.description ? `<div class="cat-desc">${c.description}</div>` : ''}
          <div class="cat-count">${c.asset_count} ativo${c.asset_count !== 1 ? 's' : ''}</div>
        </div>
        <div class="cat-actions">
          <button class="btn-icon" title="Editar" onclick="showCategoryModal(${c.id},'${esc(c.name)}','${esc(c.description||'')}')">${I.edit}</button>
          <button class="btn-icon" title="Remover" onclick="deleteCategory(${c.id})">${I.trash}</button>
        </div>
      </div>
    `).join('')}</div>`;
  } catch(e) { toast(e.message, 'error'); }
}

function showCategoryModal(id = null, name = '', desc = '') {
  openModal(id ? 'Editar Categoria' : 'Nova Categoria', `
    <div class="form-group">
      <label>Nome *</label>
      <input id="cat-name" class="input" placeholder="Ex: Notebook, Monitor..." value="${name}">
    </div>
    <div class="form-group">
      <label>Descrição</label>
      <textarea id="cat-desc" class="textarea" placeholder="Descreva esta categoria...">${desc}</textarea>
    </div>
  `, async () => {
    const body = {
      name: document.getElementById('cat-name').value.trim(),
      description: document.getElementById('cat-desc').value.trim() || null,
    };
    if (!body.name) { toast('Nome é obrigatório.', 'error'); return false; }
    if (id) await put(`/categories/${id}`, body);
    else    await post('/categories/', body);
    toast(id ? 'Categoria atualizada.' : 'Categoria criada.', 'success');
    fetchCategories();
  }, 'modal-sm');
}

async function deleteCategory(id) {
  if (!confirm('Remover esta categoria? Os ativos não serão excluídos.')) return;
  try {
    await del(`/categories/${id}`);
    toast('Categoria removida.', 'success');
    fetchCategories();
  } catch(e) { toast(e.message, 'error'); }
}

/* ─── Users ───────────────────────────────────────────────── */
async function loadUsers() {
  setContent(`
    <div class="page">
      <div class="page-header">
        <div><div class="page-title">Usuários</div><div class="page-subtitle">Gerencie os responsáveis pelos ativos</div></div>
        <div class="page-actions">
          ${S.user?.is_admin ? `<button class="btn btn-primary" id="btn-new-user">${I.plus} Novo Usuário</button>` : ''}
        </div>
      </div>
      <div class="card"><div id="users-content"><div class="loading-row"><table><tbody><tr><td><span class="spinner"></span></td></tr></tbody></table></div></div></div>
    </div>
  `);
  document.getElementById('btn-new-user')?.addEventListener('click', () => showUserModal());
  fetchUsers();
}

async function fetchUsers() {
  try {
    const users = await get('/users/');
    const el = document.getElementById('users-content');
    if (users.length === 0) {
      el.innerHTML = `<div class="empty">${I.users}<div class="empty-title">Nenhum usuário</div></div>`;
      return;
    }
    el.innerHTML = `
      <div class="table-wrap">
        <table>
          <thead><tr><th>Nome</th><th>E-mail</th><th>Departamento</th><th>Telefone</th><th>Status</th><th></th></tr></thead>
          <tbody>
            ${users.map(u => `
              <tr>
                <td>
                  <div class="flex-center gap-8">
                    <div class="avatar" style="width:28px;height:28px;font-size:11px">${u.name.charAt(0)}</div>
                    <div>
                      <span class="fw-500">${u.name}</span>
                      ${u.is_admin ? ' <span class="badge badge-admin">Admin</span>' : ''}
                    </div>
                  </div>
                </td>
                <td class="td-muted">${u.email}</td>
                <td class="td-muted">${u.department || '—'}</td>
                <td class="td-muted">${u.phone || '—'}</td>
                <td>${u.is_active ? `<span class="badge badge-success">${I.check}Ativo</span>` : `<span class="badge badge-gray">Inativo</span>`}</td>
                <td>
                  ${S.user?.is_admin ? `<button class="btn-icon" onclick="showUserModal(${JSON.stringify(u).replace(/"/g,'&quot;')})">${I.edit}</button>` : ''}
                </td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;
  } catch(e) { toast(e.message, 'error'); }
}

function showUserModal(user = null) {
  openModal(user ? 'Editar Usuário' : 'Novo Usuário', `
    <div class="form-row">
      <div class="form-group">
        <label>Nome *</label>
        <input id="u-name" class="input" placeholder="João Silva" value="${user?.name || ''}">
      </div>
      <div class="form-group">
        <label>E-mail *</label>
        <input id="u-email" class="input" type="email" placeholder="joao@empresa.com" value="${user?.email || ''}" ${user ? 'readonly style="background:var(--bg)"' : ''}>
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label>Departamento</label>
        <input id="u-dept" class="input" placeholder="TI, Financeiro..." value="${user?.department || ''}">
      </div>
      <div class="form-group">
        <label>Telefone</label>
        <input id="u-phone" class="input" placeholder="(11) 9999-9999" value="${user?.phone || ''}">
      </div>
    </div>
    ${!user ? `
      <div class="form-group">
        <label>Senha *</label>
        <input id="u-pass" class="input" type="password" placeholder="Mínimo 6 caracteres">
      </div>
      <div class="form-group">
        <label><input id="u-admin" type="checkbox" style="margin-right:6px"> Administrador</label>
      </div>` : `
      <div class="form-group">
        <label><input id="u-active" type="checkbox" style="margin-right:6px" ${user.is_active ? 'checked' : ''}> Usuário ativo</label>
      </div>
      <div class="form-group">
        <label><input id="u-admin" type="checkbox" style="margin-right:6px" ${user.is_admin ? 'checked' : ''}> Administrador</label>
      </div>`}
  `, async () => {
    const name = document.getElementById('u-name').value.trim();
    const email = document.getElementById('u-email').value.trim();
    if (!name) { toast('Nome é obrigatório.', 'error'); return false; }
    if (!user) {
      const pass = document.getElementById('u-pass').value;
      if (!pass || pass.length < 6) { toast('Senha deve ter no mínimo 6 caracteres.', 'error'); return false; }
      await post('/users/', {
        name, email, password: pass,
        department: document.getElementById('u-dept').value.trim() || null,
        phone: document.getElementById('u-phone').value.trim() || null,
        is_admin: document.getElementById('u-admin').checked,
      });
      toast('Usuário criado.', 'success');
    } else {
      await put(`/users/${user.id}`, {
        name,
        department: document.getElementById('u-dept').value.trim() || null,
        phone: document.getElementById('u-phone').value.trim() || null,
        is_active: document.getElementById('u-active').checked,
        is_admin: document.getElementById('u-admin').checked,
      });
      toast('Usuário atualizado.', 'success');
    }
    fetchUsers();
  });
}

/* ─── Movements ──────────────────────────────────────────── */
async function loadMovements() {
  setContent(`
    <div class="page">
      <div class="page-header">
        <div><div class="page-title">Movimentações</div><div class="page-subtitle">Histórico completo de movimentações</div></div>
      </div>
      <div class="card"><div id="mov-content"><div class="loading-row"><table><tbody><tr><td><span class="spinner"></span></td></tr></tbody></table></div></div></div>
    </div>
  `);
  try {
    const movs = await get('/movements/recent?limit=50');
    const el = document.getElementById('mov-content');
    if (movs.length === 0) {
      el.innerHTML = `<div class="empty">${I.move}<div class="empty-title">Nenhuma movimentação</div></div>`;
      return;
    }
    el.innerHTML = `
      <div class="table-wrap">
        <table>
          <thead><tr><th>Tipo</th><th>Ativo</th><th>De</th><th>Para</th><th>Observações</th><th>Data</th><th>Por</th></tr></thead>
          <tbody>
            ${movs.map(m => `
              <tr>
                <td>${movBadge(m.movement_type)}</td>
                <td class="td-mono">${m.asset_id}</td>
                <td class="td-muted text-small">${m.from_user?.name || '—'}${m.from_location ? `<br><span style="color:var(--text-3)">${m.from_location}</span>` : ''}</td>
                <td class="td-muted text-small">${m.to_user?.name || '—'}${m.to_location ? `<br><span style="color:var(--text-3)">${m.to_location}</span>` : ''}</td>
                <td class="td-muted text-small" style="max-width:200px;overflow:hidden;text-overflow:ellipsis">${m.notes || '—'}</td>
                <td class="td-muted text-small">${formatDate(m.created_at)}</td>
                <td class="td-muted">${m.created_by?.name || 'Sistema'}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>
    `;
  } catch(e) { toast(e.message, 'error'); }
}

/* ─── Modal engine ──────────────────────────────────────────── */
function openModal(title, bodyHtml, onSave, sizeClass = '') {
  closeModal();
  const overlay = document.createElement('div');
  overlay.className = 'modal-overlay';
  overlay.id = 'modal-overlay';
  overlay.innerHTML = `
    <div class="modal ${sizeClass}">
      <div class="modal-header">
        <span class="modal-title">${title}</span>
        <button class="modal-close" onclick="closeModal()">${I.x}</button>
      </div>
      <div class="modal-body">${bodyHtml}</div>
      <div class="modal-footer">
        <button class="btn btn-secondary" onclick="closeModal()">Cancelar</button>
        <button class="btn btn-primary" id="modal-save">Salvar</button>
      </div>
    </div>
  `;
  document.body.appendChild(overlay);
  overlay.addEventListener('click', e => { if (e.target === overlay) closeModal(); });

  document.getElementById('modal-save').addEventListener('click', async () => {
    const btn = document.getElementById('modal-save');
    btn.disabled = true;
    btn.innerHTML = `<span class="spinner"></span>`;
    try {
      const res = await onSave();
      if (res !== false) closeModal();
    } catch(e) {
      toast(e.message, 'error');
    } finally {
      if (document.getElementById('modal-save')) {
        btn.disabled = false;
        btn.innerHTML = 'Salvar';
      }
    }
  });
}

function closeModal() {
  document.getElementById('modal-overlay')?.remove();
}

/* ─── Helpers ──────────────────────────────────────────────── */
function statusBadge(s) {
  const map = {
    ativo:       ['badge-success', 'Ativo'],
    inativo:     ['badge-gray',    'Inativo'],
    manutencao:  ['badge-warning', 'Manutenção'],
    descartado:  ['badge-danger',  'Descartado'],
    perdido:     ['badge-purple',  'Perdido'],
    reservado:   ['badge-info',    'Reservado'],
  };
  const [cls, label] = map[s] || ['badge-gray', s];
  return `<span class="badge ${cls}"><span class="badge-dot"></span>${label}</span>`;
}

function statusLabel(s) {
  const map = { ativo:'Ativo', inativo:'Inativo', manutencao:'Manutenção', descartado:'Descartado', perdido:'Perdido', reservado:'Reservado' };
  return map[s] || s;
}

function statusOptions(selected = '') {
  return [
    ['ativo','Ativo'], ['inativo','Inativo'], ['manutencao','Manutenção'],
    ['descartado','Descartado'], ['perdido','Perdido'], ['reservado','Reservado'],
  ].map(([v,l]) => `<option value="${v}" ${v === selected ? 'selected' : ''}>${l}</option>`).join('');
}

function movBadge(t) {
  const map = {
    atribuicao:        ['badge-success', 'Atribuição'],
    devolucao:         ['badge-info',    'Devolução'],
    transferencia:     ['badge-purple',  'Transferência'],
    entrada_manutencao:['badge-warning', 'Ent. Manutenção'],
    saida_manutencao:  ['badge-info',    'Saí. Manutenção'],
    descarte:          ['badge-danger',  'Descarte'],
    aquisicao:         ['badge-success', 'Aquisição'],
  };
  const [cls, label] = map[t] || ['badge-gray', t];
  return `<span class="badge ${cls}">${label}</span>`;
}

function formatDate(iso) {
  if (!iso) return '—';
  return new Date(iso).toLocaleString('pt-BR', { day:'2-digit', month:'2-digit', year:'numeric', hour:'2-digit', minute:'2-digit' });
}

function esc(str) { return (str || '').replace(/'/g, "\\'").replace(/"/g, '&quot;'); }

async function exportFile(path, filename) {
  try {
    const res = await api('GET', path);
    if (res instanceof Response) {
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a'); a.href = url; a.download = filename;
      a.click(); URL.revokeObjectURL(url);
    }
  } catch(e) { toast(e.message, 'error'); }
}

/* ─── Toast ──────────────────────────────────────────────────── */
function toast(msg, type = 'info') {
  const icons = { success: I.check, error: I.alert, info: I.info };
  const el = document.createElement('div');
  el.className = `toast toast-${type === 'error' ? 'error' : type === 'success' ? 'success' : 'info'}`;
  el.innerHTML = `${icons[type] || I.info}<span class="toast-msg">${msg}</span>`;
  document.getElementById('toast-container').appendChild(el);
  setTimeout(() => el.remove(), 4000);
}

/* ─── Init ──────────────────────────────────────────────────── */
renderApp();
