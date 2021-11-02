const { GraphQLServer } = require("graphql-yoga");
const fetch = require("node-fetch");

const typeDefs = `
    type Query {
        hello(name: String): String!
    }
`;

const resolvers = {
  Query: {
    hello: (_, { name }) => `Hello ${name || "World"}`,
  },
};

const server = new GraphQLServer({ typeDefs, resolvers });
server.start(() => console.log("Server is running on port 4000"));

//HTTP request:  https://cloud.iexapis.com/stable/stock/aapl/quote?token={yourApiToken}

// response :
// {
//     avgTotalVolume: 64294613,
//     calculationPrice: "close",
//     change: 1.06,
//     changePercent: 0.00718,
//     close: null,
//     closeSource: "official",
//     closeTime: null,
//     companyName: "Apple Inc",
//     currency: "USD",
//     delayedPrice: null,
//     delayedPriceTime: null,
//     extendedChange: null,
//     extendedChangePercent: null,
//     extendedPrice: null,
//     extendedPriceTime: null,
//     high: null,
//     highSource: null,
//     highTime: null,
//     iexAskPrice: 0,
//     iexAskSize: 0,
//     iexBidPrice: 0,
//     iexBidSize: 0,
//     iexClose: 148.61,
//     iexCloseTime: 1630094397006,
//     iexLastUpdated: 0,
//     iexMarketPercent: null,
//     iexOpen: 148.61,
//     iexOpenTime: 1630094397006,
//     iexRealtimePrice: 0,
//     iexRealtimeSize: 0,
//     iexVolume: 0,
//     lastTradeTime: 1630094399766,
//     latestPrice: 148.6,
//     latestSource: "Close",
//     latestTime: "August 27, 2021",
//     latestUpdate: 1630094401111,
//     latestVolume: null,
//     low: null,
//     lowSource: null,
//     lowTime: null,
//     marketCap: 2456382667600,
//     oddLotDelayedPrice: null,
//     oddLotDelayedPriceTime: null,
//     open: null,
//     openTime: null,
//     openSource: "official",
//     peRatio: 29.14,
//     previousClose: 147.54,
//     previousVolume: 48597195,
//     primaryExchange: "NASDAQ",
//     symbol: "AAPL",
//     volume: null,
//     week52High: 151.68,
//     week52Low: 102.44,
//     ytdChange: 0.13234515925327187,
//     isUSMarketOpen: false
//     }
