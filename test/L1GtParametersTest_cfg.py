# The following comments couldn't be translated into the new config version:

# cfg file to test L1 GT parameters

import FWCore.ParameterSet.Config as cms

# process
process = cms.Process("L1GtParametersTest")
process.l1GtParametersTest = cms.EDAnalyzer("L1GtParametersTester")

# number of events and source
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.source = cms.Source("EmptySource")

# configuration
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtParametersConfig_cff")


# path to be run
process.p = cms.Path(process.l1GtParametersTest)

