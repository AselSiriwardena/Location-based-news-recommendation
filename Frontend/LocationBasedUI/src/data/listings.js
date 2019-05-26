const listings = [
    {
        title: 'Mostly Viewed',     //expirience or something
        boldTitle: false,
        showAddToFav: true,
        listings: [
            {
                id: 1,
                photo: require('./photos/terrorism.jpg'),
                type: 'POLITICS - COLOMBO',
                title: 'Factors that lead to Terrorism Must be resolved immediately',
                price: 20,
                priceType: 'per person',
                stars: 29,
            },
            {
                id: 2,
                photo: require('./photos/vavniya.jpg'),
                type: 'TERRORIST - VAVUNIYA',
                title: '36 Pakisthani deportees escorted to community centre in Vavuniya',
                price: 19,
                priceType: 'per person',
                stars: 4,
            },
            {
                id: 3,
                photo: require('./photos/worldCp.jpg'),
                type: 'SPORTS - SRI LANKA',
                title: 'Sri Lanka looks to regroup ahead of World Cup',
                price: 19,
                priceType: 'per person',
                stars: 30,
            },
            {
                id: 4,
                photo: require('./photos/heros.jpg'),
                type: 'LOCAL - SRI LANKA',
                title: 'The nation honours its fallen heroes',
                price: 57,
                priceType: 'per person',
                stars: 70,
            },
            {
                id: 5,
                photo: require('./photos/antiAir.jpg'),
                type: 'TERRORIST-VAVUNIYA',
                title: 'Anti air craft Bullets found in Vavuniya',
                price: 61,
                priceType: 'per person',
                stars: 66,
            },
            {
                id: 6,
                photo: require('./photos/listing6.png'),
                type: 'LOCAL - KALUTHARA',
                title: 'Water Cuts for several areas',
                price: 55,
                priceType: 'per person',
                stars: 15,
            }
        ]
    },
    {
        title: 'Politics',
        boldTitle: false,
        showAddToFav: true,
        listings: [
            {
                id: 7,
                photo: require('./photos/1557240733-Relief-package-to-strengthen-tourism-industry-affected-by-Easter-attacks-approved-1.jpg'),
                type: 'POLITICS',
                title: 'Relief package to strengthen tourism industry affected by Easter attacks approved',
                price: 72,
                priceType: 'per night',
                stars: 101,
            },
            {
                id: 8,
                photo: require('./photos/1557249907-President-requests-foreign-envoys-to-lift-travel-restrictions-to-Sri-Lanka-1.jpg'),
                type: 'POLITICS',
                title: 'President requests foreign envoys to lift travel restrictions to Sri Lanka',
                price: 69,
                priceType: 'per night',
                stars: 119,
            },
            {
                id: 9,
                photo: require('./photos/1557291836-National-Vesak-Festival-restricted-to-2-days-A.jpg'),
                type: 'POLITICS',
                title: 'National Vesak Festival restricted to 2 days',
                price: 152,
                priceType: 'per night',
                stars: 320,
            },
            {
                id: 10,
                photo: require('./photos/1558225286-Gotabaya-Rajapaksa-confirms-presidential-run-report-1.jpg'),
                type: 'POLITICS',
                title: 'Gotabaya Rajapaksa confirms presidential run report 1',
                price: 116,
                priceType: 'per night',
                stars: 300,
            },
            {
                id: 11,
                photo: require('./photos/1558257272-Send-children-to-schools-without-fear-Mahinda-1.jpg'),
                type: 'POLITICS',
                title: 'Send children to schools without fear Mahinda',
                price: 182,
                priceType: 'per night',
                stars: 132,
            }
        ]
    },
    {
        title: 'LOCAl',        //general
        boldTitle: true,
        showAddToFav: false,
        listings: [
            {
                id: 12,
                photo: require('./photos/listing12.png'),
                type: 'RESERVATION',
                title: 'G\'raj Mahal',
                price: '30',
                priceType: 'per person',
                stars: 0,
            },
            {
                id: 13,
                photo: require('./photos/listing13.png'),
                type: 'RESERVATION',
                title: 'Le Fond',
                price: '30',
                priceType: 'per person',
                stars: 0,
            },
            {
                id: 14,
                photo: require('./photos/listing14.png'),
                type: 'RESERVATION',
                title: 'The Glass Onion',
                price: '34',
                priceType: 'per person',
                stars: 0,
            },
            {
                id: 15,
                photo: require('./photos/listing15.png'),
                type: 'RESERVATION',
                title: 'The Waiting Room',
                price: '34',
                priceType: 'per person',
                stars: 0,
            },
            {
                id: 16,
                photo: require('./photos/listing16.png'),
                type: 'RESERVATION',
                title: 'Bar Boulud',
                price: '46',
                priceType: 'per person',
                stars: 0,
            }
        ]
    }
];

export default listings;
