
const header = {
  // all the properties are optional - can be left empty or deleted
  homepage: 'dtx000',
  title: 'dtx001',
}

const about = {
  // all the properties are optional - can be left empty or deleted
  name: 'dtx002',
  role: 'dtx003',
  description:
    'dtx004',
  resume: 'dtx005',
  social: {
    linkedin: 'dtx006',
    github: 'dtx007',
  },
}

const projects = [
  // projects can be added an removed
  // if there are no projects, Projects section won't show up
  dtx010
]

const skills = [
  // skills can be added or removed
  // if there are no skills, Skills section won't show up
  'dtx008',
]

const contact = {
  // email is optional - if left empty Contact section won't show up
  email: 'dtx009',
}

export { header, about, projects, skills, contact }
