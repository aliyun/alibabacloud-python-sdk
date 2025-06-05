2025-06-05 Version: 6.3.0
- Support API CreateRecognitionEntity.
- Support API CreateRecognitionLib.
- Support API CreateRecognitionSample.
- Support API DeleteRecognitionEntity.
- Support API DeleteRecognitionLib.
- Support API DeleteRecognitionSample.
- Support API ListRecognitionEntities.
- Support API ListRecognitionLibs.
- Support API ListRecognitionSamples.


2025-05-30 Version: 6.2.0
- Support API CreateHotwordLibrary.
- Support API DeleteHotwordLibrary.
- Support API GetHotwordLibrary.
- Support API ListHotwordLibraries.
- Support API UpdateHotwordLibrary.


2025-05-29 Version: 6.1.0
- Support API ListAIAgentPhoneNumber.
- Support API StartAIAgentOutboundCall.
- Support API SubmitAIAgentVideoAuditTask.
- Update API AddAdInsertion: add response parameters Body.Config.ManifestEndpointConfig.DashPrefix.
- Update API CreateLivePackageOriginEndpoint: add request parameters LivePackagingConfig.
- Update API CreateLivePackageOriginEndpoint: add response parameters Body.LivePackageOriginEndpoint.LivePackagingConfig.
- Update API DescribeAIAgentInstance: add response parameters Body.Instance.AgentConfig.
- Update API GenerateAIAgentCall: add request parameters AgentConfig.
- Update API GetAdInsertion: add response parameters Body.Config.ManifestEndpointConfig.DashPrefix.
- Update API GetLivePackageOriginEndpoint: add response parameters Body.LivePackageOriginEndpoint.LivePackagingConfig.
- Update API ListAIAgentInstance: add response parameters Body.Instances.$.AgentConfig.
- Update API ListAdInsertions: add response parameters Body.Configs.$.ManifestEndpointConfig.DashPrefix.
- Update API StartAIAgentInstance: add request parameters AgentConfig.
- Update API UpdateAIAgentInstance: add request parameters AgentConfig.
- Update API UpdateAdInsertion: add response parameters Body.Config.ManifestEndpointConfig.DashPrefix.
- Update API UpdateLivePackageOriginEndpoint: add request parameters LivePackagingConfig.
- Update API UpdateLivePackageOriginEndpoint: add response parameters Body.LivePackageOriginEndpoint.LivePackagingConfig.


2025-05-14 Version: 6.0.1
- Update API CreateMediaLiveChannel: add request parameters VideoSettings.$.VideoCodecType.
- Update API GetMediaLiveChannel: add response parameters Body.Channel.VideoSettings.$.VideoCodecType.
- Update API ListMediaLiveChannels: add response parameters Body.Channels.$.VideoSettings.$.VideoCodecType.
- Update API UpdateMediaLiveChannel: add request parameters VideoSettings.$.VideoCodecType.


2025-05-14 Version: 6.0.0
- Update API SubmitCopyrightJob: update request parameters StartTime' type has changed.
- Update API SubmitCopyrightJob: update request parameters StartTime' format has changed.
- Update API SubmitCopyrightJob: update request parameters TotalTime' type has changed.
- Update API SubmitCopyrightJob: update request parameters TotalTime' format has changed.
- Update API SubmitTraceAbJob: update request parameters StartTime' type has changed.
- Update API SubmitTraceAbJob: update request parameters StartTime' format has changed.
- Update API SubmitTraceAbJob: update request parameters TotalTime' type has changed.
- Update API SubmitTraceAbJob: update request parameters TotalTime' format has changed.


2025-04-28 Version: 5.0.7
- Update API DeleteAIAgentDialogue: add request parameters NodeId.
- Update API ListAIAgentDialogues: add request parameters RoundLimit.
- Update API ListAIAgentDialogues: add response parameters Body.Dialogues.$.Extend.
- Update API ListAIAgentDialogues: add response parameters Body.Dialogues.$.NodeId.


