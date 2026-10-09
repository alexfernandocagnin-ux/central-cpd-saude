(() => {
  const root = document.documentElement;
  const preferenceKey = "cpd-saude-theme";
  let toggle;

  const applyTheme = (dark) => {
    if (dark) root.dataset.theme = "dark";
    else delete root.dataset.theme;
    document.querySelector('meta[name="theme-color"]')?.setAttribute("content", dark ? "#041b40" : "#031b50");
    if (toggle) {
      toggle.setAttribute("aria-pressed", String(dark));
      toggle.title = dark ? "Voltar ao modo claro" : "Ativar modo escuro";
    }
  };

  let savedDark = false;
  try {
    savedDark = localStorage.getItem(preferenceKey) === "dark";
  } catch {}
  applyTheme(savedDark);

  document.addEventListener("DOMContentLoaded", () => {
    toggle = document.querySelector(".screen-toggle");
    if (!toggle) return;
    applyTheme(root.dataset.theme === "dark");
    toggle.addEventListener("click", () => {
      const dark = root.dataset.theme !== "dark";
      applyTheme(dark);
      try {
        localStorage.setItem(preferenceKey, dark ? "dark" : "light");
      } catch {}
    });
  }, { once: true });
})();
