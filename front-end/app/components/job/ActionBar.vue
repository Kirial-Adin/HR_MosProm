<script setup lang="ts"></script>

<template>
  <div class="action-bar-container">
    <img class="container__icon" src="/svg/Tag.svg" alt="" />
    <p class="container__text"><slot></slot></p>
  </div>
</template>

<style lang="scss" scoped>
@use "~/assets/styles/variables" as var;

.action-bar-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 21px;
  border: 1px #5d5c5c solid;
  border-radius: 10px;
  padding: 5px;
  gap: 3px;
  background: linear-gradient(183deg, #3c3d43 0%, #232328 100%);
}

.container__icon {
  width: 13px;
  height: 10px;
}

.container__text {
  color: var.$text-active;
  font-size: 9px;
}
</style>
