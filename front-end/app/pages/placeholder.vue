<template>
  <div class="placeholder-page">
    <div class="content-wrapper">
      <div class="placeholder-content">
        <svg
          class="placeholder-icon"
          width="120"
          height="120"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M12 2C6.48 2 2 6.48 2 12C2 17.52 6.48 22 12 22C17.52 22 22 17.52 22 12C22 6.48 17.52 2 12 2ZM13 17H11V15H13V17ZM13 13H11V7H13V13Z"
            fill="currentColor"
          />
        </svg>
        <h1 class="placeholder-title">Эта страница в разработке</h1>
        <p class="placeholder-description">
          Содержимое этой страницы будет добавлено позже. Пожалуйста,
          продолжайте, чтобы заполнить содержимое этой страницы, если хотите.
        </p>
        <nuxt-link to="/home" class="back-button">
          <span>Вернуться на главную</span>
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
@import "@/assets/styles/variables.scss";

.placeholder-page {
  min-height: 100vh;
  padding-left: $content-offset;
  display: flex;
  align-items: center;
  justify-content: center;
}

.content-wrapper {
  width: 1462px;
  max-width: calc(100vw - $content-offset - 45px);
  margin: 46px 0;
  border-radius: $radius-lg;
  border: 1px solid $border-color;
  padding: 60px 40px;
  position: relative;
}

.placeholder-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 20px;
}

.placeholder-icon {
  width: 120px;
  height: 120px;
  color: $text-muted;
  opacity: 0.5;
}

.placeholder-title {
  color: $text-primary;
  font-family: $font-family;
  font-size: 36px;
  font-weight: 600;
  line-height: normal;
  margin: 0;
}

.placeholder-description {
  color: $text-muted;
  font-family: $font-family;
  font-size: 20px;
  font-weight: 400;
  line-height: 1.5;
  max-width: 600px;
  margin: 0;
}

.back-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 30px;
  margin-top: 20px;
  border-radius: $radius-md;
  border: 1px solid $border-secondary;
  background: $gradient-button;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease;

  span {
    color: $text-primary;
    font-family: $font-family;
    font-size: 20px;
    font-weight: 400;
    line-height: normal;
  }

  &:hover {
    background: linear-gradient(150deg, #4c4d53 1.62%, #2a2a2f 70.36%);
    transform: translateY(-2px);
  }
}

@media (max-width: 1600px) {
  .placeholder-page {
    padding-left: 320px;
  }

  .content-wrapper {
    max-width: calc(100vw - 320px - 40px);
  }
}

@media (max-width: 1400px) {
  .placeholder-page {
    padding-left: 280px;
  }

  .content-wrapper {
    max-width: calc(100vw - 280px - 40px);
  }

  .placeholder-title {
    font-size: 30px;
  }

  .placeholder-description {
    font-size: 18px;
  }
}

@media (max-width: 1200px) {
  .placeholder-page {
    padding-left: 220px;
  }

  .content-wrapper {
    max-width: calc(100vw - 220px - 30px);
  }

  .placeholder-title {
    font-size: 26px;
  }

  .placeholder-description {
    font-size: 16px;
  }
}

@media (max-width: 768px) {
  .placeholder-page {
    padding-left: 0;
    padding-top: 80px;
  }

  .content-wrapper {
    max-width: calc(100vw - 20px);
    margin: 20px 10px;
    padding: 40px 20px;
  }

  .placeholder-icon {
    width: 80px;
    height: 80px;
  }

  .placeholder-title {
    font-size: 22px;
  }

  .placeholder-description {
    font-size: 14px;
  }

  .back-button {
    span {
      font-size: 16px;
    }
  }
}
</style>
