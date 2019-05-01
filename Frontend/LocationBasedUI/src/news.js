//we are going to fetch the JSON that contains the headlines from the News API

const url =
  "https://newsapi.org/v2/top-headlines?country=us&apiKey=cf481d468fd64233b44db8cb491fca51";

export async function getNews() {
  let result = await fetch(url).then(response => response.json());
  return result.articles;
}

// export getNews func to use in ApplicationCache.js