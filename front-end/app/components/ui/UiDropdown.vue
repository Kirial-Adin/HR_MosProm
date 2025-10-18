<!-- components/DropdownInput.vue -->
<script setup lang="ts">
const props = defineProps<{
  options: string[];
  label?: string;
  placeholder?: string;
  modelValue?: string;
  maxItems?: number;
  styles?: string;
}>();

const emit = defineEmits<{ (e: "update:modelValue", v: string): void }>();
const root = ref<HTMLElement | null>(null);
const inputEl = ref<HTMLInputElement | null>(null);

const query = ref(props.modelValue ?? "");
watch(
  () => props.modelValue,
  (v) => {
    if (v !== undefined) query.value = v ?? "";
  }
);
watch(query, (v) => emit("update:modelValue", v));

const open = ref(false);
const activeIndex = ref(0);

const filtered = computed(() => {
  const q = query.value.toLowerCase().trim();
  const arr = q
    ? props.options.filter((o) => o.toLowerCase().includes(q))
    : props.options;
  return arr;
});

function move(dir: 1 | -1) {
  if (!filtered.value.length) return;
  open.value = true;
  activeIndex.value =
    (activeIndex.value + dir + filtered.value.length) % filtered.value.length;
}

function pick(i: number) {
  query.value = filtered.value[i] || "";
  open.value = false;
  inputEl.value?.blur();
}

function deferClose() {
  // даём кликнуть по пункту прежде чем блюр закроет меню
  setTimeout(() => (open.value = false), 100);
}
</script>

<template>
  <div
    class="dd"
    ref="root"
    @keydown.down.prevent="move(1)"
    @keydown.up.prevent="move(-1)"
    @keydown.enter.prevent="pick(activeIndex)"
    @keydown.esc="open = false"
  >
    <label v-if="label" class="dd__label">{{ label }}</label>

    <input
      ref="inputEl"
      v-model="query"
      :style="styles"
      class="dd__input"
      :placeholder="placeholder"
      @focus="open = true"
      @input="
        open = true;
        activeIndex = 0;
      "
      @blur="deferClose"
    />

    <!-- Выпадает ВНИЗ: top:100%; margin-top -->
    <div v-show="open && filtered.length" class="dd__menu" role="listbox">
      <ul class="dd__list">
        <li
          v-for="(opt, i) in filtered"
          :key="i"
          :title="opt"
          :class="['dd__item', { 'is-active': i === activeIndex }]"
          @mousedown.prevent="pick(i)"
          role="option"
        >
          {{ opt }}
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.dd {
  position: relative;
  max-width: 360px;
}
.dd__label {
  display: block;
  margin: 0 0 6px;
  font-size: 14px;
  color: #555;
}
.dd__input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background: #cfcfcf;
}

/* Меню — всегда НИЖЕ инпута */
.dd__menu {
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  margin-top: 6px;
  z-index: 20;
}

/* Собственный скролл и фиксированная высота */
.dd__list {
  max-height: 220px; /* <-- высота окна */
  overflow: auto; /* <-- свой скролл */
  margin: 0;
  padding: 6px;
  list-style: none;
  background: #cfcfcf;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

/* "Длина option": ограничиваем ширину и обрезаем текст с многоточием */
.dd__item {
  padding: 8px 10px;
  border-radius: 6px;
  cursor: pointer;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis; /* <-- обрезка */
}

/* Ховер/клавиатурная подсветка */
.dd__item:hover,
.dd__item.is-active {
  background: #f2f3f584;
}
</style>
