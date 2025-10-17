<script setup lang="ts"></script>

<template>
  <div class="border"><slot></slot></div>
</template>

<style lang="scss" scoped>
.border {
  margin: 10px;
  width: 98.5%;
  height: 97vh;
  border: 1px #3d3d3d solid;
  border-radius: 23px;
}
</style>
