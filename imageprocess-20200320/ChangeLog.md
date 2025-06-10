2025-06-10 Version: 2.3.0
- Support API GenerateReport.
- Delete API ClassifyFNF.
- Delete API DetectHipKeypointXRay.
- Delete API DetectKneeKeypointXRay.
- Delete API DetectKneeXRay.
- Delete API DetectSpineMRI.
- Delete API TranslateMed.
- Update API DetectLiverSteatosis: add response parameters Body.Data.ResultUrl.
- Update API DetectLiverSteatosis: add response parameters Body.Data.Detections.$.FatFract.
- Update API DetectLiverSteatosis: add response parameters Body.Data.Detections.$.MaossScore.
- Update API PredictCVD: add response parameters Body.Data.Lesion.ImagesURL.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.AortaMaxDiam.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.AortaMaxDiamStd.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.AorticHeightIndex.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.AorticTortuosityIndex.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.ChestWidth.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.HeartLongDiam.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.HeartShortDiam.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.HeartWidth.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.LeftLungHighattRatio.
- Update API PredictCVD: add response parameters Body.Data.Lesion.FeatureScore.RightLungHighattRatio.
- Update API ScreenChestCT: add response parameters Body.Data.DetectAD.
- Update API ScreenChestCT: add response parameters Body.Data.MuscleFat.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenBC.
- Update API ScreenChestCT: add response parameters Body.Data.DetectLiverSteatosis.ResultUrl.
- Update API ScreenChestCT: add response parameters Body.Data.DetectLiverSteatosis.Detections.$.FatFract.
- Update API ScreenChestCT: add response parameters Body.Data.DetectLiverSteatosis.Detections.$.MaossScore.
- Update API ScreenChestCT: add response parameters Body.Data.DetectPdac.Lesion.LesionList.
- Update API ScreenChestCT: add response parameters Body.Data.DetectPdac.Lesion.OrganList.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.ImagesURL.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.AortaMaxDiam.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.AortaMaxDiamStd.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.AorticHeightIndex.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.AorticTortuosityIndex.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.ChestWidth.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.CoronaryCalciumScore.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.HeartLongDiam.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.HeartShortDiam.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.HeartWidth.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.LeftLungHighattRatio.
- Update API ScreenChestCT: add response parameters Body.Data.PredictCVD.Lesion.FeatureScore.RightLungHighattRatio.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenCRC.Lesion.LesionList.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenCRC.Lesion.OrganList.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenEc.Lesion.EgjVolume.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenEc.Lesion.LesionList.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenEc.Lesion.OrganList.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenGC.Lesion.LesionList.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenGC.Lesion.OrganList.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenLC.Lesion.PatientLevelProb.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenLC.Lesion.LesionList.$.ScoreAllClasses.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenLC.Lesion.PatientLevelResult.BenignProb.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenLC.Lesion.PatientLevelResult.CalcProb.
- Update API ScreenChestCT: add response parameters Body.Data.ScreenLC.Lesion.PatientLevelResult.MalignantProb.
- Update API ScreenLC: add response parameters Body.Data.Lesion.PatientLevelProb.
- Update API ScreenLC: add response parameters Body.Data.Lesion.LesionList.$.ScoreAllClassesProb.
- Update API ScreenLC: add response parameters Body.Data.Lesion.PatientLevelResult.BenignProb.
- Update API ScreenLC: add response parameters Body.Data.Lesion.PatientLevelResult.CalcProb.
- Update API ScreenLC: add response parameters Body.Data.Lesion.PatientLevelResult.MalignantProb.
- Update API SegmentOAR: add response parameters Body.Data.MaskList.


2023-12-15 Version: 2.2.0
- Generated python 2020-03-20 for imageprocess.

2023-09-04 Version: 2.1.0
- Generated python 2020-03-20 for imageprocess.

2023-05-31 Version: 2.0.29
- Release ScreenGC.
- Release ScreenLC.
- Release PredictCVD.
- Release ScreenCRC.
- Update  ScreenChestCT.

2023-04-27 Version: 2.0.28
- Release ChestCT.

2023-04-03 Version: 2.0.27
- Release CalcBMD.

2023-03-28 Version: 2.0.26
- Release SegmentLymphNode.

2023-02-14 Version: 2.0.25
- Update ScreenChestCT and DetectLungNodule.

2023-02-08 Version: 2.0.24
- Generated python 2020-03-20 for imageprocess.

2023-02-02 Version: 2.0.23
- Release TargetVolumeSegment.

2022-12-14 Version: 2.0.22
- Release ScreenEC.

2022-11-04 Version: 2.0.21
- Release ScreenEC.

2022-10-17 Version: 2.0.20
- Release ScreenEC.

2022-09-22 Version: 2.0.19
- Release ScreenEC.

2022-08-24 Version: 2.0.18
- Update  ScreenChestCT.

2022-07-25 Version: 2.0.17
- Update  SegmentOAR.

2022-07-22 Version: 2.0.16
- Update ScreenChestCT  Release SegmentOAR.

2022-06-24 Version: 2.0.15
- Update ScreenChestCT.

2022-06-20 Version: 2.0.14
- Update ScreenChestCT CalcCACS.

2022-06-13 Version: 2.0.13
- Update ScreenChestCT.

2022-06-09 Version: 2.0.12
- Update ScreenChestCT.

2022-05-27 Version: 2.0.11
- Release DetectLymph DetectPanc.

2022-04-08 Version: 2.0.10
- Release FeedbackSession.

2022-04-08 Version: 2.0.9
- Release FeedbackSession.

2022-04-06 Version: 2.0.8
- Release FeedbackSession.

2021-07-19 Version: 2.0.7
- Update ScreenChestCT.

2021-07-02 Version: 2.0.6
- Release AnalyzeChestVessel.

2021-05-14 Version: 2.0.5
- Update ScreenChestCT.

2021-04-17 Version: 2.0.4
- Update RunMedQA.

2021-04-06 Version: 2.0.3
- Update ScreenChestCT DetectRibFracture.

2021-03-31 Version: 2.0.2
- Generated python 2020-03-20 for imageprocess.

2021-03-03 Version: 2.0.1
- Update ScreenChestCT.

2021-01-06 Version: 2.0.0
- Update DetectLungNodule.

2020-12-22 Version: 1.0.10
- Release DetectRibFracture.

2020-12-03 Version: 1.0.9
- Update DetectLungNodule.

2020-10-23 Version: 1.0.8
- Update DetectLungNodule.

2020-10-23 Version: 1.0.7
- Update DetectLungNodule.

2020-10-13 Version: 1.0.6
- Release DetectSkinDisease.

2020-09-29 Version: 1.0.5
- Update CalcCACS.

2020-09-18 Version: 1.0.4
- Update DetectLungNodule, DetectSpineMRI, DetectKneeXRay, DetectCovid19Cad.

2020-09-09 Version: 1.0.3
- Release DetectKneeKeypointXRay, DetectHipKeypointXRay, CalcCACS, RunCTRegistration, ClassifyFNF.

