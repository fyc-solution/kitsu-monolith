<template>
  <div
    :class="{
      modal: true,
      'is-active': active
    }"
  >
    <div class="modal-background" @click="$emit('cancel')"></div>

    <div class="modal-content">
      <div class="box content">
        <h1 class="title">
          {{ $t('breakdown.edit_label') }}
        </h1>

        <form @submit.prevent>
          <combobox
            ref="typeField"
            :label="$t('breakdown.label')"
            :options="typeOptions"
            @enter="confirm"
            v-model="form.label"
            v-focus
          />

          <modal-footer
            :is-error="isError"
            :is-loading="isLoading"
            @confirm="confirm"
            @cancel="$emit('cancel')"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { modalMixin } from '@/components/modals/base_modal'

import Combobox from '@/components/widgets/Combobox.vue'
import ModalFooter from '@/components/modals/ModalFooter.vue'

export default {
  name: 'edit-label-modal',

  mixins: [modalMixin],

  components: {
    Combobox,
    ModalFooter
  },

  props: {
    active: {
      type: Boolean,
      default: false
    },
    isError: {
      type: Boolean,
      default: false
    },
    isLoading: {
      type: Boolean,
      default: false
    },
    label: {
      type: String
    }
  },

  emits: ['cancel', 'confirm'],

  mounted() {
    this.form.label = this.label
  },

  data() {
    return {
      form: {
        label: 'animate'
      },
      typeOptions: [
        {
          label: this.$t('breakdown.options.animate'),
          value: 'animate'
        },
        {
          label: this.$t('breakdown.options.fixed'),
          value: 'fixed'
        }
      ]
    }
  },

  methods: {
    confirm() {
      return this.$emit('confirm', this.form)
    }
  },

  watch: {
    label() {
      this.form.label = this.label
    }
  }
}
</script>

<style lang="scss" scoped>
.error {
  margin-top: 1em;
}
</style>
