2026-01-14 Version: 2.13.4
- Update API GetEssayCorrectionTask: add response parameters Body.data.totalUsage.
- Update API GetEssayCorrectionTask: add response parameters Body.data.results.$.usage.


2026-01-07 Version: 2.13.3
- Update API SubmitEssayCorrectionTask: add request parameters tasks.$.customId.


2025-12-16 Version: 2.13.2
- Update API GetVideoAnalysisTask: add response parameters Body.data.payload.output.addDatasetDocumentsResult.
- Update API GetVideoAnalysisTask: add response parameters Body.data.payload.output.videoCalculatorResult.
- Update API GetVideoAnalysisTask: add response parameters Body.data.payload.output.videoAnalysisResult.usage.imageTokens.
- Update API RunVideoAnalysis: add request parameters addDocumentParam.
- Update API RunVideoAnalysis: add response parameters Body.payload.output.addDatasetDocumentsResult.
- Update API RunVideoAnalysis: add response parameters Body.payload.output.videoCalculatorResult.
- Update API RunVideoAnalysis: add response parameters Body.payload.output.videoAnalysisResult.usage.imageTokens.
- Update API SubmitVideoAnalysisTask: add request parameters addDocumentParam.


2025-10-21 Version: 2.13.1
- Generated python 2024-08-01 for QuanMiaoLightApp.

2025-10-21 Version: 2.13.0
- Support API GetVideoDetectShotConfig.
- Support API GetVideoDetectShotTask.
- Support API RunVideoDetectShot.
- Support API SubmitVideoDetectShotTask.
- Support API UpdateVideoDetectShotConfig.
- Support API UpdateVideoDetectShotTask.


2025-10-17 Version: 2.12.1
- Update API RunVideoAnalysis: add request parameters splitType.
- Update API SubmitVideoAnalysisTask: add request parameters splitType.


2025-09-30 Version: 2.12.0
- Support API UpdateVideoAnalysisTasks.


2025-09-03 Version: 2.11.1
- Generated python 2024-08-01 for QuanMiaoLightApp.

2025-08-23 Version: 2.11.0
- Support API GetFileContent.


2025-08-01 Version: 2.10.3
- Generated python 2024-08-01 for QuanMiaoLightApp.

2025-07-29 Version: 2.10.2
- Update API GetVideoAnalysisTask: add response parameters Body.data.payload.output.videoRoleRecognitionResult.
- Update API RunVideoAnalysis: add request parameters autoRoleRecognitionVideoUrl.
- Update API RunVideoAnalysis: add request parameters videoRoles.$.isAutoRecognition.
- Update API RunVideoAnalysis: add request parameters videoRoles.$.timeIntervals.
- Update API RunVideoAnalysis: add response parameters Body.payload.output.videoRoleRecognitionResult.
- Update API SubmitVideoAnalysisTask: add request parameters autoRoleRecognitionVideoUrl.
- Update API SubmitVideoAnalysisTask: add request parameters videoRoles.$.isAutoRecognition.
- Update API SubmitVideoAnalysisTask: add request parameters videoRoles.$.timeIntervals.


2025-07-29 Version: 2.10.1
- Generated python 2024-08-01 for QuanMiaoLightApp.

2025-07-02 Version: 2.10.0
- Support API GetEssayCorrectionTask.
- Support API RunEssayCorrection.
- Support API RunOcrParse.
- Support API SubmitEssayCorrectionTask.


2025-05-30 Version: 2.9.3
- Update API RunMarketingInformationWriting: add response parameters Body.payload.output.reasonContent.


2025-05-29 Version: 2.9.2
- Update API RunHotTopicChat: add response parameters Body.payload.output.category.
- Update API RunHotTopicChat: add response parameters Body.payload.output.keyword.
- Update API RunHotTopicChat: add response parameters Body.payload.output.location.
- Update API RunHotTopicChat: add response parameters Body.payload.output.hotTopicSummaries.$.pubTime.
- Update API RunHotTopicChat: add response parameters Body.payload.output.hotTopicSummaries.$.url.


2025-05-27 Version: 2.9.1
- Update API ListAnalysisTagDetailByTaskId: add response parameters Body.data.$.sourceList.
- Update API RunEnterpriseVocAnalysis: add request parameters sourceTrace.
- Update API RunEnterpriseVocAnalysis: add response parameters Body.payload.output.reasonContent.
- Update API SubmitEnterpriseVocAnalysisTask: add request parameters sourceTrace.


2025-05-22 Version: 2.9.0
- Support API HotNewsRecommend.


2025-05-20 Version: 2.8.1
- Update API RunVideoAnalysis: add request parameters videoCaptionInfo.videoCaptionFileUrl.
- Update API SubmitVideoAnalysisTask: add request parameters videoCaptionInfo.videoCaptionFileUrl.


2025-05-15 Version: 2.8.0
- Support API ListAnalysisTagDetailByTaskId.
- Support API UpdateVideoAnalysisTask.
- Update API GetVideoAnalysisTask: add response parameters Body.data.payload.output.videoCaptionResult.videoCaptions.$.speaker.
- Update API RunVideoAnalysis: add request parameters videoCaptionInfo.
- Update API RunVideoAnalysis: add response parameters Body.payload.output.videoCaptionResult.videoCaptions.$.speaker.
- Update API SubmitVideoAnalysisTask: add request parameters videoCaptionInfo.


