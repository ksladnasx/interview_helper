const API_BASE_URL = 'http://127.0.0.1:8000'
const TOKEN_KEY = 'access_token'

export function getToken() {
  return uni.getStorageSync(TOKEN_KEY)
}

export function setToken(token) {
  uni.setStorageSync(TOKEN_KEY, token)
}

export function clearToken() {
  uni.removeStorageSync(TOKEN_KEY)
}

export function request(options) {
  const token = getToken()
  const headers = {
    'Content-Type': 'application/json',
    ...(options.header || {})
  }

  if (token) {
    headers.Authorization = `Bearer ${token}`
  }

  return new Promise((resolve, reject) => {
    uni.request({
      url: `${API_BASE_URL}${options.url}`,
      method: options.method || 'GET',
      data: options.data || {},
      header: headers,
      success: (res) => {
        const body = res.data || {}

        if (res.statusCode === 401) {
          clearToken()
        }

        if (res.statusCode >= 200 && res.statusCode < 300 && body.success !== false) {
          resolve(body.data)
          return
        }

        const message = body.message || '请求失败，请稍后再试'
        uni.showToast({ title: message, icon: 'none' })
        reject(new Error(message))
      },
      fail: (error) => {
        const message = '无法连接后端服务'
        uni.showToast({ title: message, icon: 'none' })
        reject(error)
      }
    })
  })
}

export { API_BASE_URL, TOKEN_KEY }
