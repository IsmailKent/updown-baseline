# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:55:48 2020

@author: Ismail
"""

import json

ID = int(input(("enter image id: ")))

classes = []
indomain = ("person, girl, boy, man, woman, kid, child, chef, baker, people, adult, rider, children, baby, worker, passenger, sister, biker, policeman,officer, lady, cowboy, bride, groom, male, female, guy, traveler, mother, father, gentleman, pitcher, player, skier, snowboarder,skater, skateboarder, foreigner, caller, offender, coworker, trespasser, patient, politician, soldier, grandchild, serviceman, walker,drinker, doctor, bicyclist, thief, buyer, teenager, student, camper, driver, solider, hunter, shopper, villager, cop, bicycle, bike, unicycle, minibike, trike, car, automobile, van, minivan, sedan, suv, hatchback, cab, jeep, coupe, taxicab, limo, taxi, motorcycle, scooter, motor bike, motor cycle, motorbike, moped, airplane, jetliner, plane, air plane, monoplane, aircraft, jet, airbus, biplane, seaplane bus, minibus, trolley, bus, minibus, schoolbus, trolley, train, locomotive, tramway, caboose, truck, pickup, lorry, hauler, firetruck, boat, ship, liner, sailboat, motorboat, dinghy, powerboat, speedboat, canoe, skiff, yacht, kayak, catamaran, pontoon, houseboat, vessel,rowboat, trawler, ferryboat, watercraft, tugboat, schooner, barge, ferry, sailboard, paddleboat, lifeboat, freighter, steamboat, riverboat,surfboard, battleship, steamship, traffic light, street light, traffic signal, stop light, streetlight, stoplight, fire hydrant, hydrant, stop sign, street sign, parking meter, bench, pew, cat, kitten, feline, tabby, dog, puppy, beagle, pup, chihuahua, schnauzer, dachshund, rottweiler, canine, pitbull, collie, pug, terrier, poodle, labrador, doggie,doberman, mutt, doggy, spaniel, bulldog, sheepdog, weimaraner, corgi, cocker, greyhound, retriever, brindle, hound, whippet, husky, horse, colt, pony, racehorse, stallion, equine, mare, foal, palomino, mustang, clydesdale, bronc, bronco, sheep, lamb, goat, ram, cattle, ewe, cow, cattle, oxen, ox, calf, ewe, holstein, heifer, buffalo, bull, zebu, bison, elephant, bear, panda, zebra, giraffe, backpack, knapsack, umbrella, handbag, handbag, wallet, purse, briefcase, tie, suitcase, suit case, luggage, frisbee, skis, ski, snowboard, sports ball, baseball, ball, football, soccer, basketball, softball, volleyball, pinball, fastball, racquetball, kite, baseball bat, baseball glove, skateboard, surfboard, longboard, skimboard, shortboard, wakeboard, tennis racket, bottle, wine glass, cup, fork, knife, pocketknife, knive, spoon, bowl, container, plate,banana, apple, sandwich, burger, sub, cheeseburger, hamburger, orange, lemons, broccoli, carrot, hot dog, pizza, donut, doughnut, bagel, cake, cheesecake, cupcake, shortcake, coffeecake, pancake, bird, ostrich, owl, seagull, goose, duck, parakeet, falcon, robin, pelican, waterfowl, heron, hummingbird, mallard, finch, pigeon, sparrow,seabird, osprey, blackbird, fowl, shorebird, woodpecker, egret, chickadee, quail, bluebird, kingfisher, buzzard, willet, gull, swan, bluejay,flamingo, cormorant, parrot, loon, gosling, waterbird, pheasant, rooster, sandpiper, crow, raven, turkey, oriole, cowbird, warbler, magpie,peacock, cockatiel, lorikeet, puffin, vulture, condor, macaw, peafowl, cockatoo, songbird,chair, seat, recliner, stool, couch, sofa, recliner, futon, loveseat, settee, chesterfield, potted plant, houseplant, bed, dining table, table, toilet, urinal, commode, lavatory, potty, tv, monitor, televison, television, laptop, computer, notebook, netbook, lenovo, macbook, mouse, remote, keyboard, cell phone, mobile phone, phone, cellphone, cellphone, telephone, phon, smartphone, iPhone, sink, refrigerator, fridge, refrigerator, fridge, freezer, refridgerator, frig, book, clock, vase, scissors, teddy bear, teddybear, hair drier, hairdryer, hair drier, hairdryer").split(",")
with open('nocaps_val_detections.json','r') as json_file, open('domain2.txt','r') as domain:
    data = json.load(json_file)
    #get list of all in domain objects
    domain_list = [line.strip() for line in indomain]
    ids = []
    
    # collect ids of all detected categories that are in domain
    for cat in data['categories']:
        if cat['name'] in domain_list:
            ids.append(cat['id'])
    d = {}
    for i in range(4500):
        d[i] = []
    # create dict of (image id, list of category ids in this images)
    for ann in data['annotations']:
        d[ann['image_id']].append(ann['category_id'])
        #get classes in this certain image
        if (ann['image_id']==ID):
            classes.append(ann['category_id'])
    #print(classes)
    
    #print the object names in this image
    for cat in data['categories']:
        if cat['id'] in classes:
            print(cat['name'])
    
    if (all(item in ids for item in d[ID])):
        print("in domain")
    elif (any(item in ids for item in d[ID])):
        print("near domain")
    else:
        print("out domain")
 	"""   
    for key, value in d.items():
        if (any(item in ids for item in value) and not all(item in ids for item in value)):
            print(key)
   		 """       
          
