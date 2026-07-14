<template>
  <view class="page">
    <view class="setup-card">
      <view class="setup-head">
        <view>
          <view class="title">模拟面试</view>
          <view class="desc">高级前端工程师 · 技术面 + 项目复盘</view>
        </view>
        <view class="start-btn">
          <uni-icons type="mic" size="18" color="#ffffff" />
          <text>开始</text>
        </view>
      </view>
      <view class="meta-grid">
        <view class="meta-item">
          <view class="meta-label">岗位</view>
          <view class="meta-value">前端工程师</view>
        </view>
        <view class="meta-item">
          <view class="meta-label">难度</view>
          <view class="meta-value">中高</view>
        </view>
        <view class="meta-item">
          <view class="meta-label">题型</view>
          <view class="meta-value">追问制</view>
        </view>
      </view>
    </view>

    <view class="card">
      <view class="card-title">当前问答</view>
      <view class="message ai">
        <view class="sender-icon">
          <uni-icons type="chat" size="18" color="#4F63F6" />
        </view>
        <view class="bubble">请介绍你在项目中最具挑战性的模块，并说明你如何解决它。</view>
      </view>
      <view class="message user">
        <view class="bubble">我曾主导重构一个复杂的表单系统...</view>
      </view>
      <view class="message ai">
        <view class="sender-icon">
          <uni-icons type="chat" size="18" color="#4F63F6" />
        </view>
        <view class="bubble">回答方向不错。建议补充性能指标、协作对象和最终业务结果。</view>
      </view>
    </view>

    <view class="score-card">
      <view class="score-head">
        <view>
          <view class="score-title">阶段评分</view>
          <view class="score-desc">逻辑清晰，技术细节还可展开。</view>
        </view>
        <view class="score">86</view>
      </view>
      <view class="review-row" v-for="item in reviews" :key="item.label">
        <view class="review-label">{{ item.label }}</view>
        <view class="review-text">{{ item.text }}</view>
      </view>
    </view>

    <view class="input-wrap">
      <input class="input" placeholder="请输入回答..." />
      <view class="send-btn">
        <uni-icons type="right" size="18" color="#ffffff" />
      </view>
    </view>
  </view>
</template>

<script>
export default {
  name: 'InterviewPage',
  data() {
    return {
      reviews: [
        { label: '优势', text: '逻辑清晰，能主动拆解复杂问题。' },
        { label: '不足', text: '技术细节和结果指标还不够具体。' },
        { label: '建议', text: '准备性能优化与架构设计案例。' }
      ]
    }
  }
}
</script>

<style>
.page { min-height: 100vh; padding: 28rpx 24rpx 140rpx; background: #f6f7fb; }
.setup-card, .card, .score-card { border-radius: 28rpx; background: #fff; border: 1px solid #edf0f6; box-shadow: 0 14rpx 36rpx rgba(35, 42, 59, 0.05); }
.setup-card { padding: 26rpx; }
.setup-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 20rpx; }
.title { color: #151b2d; font-size: 36rpx; font-weight: 800; }
.desc { margin-top: 8rpx; color: #7a8497; font-size: 24rpx; }
.start-btn { display: flex; align-items: center; gap: 8rpx; padding: 15rpx 20rpx; border-radius: 20rpx; background: #4F63F6; color: #fff; font-size: 25rpx; font-weight: 800; }
.meta-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12rpx; margin-top: 26rpx; }
.meta-item { padding: 18rpx; border-radius: 20rpx; background: #f6f7fb; }
.meta-label { color: #7a8497; font-size: 22rpx; }
.meta-value { margin-top: 8rpx; color: #202638; font-size: 25rpx; font-weight: 800; }
.card, .score-card { margin-top: 22rpx; padding: 24rpx; }
.card-title { color: #151b2d; font-size: 30rpx; font-weight: 800; margin-bottom: 18rpx; }
.message { display: flex; align-items: flex-start; gap: 12rpx; margin-top: 16rpx; }
.message.user { justify-content: flex-end; }
.sender-icon { width: 52rpx; height: 52rpx; display: flex; align-items: center; justify-content: center; border-radius: 18rpx; background: #eef2ff; flex-shrink: 0; }
.bubble { max-width: 82%; padding: 18rpx 20rpx; border-radius: 22rpx; background: #f8f9fd; color: #202638; font-size: 26rpx; line-height: 1.6; }
.message.user .bubble { background: #4F63F6; color: #fff; }
.score-head { display: flex; align-items: center; justify-content: space-between; gap: 20rpx; margin-bottom: 12rpx; }
.score-title { color: #151b2d; font-size: 30rpx; font-weight: 800; }
.score-desc { margin-top: 8rpx; color: #7a8497; font-size: 24rpx; }
.score { color: #4F63F6; font-size: 56rpx; font-weight: 800; }
.review-row { display: flex; gap: 18rpx; padding: 16rpx 0; border-top: 1px solid #f1f3f8; }
.review-label { width: 72rpx; color: #151b2d; font-size: 25rpx; font-weight: 800; }
.review-text { flex: 1; color: #4d5668; font-size: 25rpx; line-height: 1.55; }
.input-wrap { position: fixed; left: 24rpx; right: 24rpx; bottom: 30rpx; display: flex; align-items: center; gap: 14rpx; min-height: 88rpx; padding: 12rpx 14rpx 12rpx 22rpx; border-radius: 28rpx; background: #fff; border: 1px solid #edf0f6; box-shadow: 0 16rpx 38rpx rgba(35, 42, 59, 0.08); }
.input { flex: 1; color: #202638; font-size: 27rpx; }
.send-btn { width: 62rpx; height: 62rpx; display: flex; align-items: center; justify-content: center; border-radius: 20rpx; background: #4F63F6; }
</style>