2025-04-25 Version: 5.0.6
- Update API DeleteMediaConnectFlowInput: add request parameters InputName.
- Update API GetMediaConnectFlow: add response parameters Body.Content.FlowFailover.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.BackupCidrs.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.BackupCreateTime.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.BackupInputName.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.BackupInputStatus.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.BackupInputUrl.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.BackupMaxBitrate.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.BackupSrtLatency.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.BackupSrtPassphrase.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.BackupSrtPbkeyLen.
- Update API GetMediaConnectFlowInput: add response parameters Body.Content.InputStatus.
- Update API GetMediaConnectFlowOutput: add response parameters Body.Content.Forbid.
- Update API UpdateMediaConnectFlowInput: add request parameters InputName.


2025-04-23 Version: 5.0.5
- Update API BatchGetMediaInfos: add response parameters Body.MediaInfos.$.MediaBasicInfo.Biz.


2025-04-21 Version: 5.0.4
- Update API GetBatchMediaProducingJob: add response parameters Body.EditingBatchJob.SubJobList.$.Duration.


2025-04-08 Version: 5.0.3
- Update API DescribeNotifyConfig: add response parameters Body.AudioOssPath.
- Update API DescribeNotifyConfig: add response parameters Body.EnableAudioRecording.
- Update API ListAIAgentDialogues: add response parameters Body.Dialogues.$.AttachedFileList.
- Update API SetNotifyConfig: add request parameters AudioOssPath.
- Update API SetNotifyConfig: add request parameters EnableAudioRecording.


2025-04-02 Version: 5.0.2
- Update API QueryIProductionJob: add response parameters Body.OutputMediaIds.
- Update API QueryIProductionJob: add response parameters Body.Output.Biz.
- Update API QueryIProductionJob: add response parameters Body.Output.OutputUrl.
- Update API SubmitIProductionJob: add request parameters Output.Biz.
- Update API SubmitIProductionJob: add request parameters Output.OutputUrl.


2025-03-27 Version: 5.0.1
- Update API SubmitBatchMediaProducingJob: add request parameters TemplateConfig.


2025-03-27 Version: 5.0.0
- Update API ListSmartVoiceGroups: add request parameters VoiceType.
- Update API ListSmartVoiceGroups: add request The number of query or body parameters has changed from zero to many.


2025-03-14 Version: 4.2.0
- Support API SubmitSegmentationJob.


2025-03-07 Version: 4.1.0
- Support API CreateMediaLiveChannel.
- Support API CreateMediaLiveInput.
- Support API CreateMediaLiveInputSecurityGroup.
- Support API DeleteMediaLiveChannel.
- Support API DeleteMediaLiveInput.
- Support API DeleteMediaLiveInputSecurityGroup.
- Support API GetMediaLiveChannel.
- Support API GetMediaLiveInput.
- Support API GetMediaLiveInputSecurityGroup.
- Support API ListMediaLiveChannels.
- Support API ListMediaLiveInputSecurityGroups.
- Support API ListMediaLiveInputs.
- Support API SendMessageChatText.
- Support API StartMediaLiveChannel.
- Support API StopMediaLiveChannel.
- Support API UpdateMediaLiveChannel.
- Support API UpdateMediaLiveInput.
- Support API UpdateMediaLiveInputSecurityGroup.
- Update API GenerateAIAgentCall: add param ChatSyncConfig.
- Update API GenerateAIAgentCall: update param SessionId.
- Update API ListAIAgentDialogues: update response param.
- Update API StartAIAgentInstance: add param ChatSyncConfig.
- Update API StartAIAgentInstance: update param SessionId.


