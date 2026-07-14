<template>
  <view class="page">
    <view class="brand">
      <view class="logo">
        <uni-icons type="personadd" size="28" color="#ffffff" />
      </view>
      <view class="title">创建账号</view>
      <view class="desc">先建立账号，后续简历和分析记录都会归档到你的账户下。</view>
    </view>

    <view class="form-card">
      <view class="field">
        <view class="label">用户名</view>
        <input v-model.trim="form.username" class="input" placeholder="3-64 位用户名" />
      </view>
      <view class="field">
        <view class="label">密码</view>
        <input v-model="form.password" class="input" password placeholder="至少 6 位密码" />
      </view>
      <button class="primary-btn" :loading="loading" @click="submit">注册</button>
      <view class="switch-line">
        <text>已有账号？</text>
        <text class="link" @click="goLogin">去登录</text>
      </view>
    </view>
  </view>
</template>

<script>
import { register } from '@/services/auth.js'

export default {
  data() {
    return {
      loading: false,
      form: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    validate() {
      if (this.form.username.length < 3) {
        uni.showToast({ title: '用户名至少 3 位', icon: 'none' })
        return false
      }
      if (this.form.password.length < 6) {
        uni.showToast({ title: '密码至少 6 位', icon: 'none' })
        return false
      }
      return true
    },
    async submit() {
      if (!this.validate() || this.loading) return

      this.loading = true
      try {
        await register(this.form)
        uni.showToast({ title: '注册成功，请登录', icon: 'success' })
        setTimeout(() => {
          uni.redirectTo({ url: '/pages/auth/login' })
        }, 450)
      } finally {
        this.loading = false
      }
    },
    goLogin() {
      uni.redirectTo({ url: '/pages/auth/login' })
    }
  }
}
</script>

<style>
.page { min-height: 100vh; padding: 56rpx 24rpx 80rpx; background: #f6f7fb; }
.brand { padding: 20rpx 4rpx 34rpx; }
.logo { width: 84rpx; height: 84rpx; display: flex; align-items: center; justify-content: center; border-radius: 28rpx; background: #232a3b; }
.title { margin-top: 28rpx; color: #151b2d; font-size: 44rpx; font-weight: 800; }
.desc { margin-top: 12rpx; color: #7a8497; font-size: 26rpx; line-height: 1.5; }
.form-card { padding: 28rpx; border-radius: 30rpx; background: #fff; border: 1px solid #edf0f6; box-shadow: 0 16rpx 40rpx rgba(35, 42, 59, 0.06); }
.field { margin-bottom: 24rpx; }
.label { margin-bottom: 12rpx; color: #202638; font-size: 26rpx; font-weight: 700; }
.input { height: 88rpx; padding: 0 22rpx; border-radius: 22rpx; background: #f8f9fd; color: #202638; font-size: 28rpx; }
.primary-btn { height: 88rpx; margin-top: 10rpx; border-radius: 22rpx; background: #4F63F6; color: #fff; font-size: 29rpx; font-weight: 800; line-height: 88rpx; }
.primary-btn::after { border: 0; }
.switch-line { display: flex; justify-content: center; gap: 8rpx; margin-top: 28rpx; color: #7a8497; font-size: 25rpx; }
.link { color: #4F63F6; font-weight: 800; }
</style>
