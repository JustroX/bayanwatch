FROM ghost:latest
RUN mv content.orig/* content/

# We install git so we can pull ghost themes 
# and adapters via npm
RUN apt-get update && apt-get install -y git
COPY apps/budget-kanban/ghost/src/package.json package.json
RUN npm install --omit=dev

# Run scripts to add adapters, themes, and patches
COPY dockerfiles/infrastructure/blog/bin bin
RUN chmod +x bin/themes.sh && ./bin/themes.sh
RUN chmod +x bin/s3.sh && ./bin/s3.sh

# Run ghost entrypoint
COPY dockerfiles/infrastructure/blog/run.sh run.sh
RUN chmod +x run.sh
ENTRYPOINT ["./run.sh"]