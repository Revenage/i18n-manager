rm -rf web/templates/web
cd ../i18n-manager-js
yarn
yarn prod
cp -rf dist ../i18n-manager/web/templates
mv -f ../i18n-manager/web/templates/dist ../i18n-manager/web/templates/web 
