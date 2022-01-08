FROM cypress/base:10
COPY ../application/. /root/application
COPY ../cypress/. /root/cypress
WORKDIR ./root
RUN npm install --save-dev cypress
# RUN npx cypress open 
# RUN npx cypress run --spec "cypress/test.spec.js"