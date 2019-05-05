NUMBER_OF_SAMPLES = 8
WITH_POWER = false

def assessmentOfAdaptation (x)
    return 2*(x**2+1)
end

def re_assessmentOfAdaptation (x)
    return Math.sqrt(x/2-1).to_i()
end

def generateFirstPopulation (p)
    for i in 0..7
        p[i] = rand(1..127)
    end
end

public def to_bin(width = 1)
    '%0*b' % [width, self]
end     

def rouletteWheel (av, ng)
    roulette = Array.new(8)
    roulette_percents = Array.new(8)
    if WITH_POWER
        for i in 0..7
            roulette[i] = av[i]**2
        end
    else
        roulette = av
        #for i in 0..7
        #    roulette[i] = av[i]
        #end
    end
    sum = roulette.inject(0, &:+)
    for i in 0..7
        roulette_percents[i] = (roulette[i].to_f()/sum*100).round(2)
    end
    roulette_percents = roulette_percents.sort()
    av = av.sort()
    min_v = roulette_percents[0]
    max_v = roulette_percents[7]
    for i in 0..7
        los = rand(0..100).round(2)
        #p "Test losowania nr: #{i} z wartoscia -> #{los}"
        case los
        when 0..min_v then
            ng[i] = av[0]
        when (roulette_percents[0]+0.01)..roulette_percents[1] then
            ng[i] = av[1]
        when (roulette_percents[1]+0.01)..roulette_percents[2] then
            ng[i] = av[2]
        when (roulette_percents[2]+0.01)..roulette_percents[3] then
            ng[i] = av[3]
        when (roulette_percents[3]+0.01)..roulette_percents[4] then
            ng[i] = av[4]
        when (roulette_percents[4]+0.01)..roulette_percents[5] then
            ng[i] = av[5]
        when (roulette_percents[5]+0.01)..roulette_percents[6] then
            ng[i] = av[6]
        when (roulette_percents[6]+0.01)..100 then
            ng[i] = av[7]
        end
    end
end

def crossingChromosomes (chs)
    @retch = Array.new(8)
    @tmpch = Array.new(8)
    @tmpch = chs
    #locus = 4 #Test line.
    locus = rand(1..7) # This locus have the same value for each pair
    for k in 0..3
        @gp1 = rand(0..@tmpch.length()-1)
        loop do 
            @gp2 = rand(0..@tmpch.length()-1)
            if @gp1 != @gp2 
                break 
            end
        end
        #locus = rand(1..7) -> uncomment this for switching locus for each pair
        #p 'Temporary table with chromosomes tmpch: ' #Test line.
        #p @tmpch #Test line.
        #p 'First chromosome after modyfication by crossing : ' #Test line.
        pom = @tmpch[@gp1].slice(0..locus) + @tmpch[@gp2].slice(locus+1..15)
        #p 'Second chromosome after modyfication by crossing : ' #Test line.
        @retch[k] = @tmpch[@gp2].slice(0..locus) + @tmpch[@gp1].slice(locus+1..15)
        @retch[k+4] = pom 
        #p 'What is delete: ' #Test line.
        if @gp1>@gp2
            @tmpch.delete_at(@gp1)
            @tmpch.delete_at(@gp2)
        else
            @tmpch.delete_at(@gp2)
            @tmpch.delete_at(@gp1)
        end
    end
    return @retch
end

def mutatingGen (ch) 
    locus = rand(1..7)
    if ch[locus] == '1'
        ch[locus] = "0"
    else
        ch[locus] = "1"
    end
end

def isMutation ()
    if rand(1..100) <= 20   #The chance of mutation is set up to 20%
        return true
    else
        return false
    end
end

def Program ()
    population = Array.new(8)
    chromosomes = Array.new(8)
    adaptation_values = Array.new(8)
    next_generation = Array.new(8)
    generateFirstPopulation(population)
    for generations in 0..60
        puts "Generation number #{generations} \n"
        puts "Population: \n"
        p population
        for i in 0..7
            adaptation_values[i] = assessmentOfAdaptation(population[i])
        end
        puts "Assessment of adaptation of present population: \n"
        p adaptation_values
        rouletteWheel(adaptation_values,next_generation)
        puts "Next generation will be: \n"
        p next_generation
        for j in 0..7
            population[j] = re_assessmentOfAdaptation(next_generation[j])
            chromosomes[j] = population[j].to_bin(8)
        end
        puts "Population chromosomes: \n"
        p chromosomes
        chromosomes = crossingChromosomes(chromosomes)
        puts "Population chromosomes after crossing gens: \n"
        p chromosomes
        if isMutation()
            no = rand(0..chromosomes.length()-1)
            puts "One chromosome was mutated with result: \nFrom this: "
            p chromosomes[no]
            puts "To this: "
            mutatingGen(chromosomes[no])
            p chromosomes[no]
        end
    end
end

def test_crossing()
    #For test uncomment the lines in crossingChromosomes() ended with "Test line."
    test_chromosomes = Array.new(8)
    test_chromosomes = ["1011111111111101", "1111111111111110","1111111111111100", "1111111111111111","0000000000000000", "0000000000000000","0000000000000000", "0000000000000000"]
    mod_ar = Array.new(8)
    mod_ar = test_chromosomes
    puts '=======================Test  for crossing======================='
    p "This is test array of chromosomes: #{test_chromosomes}"
    p "Starting method for crossing. \n ======================================="
    test_chromosomes = crossingChromosomes(test_chromosomes)
    puts "======================================= \n Tables after crossing."
    p 'Materials:'
    p mod_ar
    p 'Results:'
    p test_chromosomes
end

Program()