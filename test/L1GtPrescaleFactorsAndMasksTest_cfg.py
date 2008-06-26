# cfg file to test L1 GT prescale factors and trigger mask

import FWCore.ParameterSet.Config as cms

process = cms.Process("L1GtPrescaleFactorsAndMasksTest")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.load("L1TriggerConfig.L1GtConfigProducers.L1GtPrescaleFactorsAlgoTrigConfig_cff")
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtPrescaleFactorsTechTrigConfig_cff")
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskAlgoTrigConfig_cff")
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff")
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskVetoAlgoTrigConfig_cff")
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskVetoTechTrigConfig_cff")

process.l1GtPrescaleFactorsAndMasksTest = cms.EDFilter("L1GtPrescaleFactorsAndMasksTester")

process.p = cms.Path(process.l1GtPrescaleFactorsAndMasksTest)

