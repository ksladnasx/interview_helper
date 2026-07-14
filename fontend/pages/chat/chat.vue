<template>
  <view class="page">
    <view class="chat-header">
      <view>
        <view class="chat-title">简历优化</view>
        <view class="chat-sub">基于当前简历 · 前端开发方向</view>
      </view>
      <view class="header-actions">
        <view class="icon-btn">
          <uni-icons type="refresh" size="18" color="#5b6478" />
        </view>
        <view class="icon-btn">
          <uni-icons type="copy" size="18" color="#5b6478" />
        </view>
      </view>
    </view>

    <view class="quick-actions">
      <view class="quick-chip">继续优化</view>
      <view class="quick-chip">应用建议</view>
      <view class="quick-chip">生成摘要</view>
    </view>

    <view class="chat-list">
      <view class="message ai">
        <view class="sender-icon">
          <uni-icons type="compose" size="18" color="#4F63F6" />
        </view>
        <view class="bubble">我先帮你梳理项目经历，重点增强结果表达和岗位关键词。</view>
      </view>

      <view class="message user">
        <view class="bubble">请帮我把项目经历写得更有说服力。</view>
      </view>

      <view class="message ai">
        <view class="sender-icon">
          <uni-icons type="compose" size="18" color="#4F63F6" />
        </view>
        <view class="bubble rich">
          <view class="md-title">建议改写</view>
          <view class="md-line">1. 增加量化指标，例如“首屏耗时降低 35%”。</view>
          <view class="md-line">2. 强调 React、TypeScript、性能优化等关键词。</view>
          <view class="code-block">负责核心页面性能治理，定位长任务与资源瓶颈，推动首屏耗时从 2.8s 降至 1.8s。</view>
        </view>
      </view>
    </view>

    <view class="input-wrap">
      <uni-icons type="paperclip" size="20" color="#7a8497" />
      <input class="input" placeholder="请输入你的问题..." />
      <view class="send-btn">
        <uni-icons type="right" size="18" color="#ffffff" />
      </view>
    </view>
  </view>
</template>

<script>
export default {
  name: 'ChatPage'
}
</script>

<style>
.page { min-height: 100vh; padding: 28rpx 24rpx 240rpx; display: flex; flex-direction: column; background: #f6f7fb; }
.chat-header { display: flex; align-items: center; justify-content: space-between; gap: 20rpx; }
.chat-title { color: #151b2d; font-size: 36rpx; font-weight: 800; }
.chat-sub { margin-top: 6rpx; color: #7a8497; font-size: 24rpx; }
.header-actions { display: flex; gap: 12rpx; }
.icon-btn { width: 68rpx; height: 68rpx; display: flex; align-items: center; justify-content: center; border-radius: 22rpx; background: #fff; border: 1px solid #edf0f6; }
.quick-actions { display: flex; gap: 12rpx; margin-top: 22rpx; overflow: hidden; }
.quick-chip { padding: 12rpx 18rpx; border-radius: 999rpx; background: #fff; border: 1px solid #edf0f6; color: #5b6478; font-size: 24rpx; white-space: nowrap; }
.chat-list { flex: 1; display: flex; flex-direction: column; gap: 22rpx; margin-top: 26rpx; }
.message { display: flex; align-items: flex-start; gap: 12rpx; }
.message.user { justify-content: flex-end; }
.sender-icon { width: 54rpx; height: 54rpx; border-radius: 18rpx; display: flex; align-items: center; justify-content: center; background: #eef2ff; flex-shrink: 0; }
.bubble { max-width: 82%; padding: 20rpx 22rpx; border-radius: 24rpx; color: #202638; font-size: 26rpx; line-height: 1.6; background: #fff; border: 1px solid #edf0f6; }
.message.user .bubble { background: #4F63F6; color: #fff; border-color: #4F63F6; }
.bubble.rich { max-width: 86%; }
.md-title { color: #151b2d; font-size: 28rpx; font-weight: 800; margin-bottom: 10rpx; }
.md-line { margin-top: 8rpx; }
.code-block { margin-top: 16rpx; padding: 18rpx; border-radius: 18rpx; background: #f6f7fb; color: #3d4658; font-size: 24rpx; line-height: 1.55; }
.input-wrap { position: fixed; left: 24rpx; right: 24rpx; bottom: calc(126rpx + env(safe-area-inset-bottom)); display: flex; align-items: center; gap: 14rpx; min-height: 88rpx; padding: 12rpx 14rpx 12rpx 20rpx; border-radius: 28rpx; background: #fff; border: 1px solid #edf0f6; box-shadow: 0 16rpx 38rpx rgba(35, 42, 59, 0.08); }
.input { flex: 1; color: #202638; font-size: 27rpx; }
.send-btn { width: 62rpx; height: 62rpx; display: flex; align-items: center; justify-content: center; border-radius: 20rpx; background: #4F63F6; }
</style>
