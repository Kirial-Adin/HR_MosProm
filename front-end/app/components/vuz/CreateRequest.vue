<script setup lang="ts">
import { ref } from "vue";
import AppSidebar from "../sidebar/AppSidebar.vue";
import cities from "~/components/json/russian-cities.json";

const add = ref(false);

const cityNames = cities.map((city) => city.name);

const changeAdding = () => {
  add.value = !add.value;
};
</script>

<template>
  <div>
    <AppSidebar>
      <button class="create-button">
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M2 6.857C2 5.56884 2.51172 4.33345 3.42258 3.42258C4.33345 2.51172 5.56884 2 6.857 2H12C12.2652 2 12.5196 2.10536 12.7071 2.29289C12.8946 2.48043 13 2.73478 13 3C13 3.26522 12.8946 3.51957 12.7071 3.70711C12.5196 3.89464 12.2652 4 12 4H6.857C6.09928 4 5.37259 4.301 4.8368 4.8368C4.301 5.37259 4 6.09928 4 6.857V17.143C4 17.9007 4.301 18.6274 4.8368 19.1632C5.37259 19.699 6.09928 20 6.857 20H17.143C17.9007 20 18.6274 19.699 19.1632 19.1632C19.699 18.6274 20 17.9007 20 17.143V12C20 11.7348 20.1054 11.4804 20.2929 11.2929C20.4804 11.1054 20.7348 11 21 11C21.2652 11 21.5196 11.1054 21.7071 11.2929C21.8946 11.4804 22 11.7348 22 12V17.143C22 18.4312 21.4883 19.6666 20.5774 20.5774C19.6666 21.4883 18.4312 22 17.143 22H6.857C5.56884 22 4.33345 21.4883 3.42258 20.5774C2.51172 19.6666 2 18.4312 2 17.143V6.857Z"
            fill="#D5D5D5"
          />
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M15.1371 13.2191L12.9321 14.5491L11.8991 12.8361L14.1041 11.5061L14.1071 11.5041C14.1916 11.4532 14.2695 11.3921 14.3391 11.3221L19.3491 6.2861C19.3993 6.23551 19.4476 6.18314 19.4941 6.1291C19.8251 5.7431 20.3151 4.9791 19.7221 4.3831C19.2211 3.8791 18.5031 4.3551 18.0381 4.7641C17.9134 4.87406 17.7932 4.98916 17.6781 5.1091L17.6441 5.1431L12.7041 10.1081C12.5868 10.2247 12.4949 10.3643 12.4341 10.5181L11.6101 12.5911C11.5945 12.6301 11.5915 12.673 11.6017 12.7138C11.6118 12.7546 11.6346 12.7911 11.6667 12.8183C11.6988 12.8454 11.7386 12.8617 11.7805 12.8649C11.8224 12.8681 11.8632 12.858 11.8991 12.8361L12.9321 14.5491C11.1271 15.6371 8.97208 13.8091 9.75208 11.8511L10.5771 9.7791C10.7377 9.3742 10.9793 9.00636 11.2871 8.6981L16.2261 3.7321L16.2551 3.7031C16.4021 3.5531 16.8961 3.0471 17.4951 2.6831C17.8221 2.4861 18.3441 2.2251 18.9891 2.1751C19.7291 2.1161 20.5191 2.3491 21.1391 2.9721C21.6136 3.44089 21.9121 4.05895 21.9841 4.7221C22.0336 5.239 21.9546 5.76012 21.7541 6.2391C21.4641 6.9561 20.9801 7.4831 20.7671 7.6961L15.7571 12.7321C15.5704 12.9194 15.3637 13.0818 15.1371 13.2191ZM19.5901 6.0931C19.5901 6.0931 19.5861 6.0961 19.5771 6.0991L19.5901 6.0931Z"
            fill="#D5D5D5"
          />
        </svg>
        <span>Создать заявку</span>
        <div class="button-glow"></div>
      </button>

      <button class="group-button">
        <svg
          width="54"
          height="52"
          viewBox="0 0 54 52"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M23.1 22.9999C23.3758 22.9999 23.6489 22.9456 23.9036 22.84C24.1584 22.7345 24.3899 22.5798 24.5849 22.3848C24.7799 22.1898 24.9346 21.9583 25.0401 21.7035C25.1457 21.4488 25.2 21.1757 25.2 20.8999C25.2 20.6241 25.1457 20.3511 25.0401 20.0963C24.9346 19.8415 24.7799 19.61 24.5849 19.415C24.3899 19.22 24.1584 19.0653 23.9036 18.9598C23.6489 18.8542 23.3758 18.7999 23.1 18.7999C22.543 18.7999 22.0089 19.0212 21.6151 19.415C21.2212 19.8088 21 20.3429 21 20.8999C21 21.4569 21.2212 21.991 21.6151 22.3848C22.0089 22.7787 22.543 22.9999 23.1 22.9999ZM23.1 25.3999C23.6909 25.3999 24.2761 25.2835 24.8221 25.0574C25.368 24.8312 25.8641 24.4997 26.282 24.0819C26.6998 23.664 27.0313 23.1679 27.2575 22.622C27.4836 22.076 27.6 21.4909 27.6 20.8999C27.6 20.309 27.4836 19.7238 27.2575 19.1778C27.0313 18.6319 26.6998 18.1358 26.282 17.7179C25.8641 17.3001 25.368 16.9686 24.8221 16.7424C24.2761 16.5163 23.6909 16.3999 23.1 16.3999C21.9065 16.3999 20.7619 16.874 19.918 17.7179C19.0741 18.5618 18.6 19.7064 18.6 20.8999C18.6 22.0934 19.0741 23.238 19.918 24.0819C20.7619 24.9258 21.9065 25.3999 23.1 25.3999ZM16.5192 29.0323C17.598 27.5335 19.242 26.5999 21.3432 26.5999H25.4568C27.5592 26.5999 29.202 27.5335 30.2808 29.0323C31.3284 30.4879 31.8 32.4067 31.8 34.3999C31.8 34.7182 31.6736 35.0234 31.4485 35.2484C31.2235 35.4735 30.9183 35.5999 30.6 35.5999C30.2817 35.5999 29.9765 35.4735 29.7515 35.2484C29.5264 35.0234 29.4 34.7182 29.4 34.3999C29.4 32.7475 29.004 31.3675 28.332 30.4339C27.6924 29.5435 26.7636 28.9999 25.4568 28.9999H21.3432C20.0352 28.9999 19.1076 29.5435 18.4668 30.4339C17.796 31.3663 17.4 32.7475 17.4 34.3999C17.4 34.7182 17.2736 35.0234 17.0485 35.2484C16.8235 35.4735 16.5183 35.5999 16.2 35.5999C15.8817 35.5999 15.5765 35.4735 15.3515 35.2484C15.1264 35.0234 15 34.7182 15 34.3999C15 32.4067 15.4716 30.4879 16.5192 29.0323Z"
            fill="#727272"
          />
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M30.471 18.6402L30.4374 18.6378C30.2571 18.6273 30.0782 18.5992 29.9034 18.5538C29.4894 18.4434 29.1174 18.2226 28.9482 17.8398L28.9326 17.8062C28.683 17.2422 28.9398 16.5666 29.5482 16.4622C30.1634 16.3588 30.7933 16.3844 31.3981 16.5374C32.0029 16.6904 32.5692 16.9674 33.0612 17.351C33.5531 17.7345 33.96 18.2161 34.2559 18.7653C34.5518 19.3145 34.7303 19.9191 34.78 20.541C34.8298 21.1628 34.7497 21.7881 34.5449 22.3774C34.3401 22.9666 34.015 23.5068 33.5903 23.9637C33.1656 24.4206 32.6505 24.7842 32.0778 25.0314C31.5051 25.2786 30.8872 25.4041 30.2634 25.3998C29.6466 25.395 29.2854 24.7686 29.4426 24.1722L29.4522 24.1362C29.5578 23.7306 29.8914 23.4534 30.2802 23.2794C30.456 23.2017 30.6394 23.1426 30.8274 23.103C31.3544 22.979 31.8195 22.6703 32.1385 22.2329C32.4575 21.7954 32.6091 21.2582 32.566 20.7185C32.5229 20.1789 32.2879 19.6725 31.9036 19.2912C31.5192 18.9099 31.011 18.679 30.471 18.6402ZM31.2006 27.7998C31.2006 27.4815 31.327 27.1763 31.5521 26.9513C31.7771 26.7262 32.0824 26.5998 32.4006 26.5998H32.6574C34.7598 26.5998 36.4026 27.5334 37.4814 29.0322C38.529 30.4878 39.0006 32.4066 39.0006 34.3998C39.0006 34.7181 38.8742 35.0233 38.6491 35.2483C38.4241 35.4734 38.1189 35.5998 37.8006 35.5998C37.4824 35.5998 37.1771 35.4734 36.9521 35.2483C36.727 35.0233 36.6006 34.7181 36.6006 34.3998C36.6006 32.7474 36.2046 31.3674 35.5326 30.4338C34.893 29.5434 33.9642 28.9998 32.6574 28.9998H32.4006C32.0824 28.9998 31.7771 28.8734 31.5521 28.6483C31.327 28.4233 31.2006 28.1181 31.2006 27.7998Z"
            fill="#727272"
          />
        </svg>
        <span>Моя группа</span>
      </button>
    </AppSidebar>
    <main class="application-form">
      <div class="container">
        <div class="content-box">
          <h1 class="page-title">Создание заявки</h1>

          <div class="student-section">
            <div class="section-header">
              <h2>Кого добавим в заявку?</h2>
              <div class="search-box">
                <svg
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M17 14.0061C17.7879 14.0061 18.5681 13.8509 19.2961 13.5494C20.0241 13.2479 20.6855 12.8059 21.2426 12.2487C21.7998 11.6916 22.2417 11.0302 22.5433 10.3022C22.8448 9.57425 23 8.79404 23 8.0061C23 7.21817 22.8448 6.43795 22.5433 5.71001C22.2417 4.98206 21.7998 4.32065 21.2426 3.76349C20.6855 3.20633 20.0241 2.76436 19.2961 2.46284C18.5681 2.16133 17.7879 2.0061 17 2.0061C15.4087 2.0061 13.8826 2.6382 12.7574 3.76349C11.6321 4.88878 11 6.41479 11 8.0061C11 9.59742 11.6321 11.1234 12.7574 12.2487C13.8826 13.374 15.4087 14.0061 17 14.0061ZM17 16.0061C19.1217 16.0061 21.1566 15.1632 22.6569 13.663C24.1571 12.1627 25 10.1278 25 8.0061C25 5.88441 24.1571 3.84953 22.6569 2.34924C21.1566 0.848958 19.1217 0.0061035 17 0.0061035C14.8783 0.0061035 12.8434 0.848958 11.3431 2.34924C9.84286 3.84953 9 5.88441 9 8.0061C9 10.1278 9.84286 12.1627 11.3431 13.663C12.8434 15.1632 14.8783 16.0061 17 16.0061Z"
                    fill="#7E7E7E"
                  />
                  <path
                    fill-rule="evenodd"
                    clip-rule="evenodd"
                    d="M21.3202 12.2962C21.5084 12.1093 21.7631 12.0049 22.0282 12.0059C22.2934 12.0068 22.5473 12.113 22.7342 12.3012L26.7092 16.3012C26.8909 16.4903 26.991 16.7432 26.988 17.0054C26.985 17.2676 26.8792 17.5182 26.6932 17.7031C26.5072 17.888 26.2561 17.9925 25.9938 17.994C25.7316 17.9955 25.4793 17.8939 25.2912 17.7112L21.3162 13.7112C21.1292 13.5231 21.0246 13.2685 21.0254 13.0033C21.0261 12.7382 21.1322 12.4842 21.3202 12.2972V12.2962Z"
                    fill="#7E7E7E"
                  />
                </svg>
                <input type="text" placeholder="поиск" />
              </div>
            </div>

            <div class="student-list">
              <div class="student-item">
                <span class="student-number">1</span>
                <span class="student-name">Ичмелян Эдик Янович</span>
                <span class="student-date">19.08.2007</span>
                <span class="student-group">ПИ-2502</span>
                <button class="check-button" @click="changeAdding">
                  <svg
                    v-if="add !== false"
                    width="24"
                    height="24"
                    viewBox="0 0 34 34"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M29.1614 8.46479C29.4469 8.74159 29.6108 9.12047 29.617 9.5181C29.6232 9.91573 29.4712 10.2995 29.1944 10.5851L15.0916 25.1362C14.8959 25.338 14.6617 25.4984 14.4028 25.608C14.1439 25.7175 13.8657 25.774 13.5846 25.774C13.3035 25.774 13.0253 25.7175 12.7664 25.608C12.5075 25.4984 12.2733 25.338 12.0776 25.1362L6.04813 18.9163C5.9093 18.7753 5.79975 18.6082 5.7258 18.4246C5.65186 18.241 5.61498 18.0447 5.61729 17.8468C5.6196 17.6489 5.66106 17.4534 5.73927 17.2717C5.81749 17.0899 5.93091 16.9254 6.073 16.7876C6.2151 16.6499 6.38305 16.5416 6.56717 16.4691C6.7513 16.3966 6.94796 16.3612 7.14582 16.3651C7.34368 16.3689 7.53882 16.4119 7.71999 16.4915C7.90116 16.5711 8.06478 16.6858 8.20141 16.829L13.5846 22.3816L27.0411 8.49778C27.3179 8.21224 27.6968 8.04836 28.0944 8.04217C28.4921 8.03599 28.8759 8.18801 29.1614 8.46479Z"
                      fill="black"
                    />
                  </svg>
                  <svg
                    v-else
                    width="23"
                    height="23"
                    viewBox="0 0 23 23"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M1.45512 10.9393C1.73635 10.6582 2.1181 10.5002 2.51578 10.5002L20.5145 10.4995H20.5242L20.5235 10.5002C20.9168 10.507 21.2919 10.6671 21.5676 10.9476C21.8433 11.2281 21.9978 11.606 21.9978 11.9993C21.9978 12.3926 21.8433 12.7705 21.5676 13.051C21.2919 13.3315 20.9168 13.4916 20.5235 13.4985L20.5145 13.4991L2.51578 13.4998C2.1181 13.4998 1.73635 13.3418 1.45512 13.0607C1.17387 12.7794 1.016 12.3977 1.01594 12C1.016 11.6023 1.17387 11.2206 1.45512 10.9393Z"
                      fill="#171717"
                      stroke="#171717"
                    />
                    <path
                      d="M10.6474 1.74704C10.9287 1.46579 11.3103 1.30792 11.7081 1.30786C12.1058 1.30793 12.4875 1.4658 12.7687 1.74704C13.0499 2.02827 13.2079 2.41002 13.2079 2.8077V20.8072C13.2103 21.0035 13.1737 21.1985 13.1009 21.381C13.0271 21.5659 12.9173 21.7348 12.7777 21.8768C12.6382 22.0187 12.471 22.1313 12.2874 22.2083C12.1039 22.2851 11.907 22.3249 11.7081 22.325C11.5089 22.325 11.311 22.2853 11.1273 22.2083C10.9439 22.1312 10.7772 22.018 10.6377 21.8761C10.4984 21.7342 10.389 21.5657 10.3153 21.381C10.2415 21.196 10.2048 20.998 10.2082 20.7989V2.8077C10.2083 2.40997 10.3662 2.02829 10.6474 1.74704Z"
                      fill="#171717"
                      stroke="#171717"
                    />
                  </svg>
                </button>
              </div>
            </div>

            <div class="scrollbar"></div>
          </div>

          <div class="form-section">
            <div class="left-section">
              <div class="form-group city-group">
                <label>Выберите город стажировки</label>
                <UiDropdown
                  class="select-input city"
                  placeholder="Начните вводить…"
                  :options="cityNames"
                  :styles="'height: 54px'"
                />
              </div>
              <h3 class="section-subtitle">Контакты для связи</h3>

              <div class="contacts-row">
                <div class="form-group">
                  <label>Телефон</label>
                  <div class="phone-input">
                    <span>+7</span>
                    <div class="divider-vertical" />
                    <input class="input-number" type="number" required />
                  </div>
                </div>
              </div>
              <div class="contacts-row">
                <div class="form-group">
                  <label>Почта ВУЗа</label>
                  <input class="text-input" type="email" required />
                </div>
              </div>
              <div class="form-group">
                <label>Telegram представителя вуза</label>
                <input class="text-input" required type="text" />
              </div>
            </div>

            <div class="right-section">
              <div class="form-group skills-group">
                <label>Стэк умений студентов</label>
                <div class="textarea-input"></div>
              </div>
              <div class="form-group period-group">
                <label>Период стажировки</label>
              </div>

              <div class="period-buttons">
                <button class="period-btn">1 месяц</button>
                <button class="period-btn">2 месяц</button>
                <button class="period-btn">3 месяц</button>
                <button class="period-btn">4 месяц</button>
              </div>

              <div class="checkboxes">
                <label class="checkbox-label">
                  <input type="checkbox" class="checkbox-input" />
                  <div class="checkbox"></div>
                  <span
                    >Студенты предоставили согласие на обработку своих
                    данных</span
                  >
                </label>

                <label class="checkbox-label">
                  <input type="checkbox" class="checkbox-input" />
                  <div class="checkbox"></div>
                  <span
                    >Я (представитель ВУЗа) даю согласие на обработку данных о
                    вузе, а также предоставление их компаниям</span
                  >
                </label>
              </div>

              <button class="submit-button">Создать</button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style lang="scss" scoped>