2025-02-14 Version: 4.0.0
- Support API AddAdInsertion.
- Support API AddMediaConnectFlowInput.
- Support API AddMediaConnectFlowOutput.
- Support API BatchCreateVodPackagingAsset.
- Support API CreateChannel.
- Support API CreateLivePackageChannel.
- Support API CreateLivePackageChannelGroup.
- Support API CreateLivePackageOriginEndpoint.
- Support API CreateMediaConnectFlow.
- Support API CreateProgram.
- Support API CreateSource.
- Support API CreateSourceLocation.
- Support API CreateVodPackagingAsset.
- Support API CreateVodPackagingConfiguration.
- Support API CreateVodPackagingGroup.
- Support API DeleteAIAgentDialogue.
- Support API DeleteAdInsertion.
- Support API DeleteChannel.
- Support API DeleteLivePackageChannel.
- Support API DeleteLivePackageChannelGroup.
- Support API DeleteLivePackageOriginEndpoint.
- Support API DeleteMediaConnectFlow.
- Support API DeleteMediaConnectFlowInput.
- Support API DeleteMediaConnectFlowOutput.
- Support API DeleteProgram.
- Support API DeleteSource.
- Support API DeleteSourceLocation.
- Support API DeleteVodPackagingAsset.
- Support API DeleteVodPackagingConfiguration.
- Support API DeleteVodPackagingGroup.
- Support API GenerateMessageChatToken.
- Support API GetAdInsertion.
- Support API GetChannel.
- Support API GetLivePackageChannel.
- Support API GetLivePackageChannelGroup.
- Support API GetLivePackageOriginEndpoint.
- Support API GetMediaConnectFlow.
- Support API GetMediaConnectFlowInput.
- Support API GetMediaConnectFlowOutput.
- Support API GetProgram.
- Support API GetSource.
- Support API GetSourceLocation.
- Support API GetVodPackagingAsset.
- Support API GetVodPackagingConfiguration.
- Support API GetVodPackagingGroup.
- Support API ListAIAgentDialogues.
- Support API ListAdInsertions.
- Support API ListAlerts.
- Support API ListChannelAlerts.
- Support API ListChannels.
- Support API ListLivePackageChannelGroups.
- Support API ListLivePackageChannels.
- Support API ListLivePackageOriginEndpoints.
- Support API ListPrograms.
- Support API ListSchedules.
- Support API ListSourceLocations.
- Support API ListSources.
- Support API ListVodPackagingAssets.
- Support API ListVodPackagingConfigurations.
- Support API ListVodPackagingGroups.
- Support API SendAIAgentText.
- Support API StartChannel.
- Support API StopChannel.
- Support API SubmitHighlightExtractionJob.
- Support API UpdateAdInsertion.
- Support API UpdateChannel.
- Support API UpdateLivePackageChannel.
- Support API UpdateLivePackageChannelCredentials.
- Support API UpdateLivePackageChannelGroup.
- Support API UpdateLivePackageOriginEndpoint.
- Support API UpdateMediaConnectFlowInput.
- Support API UpdateMediaConnectFlowOutput.
- Support API UpdateMediaConnectFlowStatus.
- Support API UpdateProgram.
- Support API UpdateSource.
- Support API UpdateSourceLocation.
- Update API DescribeAIAgentInstance: update response param.
- Update API GenerateAIAgentCall: add param SessionId.
- Update API StartAIAgentInstance: add param SessionId.
- Update API SubmitASRJob: add param EditingConfig.
- Update API SubmitVideoTranslationJob: add param Signature.
- Update API SubmitVideoTranslationJob: add param SignatureMehtod.
- Update API SubmitVideoTranslationJob: add param SignatureNonce.
- Update API SubmitVideoTranslationJob: add param SignatureType.
- Update API SubmitVideoTranslationJob: add param SignatureVersion.


2025-01-17 Version: 3.11.0
- Support API GetMediaConvertJob.
- Support API SubmitMediaConvertJob.


2025-01-16 Version: 3.10.0
- Support API GetProjectExportJob.
- Support API SubmitProjectExportJob.


2024-12-30 Version: 3.9.1
- Update API SubmitMediaAiAnalysisJob: add param UserData.


