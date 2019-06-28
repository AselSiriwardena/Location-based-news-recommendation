const listings = [
    {
        title: 'Mostly Viewed',     //expirience or something
        boldTitle: false,
        showAddToFav: true,
        listings: [
            {
                id: 1,
                photo: require('./photos/5603c406da44a7847978bbadfe528a5d_S.jpg'),
                type: 'LOCAL - COLOMBO',
                title: 'Politics tutor for Ranja',
                price: 20,
                priceType: 'per person',
                stars: 29,
            },
            {
                id: 2,
                photo: require('./photos/f54b49233300553237717fa9d725b92d_S.jpg'),
                type: 'SPORTS - SL',
                title: 'We know South Africa\'s game - Hathurusinghe',
                price: 19,
                priceType: 'per person',
                stars: 4,
            },
            {
                id: 3,
                photo: require('./photos/1561657569-Modi-thanks-Ranil-for-hospitality-during-his-visit-A.jpg'),
                type: 'POLITICS - SRI LANKA',
                title: 'Modi thanks Ranil for hospitality during his visit',
                price: 19,
                priceType: 'per person',
                stars: 30,
            },
            {
                id: 4,
                photo: require('./photos/pettahrailway.jpg'),
                type: 'LOCAL - SRI LANKA',
                title: '24 hour railway strike from midnight tonight',
                price: 57,
                priceType: 'per person',
                stars: 70,
            },
            {
                id: 5,
                photo: require('./photos/1561621364-Osman-Gunasekara-and-wife-arrested-at-BIA-A.jpg'),
                type: 'LOCAL-SL',
                title: 'Osman Gunasekara and wife arrested at BIA',
                price: 61,
                priceType: 'per person',
                stars: 66,
            },
            {
                id: 6,
                photo: require('./photos/6c2236ec8cf6e01a5994853a1aa5b42d_S.jpg'),
                type: 'LOCAL - NORTH CENTRAL',
                title: 'Navy finds 18.9kg of Kerala cannabis',
                price: 55,
                priceType: 'per person',
                stars: 15,
            }
        ]
    },
    {
        title: 'LOCAL',
        boldTitle: false,
        showAddToFav: true,
        listings: [
            {
                id: 7,
                photo: require('./photos/1561626514-heat-weather-advisory-0.jpg'),
                type: 'LOCAL-WEATHER',
                title: 'Heat advisory issued for four districts',
                price: 72,
                priceType: 'per night',
                stars: 101,
            },
            {
                id: 8,
                photo: require('./photos/2workers.jpg'),
                type: 'LOCAL',
                title: '2 Workers dead, 2 injured after boundry wall collapses',
                price: 69,
                priceType: 'per night',
                stars: 119,
            },
            {
                id: 9,
                photo: require('./photos/b5a62fa92f962faf54bd704b397842eb_S.jpg'),
                type: 'LOCAL',
                title: 'Sri Lankan Airlines\' Jumps on the Army\'s Environmental Bandwagon',
                price: 152,
                priceType: 'per night',
                stars: 320,
            },
            {
                id: 10,
                photo: require('./photos/00e2974680631f4f9bceb38588dc9763_S.jpg'),
                type: 'LOCAL',
                title: 'President briefs Muslim envoys on rapid normality in security situation',
                price: 116,
                priceType: 'per night',
                stars: 300,
            },
            {
                id: 11,
                photo: require('./photos/ed4b166fb36e2c27e16d3f79160bb2ac_S.jpg'),
                type: 'LOCAL-CINEMA',
                title: 'Lookalikes of Idi Amin, Mandela & Obama sought in SL',
                price: 182,
                priceType: 'per night',
                stars: 132,
            }
        ]
    },
    {
        title: 'SPORTS',        //general
        boldTitle: true,
        showAddToFav: false,
        listings: [
            {
                id: 12,
                photo: require('./photos/ckt-kUyC--621x414@LiveMint.jpg'),
                type: 'SPORTS',
                title: 'India won by 125 runs',
                price: '30',
                priceType: 'per person',
                stars: 0,
            },
            {
                id: 13,
                photo: require('./photos/D-FNJsIXoAAWPfw.jpg'),
                type: 'SPORTS',
                title: 'Cottrell whacks chahal for 4 and a 6',
                price: '30',
                priceType: 'per person',
                stars: 0,
            },
            {
                id: 14,
                photo: require('./photos/f54b49233300553237717fa9d725b92d_S.jpg'),
                type: 'SPORTS',
                title: 'We know South Africa\'s game - Hathurusinghe',
                price: '34',
                priceType: 'per person',
                stars: 0,
            },
            {
                id: 15,
                photo: require('./photos/_107559013_kovacic_reuters.jpg'),
                type: 'SPORTS',
                title: 'Mateo Kovacic: Chelsea set to sign on-loan Real Madrid midfielder',
                price: '34',
                priceType: 'per person',
                stars: 0,
            },
            {
                id: 16,
                photo: require('./photos/_107570121_hi054935367.jpg'),
                type: 'SPORTS',
                title: 'England reached their second consecutive Women\'s World Cup semi-final as they produced an excellent performance to beat Norway in Le Havre.',
                price: '46',
                priceType: 'per person',
                stars: 0,
            }
        ]
    }
];

export default listings;
