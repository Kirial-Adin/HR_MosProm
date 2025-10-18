<script setup lang="ts">
// import UiBorder from "~/components/ui/UiBorder.vue";
import vuzi from "../../json/vuzi.json";
import UiDropdown from "~/components/ui/UiDropdown.vue";
</script>

<template>
  <!-- <UiBorder> -->
  <div class="auth-container">
    <form action="">
      <h1 class="auth-title">Создание аккаунта</h1>
      <div class="field">
        <label for="name">* Имя</label>
        <input id="name" class="input-container name" type="text" required />
        <label for="secondaname">* Фамилия</label>
        <input
          id="secondaname"
          class="input-container secondaname"
          type="text"
          required
        />
        <label for="lastname">Отчество</label>
        <input id="lastname" class="input-container lastname" type="text" />
        <label for="vuzi">* Выберите ВУЗ</label>
        <UiDropdown
          class="vuzi"
          placeholder="Начните вводить…"
          :options="vuzi"
        />
        <label for="login">* Придумайте логин</label>
        <input id="login" class="input-container login" type="text" required />
        <label for="password">* Придумайте пароль</label>
        <input
          id="password"
          class="input-container password"
          type="text"
          required
        />
      </div>
      <label class="checkbox-container">
        <input type="checkbox" class="checkbox-input" />
        <div class="checkbox-content">
          <span class="checkbox-circle"></span>
          <span class="checkbox-text"
            >Я согласен на предоставление моих персональных данных
            работодателю</span
          >
        </div>
      </label>
      <div class="from-button">
        <button class="form-btn">Создать аккаунт</button>
      </div>
    </form>
  </div>
  <!-- </UiBorder> -->
</template>

<style lang="scss" scoped>
@use "~/assets/styles/variables" as var;

:root {
  --chk-size: 22px;
  --chk-color: #4f46e5; /* цвет чекбокса (индиго) */
  --chk-border: #9aa0a6; /* цвет рамки в неактивном состоянии */
}

.auth-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  margin-top: 60px;
}

.auth-title {
  color: #151515;
  margin-bottom: 15px;
}

.field {
  margin-bottom: 16px;
}
.field label {
  display: block;
  font-size: 14px;
  margin-bottom: 6px;
  color: #151515;
}

.input-container {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin-bottom: 10px;
  background-color: #cfcfcf;
}

.vuzi {
  margin-bottom: 10px;
}

.checkbox-container {
  display: inline-block;
  cursor: pointer;
  margin-bottom: 10px;
  max-width: 360px;
}

.checkbox-input {
  display: none; /* Скрываем нативный чекбокс */
}

.checkbox-content {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 8px;
}

.checkbox-circle {
  width: 28px;
  height: 24px;
  border: 2px solid #ccc;
  border-radius: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  position: relative;
}

/* Состояние отмеченного чекбокса */
.checkbox-input:checked + .checkbox-content .checkbox-circle {
  background-color: #e06565;
  border-color: #e06565;
}

.checkbox-input:checked + .checkbox-content .checkbox-circle::after {
  content: "";
  background: white;
  border-radius: 100%;
}

.checkbox-text {
  font-size: 13px;
  color: #aaaaaa;
  text-align: start;
}

.form-btn {
  width: 100%;
  padding: 12px 88.5px;
  text-align: center;
  align-items: center;
  border: none;
  border-radius: 10px;
  color: #151515;
  cursor: pointer;
  background: linear-gradient(179deg, #d7d7d7 0%, #b1b1b1 100%);
}
</style>
