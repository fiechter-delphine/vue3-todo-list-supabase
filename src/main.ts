import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import { supabase } from './lib/supabase'
import { userSession } from '@/vuetils/useAuth'
import './assets/tailwind.css'
// import router from './router'
// createApp(App).mount('#app')

const app = createApp(App)

app.use(createPinia())
// app.use(router)

app.mount('#app')

/**
 * Keeps track of if the user is logged in or out and will update userSession state accordingly.
 */
supabase.auth.onAuthStateChange((event, session) => {
  userSession.value = session
})