2025-04-29 Version: 2.7.2
- Generated python 2024-08-01 for QuanMiaoLightApp.

2025-04-17 Version: 2.7.1
- Update API RunEnterpriseVocAnalysis: add request parameters akProxy.
- Update API RunEnterpriseVocAnalysis: add request parameters apiKey.
- Update API RunMarketingInformationWriting: add request parameters apiKey.
- Update API RunMarketingInformationWriting: add response parameters Body.header.errorMessage.
- Update API RunNetworkContentAudit: add request parameters apiKey.
- Update API SubmitEnterpriseVocAnalysisTask: add request parameters apiKey.


2025-04-16 Version: 2.7.0
- Support API CancelAsyncTask.
- Support API ExportAnalysisTagDetailByTaskId.
- Support API GetEnterpriseVocAnalysisTask.
- Support API RunEnterpriseVocAnalysis.
- Support API SubmitEnterpriseVocAnalysisTask.


2025-04-10 Version: 2.6.5
- Update API RunTagMiningAnalysis: add request parameters apiKey.
- Update API SubmitTagMiningAnalysisTask: add request parameters apiKey.


2025-03-27 Version: 2.6.4
- Update API RunVideoAnalysis: add request parameters excludeGenerateOptions.
- Update API SubmitVideoAnalysisTask: add request parameters deduplicationId.
- Update API SubmitVideoAnalysisTask: add request parameters excludeGenerateOptions.


2025-03-18 Version: 2.6.3
- Update API RunVideoAnalysis: add param splitInterval.
- Update API SubmitVideoAnalysisTask: add param splitInterval.


2025-03-17 Version: 2.6.2
- Update API RunHotTopicSummary: update param stepForCustomSummaryStyleConfig.


2025-03-13 Version: 2.6.1
- Update API GetVideoAnalysisTask: update response param.
- Update API RunVideoAnalysis: add param faceIdentitySimilarityMinScore.
- Update API RunVideoAnalysis: add param textProcessTasks.
- Update API RunVideoAnalysis: add param videoShotFaceIdentityCount.
- Update API RunVideoAnalysis: update response param.
- Update API SubmitVideoAnalysisTask: add param faceIdentitySimilarityMinScore.
- Update API SubmitVideoAnalysisTask: add param textProcessTasks.
- Update API SubmitVideoAnalysisTask: add param videoShotFaceIdentityCount.


2025-03-10 Version: 2.6.0
- Support API GetTagMiningAnalysisTask.
- Support API SubmitTagMiningAnalysisTask.


2025-01-23 Version: 2.5.1
- Update API RunStyleWriting: add param processStage.
- Update API RunStyleWriting: add param useSearch.
- Update API RunStyleWriting: update param learningSamples.
- Update API RunStyleWriting: update param referenceMaterials.
- Update API RunStyleWriting: update param writingTheme.


2025-01-17 Version: 2.5.0
- Support API RunNetworkContentAudit.
- Support API RunScriptChat.
- Support API RunScriptRefine.
- Update API GetVideoAnalysisTask: update response param.
- Update API RunVideoAnalysis: update response param.


2025-01-16 Version: 2.4.0
- Support API RunScriptChat.
- Support API RunScriptRefine.
- Update API GetVideoAnalysisTask: update response param.
- Update API RunVideoAnalysis: update response param.


2025-01-15 Version: 2.3.0
- Support API RunScriptChat.
- Support API RunScriptRefine.
- Update API GetVideoAnalysisTask: update response param.
- Update API RunVideoAnalysis: update response param.


2025-01-14 Version: 2.2.0
- Support API GetVideoAnalysisConfig.
- Support API GetVideoAnalysisTask.
- Support API SubmitVideoAnalysisTask.
- Support API UpdateVideoAnalysisConfig.
- Update API RunVideoAnalysis: add param frameSampleMethod.
- Update API RunVideoAnalysis: add param language.
- Update API RunVideoAnalysis: add param videoRoles.
- Update API RunVideoAnalysis: update response param.


2024-12-26 Version: 2.1.0
- Support API GenerateOutputFormat.
- Support API RunTagMiningAnalysis.


2024-12-11 Version: 2.0.1
- Update API RunHotTopicChat: add param messages.


2024-12-05 Version: 2.0.0
- Delete API RunCommentGeneration.
- Update API RunHotTopicChat: update response param.


2024-11-06 Version: 1.4.1
- Update API RunMarketingInformationWriting: add param customLimitation.
- Update API RunMarketingInformationWriting: add param inputExample.
- Update API RunMarketingInformationWriting: add param outputExample.


2024-11-01 Version: 1.4.0
- Support API RunHotTopicChat.
- Support API RunHotTopicSummary.


2024-09-26 Version: 1.3.0
- Support API GenerateBroadcastNews.
- Support API RunCommentGeneration.
- Update API RunVideoAnalysis: add param snapshotInterval.
- Update API RunVideoAnalysis: add param videoExtraInfo.


2024-09-14 Version: 1.2.0
- Support API ListHotTopicSummaries.
- Update API RunVideoAnalysis: update response param.


2024-09-14 Version: 1.1.0
- Support API ListHotTopicSummaries.
- Update API RunVideoAnalysis: update response param.


2024-09-05 Version: 1.0.0
- Generated python 2024-08-01 for QuanMiaoLightApp.

