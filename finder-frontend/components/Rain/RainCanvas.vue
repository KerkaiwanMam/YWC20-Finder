<template>
  <canvas ref="rainCanvas" class="absolute top-0 left-0 w-full h-full"></canvas>
</template>

<script setup>
import { onMounted, ref } from 'vue'

const rainCanvas = ref(null)

onMounted(() => {
  const canvas = rainCanvas.value
  const ctx = canvas.getContext('2d')
  canvas.width = window.innerWidth
  canvas.height = window.innerHeight

  // Create rain drops
  const drops = Array(300).fill().map(() => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    l: Math.random() * 20 + 10,
    xs: -2 + Math.random() * 4 + 2,
    ys: Math.random() * 10 + 10
  }))

  // Lightning state
  let lightningTimer = 0
  let lightningOpacity = 0

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

  function drawLightning() {
    if (Math.random() < 0.002 && lightningTimer <= 0) {
      lightningOpacity = 1
      lightningTimer = 20
    }

    if (lightningTimer > 0) {
      ctx.fillStyle = `rgba(255, 255, 255, ${lightningOpacity})`
      ctx.fillRect(0, 0, canvas.width, canvas.height)
      lightningOpacity -= 0.08
      lightningTimer--
    }
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    drawRain()
    moveRain()
    drawLightning()
    requestAnimationFrame(draw)
  }

  draw()
})
</script>
