# cfg file to test L1 GT trigger menu

import FWCore.ParameterSet.Config as cms

# choose one (and only one) of the following source
l1MenuSource='sqlFile'
#l1MenuSource='xmlFile'
#l1MenuSource='globalTag'


if l1MenuSource == 'sqlFile' :
    # the menu will be read from the SQL file instead of the global tag
    #useSqlFile = '/afs/cern.ch/user/g/ghete/public/L1Menu/sqlFile/L1Menu_Commissioning2010_v2_mc.db'
    #menuDbTag = 'L1GtTriggerMenu_L1Menu_Commissioning2010_v2_mc'
    useSqlFile = '/afs/cern.ch/user/g/ghete/public/L1Menu/sqlFile/L1Menu_MC2010_v0_mc.db'
    menuDbTag = 'L1GtTriggerMenu_L1Menu_MC2010_v0_mc'
elif l1MenuSource == 'xmlFile' :
    # explicit choice of the L1 menu
    # un-comment the corresponding menu in the list of the menus
    print '   Using an xml file to overwrite the L1 menu from the global tag'    

else :
    print '   Using default L1 trigger menu from Global Tag ', useGlobalTag    
    
     
# choose a valid global tag for the release you are using 
# for the option "l1MenuSource='globalTag'", the menu from global tag will be printed  
#
# 3_6_X gTags
#useGlobalTag = 'MC_36Y_V4'
#useGlobalTag='START36_V4'

# 3_5_X gTags
#useGlobalTag='MC_3XY_V26'
useGlobalTag='START3X_V26'

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

if l1MenuSource == 'xmlFile' :
    process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMenuConfig_cff')
    process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')
    
    #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1x1032.L1Menu2007_cff")
    process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1x1032.L1Menu_Test_cff")

    #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu2008_2E31_cff")
    #
    #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v0_L1T_Scales_20080922_Imp0_Unprescaled_cff")
    #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v1_L1T_Scales_20080922_Imp0_Unprescaled_cff")
    #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v2_L1T_Scales_20080922_Imp0_Unprescaled_cff")
    #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v2_L1T_Scales_20090519_Imp0_Unprescaled_cff")
    #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v2_L1T_Scales_20090624_Imp0_Unprescaled_cff")
    #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v4_L1T_Scales_20090624_Imp0_Unprescaled_cff")

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
    #process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_Commissioning2009_v5_L1T_Scales_20080926_startup_Imp0_Unprescaled_cff")

elif l1MenuSource == 'sqlFile' :
    if useSqlFile != '' :
        print '   Retrieve L1 trigger menu only from SQLlite file ' 
        print '       ', useSqlFile   
        print '       '

        from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
        process.l1conddb = cms.ESSource("PoolDBESSource",
                                CondDBSetup,
                                connect = cms.string('sqlite_file:' + useSqlFile),
                                toGet = cms.VPSet(cms.PSet(
                                            record = cms.string('L1GtTriggerMenuRcd'),
                                            tag = cms.string(menuDbTag))),
                                            BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService')
                                            )
        process.es_prefer_l1conddb = cms.ESPrefer("PoolDBESSource","l1conddb")
       
    else :
        print '   Error: no SQL file is given; please provide a valid SQL file for option sqlFile'    

else :
    print '   Printing default L1 trigger menu from Global Tag ', useGlobalTag    



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
    threshold = cms.untracked.string('ERROR'), ## DEBUG 
    
    ERROR = cms.untracked.PSet( ## DEBUG, all messages  

        limit = cms.untracked.int32(-1)
    )
)


