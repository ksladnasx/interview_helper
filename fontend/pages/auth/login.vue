<template>
  <view class="page">
    <view class="brand">
      <view class="logo">
        <uni-icons type="person" size="28" color="#ffffff" />
      </view>
      <view class="title">登录账号</view>
      <view class="desc">登录后可以同步简历、分析记录和面试进度。</view>
    </view>

    <view class="form-card">
      <view class="field">
        <view class="label">用户名</view>
        <input v-model.trim="form.username" class="input" placeholder="请输入用户名" />
      </view>
      <view class="field">
        <view class="label">密码</view>
        <input v-model="form.password" class="input" password placeholder="请输入密码" />
      </view>
      <button class="primary-btn" :loading="loading" @click="submit">登录</button>
      <view class="switch-line">
        <text>还没有账号？</text>
        <text class="link" @click="goRegister">立即注册</text>
      </view>
    </view>
  </view>
</template>

<script>
import { login } from '@/services/auth.js'

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
        await login(this.form)
        uni.showToast({ title: '登录成功', icon: 'success' })
        setTimeout(() => {
          uni.switchTab({ url: '/pages/profile/profile' })
        }, 350)
      } finally {
        this.loading = false
      }
    },
    goRegister() {
      uni.navigateTo({ url: '/pages/auth/register' })
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
