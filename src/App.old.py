<!-- <script setup lang="ts">
import Auth from '@/components/Auth.vue'
import PasswordReset from '@/components/PasswordReset.vue'
import TodoList from '@/components/TodoList.vue'
import Loading from '@/components/Loading.vue'
import Footer from '@/components/Footer.vue'
import { userSession, handleLogout } from '@/vuetils/useAuth'
import { getParameterByName } from '@/lib/helpers'
import { ref, computed } from 'vue'

//   computed: {
//     showPasswordReset: function() {
//       const requestType = getParameterByName('type', location.href)
//       return requestType === 'recovery'
//     }
//   },
//   setup() {
//     return { userSession, handleLogout }
//   },
// }

// const count = ref(0)

// // inferred type: ComputedRef<number>
// const double = computed(() => count.value * 2)

</script>

<template>
  <div id="app" class="w-full h-full flex flex-col justify-center bg-gray-300">
    <div
      v-if="showPasswordReset"
      class="w-full h-full flex flex-col justify-center items-center p-4"
    >
      <PasswordReset />
    </div>
    <div
      v-else-if="userSession === null"
      class="w-full h-full flex flex-col justify-center items-center p-4"
    >
      <Auth />
    </div>
    <div v-else class="w-full h-full flex flex-col justify-center items-center p-4 max-w-sm m-auto">
      <Suspense>
        <template #default>
          <div>
            <TodoList />
            <button class="btn-black w-full mt-12" @click="handleLogout">
              Logout
            </button>
          </div>
        </template>
        <template #fallback>
          <Loading />
        </template>
      </Suspense>
    </div>
    <Footer />
  </div>
</template>
 -->
