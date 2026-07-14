import { clearToken, getToken, request, setToken } from '@/utils/request.js'

export function hasToken() {
  return Boolean(getToken())
}

export async function register(payload) {
  return request({
    url: '/api/auth/register',
    method: 'POST',
    data: payload
  })
}

export async function login(payload) {
  const result = await request({
    url: '/api/auth/login',
    method: 'POST',
    data: payload
  })

  if (result && result.access_token) {
    setToken(result.access_token)
  }

  return result
}

export function getCurrentUser() {
  return request({
    url: '/api/auth/me'
  })
}

export function logout() {
  clearToken()
}
