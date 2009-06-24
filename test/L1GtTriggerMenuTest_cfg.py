# cfg file to test L1 GT trigger menu

import FWCore.ParameterSet.Config as cms
 
# choose one global tag to print the menu  
useGlobalTag = 'IDEAL_31X'
#useGlobalTag='STARTUP_31X'

# explicit choice of the L1 menu
#    default menu from Global Tag: put l1Menu = ''
#    otherwise, use 'myMenu' and un-comment the corresponding menu in the list of the menus

l1Menu = 'myMenu'

# process
process = cms.Process("L1GtTriggerMenuTest")
process.l1GtTriggerMenuTest = cms.EDAnalyzer("L1GtTriggerMenuTester")

# number of events and source
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

# load and configure modules via Global Tag
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions

process.load('Configuration.StandardSequences.Geometry_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.GlobalTag.globaltag = useGlobalTag+'::All'


# explicit choice of the L1 menu, overwriting the Global Tag menu

if l1Menu != '' :
    process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMenuConfig_cff')
    process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')
    
    if l1Menu == 'myMenu' :
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1x1032.L1Menu2007_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1x1032.L1Menu_Test_cff")

        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu2008_2E31_cff")
        #
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v0_L1T_Scales_20080922_Imp0_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v1_L1T_Scales_20080922_Imp0_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v2_L1T_Scales_20080922_Imp0_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v2_L1T_Scales_20090519_Imp0_Unprescaled_cff")
        process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v2_L1T_Scales_20090624_Imp0_Unprescaled_cff")

        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1030.L1Menu2008_2E30_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1030.L1Menu_2008MC_2E30_Unprescaled_cff")
        #
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1030.L1Menu_2008MC_2E30_v1_L1T_Scales_20080922_Imp0_Unprescaled_cff")

        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_startup_v3_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_startup_v4_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_startup_v5_Unprescaled_cff")
        #
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_startup2_v1_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_startup2_v2_Unprescaled_cff")
        #
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_startup2_v3_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_startup2_v4_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v0_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v1_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v2_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff")
        #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v3_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff")
    else :
        print 'No such L1 menu: ', l1Menu 
else :
    print '   Using default L1 trigger menu from Global Tag ', useGlobalTag    




# path to be run
process.p = cms.Path(process.l1GtTriggerMenuTest)

# services

# Message Logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.debugModules = ['l1GtTriggerMenuTest']
process.MessageLogger.cout = cms.untracked.PSet(
    #INFO = cms.untracked.PSet(
    #    limit = cms.untracked.int32(-1)
    #)#,
    threshold = cms.untracked.string('DEBUG'), ## DEBUG 
    
    DEBUG = cms.untracked.PSet( ## DEBUG, all messages  

        limit = cms.untracked.int32(-1)
    )
)


