<script setup lang="ts">
import { ref } from "vue";

interface News {
  id: number;
  title: string;
  timestamp: string;
  content: string;
  image: string;
  imageLarge: string;
}

const newsList = ref<News[]>([
  {
    id: 1,
    title:
      "Для абитуриентов инженерных специальностей могут ввести четвертый ЕГЭ",
    timestamp: "12:37 14.10.2025",
    content: `Минобрнауки хочет дать возможность сдавать на инженерно-технические направления  четвертый ЕГЭ, который бы давал дополнительно до 25 баллов при  поступлении, заявил глава министерства Валерий Фальков.

"Дать возможность на инженерно-технические специальности и направления…  предъявлять четвертый дополнительный ЕГЭ по усмотрению самого  абитуриента. Таким образом, на то же машиностроение, условно, при  сегодняшнем русском языке, математике и физике можно было бы предъявить  информатику, если она у вас есть. И получить до 25 дополнительных  баллов, в зависимости от того, сколько баллов вы получили за экзамен", - сказал Фальков на заседании Совета Российского Союза ректоров.`,
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/5e66fe69a3b3659e4a31038908c7e202eacd6c6f?width=2840",
    imageLarge:
      "https://api.builder.io/api/v1/image/assets/TEMP/4835d05825af0d86184bb4ae224eac8531461b16?width=2840",
  },
  {
    id: 2,
    title: "На развитие образования в 2026 году выделят 669,1 миллиарда рублей",
    timestamp: "18:47 06.10.2025",
    content: `МОСКВА, 6 окт - РИА Новости. На реализацию государственной программы развития образования в 2026  году планируется выделить 669,1 миллиарда рублей, сообщил глава  Минпросвещения РФ Сергей Кравцов.

"В проекте федерального закона на реализацию государственной программы  развития образования на 2026 год предусмотрено 669 миллиардов рублей 100 миллионов рублей, идет увеличение", - сказал министр на заседании  комитета Государственной Думы по просвещению. Кравцов добавил, что в 2027 году планируется выделить 719,5 миллиарда рублей, а в 2028 году - 806,9 миллиарда рублей.`,
    image:
      "https://api.builder.io/api/v1/image/assets/TEMP/ad33659c33381eac40061641b81f19d65a13ad9f?width=2840",
    imageLarge:
      "https://api.builder.io/api/v1/image/assets/TEMP/54d0bb9f9707d3799d92a0f50d1f7a41697b8b8e?width=2840",
  },
]);
</script>

<template>
  <div class="news-page">
    <div class="content-wrapper">
      <div class="news-list">
        <NewsNewsCard
          v-for="newsItem in newsList"
          :key="newsItem.id"
          :news="newsItem"
        />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@use "~/assets/styles/variables" as var;

.news-page {
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

.news-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

@media (max-width: 1600px) {
  .news-page {
    padding-left: 320px;
  }

  .content-wrapper {
    max-width: calc(100vw - 320px - 40px);
  }
}

@media (max-width: 1400px) {
  .news-page {
    padding-left: 280px;
  }

  .content-wrapper {
    max-width: calc(100vw - 280px - 40px);
  }
}

@media (max-width: 1200px) {
  .news-page {
    padding-left: 220px;
  }

  .content-wrapper {
    max-width: calc(100vw - 220px - 30px);
  }
}

@media (max-width: 768px) {
  .news-page {
    padding-left: 0;
    padding-top: 80px;
  }

  .content-wrapper {
    max-width: calc(100vw - 20px);
    margin: 20px 10px;
  }
}
</style>
