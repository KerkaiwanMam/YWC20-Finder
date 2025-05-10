<template>
  <canvas ref="rainCanvas" class="absolute top-0 left-0 w-full h-full"></canvas>
</template>

<script setup>
import { onMounted, ref, reactive, onBeforeUnmount } from 'vue'

const rainCanvas = ref(null)
const isMobile = ref(false)  // เช็คว่าเป็นมือถือหรือไม่
const lightOnTouch = reactive({
  x: 0,
  y: 0,
  isTouched: false
})

const resizeCanvas = () => {
  const canvas = rainCanvas.value
  canvas.width = window.innerWidth
  canvas.height = window.innerHeight
}

onMounted(() => {
  const canvas = rainCanvas.value
  const ctx = canvas.getContext('2d')
  resizeCanvas()  // ตั้งค่าขนาดแคนวาสตามขนาดหน้าจอเริ่มต้น

  // ตรวจสอบว่าเป็นอุปกรณ์มือถือหรือไม่
  isMobile.value = /Mobi|Android/i.test(navigator.userAgent)

  // Rain drops
  const drops = Array(300).fill().map(() => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    l: Math.random() * 20 + 10,
    xs: -2 + Math.random() * 4 + 2,
    ys: Math.random() * 10 + 10
  }))

  // หมอก
  const fogs = Array(5).fill().map(() => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    speedX: Math.random() * 0.5 + 0.5,
    speedY: Math.random() * 0.5 + 0.5,
    opacity: Math.random() * 0.3 + 0.1
  }))

  // Static blurred light positions
  const lights = Array(10).fill().map(() => ({
    x: Math.random() * canvas.width,
    y: canvas.height - 100 + Math.random() * 100,
    radius: 40 + Math.random() * 60,
    color: Math.random() > 0.5 ? '#ffaa55' : '#88ccff'
  }))

  function drawBlurLights() {
    for (let light of lights) {
      const gradient = ctx.createRadialGradient(
        light.x, light.y, 0,
        light.x, light.y, light.radius
      )
      gradient.addColorStop(0, light.color)
      gradient.addColorStop(1, 'transparent')

      ctx.globalAlpha = 0.3
      ctx.fillStyle = gradient
      ctx.beginPath()
      ctx.arc(light.x, light.y, light.radius, 0, Math.PI * 2)
      ctx.fill()
    }
    ctx.globalAlpha = 1.0
  }

  function drawRain() {
    ctx.strokeStyle = 'rgba(174,194,224,0.5)'
    ctx.lineWidth = 1
    ctx.lineCap = 'round'
    for (let d of drops) {
      ctx.beginPath()
      ctx.moveTo(d.x, d.y)
      ctx.lineTo(d.x + d.xs, d.y + d.l)
      ctx.stroke()
    }
  }

  function moveRain() {
    for (let d of drops) {
      d.x += d.xs
      d.y += d.ys
      if (d.y > canvas.height || d.x > canvas.width) {
        d.x = Math.random() * canvas.width
        d.y = -20
      }
    }
  }

  function drawFog() {
    ctx.save()  // เก็บสถานะปัจจุบันของ ctx
    ctx.filter = 'blur(8px)'  // เพิ่มเบลอให้กับหมอก (ปรับค่าตามต้องการ)

    for (let fog of fogs) {
      ctx.fillStyle = `rgba(200, 200, 200, ${fog.opacity})`
      ctx.beginPath()
      ctx.arc(fog.x, fog.y, 40, 0, Math.PI * 2)
      ctx.fill()

      fog.x += fog.speedX
      fog.y += fog.speedY

      if (fog.x > canvas.width || fog.y > canvas.height || fog.x < 0 || fog.y < 0) {
        fog.x = Math.random() * canvas.width
        fog.y = Math.random() * canvas.height
      }
    }

    ctx.restore()  // คืนค่าการตั้งค่าสถานะก่อนหน้านี้
  }

  function drawLighting() {
    if (Math.random() < 0.002) {
      ctx.fillStyle = `rgba(255, 255, 255, 0.6)`
      ctx.fillRect(0, 0, canvas.width, canvas.height)
    }
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    drawBlurLights()        // Draw blurred streetlights first (background)
    drawRain()
    moveRain()
    drawFog()
    drawLighting()

    // แสดงแสงไฟที่ตอบสนองต่อการแตะ
    if (lightOnTouch.isTouched) {
      ctx.fillStyle = 'rgba(255, 255, 255, 0.6)'
      ctx.beginPath()
      ctx.arc(lightOnTouch.x, lightOnTouch.y, 50, 0, Math.PI * 2)
      ctx.fill()
    }

    requestAnimationFrame(draw)
  }

  // รองรับการแตะและเปลี่ยนแปลงแสงไฟ
  const handleTouch = (event) => {
    lightOnTouch.x = event.touches[0].clientX
    lightOnTouch.y = event.touches[0].clientY
    lightOnTouch.isTouched = true
    setTimeout(() => lightOnTouch.isTouched = false, 200)
  }

  // รองรับการเคลื่อนเมาส์
  const handleMouseMove = (event) => {
    if (!isMobile.value) {
      lightOnTouch.x = event.clientX
      lightOnTouch.y = event.clientY
    }
  }

  // เพิ่ม event listeners
  canvas.addEventListener('touchstart', handleTouch)
  canvas.addEventListener('mousemove', handleMouseMove)

  // รองรับการเปลี่ยนขนาดหน้าจอ
  window.addEventListener('resize', resizeCanvas)

  draw()
})

onBeforeUnmount(() => {
  // ลบ event listeners เมื่อคอมโพเนนต์ถูกทำลาย
  window.removeEventListener('resize', resizeCanvas)
})
</script>

<style scoped>
canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
