class Ankara{
    constructor(temperator,mood){
        this.mood=mood
        this.temperator=temperator
    }
    getPattern(){
        if(this.temperator>=20 &&this.mood>=5){
            return "wear bright color and light ankara"
        }
        else{
            return "wear dull color and heavy ankara"
        }
    }
}

let ankara=new Ankara(32,6)
let ankaras=new Ankara(19,3)
console.log(ankara.getPattern());
console.log(ankaras.getPattern());

class Migration{
    constructor(weather_patterns,river_levels,predator_location,locations,species){
this.weather_patterns=weather_patterns
this.river_levels=river_levels
this.predator_location=predator_location
this.locations=locations
this.species=species
    }
    movement(){
        if(this.weather_patterns==="rainy" && this.river_levels==="high" && this.locations==="Mara" && this.species==="wildbeast"){
            return "wildbeast will move stay in Mara"
        }
        else{
            return "wildbeast will move to another location"
        }
           
    }

}
let migration=new Migration("rainy","high","Mara","wildbeast")
console.log(migration.movement());
let migrations=new Migration("dry","low","Mara","wildbeast")
console.log(migrations.movement());

class Nollywood{
    constructor(nameFilm,cast,schedule,locations,budjet){
        this.nameFilm=nameFilm
        this.cast=cast
        this.schedule=schedule
        this.budjet=budjet
        this.locations=locations
    }
    planMovie(){
        return `${this.nameFilm} will have the following cast ${this.cast} and will be shoot at ${this.schedule} at ${this.locations} giving it a budjet of ${this.budjet}`
    }
}
let nollywood=new Nollywood("Cinderella",["John Doe","Mary Sinachi","Mercy Mbone"],("24-05-2023","10.00AM to 12.00AM"),"Abuja","$10000")
console.log(nollywood.planMovie());

class Baobab{
    constructor(name_fruit,power_fruit,effect_fruit,season){
        this.name_fruit=name_fruit
        this.power_fruit=power_fruit
        this.effect_fruit=effect_fruit
        this.season=season
    }
}
let empty_fruit=[]
let baobab=new Baobab("baobab","strong","good","wet")
let baobabs=new Baobab("baobab1","strong","good","dry")
empty_fruit.push(baobab)
console.log(baobab);

class Season{
    constructor(season){
        this.season=season
    }
    predictFruit(){
let fruit=empty_fruit.filter(item=>item.season ===this.season)
return fruit
    }
}
let season1=new Season("wet")
let season2=new Season("dry")
console.log(season1.predictFruit());