.create-button {
  width: 100%;
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 0 15px;
  border-radius: 10px;
  border: 1px solid #879ae3;
  background: linear-gradient(150deg, #c03636 1.62%, #ee6b6b 70.36%);
  cursor: pointer;
  font-family: "Roboto", sans-serif;
  font-size: 24px;
  font-weight: 400;
  color: #fff;
  margin-bottom: 15px;
  position: relative;
  overflow: hidden;

  @media (max-width: 1024px) {
    font-size: 20px;
    height: 46px;
  }

  svg {
    flex-shrink: 0;
  }

  .button-glow {
    position: absolute;
    right: 1px;
    top: 12px;
    width: 5px;
    height: 28px;
    border-radius: 3px 0 0 3px;
    background: #fff;
    box-shadow: 0 0 130.637px 0 #fff, 0 0 74.65px 0 #fff, 0 0 43.546px 0 #fff,
      0 0 21.773px 0 #fff, 0 0 6.221px 0 #fff, 0 0 3.11px 0 #fff;
  }
}

.group-button {
  width: 100%;
  height: 52px;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 0 15px;
  border-radius: 10px;
  background: transparent;
  border: none;
  cursor: pointer;
  font-family: "Roboto", sans-serif;
  font-size: 24px;
  font-weight: 400;
  color: #727272;
  margin-bottom: 56px;

  @media (max-width: 1024px) {
    font-size: 20px;
    height: 46px;
  }

  svg {
    width: 24px;
    height: 24px;
    flex-shrink: 0;
  }
}

.application-form {
  margin-left: 363px;
  padding: 46px 30px;
  min-height: 100vh;

  @media (max-width: 1024px) {
    margin-left: 280px;
    padding: 30px 20px;
  }

  @media (max-width: 768px) {
    margin-left: 0;
    margin-top: 60px;
    padding: 20px;
  }
}

.container {
  max-width: 1462px;
  margin: 0 auto;
}

.page-title {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 21px;
  color: #727272;
  text-align: center;
  font-family: "Roboto", sans-serif;
  font-size: 24px;
  font-weight: 400;
  margin-bottom: 32px;
  border-bottom: 1px solid #3d3d3d;
  overflow: hidden;

  @media (max-width: 768px) {
    font-size: 20px;
    margin-bottom: 20px;
  }
}

.content-box {
  border-radius: 23px;
  border: 1px solid #3d3d3d;
  overflow: hidden;
}

.student-section {
  border-bottom: 1px solid #3d3d3d;
  padding: 10px 30px;
  position: relative;

  @media (max-width: 768px) {
    padding: 20px;
  }
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 42px;

  @media (max-width: 768px) {
    flex-direction: column;
    gap: 15px;
    align-items: flex-start;
  }

  h2 {
    color: #727272;
    font-family: "Roboto", sans-serif;
    font-size: 24px;
    font-weight: 400;

    @media (max-width: 768px) {
      font-size: 18px;
    }
  }
}

.search-box {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 2px 17px;
  width: 362px;
  height: 34px;
  border-radius: 10px;
  background: #d9d9d9;

  @media (max-width: 768px) {
    width: 100%;
  }

  svg {
    flex-shrink: 0;
    fill: #7e7e7e;
    width: 20px;
    height: 20px;
  }

  input {
    border: none;
    background: transparent;
    color: #7e7e7e;
    font-family: "Roboto", sans-serif;
    font-size: 24px;
    font-weight: 400;
    outline: none;
    width: 100%;

    @media (max-width: 768px) {
      font-size: 18px;
    }

    &::placeholder {
      color: #7e7e7e;
    }
  }
}

.student-list {
  background: #ededed;
  border-radius: 5px;
  box-shadow: 0 -1px 4px 0 rgba(0, 0, 0, 0.25) inset,
    0 4px 4.4px 0 rgba(0, 0, 0, 0.23) inset;
  padding: 20px;
  min-height: 389px;
  max-height: 389px;
  overflow-y: auto;

  @media (max-width: 768px) {
    padding: 15px;
    max-height: none;
  }
}

.student-item {
  display: grid;
  grid-template-columns: auto 1fr auto auto auto;
  align-items: center;
  gap: 78px;
  padding: 26px 65px;
  border-radius: 23px;
  border: 1px solid #ededed;
  background: #d7d7d7;
  height: 80px;

  @media (max-width: 1024px) {
    gap: 40px;
    padding: 25px 35px;
  }

  @media (max-width: 768px) {
    grid-template-columns: auto 1fr;
    gap: 15px;
    padding: 20px;
    height: auto;
  }

  .student-number {
    color: #000;
    font-family: "Roboto", sans-serif;
    font-size: 24px;
    font-weight: 400;

    @media (max-width: 768px) {
      font-size: 18px;
    }
  }

  .student-name {
    color: #000;
    font-family: "Roboto", sans-serif;
    font-size: 24px;
    font-weight: 400;

    @media (max-width: 768px) {
      font-size: 18px;
      grid-column: 2 / -1;
    }
  }

  .student-date,
  .student-group {
    color: #000;
    font-family: "Roboto", sans-serif;
    font-size: 24px;
    font-weight: 400;

    @media (max-width: 768px) {
      font-size: 16px;
      grid-column: span 1;
    }
  }

  .check-button {
    background: transparent;
    border: none;
    cursor: pointer;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}

.scrollbar {
  position: absolute;
  right: 30px;
  top: 191px;
  width: 9px;
  height: 148px;
  border-radius: 25px;
  background: #333;

  @media (max-width: 768px) {
    display: none;
  }
}

.form-section {
  display: flex;
  flex-direction: row;
  gap: 36px;
  padding: 30px;

  @media (max-width: 768px) {
    padding: 20px;
  }
}

.left-section {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.right-section {
  display: flex;
  flex-direction: column;
}

.form-row {
  display: flex;
  gap: 36px;
  margin-bottom: 36px;

  @media (max-width: 768px) {
    flex-direction: column;
    gap: 20px;
  }
}

.form-group {
  label {
    display: block;
    color: #000;
    font-family: "Roboto", sans-serif;
    font-size: 20px;
    font-weight: 400;
    margin-bottom: 7px;

    @media (max-width: 768px) {
      font-size: 16px;
    }
  }
}

.select-input {
  width: 366px;
  height: 54px;
}

.text-input,
.phone-input {
  width: 366px;
  height: 54px;
  border-radius: 6px;
  background: #d7d7d7;
  display: flex;
  align-items: center;
  padding: 15px 18px;
  gap: 10px;
  outline: none;
  border: none;
  font-size: 20px;
  font-weight: 400;

  @media (max-width: 768px) {
    width: 100%;
  }

  svg {
    margin-left: auto;
  }
}

.phone-input {
  span {
    color: #000;
    font-family: "Roboto", sans-serif;
    font-size: 20px;
    font-weight: 400;

    @media (max-width: 768px) {
      font-size: 18px;
    }
  }

  .divider-vertical {
    width: 1px;
    height: 28px;
    background: #000;
  }

  .input-number {
    width: 310px;
    height: 40px;
    border: none;
    background: #d7d7d7;
    padding: 5px;
    font-size: 20px;
    outline: none;
    appearance: none;
  }
  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
  }
}

.city-group {
  height: 100px;
  border-bottom: 1px #000000 solid;
}

.skills-group {
  flex: 1;

  .textarea-input {
    width: 100%;
    height: 168px;
    border-radius: 6px;
    background: #d7d7d7;
  }
}

.contacts-section {
  .section-subtitle {
    color: #3d3d3d;
    font-family: "Roboto", sans-serif;
    font-size: 20px;
    font-weight: 400;
    margin-bottom: 17px;

    @media (max-width: 768px) {
      font-size: 18px;
    }
  }

  .divider {
    width: 366px;
    height: 1px;
    background: #000;
    margin-bottom: 17px;

    @media (max-width: 768px) {
      width: 100%;
    }
  }
}

.contacts-row {
  display: flex;
  gap: 36px;
  margin-bottom: 18px;

  @media (max-width: 768px) {
    flex-direction: column;
    gap: 20px;
  }
}

.period-group {
  label {
    width: 190px;

    @media (max-width: 768px) {
      width: 100%;
    }
  }
}

.period-buttons {
  display: flex;
  gap: 10px;
  flex: 1;

  @media (max-width: 768px) {
    flex-wrap: wrap;
  }

  .period-btn {
    flex: 1;
    height: 54px;
    padding: 15px 18px;
    border-radius: 6px;
    background: #d7d7d7;
    border: none;
    color: #000;
    font-family: "Roboto", sans-serif;
    font-size: 20px;
    font-weight: 400;
    cursor: pointer;
    transition: background 0.2s;

    @media (max-width: 768px) {
      font-size: 16px;
      min-width: calc(50% - 5px);
    }

    &:hover {
      background: #c7c7c7;
    }
  }
}

.checkboxes {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: 20px 0 28px;

  .checkbox-label {
    display: flex;
    align-items: center;
    gap: 9px;
    cursor: pointer;
    position: relative;

    // Скрываем настоящий input
    .checkbox-input {
      position: absolute;
      opacity: 0;
      width: 0;
      height: 0;

      // Стили для checked состояния
      &:checked + .checkbox {
        background: #e06565; // Зеленый цвет при выборе
        border-color: #e06565;

        // Добавляем галочку
        &::after {
          content: "";
          position: absolute;
          left: 6px;
          top: 2px;
          width: 4px;
          height: 8px;
          border: solid white;
          border-width: 0 2px 2px 0;
          transform: rotate(45deg);
        }
      }

      // Стили при фокусе (для доступности)
      &:focus + .checkbox {
        box-shadow: 0 0 0 2px rgba(182, 46, 46, 0.3);
      }
    }

    .checkbox {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: #dcdcdc;
      border: 2px solid #ccc;
      flex-shrink: 0;
      position: relative;
      transition: all 0.3s ease;
    }

    span {
      color: #aaa;
      font-family: "Roboto", sans-serif;
      font-size: 13px;
      font-weight: 400;
      transition: color 0.3s ease;

      @media (max-width: 768px) {
        font-size: 12px;
      }
    }

    // Меняем цвет текста при выборе
    .checkbox-input:checked ~ span {
      color: #333; // Более темный цвет для выбранного элемента
    }
  }
}

.submit-button {
  width: 100%;
  max-width: 997px;
  height: 52px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border: 1px solid #879ae3;
  background: linear-gradient(150deg, #c03636 1.62%, #ee6b6b 70.36%);
  color: #fff;
  font-family: "Roboto", sans-serif;
  font-size: 24px;
  font-weight: 400;
  cursor: pointer;
  transition: transform 0.2s;

  @media (max-width: 768px) {
    font-size: 20px;
  }

  &:hover {
    transform: translateY(-2px);
  }
}
</style>
