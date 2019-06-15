NUMBER_OF_DATA_FOR_LEARNING = 10
FUNCTION_COEFFICIENTS_A = 1 
FUNCTION_COEFFICIENTS_B = 1

class Perceptron

    def initialize(data)
        @@data = data
        @@result = Array.new(NUMBER_OF_DATA_FOR_LEARNING)
        @@w1 = rand(0.0..1.0)
        @@w2 = 1 - @@w1
        @@e = 0
        @@limit = 5
        p @@data
    end

    class << self
        attr_accessor :w1
    end

    def w1
        @@w1
    end

    def w2
        @@w2
    end

    def result
        @@result
    end

    def startLearning(targets)
        for i in 0..NUMBER_OF_DATA_FOR_LEARNING-1
            @@result[i] = analyse(@@data[i][0],@@data[i][1],targets[i],0)
        end
    end

    def analyse(x, y, t, b = 0)
        a = @@w1*x + @@w1*y + b
        if a > 0
            r = 1
        else
            r = 0
        end
        @@e = t - r
        if @@e!=0 && @@limit>0 
            @@w1 = @@w1 + @@e * x
            @@w2 = @@w2 + @@e * y 
            @@limit -= 1
            analyse(x, y, t, 0)
        else  
            @@limit = 5
            return r
        end
    end
end

def initLearningData()
    for i in 0..NUMBER_OF_DATA_FOR_LEARNING-1
        @dl[i][0] = rand(-10.0..10.0)
        @dl[i][1] = rand(-10.0..10.0)
    end
end

def initTargets()
    for i in 0..NUMBER_OF_DATA_FOR_LEARNING-1
        @target[i] = FUNCTION_COEFFICIENTS_A * @dl[i][0] + FUNCTION_COEFFICIENTS_B * @dl[i][1]
    end
end

def Program()
    @dl = Array.new(NUMBER_OF_DATA_FOR_LEARNING) {Array.new(2,)} #dl -> data for learnings
    @target = Array.new(NUMBER_OF_DATA_FOR_LEARNING)

        
    initLearningData()
    initTargets()

    perceptron = Perceptron.new(@dl)
    perceptron.startLearning(@target)
    p perceptron.w1
    p perceptron.w2
    p perceptron.result
end

Program()