2024-12-27 Version: 3.9.0
- Support API SubmitScreenMediaHighlightsJob.


2024-12-24 Version: 3.8.1
- Update API GetSmartHandleJob: update response param.
- Update API ListSearchLib: update response param.
- Update API QuerySearchLib: update response param.


2024-12-13 Version: 3.8.0
- Support API SendAIAgentDataChannelMessage.
- Support API TakeoverAIAgentCall.


2024-12-12 Version: 3.7.0
- Support API QueryCopyrightExtractJob.
- Support API QueryCopyrightJobList.
- Support API QueryTraceAbJobList.
- Support API QueryTraceExtractJob.
- Support API QueryTraceM3u8JobList.
- Support API SubmitCopyrightExtractJob.
- Support API SubmitCopyrightJob.
- Support API SubmitTraceAbJob.
- Support API SubmitTraceExtractJob.
- Support API SubmitTraceM3u8Job.
- Update API GetMediaProducingJob: update response param.
- Update API ListSearchLib: update response param.
- Update API SearchMediaClipByFace: update response param.


2024-11-20 Version: 3.6.4
- Update API GenerateAIAgentCall: add param UserData.
- Update API StartRtcRobotInstance: update param Config.


2024-11-05 Version: 3.6.3
- Update API StartRtcRobotInstance: update param Config.
- Update API SubmitIProductionJob: add param ModelId.


2024-10-24 Version: 3.6.2
- Update API GetCustomTemplate: update response param.
- Update API ListCustomTemplates: update response param.


2024-10-17 Version: 3.6.1
- Update API SearchMediaByAILabel: add param MatchingMode.


2024-09-24 Version: 3.6.0
- Support API DescribeAIAgentInstance.
- Support API DescribeNotifyConfig.
- Support API GenerateAIAgentCall.
- Support API ListAIAgentInstance.
- Support API SendAIAgentSpeech.
- Support API SetNotifyConfig.
- Support API StartAIAgentInstance.
- Support API StopAIAgentInstance.
- Support API UpdateAIAgentInstance.


2024-08-27 Version: 3.5.1
- Generated python 2020-11-09 for ICE.

2024-08-26 Version: 3.5.0
- Support API ListSearchLib.
- Support API SearchIndexJobRerun.
- Update API SearchMedia: update response param.


2024-08-26 Version: 3.4.0
- Support API SubmitSportsHighlightsJob.


2024-08-14 Version: 3.3.1
- Update API ListMediaProducingJobs: add param ProjectId.


2024-08-01 Version: 3.3.0
- Support API ListEditingProjects.


2024-07-31 Version: 3.2.0
- Support API DescribeRtcRobotInstance.
- Support API StartRtcRobotInstance.
- Support API StopRtcRobotInstance.
- Support API UpdateRtcRobotInstance.
- Update API ListSmartVoiceGroups: update response param.


2024-07-30 Version: 3.1.1
- Update API ListSmartVoiceGroups: update response param.


2024-07-25 Version: 3.1.0
- Support API SubmitMediaAiAnalysisJob.


2024-07-23 Version: 3.0.0
- Update API GetBatchMediaProducingJob: delete param Signature.
- Update API GetBatchMediaProducingJob: delete param SignatureMehtod.
- Update API GetBatchMediaProducingJob: delete param SignatureNonce.
- Update API GetBatchMediaProducingJob: delete param SignatureType.
- Update API GetBatchMediaProducingJob: delete param SignatureVersion.
- Update API GetBatchMediaProducingJob: update response param.
- Update API ListDNADB: update response param.


2024-06-26 Version: 2.7.0
- Support API GetStorageList.


2024-06-24 Version: 2.6.0
- Support API SubmitVideoTranslationJob.


2024-06-04 Version: 2.5.1
- Update API GetMediaInfo: update response param.


