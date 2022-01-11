FROM cypress/base:10
COPY ./cypress/ /root/cypress
WORKDIR ./root/cypress
RUN npm install
RUN npx cypress run --spec cypress/integration/test.spec.js