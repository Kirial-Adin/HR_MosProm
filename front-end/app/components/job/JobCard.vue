<script setup lang="ts">
import ActionBar from "./ActionBar.vue";
import { NuxtImg } from "#components";

interface Job {
  id: number;
  title: string;
  company: string;
  author: string;
  description: string;
  image: string;
  logo: string;
  views: number;
  tags: string[];
}

defineProps<{
  job: Job;
}>();
</script>

<template>
  <div class="job-card">
    <div class="card-background"></div>
    <NuxtImg :src="job.image" :alt="job.title" class="card-image" />
    <NuxtImg :src="job.logo" :alt="job.company" class="card-logo" />
    <h3 class="card-title">{{ job.title }}</h3>
    <p class="card-author">{{ job.author }}</p>
    <p class="card-description">{{ job.description }}</p>

    <div class="card-footer">
      <div class="views-section">
        <svg
          class="eye-icon"
          width="15"
          height="13"
          viewBox="0 0 15 13"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M14.0637 5.8168C14.3877 6.29491 14.3877 6.94036 14.0637 7.4177C13.0431 8.92066 10.5944 12.0153 7.73565 12.0153C4.87688 12.0153 2.42825 8.92066 1.40765 7.4177C1.24978 7.18888 1.16406 6.9072 1.16406 6.61725C1.16406 6.32729 1.24978 6.04562 1.40765 5.8168C2.42825 4.31384 4.87688 1.21924 7.73565 1.21924C10.5944 1.21924 13.0431 4.31384 14.0637 5.8168Z"
            stroke="#202020"
            stroke-width="0.888125"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
          <path
            d="M7.73534 8.93058C8.86795 8.93058 9.78612 7.89482 9.78612 6.61714C9.78612 5.33947 8.86795 4.30371 7.73534 4.30371C6.60273 4.30371 5.68457 5.33947 5.68457 6.61714C5.68457 7.89482 6.60273 8.93058 7.73534 8.93058Z"
            stroke="#202020"
            stroke-width="0.888125"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
        <span class="views-count">{{ job.views }} views</span>
      </div>
      <div class="action-bar">
        <ActionBar v-for="tag in job.tags" :key="tag">{{ tag }}</ActionBar>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@use "~/assets/styles/variables" as var;

.job-card {
  width: 340px;
  height: 229px;
  flex-shrink: 0;
  border-radius: var.$radius-md;
  background: var.$bg-card;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-4px);
  }
}

.card-background {
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: var.$radius-md;
  pointer-events: none;
}

.card-image {
  width: 100%;
  height: 104px;
  flex-shrink: 0;
  border-radius: var.$radius-md var.$radius-md 0 0;
  object-fit: cover;
  position: absolute;
  left: 0;
  top: 0;
}

.card-logo {
  width: 63px;
  height: 63px;
  flex-shrink: 0;
  aspect-ratio: 1/1;
  border-radius: var.$radius-sm;
  position: absolute;
  left: 9px;
  top: 80px;
  object-fit: cover;
}

.card-title {
  position: absolute;
  left: 76px;
  top: 105px;
  width: 212px;
  height: 27px;
  color: var.$text-black;
  font-family: var.$font-family;
  font-size: 23px;
  font-weight: 400;
  line-height: normal;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-author {
  position: absolute;
  left: 76px;
  top: 132px;
  height: 12px;
  color: var.$text-description;
  font-family: var.$font-family;
  font-size: 10px;
  font-weight: 400;
  line-height: normal;
  margin: 0;
}

.card-description {
  position: absolute;
  left: 10px;
  top: 151px;
  width: 320px;
  height: 26px;
  color: var.$text-description;
  text-align: start;
  font-family: var.$font-family;
  font-size: 11.5px;
  font-weight: 400;
  line-height: normal;
  margin: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.card-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 8px;
}

.views-section {
  position: absolute;
  right: 12px;
  top: -67px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.eye-icon {
  width: 13px;
  height: 11px;
  flex-shrink: 0;
}

.views-count {
  color: var.$text-description;
  text-align: right;
  font-family: var.$font-family;
  font-size: 9px;
  font-weight: 400;
  line-height: normal;
}

.action-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  width: 325px;
  height: 31px;
  flex-shrink: 0;
  border-radius: 13px;
  background: var.$bg-input;
  box-shadow: var.$shadow-inset;
  cursor: pointer;
  transition: opacity 0.3s ease;
  padding: 5px;
  gap: 6px;

  &:hover {
    opacity: 0.8;
  }
}

@media (max-width: 1400px) {
  .job-card {
    width: 300px;
    height: 205px;
  }

  .card-image {
    height: 90px;
  }

  .card-logo {
    width: 55px;
    height: 55px;
    top: 70px;
  }

  .card-title {
    left: 70px;
    top: 92px;
    font-size: 20px;
  }

  .card-author {
    left: 70px;
    top: 115px;
  }

  .card-description {
    top: 132px;
    width: 280px;
  }

  .action-bar {
    width: 285px;
  }

  .views-section {
    top: -50px;
  }
}

@media (max-width: 1200px) {
  .job-card {
    width: 280px;
    height: 200px;
  }

  .card-image {
    height: 85px;
  }

  .card-logo {
    width: 50px;
    height: 50px;
    top: 65px;
  }

  .card-title {
    left: 65px;
    top: 87px;
    font-size: 18px;
  }

  .action-bar {
    width: 265px;
  }
}

@media (max-width: 768px) {
  .job-card {
    width: 100%;
    max-width: 400px;
  }
}
</style>