2024-06-03 Version: 2.5.0
- Support API SearchMediaByHybrid.
- Update API SearchMediaByAILabel: update response param.


2024-05-22 Version: 2.4.1
- Update API SubmitTextGenerateJob: add param Action.


2024-05-22 Version: 2.4.1
- Update API SubmitTextGenerateJob: add param Action.


2024-04-28 Version: 2.4.0
- Support API ListBatchMediaProducingJobs.
- Support API ListMediaProducingJobs.
- Support API SubmitTextGenerateJob.
- Update API DeleteLiveSnapshotFiles: update response param.
- Update API GetBatchMediaProducingJob: add param Action.
- Update API GetBatchMediaProducingJob: add param Signature.
- Update API GetBatchMediaProducingJob: add param SignatureMehtod.
- Update API GetBatchMediaProducingJob: add param SignatureNonce.
- Update API GetBatchMediaProducingJob: add param SignatureType.
- Update API GetBatchMediaProducingJob: add param SignatureVersion.
- Update API GetBatchMediaProducingJob: update response param.
- Update API GetMediaInfo: add param ReturnDetailedInfo.
- Update API GetMediaInfo: update response param.
- Update API GetSmartHandleJob: update response param.
- Update API QueryIProductionJob: add param Action.
- Update API RegisterMediaInfo: add param SmartTagTemplateId.
- Update API SubmitIProductionJob: add param Action.
- Update API SubmitMediaCensorJob: add param AccessKeyId.
- Update API SubmitMediaCensorJob: add param Action.


2024-03-04 Version: 2.3.0
- Support API SubmitTextGenerateJob.
- Delete API SubmitSubtitleProduceJob.
- Update API DeleteLiveSnapshotFiles: update response param.
- Update API GetBatchMediaProducingJob: add param Action.
- Update API GetBatchMediaProducingJob: add param Signature.
- Update API GetBatchMediaProducingJob: add param SignatureMehtod.
- Update API GetBatchMediaProducingJob: add param SignatureNonce.
- Update API GetBatchMediaProducingJob: add param SignatureType.
- Update API GetBatchMediaProducingJob: add param SignatureVersion.
- Update API GetSmartHandleJob: update response param.
- Update API QueryIProductionJob: add param Action.
- Update API SubmitIProductionJob: add param Action.
- Update API SubmitMediaCensorJob: add param AccessKeyId.
- Update API SubmitMediaCensorJob: add param Action.


2024-02-27 Version: 2.2.4
- Delete API SubmitSubtitleProduceJob.
- Update API DeleteLiveSnapshotFiles: update response param.
- Update API GetBatchMediaProducingJob: add param Action.
- Update API GetBatchMediaProducingJob: add param Signature.
- Update API GetBatchMediaProducingJob: add param SignatureMehtod.
- Update API GetBatchMediaProducingJob: add param SignatureNonce.
- Update API GetBatchMediaProducingJob: add param SignatureType.
- Update API GetBatchMediaProducingJob: add param SignatureVersion.
- Update API GetSmartHandleJob: update response param.
- Update API QueryIProductionJob: add param Action.
- Update API SubmitIProductionJob: add param Action.
- Update API SubmitMediaCensorJob: add param AccessKeyId.
- Update API SubmitMediaCensorJob: add param Action.


2024-02-22 Version: 2.2.3
- Delete API SubmitSubtitleProduceJob.
- Update API DeleteLiveSnapshotFiles: update response param.
- Update API GetBatchMediaProducingJob: add param Action.
- Update API GetBatchMediaProducingJob: add param Signature.
- Update API GetBatchMediaProducingJob: add param SignatureMehtod.
- Update API GetBatchMediaProducingJob: add param SignatureNonce.
- Update API GetBatchMediaProducingJob: add param SignatureType.
- Update API GetBatchMediaProducingJob: add param SignatureVersion.
- Update API SubmitMediaCensorJob: add param AccessKeyId.
- Update API SubmitMediaCensorJob: add param Action.


