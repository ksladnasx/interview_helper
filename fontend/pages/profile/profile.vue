<template>
  <view class="page">
    <view class="profile-card">
      <view class="avatar">
        <image v-if="avatarUrl" class="avatar-image" :src="avatarUrl" mode="aspectFill" />
        <text v-else>{{ avatarText }}</text>
      </view>
      <view class="profile-main">
        <view class="name">{{ displayName }}</view>
        <view class="bio">{{ bioText }}</view>
      </view>
      <view class="edit-btn" @click="handlePrimaryAction">
        <uni-icons :type="isLoggedIn ? 'compose' : 'person'" size="17" color="#5b6478" />
      </view>
    </view>

    <view v-if="!isLoggedIn" class="login-panel">
      <view class="login-title">登录后使用完整功能</view>
      <view class="login-desc">简历、分析记录和面试数据会保存到你的账号。</view>
      <button class="login-btn" @click="goLogin">登录 / 注册</button>
    </view>

    <view v-else class="stats">
      <view class="stat-item">
        <view class="stat-num">2</view>
        <view class="stat-label">简历</view>
      </view>
      <view class="stat-item">
        <view class="stat-num">12</view>
        <view class="stat-label">分析</view>
      </view>
      <view class="stat-item">
        <view class="stat-num">5</view>
        <view class="stat-label">面试</view>
      </view>
    </view>

    <view class="menu-card">
      <view class="item" v-for="item in visibleItems" :key="item.title" @click="handleMenu(item)">
        <view class="item-left">
          <view class="item-icon">
            <uni-icons :type="item.icon" size="18" color="#4F63F6" />
          </view>
          <view class="item-title" :class="{ danger: item.action === 'logout' }">{{ item.title }}</view>
        </view>
        <uni-icons v-if="item.action !== 'logout'" type="right" size="16" color="#a7afbf" />
      </view>
    </view>
  </view>
</template>

<script>
import { getCurrentUser, hasToken, logout } from '@/services/auth.js'

export default {
  data() {
    return {
      loading: false,
      user: null,
      items: [
        { title: '我的简历', icon: 'paperclip' },
        { title: '历史分析', icon: 'search' },
        { title: '模拟面试记录', icon: 'chat' },
        { title: '设置', icon: 'settings' },
        { title: '关于我们', icon: 'info' },
        { title: '退出登录', icon: 'person', action: 'logout', authOnly: true }
      ]
    }
  },
  computed: {
    isLoggedIn() {
      return Boolean(this.user)
    },
    displayName() {
      return this.user ? this.user.username : '未登录'
    },
    avatarText() {
      return this.user && this.user.username ? this.user.username.slice(0, 1).toUpperCase() : '访'
    },
    avatarUrl() {
      return this.user?.avatar || ''
    },
    bioText() {
      return this.user ? `用户 ID ${this.user.id} · 已连接后端账号` : '登录后同步你的求职数据'
    },
    visibleItems() {
      return this.items.filter((item) => !item.authOnly || this.isLoggedIn)
    }
  },
  onShow() {
    this.loadUser()
  },
  methods: {
    async loadUser() {
      if (!hasToken()) {
        this.user = null
        return
      }

      this.loading = true
      try {
        this.user = await getCurrentUser()
      } catch (error) {
        this.user = null
      } finally {
        this.loading = false
      }
    },
    handlePrimaryAction() {
      if (!this.isLoggedIn) {
        this.goLogin()
      }
    },
    goLogin() {
      uni.navigateTo({ url: '/pages/auth/login' })
    },
    handleMenu(item) {
      if (item.action === 'logout') {
        logout()
        this.user = null
        uni.showToast({ title: '已退出登录', icon: 'success' })
      }
    }
  }
}
</script>

<style>
.page {
  min-height: 100vh;
  padding: 28rpx 24rpx 140rpx;
  background: #f6f7fb;
}

.profile-card,
.stats,
.menu-card,
.login-panel {
  background: #fff;
  border: 1px solid #edf0f6;
  box-shadow: 0 14rpx 36rpx rgba(35, 42, 59, 0.05);
}

.profile-card {
  display: flex;
  align-items: center;
  gap: 20rpx;
  padding: 26rpx;
  border-radius: 28rpx;
}

.avatar {
  width: 96rpx;
  height: 96rpx;
  flex-shrink: 0;
  border-radius: 32rpx;
  background: #232a3b;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 38rpx;
  font-weight: 800;
  overflow: hidden;
}

.avatar-image {
  width: 100%;
  height: 100%;
}

.profile-main {
  flex: 1;
  min-width: 0;
}

.name {
  color: #151b2d;
  font-size: 34rpx;
  font-weight: 800;
}

.bio {
  margin-top: 8rpx;
  color: #7a8497;
  font-size: 24rpx;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.edit-btn {
  width: 66rpx;
  height: 66rpx;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 22rpx;
  background: #f6f7fb;
}

.login-panel {
  margin-top: 22rpx;
  padding: 26rpx;
  border-radius: 26rpx;
}

.login-title {
  color: #151b2d;
  font-size: 30rpx;
  font-weight: 800;
}

.login-desc {
  margin-top: 8rpx;
  color: #7a8497;
  font-size: 25rpx;
  line-height: 1.5;
}

.login-btn {
  height: 82rpx;
  margin-top: 22rpx;
  border-radius: 22rpx;
  background: #4F63F6;
  color: #fff;
  font-size: 28rpx;
  font-weight: 800;
  line-height: 82rpx;
}

.login-btn::after {
  border: 0;
}

.stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  margin-top: 22rpx;
  padding: 20rpx 0;
  border-radius: 26rpx;
}

.stat-item {
  text-align: center;
}

.stat-num {
  color: #151b2d;
  font-size: 34rpx;
  font-weight: 800;
}

.stat-label {
  margin-top: 6rpx;
  color: #7a8497;
  font-size: 23rpx;
}

.menu-card {
  margin-top: 22rpx;
  padding: 6rpx 22rpx;
  border-radius: 26rpx;
}

.item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 24rpx 0;
  border-bottom: 1px solid #f1f3f8;
}

.item:last-child {
  border-bottom: 0;
}

.item-left {
  display: flex;
  align-items: center;
  gap: 16rpx;
}

.item-icon {
  width: 56rpx;
  height: 56rpx;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 18rpx;
  background: #eef2ff;
}

.item-title {
  color: #202638;
  font-size: 28rpx;
  font-weight: 700;
}

.item-title.danger {
  color: #d04f4f;
}
</style>
