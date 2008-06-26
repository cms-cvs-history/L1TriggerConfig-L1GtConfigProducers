import FWCore.ParameterSet.Config as cms

from L1TriggerConfig.L1GtConfigProducers.l1GtPrescaleFactorsAlgoTrig_cfi import *
l1GtPrescaleFactorsAlgoTrig.PrescaleFactorsSet = cms.VPSet(cms.PSet(
    PrescaleFactors = cms.vint32(1000000, 1000000, 100000, 100000, 100000, 
        100000, 100000, 10000, 10000, 1000, 
        100, 1, 1, 1, 1, 
        10000, 1000, 100, 100, 1, 
        1, 1, 10000, 10000, 100, 
        1, 1, 1, 10000, 1000, 
        1000, 1, 1, 1000, 100, 
        1, 1, 1, 1, 10000, 
        1, 1, 1, 1, 4000, 
        2000, 1, 1, 1, 1, 
        1, 1, 1000, 100, 100, 
        1, 1, 1, 1, 20, 
        1, 1, 1, 1, 1, 
        20, 1, 1, 1, 1, 
        1, 20, 1, 1, 1, 
        1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 
        100, 1, 1, 1, 1, 
        1, 1, 1, 10000, 1, 
        1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 
        1, 1, 1, 5000, 1, 
        1, 1, 1, 1, 1, 
        1, 1, 1)
))