2024-02-19 Version: 2.2.2
- Update API DeleteLiveSnapshotFiles: update response param.
- Update API GetBatchMediaProducingJob: add param Action.
- Update API GetBatchMediaProducingJob: add param Signature.
- Update API GetBatchMediaProducingJob: add param SignatureMehtod.
- Update API GetBatchMediaProducingJob: add param SignatureNonce.
- Update API GetBatchMediaProducingJob: add param SignatureType.
- Update API GetBatchMediaProducingJob: add param SignatureVersion.


2024-02-19 Version: 2.2.2
- Update API DeleteLiveSnapshotFiles: update response param.
- Update API GetBatchMediaProducingJob: add param Action.
- Update API GetBatchMediaProducingJob: add param Signature.
- Update API GetBatchMediaProducingJob: add param SignatureMehtod.
- Update API GetBatchMediaProducingJob: add param SignatureNonce.
- Update API GetBatchMediaProducingJob: add param SignatureType.
- Update API GetBatchMediaProducingJob: add param SignatureVersion.


2024-01-30 Version: 2.2.1
- Generated python 2020-11-09 for ICE.

2024-01-29 Version: 2.2.0
- Support API GetBatchMediaProducingJob.
- Support API SubmitBatchMediaProducingJob.
- Update API GetMediaProducingJobupdate response param.
- Update API ListPublicMediaBasicInfosadd BusinessType param.
- Update API SubmitDynamicChartJobupdate RegionId param.


2024-01-26 Version: 2.1.1
- Update API GetMediaProducingJobupdate response param.
- Update API ListPublicMediaBasicInfosadd BusinessType param.
- Update API SubmitDynamicChartJobupdate RegionId param.


2023-11-23 Version: 2.1.0
- Generated python 2020-11-09 for ICE.

2023-11-22 Version: 2.0.0
- Generated python 2020-11-09 for ICE.

2023-08-25 Version: 1.4.0
- Generated python 2020-11-09 for ICE.

2023-06-06 Version: 1.3.12
- Add KMS apis and hls encryption transcoding.

2023-05-18 Version: 1.3.11
- Add conditional transcoding parameters.

2023-04-27 Version: 1.3.10
- Add field MediaMetadata for api SubmitMediaProducingJob, which indicates the meta data of the output media produced by the editing job.

2023-04-21 Version: 1.3.9
- Add api called SubmitAvatarVideoJob, which render avatar videos.

2023-03-14 Version: 1.3.8
- Add templateType params in CreateEditingProject API.

2023-03-01 Version: 1.3.7
- Add jobResults params in GetSmartHandleJob API.

2023-02-03 Version: 1.3.6
- Add GetTemplateParams API.

2023-01-18 Version: 1.3.5
- Add DNA API.

2022-12-31 Version: 1.3.4
- Add RequestSource param to GetEditingProject API.

2022-11-21 Version: 1.3.3
- Add QueryMediaCensorJobList.

2022-09-22 Version: 1.3.2
- SubmitLiveEditingJob response add VodMediaId.

2022-08-29 Version: 1.3.1
- Change RegisterMediaInfo.

2022-07-20 Version: 1.3.0
- Ass new api called SubmitMediaInfoJob, which submit mediaInfo job.
- Ass new api called SubmitMediaCensorJob, which submit mediaCensor job.
- Ass new api called SubmitIProductionJob, which submit iProduction job.
- Ass new api called SubmitTranscodeJob, which submit transcode job.
- Ass new api called SubmitDynamicImageJob, which submit dynamicImage job.
- Ass new api called SubmitSnapshotJob, which submit snapshot job.

2022-06-08 Version: 1.2.0
- Add page params in ListTemplates API.

2021-12-23 Version: 1.1.6
- Add a new API called SubmitDynamicChartJob, which produce chart video throuth xlsx file.

