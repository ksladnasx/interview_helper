<template>
  <view class="page">
    <view class="input-card">
      <view class="card-title">岗位 JD</view>
      <textarea class="textarea" placeholder="粘贴岗位描述，系统会提取职责、技能和关键词" />
      <view class="btn-row">
        <view class="btn ghost">
          <uni-icons type="paperclip" size="17" color="#5b6478" />
          <text>上传 JD</text>
        </view>
        <view class="btn primary">
          <uni-icons type="search" size="17" color="#ffffff" />
          <text>开始分析</text>
        </view>
      </view>
    </view>

    <view class="match-card">
      <view>
        <view class="result-title">岗位匹配度</view>
        <view class="result-score">89%</view>
        <view class="result-sub">适合投递，建议补齐工程化关键词。</view>
      </view>
      <view class="match-icon">
        <uni-icons type="flag" size="32" color="#4F63F6" />
      </view>
    </view>

    <view class="card">
      <view class="card-title with-icon">
        <uni-icons type="checkmarkempty" size="18" color="#0F9F8A" />
        <text>符合技能</text>
      </view>
      <view class="tag-list">
        <view class="tag fit" v-for="item in fitSkills" :key="item">{{ item }}</view>
      </view>
    </view>

    <view class="card">
      <view class="card-title with-icon">
        <uni-icons type="closeempty" size="18" color="#C56A15" />
        <text>建议补充</text>
      </view>
      <view class="tag-list">
        <view class="tag gap" v-for="item in gapSkills" :key="item">{{ item }}</view>
      </view>
    </view>

    <view class="card">
      <view class="card-title with-icon">
        <uni-icons type="compose" size="18" color="#4F63F6" />
        <text>修改方向</text>
      </view>
      <view class="advice" v-for="item in advices" :key="item">{{ item }}</view>
    </view>

    <view class="bottom-btn">
      <uni-icons type="compose" size="19" color="#ffffff" />
      <text>生成针对该岗位的新简历</text>
    </view>
  </view>
</template>

<script>
export default {
  name: 'JobsPage',
  data() {
    return {
      fitSkills: ['React', 'TypeScript', 'Vue3', 'Axios'],
      gapSkills: ['Docker', 'CI/CD', 'Node.js'],
      advices: [
        '把性能优化、组件抽象和工程化经验放到项目描述前半段。',
        '补充构建部署流程，体现你对团队研发效率的影响。',
        '针对 JD 中的关键词调整技能顺序，减少无关内容。'
      ]
    }
  }
}
</script>

<style>
.page { min-height: 100vh; padding: 28rpx 24rpx 160rpx; background: #f6f7fb; }
.input-card, .match-card, .card { border-radius: 28rpx; background: #fff; border: 1px solid #edf0f6; box-shadow: 0 14rpx 36rpx rgba(35, 42, 59, 0.05); }
.input-card { padding: 24rpx; }
.card-title { color: #151b2d; font-size: 30rpx; font-weight: 800; }
.card-title.with-icon { display: flex; align-items: center; gap: 8rpx; margin-bottom: 16rpx; }
.textarea { width: 100%; min-height: 230rpx; margin-top: 18rpx; padding: 20rpx; border: 1px solid #e2e6ef; border-radius: 22rpx; background: #fbfcff; color: #202638; font-size: 26rpx; line-height: 1.5; }
.btn-row { display: flex; gap: 14rpx; margin-top: 18rpx; }
.btn { flex: 1; display: flex; align-items: center; justify-content: center; gap: 8rpx; height: 76rpx; border-radius: 20rpx; font-size: 26rpx; font-weight: 700; }
.btn.primary { background: #4F63F6; color: #fff; }
.btn.ghost { background: #f6f7fb; color: #5b6478; }
.match-card { display: flex; align-items: center; justify-content: space-between; margin-top: 22rpx; padding: 30rpx; }
.result-title { color: #7a8497; font-size: 24rpx; }
.result-score { margin-top: 8rpx; color: #151b2d; font-size: 70rpx; font-weight: 800; line-height: 1; }
.result-sub { margin-top: 14rpx; color: #5b6478; font-size: 26rpx; }
.match-icon { width: 108rpx; height: 108rpx; display: flex; align-items: center; justify-content: center; border-radius: 34rpx; background: #eef2ff; }
.card { margin-top: 22rpx; padding: 24rpx; }
.tag-list { display: flex; flex-wrap: wrap; gap: 12rpx; }
.tag { padding: 12rpx 18rpx; border-radius: 999rpx; font-size: 25rpx; font-weight: 700; }
.tag.fit { background: #eaf8f5; color: #0F8F7D; }
.tag.gap { background: #fff3e7; color: #b65e10; }
.advice { padding: 14rpx 0; color: #4d5668; font-size: 26rpx; line-height: 1.6; border-bottom: 1px solid #f1f3f8; }
.advice:last-child { border-bottom: 0; }
.bottom-btn { position: fixed; left: 24rpx; right: 24rpx; bottom: 34rpx; display: flex; align-items: center; justify-content: center; gap: 10rpx; height: 92rpx; border-radius: 24rpx; background: #4F63F6; color: #fff; font-size: 28rpx; font-weight: 800; box-shadow: 0 16rpx 36rpx rgba(79, 99, 246, 0.24); }
</style>
