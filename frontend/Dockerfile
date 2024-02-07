# Stage 1: Build the Vue.js application
FROM node:14 as build-stage

WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm install @vue/cli-service

COPY . .

RUN npm run build

# Stage 2: Serve the application with nginx
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

