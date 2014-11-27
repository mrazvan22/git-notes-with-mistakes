speed :: [Double] -> Int -> Double
speed xvs n = (xvs !! n) - (sum ( map ( (-) (xvs !! n)) xvs )) * 0.125/fromIntegral(length(xvs))
