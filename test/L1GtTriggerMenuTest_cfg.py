# cfg file to test L1 GT trigger menu

import FWCore.ParameterSet.Config as cms

process = cms.Process("L1GtTriggerMenuTest")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")

#process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1x1032.L1Menu2007_cff")
#process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1030.L1Menu2008_2E30_cff")
#process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu2008_2E31_cff")
process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1x1032.L1MenuTestCondCorrelation_cff")

process.l1GtTriggerMenuTest = cms.EDAnalyzer("L1GtTriggerMenuTester")

process.p = cms.Path(process.l1GtTriggerMenuTest)


# Message Logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.debugModules = ['l1GtTriggerMenuTest']
process.MessageLogger.cout = cms.untracked.PSet(
    INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1)
    ),
    threshold = cms.untracked.string('DEBUG'), ## DEBUG 

    DEBUG = cms.untracked.PSet( ## DEBUG, all messages  

        limit = cms.untracked.int32(-1)
    )
)

