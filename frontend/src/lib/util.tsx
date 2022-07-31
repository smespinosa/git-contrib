export const gradient = (
  colorStart: string,
  colorEnd: string,
  steps: number
) => {
  const colors: string[] = []

  for (let i = 0; i < steps; i++) {
    const ratio = (Math.round(100 / steps) * i) / 100
    const color = calculateMiddleColor(colorStart, colorEnd, ratio)
    colors.push(color)
  }
  return colors
}

export const calculateMiddleColor = (
  color1 = 'FF0000',
  color2 = '00FF00',
  ratio: number
) => {
  const hex = (color: number) => {
    const colorString = color.toString(16)
    return colorString.length === 1 ? `0${colorString}` : colorString
  }

  const r = Math.ceil(
    parseInt(color2.substring(0, 2), 16) * ratio +
      parseInt(color1.substring(0, 2), 16) * (1 - ratio)
  )
  const g = Math.ceil(
    parseInt(color2.substring(2, 4), 16) * ratio +
      parseInt(color1.substring(2, 4), 16) * (1 - ratio)
  )
  const b = Math.ceil(
    parseInt(color2.substring(4, 6), 16) * ratio +
      parseInt(color1.substring(4, 6), 16) * (1 - ratio)
  )

  return hex(r) + hex(g) + hex(b)
}
