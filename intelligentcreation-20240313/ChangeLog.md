2025-04-17 Version: 2.14.0
- Support API CreateProductImage.
- Support API GetAICoachAssessmentPoint.
- Support API QueryImageToVideoTask.
- Support API SendSdkStreamMessage.
- Support API SubmitImageToVideoTask.
- Update API CreateAnchor: add request parameters body.anchorCategory.
- Update API CreateAnchor: add request parameters body.videoOssKey.
- Update API GetAICoachScript: add response parameters Body.closingRemarks.
- Update API GetAICoachScript: add response parameters Body.expressivenessList.
- Update API GetAICoachScript: add response parameters Body.gifDynamicUrl.
- Update API GetAICoachScript: add response parameters Body.gifStaticUrl.
- Update API GetAICoachScript: add response parameters Body.openingRemarks.
- Update API GetAICoachScript: add response parameters Body.weights.assessmentPointEnabled.
- Update API ListAICoachScriptPage: add response parameters Body.list.$.closingRemarks.
- Update API ListAICoachScriptPage: add response parameters Body.list.$.gifDynamicUrl.
- Update API ListAICoachScriptPage: add response parameters Body.list.$.gifStaticUrl.
- Update API ListAICoachScriptPage: add response parameters Body.list.$.openingRemarks.
- Update API ListAICoachScriptPage: add response parameters Body.list.$.weights.assessmentPointEnabled.
- Update API ListAICoachTaskPage: add request parameters endTime.
- Update API ListAICoachTaskPage: add request parameters startTime.
- Update API ListAICoachTaskPage: add response parameters Body.taskList.$.gmtCreate.
- Update API ListAnchor: add request parameters anchorId.
- Update API QueryAvatarProject: add response parameters Body.scriptModelTag.
- Update API QueryAvatarProject: add response parameters Body.frames.$.index.
- Update API QueryAvatarProject: add response parameters Body.frames.$.layers.$.index.
- Update API QueryAvatarProject: add response parameters Body.frames.$.videoScript.emotion.
- Update API QueryAvatarProject: add response parameters Body.frames.$.videoScript.pitchRate.
- Update API QueryAvatarProject: add response parameters Body.frames.$.videoScript.textContent.
- Update API QueryAvatarProject: add response parameters Body.frames.$.videoScript.voiceLanguage.
- Update API QueryAvatarProject: add response parameters Body.frames.$.videoScript.volume.
- Update API SaveAvatarProject: add request parameters body.scriptModelTag.
- Update API SaveAvatarProject: add request parameters body.frames.$.index.
- Update API SaveAvatarProject: add request parameters body.frames.$.layers.$.index.
- Update API SaveAvatarProject: add request parameters body.frames.$.videoScript.emotion.
- Update API SaveAvatarProject: add request parameters body.frames.$.videoScript.pitchRate.
- Update API SaveAvatarProject: add request parameters body.frames.$.videoScript.textContent.
- Update API SubmitProjectTask: add request parameters body.frames.$.layers.$.material.mask.


2025-04-10 Version: 2.13.0
- Support API GetAICoachCheatDetection.
- Update API SelectResource: add response parameters Body.aliyunUid.


2025-04-08 Version: 2.12.2
- Update API BatchCreateAICoachTask: add request parameters body.studentList.
- Update API CreateAICoachTask: add request parameters body.studentAudioUrl.
- Update API GetAICoachScript: add response parameters Body.appendQuestionFlag.
- Update API GetAICoachScript: add response parameters Body.checkCheatConfig.


2025-03-27 Version: 2.12.1
- Update API GetAICoachScript: add response parameters Body.points.$.answerList.$.answerValues.
- Update API GetAICoachScript: add response parameters Body.points.$.answerList.$.enabledKeyword.


2025-03-13 Version: 2.12.0
- Support API BatchAddDocument.
- Support API BatchGetTrainTask.
- Support API BatchGetVideoClipTask.
- Support API CreateTrainTask.
- Support API CreateVideoClipTask.
- Support API DescribeDocument.
- Support API ListAgents.
- Support API ListKnowledgeBase.
- Update API GetAICoachScript: update response param.
- Update API GetAICoachTaskSessionHistory: update response param.
- Update API GetOssUploadToken: add param uploadType.
- Update API ListVoiceModels: add param voiceLanguage.
- Update API SaveAvatarProject: update param body.
- Update API SubmitProjectTask: update param body.


