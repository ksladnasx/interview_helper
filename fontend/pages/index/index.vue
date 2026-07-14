<template>
	<view class="page">
		<view class="topbar">
			<view class="avatar">
				<image v-if="avatarUrl" class="avatar-image" :src="avatarUrl" mode="aspectFill" />
				<text v-else>{{ avatarText }}</text>
			</view>
			<view class="top-copy">
				<view class="eyebrow">{{ greetingText }}</view>
				<view class="headline">{{ headlineText }}</view>
			</view>
			<view class="icon-button">
				<uni-icons type="sound" size="20" color="#5b6478" />
			</view>
		</view>

		<view class="summary-panel">
			<view class="summary-main">
				<view class="summary-label">简历健康度</view>
				<view class="summary-score">85<text class="summary-unit">分</text></view>
				<view class="summary-desc">结构清晰，项目成果还可以再量化。</view>
			</view>
			<view class="summary-side">
				<view class="mini-stat">
					<text class="mini-num">3</text>
					<text class="mini-label">待优化项</text>
				</view>
				<view class="mini-stat">
					<text class="mini-num">89%</text>
					<text class="mini-label">最高匹配</text>
				</view>
			</view>
		</view>

		<view class="section-head">
			<view class="section-title">常用功能</view>
			<view class="section-more">全部</view>
		</view>
		<view class="feature-grid">
			<view class="feature-card" v-for="item in features" :key="item.title" @click="openFeature(item.path)">
				<view class="feature-icon" :class="item.tone">
					<uni-icons :type="item.icon" size="24" :color="item.color" />
				</view>
				<view class="feature-copy">
					<view class="feature-title">{{ item.title }}</view>
					<view class="feature-desc">{{ item.desc }}</view>
				</view>
				<uni-icons type="right" size="15" color="#a7afbf" />
			</view>
		</view>

		<view class="section-card">
			<view class="section-head inner">
				<view class="section-title">最近记录</view>
				<view class="section-more">查看</view>
			</view>
			<view class="record-item" v-for="record in records" :key="record.title">
				<view class="record-icon">
					<uni-icons type="compose" size="18" color="#667085" />
				</view>
				<view class="record-main">
					<view class="record-title">{{ record.title }}</view>
					<view class="record-time">{{ record.time }}</view>
				</view>
				<view class="score">{{ record.score }}</view>
			</view>
		</view>

		<view class="section-card">
			<view class="section-head inner">
				<view class="section-title">今日建议</view>
				<view class="quiet-chip">简历</view>
			</view>
			<view class="suggestion-item" v-for="item in suggestions" :key="item">
				<uni-icons type="checkmarkempty" size="16" color="#5C6CFF" />
				<text>{{ item }}</text>
			</view>
		</view>
	</view>
</template>

