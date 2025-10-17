<script setup lang="ts">
import { ref } from "vue";
import JobCard from "../components/job/JobCard.vue";

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
  icons: string[];
}

const jobs = ref<Job[]>([
  {
    id: 1,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 2,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 3,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 4,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 5,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 6,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 7,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 8,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 9,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 10,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 11,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 12,
    title: "ST_name",
    company: "Company Name",
    author: "by_...",
    description:
      "description_description_description_description_description_description_description_description_description_description_...",
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/435667ffb7267c6948a0d894fb9d40db3f4bfdfe?width=680",
    logo: "https://api.builder.io/api/v1/image/assets/TEMP/22303dbc394afc7a49397922b7f7bd2cc16fedf3?width=126",
    views: 0,
    tags: ["Hello, World!", "Hello, Code!"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
  {
    id: 13,
    title: "Cybersecurity",
    company: "Company Name",
    author: "by_MTS group",
    description:
      "MTS Start — стажировка продолжительностью до 12 месяцев в различных областях бизнеса и IT. Предназначена для специалистов с небольшим опытом ...",
    image: "/svg/MTC.svg",
    logo: "svg/Logo_MTC.svg",
    views: 1323,
    tags: ["с 16 лет", "оффлайн", "оплачиваемая"],
    icons: ["./icons/IconTag__16+.svg", "./icons/IconTag__16+.svg"],
  },
]);
</script>

<template>
  <div class="home-page">
    <SidebarAppSidebar />
    <div class="content-wrapper">
      <div class="header-section">
        <h1 class="page-title">Все стажировки</h1>
        <div class="header-controls">
          <span class="available-count">доступно: 0</span>
          <button class="control-button">
            <span>Фильтры</span>
            <svg
              width="18"
              height="11"
              viewBox="0 0 18 11"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M0 1C0 0.734784 0.105357 0.48043 0.292893 0.292893C0.48043 0.105357 0.734784 0 1 0H17C17.2652 0 17.5196 0.105357 17.7071 0.292893C17.8946 0.48043 18 0.734784 18 1C18 1.26522 17.8946 1.51957 17.7071 1.70711C17.5196 1.89464 17.2652 2 17 2H1C0.734784 2 0.48043 1.89464 0.292893 1.70711C0.105357 1.51957 0 1.26522 0 1ZM2 5.5C2 5.23478 2.10536 4.98043 2.29289 4.79289C2.48043 4.60536 2.73478 4.5 3 4.5H15C15.2652 4.5 15.5196 4.60536 15.7071 4.79289C15.8946 4.98043 16 5.23478 16 5.5C16 5.76522 15.8946 6.01957 15.7071 6.20711C15.5196 6.39464 15.2652 6.5 15 6.5H3C2.73478 6.5 2.48043 6.39464 2.29289 6.20711C2.10536 6.01957 2 5.76522 2 5.5ZM5 10C5 9.73478 5.10536 9.48043 5.29289 9.29289C5.48043 9.10536 5.73478 9 6 9H12C12.2652 9 12.5196 9.10536 12.7071 9.29289C12.8946 9.48043 13 9.73478 13 10C13 10.2652 12.8946 10.5196 12.7071 10.7071C12.5196 10.8946 12.2652 11 12 11H6C5.73478 11 5.48043 10.8946 5.29289 10.7071C5.10536 10.5196 5 10.2652 5 10Z"
                fill="#727272"
              />
            </svg>
          </button>
          <button class="control-button">
            <span>Сортировка</span>
            <svg
              width="18"
              height="19"
              viewBox="0 0 18 19"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M3.79312 0.278139C3.98064 0.100047 4.23494 0 4.5001 0C4.76526 0 5.01956 0.100047 5.20709 0.278139L8.70701 3.60304C8.79992 3.69124 8.87363 3.79596 8.92393 3.91123C8.97424 4.02649 9.00016 4.15004 9.0002 4.27481C9.00025 4.39959 8.97443 4.52316 8.9242 4.63845C8.87398 4.75375 8.80035 4.85852 8.70751 4.94678C8.61467 5.03504 8.50443 5.10507 8.3831 5.15286C8.26177 5.20065 8.13172 5.22527 8.00038 5.22532C7.86903 5.22536 7.73896 5.20083 7.6176 5.15312C7.49623 5.10541 7.38595 5.03546 7.29304 4.94726L5.50008 3.24395V12.3494C5.50008 12.6014 5.39472 12.843 5.20719 13.0212C5.01966 13.1993 4.76531 13.2994 4.5001 13.2994C4.23489 13.2994 3.98054 13.1993 3.79301 13.0212C3.60548 12.843 3.50012 12.6014 3.50012 12.3494V3.2449L1.70716 4.94726C1.61426 5.03546 1.50397 5.10541 1.38261 5.15312C1.26124 5.20083 1.13117 5.22536 0.999827 5.22532C0.868481 5.22527 0.738431 5.20065 0.617101 5.15286C0.495772 5.10507 0.385539 5.03504 0.292696 4.94678C0.199854 4.85852 0.12622 4.75375 0.075999 4.63845C0.0257782 4.52316 -4.63671e-05 4.39959 6.24951e-08 4.27481C4.64921e-05 4.15004 0.025963 4.02649 0.0762696 3.91123C0.126576 3.79596 0.200288 3.69124 0.293196 3.60304L3.79312 0.278139ZM13.4999 5.69963C13.7651 5.69963 14.0195 5.79972 14.207 5.97787C14.3945 6.15603 14.4999 6.39766 14.4999 6.64961V15.756L16.2928 14.0527C16.4805 13.8746 16.7349 13.7746 17.0002 13.7747C17.2654 13.7748 17.5198 13.875 17.7073 14.0532C17.8948 14.2315 18.0001 14.4732 18 14.7252C17.9999 14.9772 17.8944 15.2188 17.7068 15.397L14.2069 18.7219C14.0194 18.9 13.7651 19 13.4999 19C13.2347 19 12.9804 18.9 12.7929 18.7219L9.29299 15.397C9.10536 15.2188 8.99989 14.9772 8.9998 14.7252C8.99971 14.4732 9.10499 14.2315 9.29249 14.0532C9.48 13.875 9.73436 13.7748 9.99962 13.7747C10.2649 13.7746 10.5193 13.8746 10.707 14.0527L12.4999 15.756V6.64961C12.4999 6.39766 12.6053 6.15603 12.7928 5.97787C12.9803 5.79972 13.2347 5.69963 13.4999 5.69963Z"
                fill="#727272"
              />
            </svg>
          </button>
        </div>
      </div>

      <div class="jobs-grid">
        <JobCard v-for="job in jobs" :key="job.id" :job="job" />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@use "~/assets/styles/variables" as var;

.home-page {
  min-height: 100vh;
  padding-left: var.$content-offset;
}

.content-wrapper {
  width: 1462px;
  max-width: calc(100vw - var.$content-offset - 45px);
  margin: 46px 0 46px 0;
  border-radius: var.$radius-lg;
  border: 1px solid var.$border-color;
  padding: 21px;
  position: relative;
}

.header-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 21px;
  border-bottom: 1px solid var.$border-color;
  margin-bottom: 21px;
}

.page-title {
  color: var.$text-primary;
  font-family: var.$font-family;
  font-size: 24px;
  font-weight: 400;
  line-height: normal;
  margin: 0;
}

.header-controls {
  display: flex;
  align-items: center;
  gap: 20px;
}

.available-count {
  color: var.$text-muted;
  text-align: center;
  font-family: var.$font-family;
  font-size: 24px;
  font-weight: 400;
  line-height: normal;
}

.control-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  height: 41px;
  padding: 0 15px;
  border-radius: var.$radius-sm;
  background: var.$bg-input;
  box-shadow: var.$shadow-inset;
  border: none;
  cursor: pointer;
  transition: opacity 0.3s ease;

  span {
    color: var.$text-muted;
    font-family: var.$font-family;
    font-size: 24px;
    font-weight: 400;
    line-height: normal;
  }

  svg {
    width: 18px;
    flex-shrink: 0;
    fill: var.$text-muted;
  }

  &:hover {
    opacity: 0.8;
  }
}