2025-02-25 Version: 2.11.1
- Update API GetAICoachScript: update response param.


2025-02-24 Version: 2.11.0
- Support API GetAICoachScript.
- Update API CreateAICoachTaskSession: update response param.
- Update API GetAICoachTaskSessionHistory: update response param.
- Update API SendSdkMessage: update param body.


2025-01-23 Version: 2.10.1
- Update API GetAICoachTaskSessionReport: update response param.
- Update API ListAICoachScriptPage: update response param.


2025-01-20 Version: 2.10.0
- Support API BatchCreateAICoachTask.
- Update API ListAICoachScriptPage: add param name.
- Update API ListAICoachScriptPage: add param type.
- Update API ListAICoachScriptPage: update response param.
- Update API SaveAvatarProject: update param body.
- Update API StartAvatarSession: update param body.


2024-12-25 Version: 2.9.0
- Support API CreateAICoachTask.
- Support API ListAICoachScriptPage.


2024-12-17 Version: 2.8.0
- Support API BatchQueryIndividuationText.
- Support API CreateAnchor.
- Support API CreateIndividuationProject.
- Support API CreateIndividuationTextTask.
- Support API DeleteIndividuationProject.
- Support API DeleteIndividuationText.
- Support API QueryIndividuationTextTask.
- Support API SendSdkMessage.


2024-12-17 Version: 2.7.1
- Update API GetAICoachTaskSessionHistory: add param pageNumber.
- Update API GetAICoachTaskSessionHistory: add param pageSize.
- Update API GetAICoachTaskSessionHistory: update response param.
- Update API GetAICoachTaskSessionReport: update response param.
- Update API ListAnchor: add param anchorCategory.
- Update API SubmitProjectTask: update param body.


2024-11-14 Version: 2.7.0
- Support API CloseAICoachTaskSession.
- Support API CreateAICoachTaskSession.
- Support API FinishAICoachTaskSession.
- Support API GetAICoachTaskSessionHistory.
- Support API GetAICoachTaskSessionReport.
- Support API ListAICoachTaskPage.


2024-10-24 Version: 2.6.0
- Support API OperateAvatarProject.
- Support API QuerySessionInfo.
- Support API SaveAvatarProject.
- Update API ListAnchor: add param resSpecType.
- Update API ListVoiceModels: add param resSpecType.
- Update API QueryAvatarProject: update response param.
- Update API StartAvatarSession: update param body.
- Update API SubmitProjectTask: update param body.


2024-09-29 Version: 2.5.0
- Support API InteractText.
- Support API ListAvatarProject.
- Update API SubmitProjectTask: update param body.


2024-09-09 Version: 2.4.0
- Support API CreateRealisticPortrait.
- Support API QueryTextStream.
- Support API SelectImageTask.
- Support API TransferPortraitStyle.
- Update API StartAvatarSession: update response param.
- Update API SubmitProjectTask: update param body.


2024-08-20 Version: 2.3.0
- Support API BatchGetProjectTask.


2024-08-07 Version: 2.2.0
- Support API CountText.
- Update API ListTexts: add param keyword.
- Update API SubmitProjectTask: update param body.


2024-07-22 Version: 2.1.4
- Generated python 2024-03-13 for IntelligentCreation.

2024-07-22 Version: 2.1.3
- Generated python 2024-03-13 for IntelligentCreation.

2024-07-22 Version: 2.1.2
- Generated python 2024-03-13 for IntelligentCreation.

2024-07-19 Version: 2.1.1
- Generated python 2024-03-13 for IntelligentCreation.

2024-07-19 Version: 2.1.0
- Support API AddTextFeedback.
- Support API CheckSession.
- Support API GetProjectTask.
- Support API GetTextTemplate.
- Support API ListAnchor.
- Support API ListVoiceModels.
- Support API QueryAvatarProject.
- Support API QueryAvatarResource.
- Support API SelectResource.
- Support API SendTextMsg.
- Support API StartAvatarSession.
- Support API StopAvatarSession.
- Support API StopProjectTask.
- Support API SubmitProjectTask.


2024-06-17 Version: 2.0.2
- Generated python 2024-03-13 for IntelligentCreation.

2024-06-13 Version: 2.0.1
- Generated python 2024-03-13 for IntelligentCreation.

2024-05-29 Version: 2.0.0
- Support API ListTexts.
- Update API ListTextThemes: add param industry.


2024-05-20 Version: 1.0.0
- Generated python 2024-03-13 for IntelligentCreation.