<script>
	import { getCurrentUser, hasToken } from '@/services/auth.js'

	export default {
		data() {
			return {
				user: null,
				features: [
					{ icon: 'upload', title: '上传简历', desc: 'PDF / DOCX 文件管理', path: '/pages/resume/resume', tone: 'blue', color: '#4F63F6' },
					{ icon: 'search', title: '简历分析', desc: '结构、内容与表达诊断', path: '/pages/analysis/analysis', tone: 'green', color: '#0F9F8A' },
					{ icon: 'flag', title: '岗位匹配', desc: '对齐 JD 与技能关键词', path: '/pages/jobs/jobs', tone: 'orange', color: '#C56A15' },
					{ icon: 'chat', title: '模拟面试', desc: '按岗位生成追问与点评', path: '/pages/interview/interview', tone: 'purple', color: '#6B5DD3' }
				],
				records: [
					{ title: 'React 前端岗位', time: '今天 09:30', score: '89分' },
					{ title: '产品经理岗位', time: '昨天 18:10', score: '82分' }
				],
				suggestions: [
					'给项目结果补充关键指标，例如转化率、耗时、性能提升。',
					'把性能优化经验提前到前两段，方便招聘方快速扫读。',
					'补充一个 AI 工具协作场景，让能力画像更贴近新岗位。'
				]
			}
		},
		computed: {
			displayName() {
				return this.user?.username || '用户'
			},
			avatarText() {
				return this.user?.username ? this.user.username.slice(0, 1).toUpperCase() : '我'
			},
			avatarUrl() {
				return this.user?.avatar || ''
			},
			greetingText() {
				return this.user ? '欢迎回来，' + this.displayName : '欢迎使用 AI Career Copilot'
			},
			headlineText() {
				return this.user ? '今天继续完善你的简历吧。' : '登录后可以同步你的头像和个人信息。'
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

				try {
					this.user = await getCurrentUser()
				} catch (error) {
					this.user = null
				}
			},
			openFeature(path) {
				uni.navigateTo({
					url: path
				})
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

	.topbar {
		display: flex;
		align-items: center;
		gap: 18rpx;
	}

	.avatar {
		width: 82rpx;
		height: 82rpx;
		border-radius: 28rpx;
		background: #232a3b;
		color: #fff;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 32rpx;
		font-weight: 700;
		overflow: hidden;
	}

	.avatar-image {
		width: 100%;
		height: 100%;
	}

	.top-copy {
		flex: 1;
		min-width: 0;
	}

	.eyebrow {
		color: #7a8497;
		font-size: 24rpx;
	}

	.headline {
		margin-top: 6rpx;
		color: #151b2d;
		font-size: 36rpx;
		font-weight: 700;
		line-height: 1.25;
	}

	.icon-button {
		width: 72rpx;
		height: 72rpx;
		border-radius: 24rpx;
		display: flex;
		align-items: center;
		justify-content: center;
		background: #fff;
		border: 1px solid #edf0f6;
	}

	.summary-panel {
		display: flex;
		gap: 22rpx;
		margin-top: 30rpx;
		padding: 28rpx;
		border-radius: 28rpx;
		background: #fff;
		border: 1px solid #edf0f6;
		box-shadow: 0 16rpx 40rpx rgba(35, 42, 59, 0.06);
	}

	.summary-main {
		flex: 1;
		min-width: 0;
	}

	.summary-label,
	.mini-label {
		color: #7a8497;
		font-size: 24rpx;
	}

	.summary-score {
		margin-top: 6rpx;
		color: #151b2d;
		font-size: 64rpx;
		font-weight: 800;
		line-height: 1;
	}

	.summary-unit {
		margin-left: 6rpx;
		font-size: 26rpx;
		font-weight: 600;
		color: #7a8497;
	}

	.summary-desc {
		margin-top: 14rpx;
		color: #5b6478;
		font-size: 25rpx;
		line-height: 1.45;
	}

	.summary-side {
		width: 178rpx;
		display: flex;
		flex-direction: column;
		gap: 12rpx;
	}

	.mini-stat {
		padding: 18rpx;
		border-radius: 22rpx;
		background: #f8f9fd;
	}

	.mini-num {
		display: block;
		color: #4F63F6;
		font-size: 30rpx;
		font-weight: 800;
	}

	.section-head {
		display: flex;
		align-items: center;
		justify-content: space-between;
		margin-top: 32rpx;
		margin-bottom: 16rpx;
	}

	.section-head.inner {
		margin: 0 0 10rpx;
	}

	.section-title {
		color: #151b2d;
		font-size: 30rpx;
		font-weight: 800;
	}

	.section-more {
		color: #7a8497;
		font-size: 24rpx;
	}

	.feature-grid {
		display: flex;
		flex-direction: column;
		gap: 14rpx;
	}

	.feature-card {
		display: flex;
		align-items: center;
		gap: 18rpx;
		padding: 22rpx;
		border-radius: 24rpx;
		background: #fff;
		border: 1px solid #edf0f6;
	}

	.feature-icon,
	.record-icon {
		width: 74rpx;
		height: 74rpx;
		border-radius: 22rpx;
		display: flex;
		align-items: center;
		justify-content: center;
		flex-shrink: 0;
	}

	.feature-icon.blue { background: #eef2ff; }
	.feature-icon.green { background: #eaf8f5; }
	.feature-icon.orange { background: #fff3e7; }
	.feature-icon.purple { background: #f0edff; }

	.feature-copy,
	.record-main {
		flex: 1;
		min-width: 0;
	}

	.feature-title,
	.record-title {
		color: #202638;
		font-size: 28rpx;
		font-weight: 700;
	}

	.feature-desc,
	.record-time {
		margin-top: 6rpx;
		color: #7a8497;
		font-size: 24rpx;
	}

	.section-card {
		margin-top: 22rpx;
		padding: 24rpx;
		border-radius: 26rpx;
		background: #fff;
		border: 1px solid #edf0f6;
	}

	.record-item {
		display: flex;
		align-items: center;
		gap: 16rpx;
		padding: 18rpx 0;
		border-bottom: 1px solid #f1f3f8;
	}

	.record-item:last-child {
		border-bottom: 0;
		padding-bottom: 6rpx;
	}

	.record-icon {
		width: 62rpx;
		height: 62rpx;
		border-radius: 20rpx;
		background: #f6f7fb;
	}

	.score {
		color: #4F63F6;
		font-size: 28rpx;
		font-weight: 800;
	}

	.quiet-chip {
		padding: 8rpx 16rpx;
		border-radius: 999rpx;
		background: #f6f7fb;
		color: #6d7688;
		font-size: 22rpx;
	}

	.suggestion-item {
		display: flex;
		align-items: flex-start;
		gap: 12rpx;
		padding: 14rpx 0;
		color: #4d5668;
		font-size: 26rpx;
		line-height: 1.55;
	}
</style>