.jobs-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  padding: 0 0 20px 0;
}

@media (max-width: 1600px) {
  .home-page {
    padding-left: 320px;
  }

  .content-wrapper {
    max-width: calc(100vw - 320px - 40px);
  }

  .jobs-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 1400px) {
  .home-page {
    padding-left: 280px;
  }

  .content-wrapper {
    max-width: calc(100vw - 280px - 40px);
  }

  .page-title {
    font-size: 20px;
  }

  .available-count {
    font-size: 20px;
  }

  .control-button {
    height: 36px;

    span {
      font-size: 20px;
    }

    svg {
      width: 16px;
    }
  }
}

@media (max-width: 1200px) {
  .home-page {
    padding-left: 220px;
  }

  .content-wrapper {
    max-width: calc(100vw - 220px - 30px);
  }

  .jobs-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .page-title {
    font-size: 18px;
  }

  .available-count {
    font-size: 18px;
  }

  .control-button {
    span {
      font-size: 18px;
    }

    svg {
      width: 14px;
    }
  }
}

@media (max-width: 768px) {
  .home-page {
    padding-left: 0;
    padding-top: 80px;
  }

  .content-wrapper {
    max-width: calc(100vw - 20px);
    margin: 20px 10px;
  }

  .header-section {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .header-controls {
    width: 100%;
    flex-wrap: wrap;
    gap: 10px;
  }

  .control-button {
    flex: 1;
    min-width: 120px;

    span {
      font-size: 16px;
    }
  }

  .jobs-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }
}
</style>
