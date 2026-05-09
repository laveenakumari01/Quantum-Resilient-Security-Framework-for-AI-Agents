const BASE_URL = "http://localhost:8000";

// function to save token
export function saveToken(token) {
  localStorage.setItem("token", token);
}

export function getToken() {
  return localStorage.getItem("token");
}

// Login function
export async function loginUser(email, password) {
  const formData = new URLSearchParams();
  formData.append("username", email);
  formData.append("password", password);

  const response = await fetch(`${BASE_URL}/token`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: formData,
  });

  if (!response.ok) throw new Error("Login failed");
  const data = await response.json();
  
  // save Token 
  localStorage.setItem("token", data.access_token);
  sessionStorage.setItem("token", data.access_token);
  return data;
}

// function of fetching data from backend
export async function fetchFromBackend(endpoint) {
  const token = localStorage.getItem("token") || sessionStorage.getItem("token");
  try {
    const res = await fetch(`${BASE_URL}${endpoint}`, {
      headers: { 
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json"
      }
    });
    if (!res.ok) return null;
    return await res.json();
  } catch (e) {
    return null;
  }
}

export async function getLogs() {
  return fetchFromBackend('/agent/logs');
}

export async function getAlerts() {
  return fetchFromBackend('/alerts');
}

export async function getStats() {
  return fetchFromBackend('/agent/stats');
}