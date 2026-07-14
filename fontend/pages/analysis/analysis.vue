<template>
  <view class="page">
    <view class="score-panel">
      <view class="score-copy">
        <view class="label">整体评分</view>
        <view class="score-value">85<text>分</text></view>
        <view class="score-desc">简历结构完整，技术表达清楚，项目成果需要更具体。</view>
      </view>
      <view class="score-ring">
        <uni-icons type="star" size="34" color="#4F63F6" />
      </view>
    </view>

    <view class="metric-card">
      <view class="metric-row" v-for="item in metrics" :key="item.name">
        <view class="metric-name">{{ item.name }}</view>
        <view class="metric-bar">
          <view class="metric-fill" :style="{ width: item.value + '%' }"></view>
        </view>
        <view class="metric-score">{{ item.score }}</view>
      </view>
    </view>

    <view class="card">
      <view class="card-title">
        <uni-icons type="checkmarkempty" size="18" color="#0F9F8A" />
        <text>优势</text>
      </view>
      <view class="tag-list">
        <view class="tag success">项目经验丰富</view>
        <view class="tag success">技术深度较强</view>
        <view class="tag success">表达条理清晰</view>
      </view>
    </view>

    <view class="card">
      <view class="card-title">
        <uni-icons type="info" size="18" color="#C56A15" />
        <text>不足</text>
      </view>
      <view class="point" v-for="item in weaknesses" :key="item">{{ item }}</view>
    </view>

    <view class="card">
      <view class="card-title">
        <uni-icons type="compose" size="18" color="#4F63F6" />
        <text>优化建议</text>
      </view>
      <view class="advice-item" v-for="item in advices" :key="item">
        <view class="dot"></view>
        <text>{{ item }}</text>
      </view>
    </view>

    <view class="detail-card">
      <view class="detail-head">
        <view class="card-title no-margin">分析详情</view>
        <uni-icons type="bottom" size="18" color="#7a8497" />
      </view>
      <view class="detail-text">项目经历已经覆盖核心职责，但“做了什么”和“带来什么结果”之间还可以建立更明确的因果关系。</view>
    </view>

    <view class="bottom-btn">
      <uni-icons type="compose" size="19" color="#ffffff" />
      <text>立即优化简历</text>
    </view>
  </view>
</template>

<script>
export default {
  name: 'AnalysisPage',
  data() {
    return {
      metrics: [
        { name: '项目经验', value: 86, score: '4.3' },
        { name: '技术深度', value: 92, score: '4.6' },
        { name: '表达能力', value: 72, score: '3.6' }
      ],
      weaknesses: [
        '缺少量化成果，建议增加关键数据。',
        '部分技能栈描述偏散，建议按岗位相关性排序。'
      ],
      advices: [
        '增强项目成绩展示，突出业务价值和技术亮点。',
        '增加 React、TypeScript、性能优化等岗位关键词。',
        '把团队协作和问题拆解过程写得更具体。'
      ]
    }
  }
}
</script>

<style>
.page { min-height: 100vh; padding: 28rpx 24rpx 160rpx; background: #f6f7fb; }
.score-panel { display: flex; align-items: center; gap: 22rpx; padding: 30rpx; border-radius: 30rpx; background: #fff; border: 1px solid #edf0f6; box-shadow: 0 16rpx 40rpx rgba(35, 42, 59, 0.06); }
.score-copy { flex: 1; min-width: 0; }
.label { color: #7a8497; font-size: 24rpx; }
.score-value { margin-top: 8rpx; color: #151b2d; font-size: 72rpx; font-weight: 800; line-height: 1; }
.score-value text { margin-left: 6rpx; color: #7a8497; font-size: 28rpx; font-weight: 600; }
.score-desc { margin-top: 16rpx; color: #5b6478; font-size: 26rpx; line-height: 1.5; }
.score-ring { width: 104rpx; height: 104rpx; border-radius: 36rpx; display: flex; align-items: center; justify-content: center; background: #eef2ff; }
.metric-card, .card, .detail-card { margin-top: 22rpx; padding: 24rpx; border-radius: 26rpx; background: #fff; border: 1px solid #edf0f6; }
.metric-row { display: flex; align-items: center; gap: 16rpx; padding: 16rpx 0; }
.metric-name { width: 128rpx; color: #202638; font-size: 26rpx; font-weight: 700; }
.metric-bar { flex: 1; height: 12rpx; border-radius: 999rpx; background: #eef0f6; overflow: hidden; }
.metric-fill { height: 100%; border-radius: 999rpx; background: #4F63F6; }
.metric-score { width: 56rpx; text-align: right; color: #7a8497; font-size: 24rpx; }
.card-title { display: flex; align-items: center; gap: 8rpx; margin-bottom: 16rpx; color: #151b2d; font-size: 30rpx; font-weight: 800; }
.card-title.no-margin { margin-bottom: 0; }
.tag-list { display: flex; flex-wrap: wrap; gap: 12rpx; }
.tag { padding: 10rpx 16rpx; border-radius: 999rpx; font-size: 24rpx; font-weight: 600; }
.tag.success { background: #eaf8f5; color: #0F8F7D; }
.point { padding: 14rpx 0; color: #4d5668; font-size: 26rpx; line-height: 1.6; border-bottom: 1px solid #f1f3f8; }
.point:last-child { border-bottom: 0; }
.advice-item { display: flex; align-items: flex-start; gap: 12rpx; padding: 12rpx 0; color: #4d5668; font-size: 26rpx; line-height: 1.6; }
.dot { width: 10rpx; height: 10rpx; margin-top: 16rpx; border-radius: 50%; background: #4F63F6; flex-shrink: 0; }
.detail-head { display: flex; align-items: center; justify-content: space-between; }
.detail-text { margin-top: 16rpx; color: #5b6478; font-size: 26rpx; line-height: 1.6; }
.bottom-btn { position: fixed; left: 24rpx; right: 24rpx; bottom: 34rpx; display: flex; align-items: center; justify-content: center; gap: 10rpx; height: 92rpx; border-radius: 24rpx; background: #4F63F6; color: #fff; font-size: 29rpx; font-weight: 800; box-shadow: 0 16rpx 36rpx rgba(79, 99, 246, 0.24); }
</style>