2021-11-26 Version: 1.1.5
- Add a new API called GetPublicMediaInfo, which gets information of copyrighted public media.
- Add a new API called DescribeMaterialPackageInfo, which describes the available material packages.
- Add a new API called AddFavoritePublicMedia, which adds public media to favorite for the user.
- Add a new API called CancelFavoritePublicMedia, which removes public media from user favorite.
- Add a new API called SearchPublicMediaInfo, which searches copyrighted public media.
- Update the return value of an existed API called ListAllPublicMediaTags, adding field Options.
- Update the return value of an existed API called GetMediaInfo, adding field DynamicMetaData.
- Modify the data type of the return value of an existed API called GetEditingProjectMaterials, where ProjectMaterials should be a list instead of a string.
- Modify the data type of the return value of an existed API called AddEditingProjectMaterials, where ProjectMaterials should be a list instead of a string.
- Update the input params of an existing API called SubmitMediaProducingJob, adding field EditingProduceConfig.

2021-11-16 Version: 1.1.4
- Add a new API called BatchGetMediaInfos, which get multi media infos through mediaids.
- Add a new API called GetTemplateMaterials, which get material urls of VeTemplates.

2021-11-04 Version: 1.1.3
- Add relatedMediaIds param in GetTemplate API.

2021-09-10 Version: 1.1.2
- Add post method to Template API.

2021-08-12 Version: 1.1.1
- Fix GetSmartHandleJob type conversion error.

2021-08-10 Version: 1.1.0
- Add template clipsParam param.

2021-07-15 Version: 1.0.9
- Fix bugs.

2021-07-09 Version: 1.0.8
- Add a new API called ListSysTemplates, which list system templates.
- Add a new API called ListTemplates, which list user templates.
- Add a new API called AddTemplate, which add a new templates.
- Add a new API called UpdateTemplate, which update template configs.
- Add a new API called DeleteTemplate, which delete templates.
- Add vod output config in SubmitH2VJob.
- Add vod output config in SubmitDelogoJob.
- Add vod output config in SubmitMattingJob.

2021-06-03 Version: 1.0.7
- SubmitMediaProducingJob return MediaId in the result.

2021-04-16 Version: 1.0.5
- Add a new API called SubmitH2VJob, which submit horizontal to vertical job.
- Add a new API called SubmitDelogoJob, which submit delogo job.
- Add a new API called SubmitMattingJob, which submit matting job.
- Add a new API called SubmitAudioProduceJob, which produce audio from text.

2021-03-26 Version: 1.0.3
- Add a new API called AddEditingProjectMaterials, which adds one or more materials to the editing project.
- Add a new API called GetEditingProjectMaterials, which gets all the materials in the editing project.
- Add a new API called DeleteEditingProjectMaterials, which deletes specified materials in the editing according to mediaIds or media type .
- Add a new API called ListPublicMediaBasicInfos, which lists the basic information of all public media with a specified media tag.
- Add a new API called ListAllPublicMediaTags, which lists all the media tags for the public media.

2021-02-03 Version: 1.0.0
- Add a new API called RegisterMediaInfo, which registers a new media asset in ICE.
- Add a new API called GetMediaInfo, which returns all the information of a media asset.
- Add a new API called UpdateMediaInfo, which updates the information of a media asset.
- Add a new API called DeleteMediaInfos, which batch deletes media.
- Add a new API called ListMediaBasicInfos, which lists the basic information of all media that match the input criterions.
- Add a new API called CreateEditingProject, which creates an editing project in ICE.
- Add a new API called GetEditingProject, which returns all the information of an editing project.
- Add a new API called UpdateEditingProject, which updates an editing project.
- Add a new API called DeleteEditingProjects, which batch deletes editing projects.
- Add a new API called SearchEditingProjects, which searches editing projects based on the input criterions.
- Add a new API called SubmitMediaProducingJob, which initiates the job for producing media.
- Add a new API called GetMediaProducingJob, which querys the result of the media producing job.

