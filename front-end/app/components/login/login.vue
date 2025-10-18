<template>
  <div class="login-page">
    <header class="header">
      <NuxtImg :src="LogoIcon" alt="Yandex" width="180" height="30"/>
    </header>

    <main class="main-content">
      <div class="login-container">
        <h1 class="title">Вход в аккаунт</h1>

        <form class="login-form" @submit.prevent="handleLogin">
          <div class="form-group">
            <label for="login" class="form-label">Логин</label>
            <input
                id="login"
                v-model="loginData.username"
                type="text"
                class="form-input"
                autocomplete="username"
            />
          </div>

          <div class="form-group">
            <label for="password" class="form-label">Пароль</label>
            <div class="password-wrapper">
              <input
                  id="password"
                  v-model="loginData.password"
                  :type="showPassword ? 'text' : 'password'"
                  class="form-input"
                  autocomplete="current-password"
              />
              <button
                  type="button"
                  class="password-toggle"
                  @click="showPassword = !showPassword"
                  aria-label="Toggle password visibility"
              >
                <NuxtImg :src="showPassword ? EyeOffIcon : EyeIcon" alt="Toggle password" width="20" height="20" />
              </button>
            </div>
            <span class="form-hint">Должно быть не менее 8 символов</span>
          </div>

          <button type="submit" class="btn btn-primary">
            Войти
          </button>

          <div class="divider">
            <span>Вход с помощью</span>
          </div>

          <button type="button" class="btn btn-yandex btn-main">
            <NuxtImg :src="YandexIcon" alt="Yandex" width="20" height="20" />
            Yandex
          </button>

          <button type="button" class="btn btn-secondary btn-main">
            Регистрация
          </button>
        </form>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import EyeIcon from '/svg/EyeIcon.svg'
import EyeOffIcon from '/svg/EyeOffIcon.svg'
import YandexIcon from '/svg/YandexIcon.svg'
import LogoIcon from '/svg/LogoIcon.svg'

const loginData = ref({
  username: '',
  password: ''
})

const showPassword = ref(false)

const handleLogin = () => {
  // Здесь будет логика входа
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  height: 100vh;
  background-color: #1a1a1a;
  color: #ffffff;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.header {
  padding: 20px 30px;
  flex-shrink: 0;
}

.main-content {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.login-container {
  width: 100%;
  max-width: 400px;
}

.title {
  font-size: 28px;
  font-weight: 600;
  text-align: center;
  margin-bottom: 32px;
  color: #ffffff;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-size: 16px;
  font-weight: 500;
  color: #e0e0e0;
}

.form-input {
  width: 100%;
  padding: 12px 16px;
  background-color: #2a2a2a;
  border-radius: 8px;
  border: none;
  color: #ffffff;
  font-size: 16px;
  transition: all 0.2s;
}

.form-input:focus {
  outline: none;
  background-color: #2f2f2f;
}

.form-input::placeholder {
  color: #666666;
}

.password-wrapper {
  position: relative;
}

.password-toggle {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #888888;
  cursor: pointer;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s;
  width: 28px;
  height: 28px;
}

.password-toggle:hover {
  color: #ffffff;
}

.form-hint {
  font-size: 12px;
  color: #888888;
}

.btn {
  width: 100%;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 20px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.btn-primary {
  background: linear-gradient(177deg, rgba(60, 61, 67, 1) 0%, rgba(35, 35, 40, 1) 60%);
  color: #ffffff;
}

.btn-primary:hover {
  background-color: #454545;
}

.btn-secondary {
  background-color: transparent;
  color: #ffffff;
}

.btn-yandex {
  background-color: #2a2a2a;
  color: #ffffff;
}

.divider {
  position: relative;
  text-align: center;
  margin: 8px 0;
}

.divider::before,
.divider::after {
  content: '';
  position: absolute;
  top: 50%;
  width: calc(50% - 80px);
  height: 1px;
  background-color: #3a3a3a;
}

.divider::before {
  left: 0;
}

.divider::after {
  right: 0;
}

.divider span {
  font-size: 13px;
  color: #888888;
  background-color: #1a1a1a;
  padding: 0 12px;
}
</style>