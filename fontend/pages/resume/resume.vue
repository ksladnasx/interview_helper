<template>
  <view class="page">
    <view class="page-head">
      <view>
        <view class="title">简历中心</view>
        <view class="desc">管理文件版本，快速进入分析和优化流程。</view>
      </view>
      <view class="upload-btn">
        <uni-icons type="upload" size="18" color="#ffffff" />
        <text>上传</text>
      </view>
    </view>

    <view class="resume-card active">
      <view class="file-icon">
        <uni-icons type="paperclip" size="24" color="#4F63F6" />
      </view>
      <view class="file-main">
        <view class="file-top">
          <view class="file-name">王涵_前端开发简历.pdf</view>
          <view class="status">当前</view>
        </view>
        <view class="file-meta">上传于 2026-07-14 · 1.2MB · 今天更新</view>
        <view class="file-actions">
          <view class="text-btn">
            <uni-icons type="eye" size="15" color="#5b6478" />
            <text>查看</text>
          </view>
          <view class="text-btn">
            <uni-icons type="refresh" size="15" color="#5b6478" />
            <text>替换</text>
          </view>
          <view class="text-btn danger">
            <uni-icons type="trash" size="15" color="#d04f4f" />
            <text>删除</text>
          </view>
        </view>
      </view>
    </view>

    <view class="section-title">历史版本</view>
    <view class="list-card">
      <view class="resume-row" v-for="item in resumes" :key="item.name">
        <view class="row-icon">
          <uni-icons type="paperclip" size="18" color="#7a8497" />
        </view>
        <view class="row-main">
          <view class="row-name">{{ item.name }}</view>
          <view class="row-meta">{{ item.time }} · {{ item.size }}</view>
        </view>
        <view class="row-status">{{ item.status }}</view>
      </view>
    </view>

    <view class="action-grid">
      <view class="action-card primary">
        <uni-icons type="search" size="22" color="#ffffff" />
        <text>简历分析</text>
      </view>
      <view class="action-card">
        <uni-icons type="compose" size="22" color="#4F63F6" />
        <text>内容优化</text>
      </view>
      <view class="action-card">
        <uni-icons type="flag" size="22" color="#4F63F6" />
        <text>岗位匹配</text>
      </view>
      <view class="action-card">
        <uni-icons type="download" size="22" color="#4F63F6" />
        <text>导出 PDF</text>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      resumes: [
        { name: '王涵_产品实习简历.docx', time: '2026-07-10', size: '420KB', status: '待优化' },
        { name: '王涵_校招通用版.pdf', time: '2026-07-02', size: '980KB', status: '已归档' }
      ]
    }
  }
}
</script>

<style>
.page { min-height: 100vh; padding: 28rpx 24rpx 140rpx; background: #f6f7fb; }
.page-head { display: flex; align-items: flex-start; justify-content: space-between; gap: 20rpx; }
.title { color: #151b2d; font-size: 38rpx; font-weight: 800; }
.desc { margin-top: 8rpx; color: #7a8497; font-size: 25rpx; line-height: 1.45; }
.upload-btn { display: flex; align-items: center; gap: 8rpx; flex-shrink: 0; padding: 16rpx 20rpx; border-radius: 20rpx; background: #4F63F6; color: #fff; font-size: 25rpx; font-weight: 700; }
.resume-card, .list-card, .action-card { background: #fff; border: 1px solid #edf0f6; box-shadow: 0 14rpx 36rpx rgba(35, 42, 59, 0.05); }
.resume-card { display: flex; gap: 18rpx; margin-top: 28rpx; padding: 24rpx; border-radius: 28rpx; }
.resume-card.active { border-color: #dfe5ff; }
.file-icon, .row-icon { display: flex; align-items: center; justify-content: center; flex-shrink: 0; background: #eef2ff; }
.file-icon { width: 78rpx; height: 78rpx; border-radius: 24rpx; }
.file-main, .row-main { flex: 1; min-width: 0; }
.file-top { display: flex; align-items: center; gap: 12rpx; }
.file-name, .row-name { color: #202638; font-size: 28rpx; font-weight: 700; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.status { padding: 6rpx 12rpx; border-radius: 999rpx; background: #eef2ff; color: #4F63F6; font-size: 22rpx; font-weight: 700; }
.file-meta, .row-meta { margin-top: 8rpx; color: #7a8497; font-size: 24rpx; }
.file-actions { display: flex; gap: 18rpx; margin-top: 22rpx; }
.text-btn { display: flex; align-items: center; gap: 6rpx; color: #5b6478; font-size: 24rpx; }
.text-btn.danger { color: #d04f4f; }
.section-title { margin: 32rpx 0 16rpx; color: #151b2d; font-size: 30rpx; font-weight: 800; }
.list-card { padding: 6rpx 22rpx; border-radius: 26rpx; }
.resume-row { display: flex; align-items: center; gap: 16rpx; padding: 22rpx 0; border-bottom: 1px solid #f1f3f8; }
.resume-row:last-child { border-bottom: 0; }
.row-icon { width: 58rpx; height: 58rpx; border-radius: 18rpx; background: #f6f7fb; }
.row-status { color: #7a8497; font-size: 24rpx; }
.action-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16rpx; margin-top: 24rpx; }
.action-card { display: flex; align-items: center; justify-content: center; gap: 10rpx; min-height: 96rpx; border-radius: 24rpx; color: #202638; font-size: 27rpx; font-weight: 700; }
.action-card.primary { background: #4F63F6; color: #fff; border-color: #4F63F6; }
</style>
