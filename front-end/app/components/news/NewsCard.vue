<template>
  <div class="news-card">
    <div class="mask-group">
      <img :src="news.image" :alt="news.title" class="news-image" />
      <img :src="news.imageLarge" :alt="news.title" class="news-image-large" />
    </div>
    <div class="gradient-overlay-top"></div>
    <h2 class="news-title">{{ news.title }}</h2>
    <time class="news-timestamp">{{ news.timestamp }}</time>
    <p class="news-content">{{ news.content }}</p>
    <div class="gradient-overlay-bottom"></div>
    <button class="read-more-button">
      <span>Читать больше</span>
    </button>
    <div class="active-indicator"></div>
  </div>
</template>

<script setup lang="ts">
interface News {
  id: number
  title: string
  timestamp: string
  content: string
  image: string
  imageLarge: string
}

defineProps<{
  news: News
}>()
</script>

<style scoped lang="scss">
@import '@/assets/styles/variables.scss';

.news-card {
  width: 100%;
  max-width: 1420px;
  height: 470px;
  flex-shrink: 0;
  border-radius: $radius-md;
  background: $bg-secondary;
  position: relative;
  overflow: hidden;
  margin: 0 auto 20px;
}

.mask-group {
  width: 100%;
  height: 226px;
  flex-shrink: 0;
  position: absolute;
  left: 0;
  top: 0;
}

.news-image {
  width: 100%;
  height: 226px;
  flex-shrink: 0;
  border-radius: $radius-md $radius-md 0 0;
  position: absolute;
  left: 0;
  top: 0;
  object-fit: cover;
}

.news-image-large {
  width: 100%;
  height: 314px;
  flex-shrink: 0;
  border-radius: $radius-md $radius-md 0 0;
  position: absolute;
  left: 0;
  top: 0;
  object-fit: cover;
}

.gradient-overlay-top {
  width: 100%;
  height: 104px;
  flex-shrink: 0;
  background: $gradient-overlay;
  position: absolute;
  left: 0;
  top: 122px;
  pointer-events: none;
}

.news-title {
  position: absolute;
  left: 19px;
  top: 170px;
  width: calc(100% - 38px);
  max-width: 1381px;
  color: $text-white;
  font-family: $font-family;
  font-size: 48px;
  font-weight: 600;
  line-height: 114.82%;
  margin: 0;
  z-index: 2;
}

.news-timestamp {
  position: absolute;
  right: 20px;
  top: 252px;
  width: 156px;
  color: $text-timestamp;
  text-align: right;
  font-family: $font-family;
  font-size: 20px;
  font-weight: 400;
  line-height: normal;
  z-index: 2;
}

.news-content {
  position: absolute;
  left: 19px;
  top: 298px;
  width: calc(100% - 38px);
  max-width: 1381px;
  color: $text-white;
  font-family: $font-family;
  font-size: 20px;
  font-weight: 400;
  line-height: normal;
  margin: 0;
  white-space: pre-line;
  z-index: 2;
}

.gradient-overlay-bottom {
  width: 100%;
  height: 154px;
  flex-shrink: 0;
  border-radius: 0 0 $radius-md $radius-md;
  background: $gradient-overlay;
  position: absolute;
  left: 0;
  top: 316px;
  pointer-events: none;
}

.read-more-button {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 398px;
  display: flex;
  width: 1067px;
  max-width: calc(100% - 40px);
  height: 52px;
  padding: 0 15px;
  justify-content: center;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
  border-radius: $radius-md;
  border: 1px solid $border-secondary;
  background: $gradient-button;
  cursor: pointer;
  z-index: 3;
  transition: all 0.3s ease;

  span {
    color: $text-primary;
    font-family: $font-family;
    font-size: 24px;
    font-weight: 400;
    line-height: normal;
  }

  &:hover {
    background: linear-gradient(150deg, #4C4D53 1.62%, #2A2A2F 70.36%);
    transform: translateX(-50%) translateY(-2px);
  }
}

.active-indicator {
  position: absolute;
  right: 0;
  top: 250px;
  width: 5px;
  height: 28px;
  border-radius: 3px 0 0 3px;
  background: $text-white;
  box-shadow: $shadow-glow;
  z-index: 4;
}

@media (max-width: 1400px) {
  .news-card {
    height: 420px;
  }

  .news-title {
    font-size: 40px;
    top: 150px;
  }

  .news-timestamp {
    top: 230px;
    font-size: 18px;
  }

  .news-content {
    top: 270px;
    font-size: 18px;
  }

  .gradient-overlay-bottom {
    top: 286px;
  }

  .read-more-button {
    top: 350px;
    width: 900px;
    height: 48px;

    span {
      font-size: 22px;
    }
  }
}

@media (max-width: 1200px) {
  .news-card {
    height: 380px;
  }

  .mask-group {
    height: 200px;
  }

  .news-image {
    height: 200px;
  }

  .news-image-large {
    height: 280px;
  }

  .news-title {
    font-size: 32px;
    top: 130px;
  }

  .news-timestamp {
    top: 210px;
    font-size: 16px;
  }

  .news-content {
    top: 240px;
    font-size: 16px;
  }

  .gradient-overlay-bottom {
    top: 256px;
  }

  .read-more-button {
    top: 310px;
    width: 700px;
    height: 44px;

    span {
      font-size: 20px;
    }
  }
}

@media (max-width: 768px) {
  .news-card {
    height: 350px;
  }

  .mask-group {
    height: 180px;
  }

  .news-image {
    height: 180px;
  }

  .news-image-large {
    height: 250px;
  }

  .news-title {
    font-size: 24px;
    top: 110px;
    left: 15px;
    width: calc(100% - 30px);
  }

  .news-timestamp {
    top: 190px;
    right: 15px;
    font-size: 14px;
  }

  .news-content {
    top: 215px;
    font-size: 14px;
    left: 15px;
    width: calc(100% - 30px);
  }

  .gradient-overlay-bottom {
    top: 230px;
  }

  .read-more-button {
    top: 285px;
    width: calc(100% - 30px);
    height: 40px;

    span {
      font-size: 18px;
    }
  }

  .active-indicator {
    display: none;
  }
}
</style>
