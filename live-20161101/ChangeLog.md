2025-12-24 Version: 2.5.0
- Support API ListLiveTagResources.


2025-12-05 Version: 2.4.0
- Support API DescribeLiveRtcRecordUsageData.


2025-12-02 Version: 2.3.3
- Update API StartRtcCloudRecording: add request parameters NotifyFileUploadedFormat.


2025-11-07 Version: 2.3.2
- Update API DescribeLiveStreamsNotifyRecords: add response parameters Body.NotifyRecordsInfo.$.NotifyHeader.


2025-11-04 Version: 2.3.1
- Update API AddLiveRecordNotifyConfig: add request parameters NotifyAuthKey.
- Update API AddLiveRecordNotifyConfig: add request parameters NotifyReqAuth.
- Update API DescribeLiveRecordNotifyConfig: add response parameters Body.LiveRecordNotifyConfig.NotifyAuthKey.
- Update API DescribeLiveRecordNotifyConfig: add response parameters Body.LiveRecordNotifyConfig.NotifyReqAuth.
- Update API DescribeLiveRecordNotifyRecords: add response parameters Body.CallbackList.$.NotifyHeader.
- Update API UpdateLiveRecordNotifyConfig: add request parameters NotifyAuthKey.
- Update API UpdateLiveRecordNotifyConfig: add request parameters NotifyReqAuth.


2025-10-29 Version: 2.3.0
- Support API PutRecordStorageLifeCycle.
- Update API AddCustomLiveStreamTranscode: add request parameters DeInterlaced.
- Update API DescribeLiveStreamTranscodeInfo: add response parameters Body.DomainTranscodeList.$.CustomTranscodeParameters.DeInterlaced.
- Update API UpdateCustomLiveStreamTranscode: add request parameters DeInterlaced.


2025-09-09 Version: 2.2.0
- Support API ListRTCLiveRooms.


2025-08-20 Version: 2.1.4
- Generated python 2016-11-01 for live.

2025-08-12 Version: 2.1.3
- Update API DescribeLiveRecordNotifyRecords: add response parameters Body.CallbackList.$.NotifyResponse.
- Update API DescribeRtcCloudRecordingFiles: add response parameters Body.TaskInfo.RecordFileList.VodMediaList.
- Update API StartRtcCloudRecording: add request parameters MaxIdleTime.
- Update API StartRtcCloudRecording: add request parameters NotifyAuthKey.
- Update API StartRtcCloudRecording: add request parameters StorageParams.VodParams.
- Update API StartRtcCloudRecording: add request parameters StorageParams.FileInfo.$.FilePathPrefix.


2025-07-31 Version: 2.1.2
- Update API DescribeLiveStreamsNotifyRecords: add response parameters Body.NotifyRecordsInfo.$.NotifyResponse.


2025-07-30 Version: 2.1.1
- Update API AddLiveStreamMerge: add request parameters LiveMerger.
- Update API AddLiveStreamMerge: add request parameters MergeParameters.
- Update API AddLiveStreamMerge: add response parameters Body.Message.
- Update API DescribeLiveStreamMerge: add response parameters Body.LiveStreamMergeList.$.LiveMerger.
- Update API DescribeLiveStreamMerge: add response parameters Body.LiveStreamMergeList.$.MergeParameters.


2025-07-29 Version: 2.1.0
- Support API DescribeLiveUserStreamMetricData.


2025-07-15 Version: 2.0.0
- Support API AddLiveAIProduceRules.
- Support API AddLiveAISubtitle.
- Support API AddLiveCenterTransfer.
- Support API AddLiveMessageGroupBand.
- Support API AddLivePackageConfig.
- Support API AddLiveStreamMerge.
- Support API BanLiveMessageGroup.
- Support API BatchGetOnlineUsers.
- Support API CancelMuteGroupUser.
- Support API ChangeLiveDomainResourceGroup.
- Support API CheckLiveMessageUsersInGroup.
- Support API CheckLiveMessageUsersOnline.
- Support API CreateEdgeTranscodeJob.
- Support API CreateEventSub.
- Support API CreateLiveAIStudio.
- Support API CreateLiveDelayConfig.
- Support API CreateLiveMessageApp.
- Support API CreateLiveMessageGroup.
- Support API CreateLivePrivateLine.
- Support API CreateLivePullToPush.
- Support API CreateRTCWhipStreamAddress.
- Support API CreateRoomRealTimeStreamAddress.
- Support API CreateRtcAsrTask.
- Support API CreateRtcMPUEventSub.
- Support API DeleteChannel.
- Support API DeleteEdgeTranscodeJob.
- Support API DeleteEventSub.
- Support API DeleteLiveAIProduceRules.
- Support API DeleteLiveAIStudio.
- Support API DeleteLiveAISubtitle.
- Support API DeleteLiveCenterTransfer.
- Support API DeleteLiveDelayConfig.
- Support API DeleteLiveMessageGroup.
- Support API DeleteLiveMessageGroupMessage.
- Support API DeleteLiveMessageUserMessage.
- Support API DeleteLivePackageConfig.
- Support API DeleteLivePrivateLine.
- Support API DeleteLivePullToPush.
- Support API DeleteLiveStreamBlock.
- Support API DeleteLiveStreamMerge.
- Support API DeleteRtcAsrTask.
- Support API DeleteRtcMPUEventSub.
- Support API DescribeChannelParticipants.
- Support API DescribeChannelUsers.
- Support API DescribeLiveAIProduceRules.
- Support API DescribeLiveAIStudio.
- Support API DescribeLiveAISubtitle.
- Support API DescribeLiveCdnDiagnoseInfo.
- Support API DescribeLiveCenterStreamRateData.
- Support API DescribeLiveCenterTransfer.
- Support API DescribeLiveDelayConfig.
- Support API DescribeLiveDelayedStreamingUsage.
- Support API DescribeLiveDomainByCertificate.
- Support API DescribeLiveDomainEdgeLog.
- Support API DescribeLiveDomainLogExTtl.
- Support API DescribeLiveDomainMonitoringUsageData.
- Support API DescribeLiveDomainMultiStreamConfig.
- Support API DescribeLiveDomainPublishErrorCode.
- Support API DescribeLiveDomainTranscodeParams.
- Support API DescribeLiveGrtnDuration.
- Support API DescribeLiveHttpsDomainList.
- Support API DescribeLiveInteractionMetricData.
- Support API DescribeLiveIpInfo.
- Support API DescribeLiveMessageApp.
- Support API DescribeLiveMessageGroup.
- Support API DescribeLiveMessageGroupBand.
- Support API DescribeLivePackageConfig.
- Support API DescribeLivePrivateLineAreas.
- Support API DescribeLivePrivateLineAvailGA.
- Support API DescribeLivePullToPush.
- Support API DescribeLivePullToPushList.
- Support API DescribeLivePushProxyLog.
- Support API DescribeLivePushProxyUsageData.
- Support API DescribeLiveRecordNotifyRecords.
- Support API DescribeLiveStreamDetailFrameRateAndBitRateData.
- Support API DescribeLiveStreamMerge.
- Support API DescribeLiveStreamPreloadTasks.
- Support API DescribeLiveStreamPushMetricDetailData.
- Support API DescribeLiveStreamTranscodeMetricData.
- Support API DescribeLiveStreamsTotalCount.
- Support API DescribeLiveTrafficDomainLog.
- Support API DescribeLiveUpVideoAudioInfo.
- Support API DescribeLiveUserTrafficLog.
- Support API DescribeLiveVerifyContent.
- Support API DescribeMeterLiveBypassDuration.
- Support API DescribeRtcCloudRecordingFiles.
- Support API DescribeRtcMPUEventSub.
- Support API DescribeStreamLocationBlock.
- Support API DescribeUidOnlineStreams.
- Support API GetEdgeTranscodeJob.
- Support API GetEdgeTranscodeTemplate.
- Support API GetTranscodeTaskStatus.
- Support API KickLiveMessageGroupUser.
- Support API ListEdgeTranscodeJob.
- Support API ListEdgeTranscodeTemplate.
- Support API ListEventSub.
- Support API ListEventSubEvent.
- Support API ListLiveDelayConfig.
- Support API ListLiveMessageApps.
- Support API ListLiveMessageGroupByPage.
- Support API ListLiveMessageGroupMessages.
- Support API ListLiveMessageGroupUsers.
- Support API ListLiveMessageGroups.
- Support API ListMuteGroupUser.
- Support API ListRtcMPUEventSubRecord.
- Support API ListRtcMPUTaskDetail.
- Support API LiveUpstreamQosData.
- Support API MiguLivePullToPushStart.
- Support API MiguLivePullToPushStatus.
- Support API ModifyLiveAIStudio.
- Support API ModifyLiveMessageAppAudit.
- Support API ModifyLiveMessageAppCallback.
- Support API ModifyLiveMessageAppDisable.
- Support API ModifyLiveMessageGroup.
- Support API ModifyLiveMessageGroupBand.
- Support API ModifyLiveMessageUserInfo.
- Support API MuteAllGroupUser.
- Support API MuteGroupUser.
- Support API QueryLiveDomainMultiStreamList.
- Support API QueryRtcAsrTasks.
- Support API RecoverLiveMessageDeletedGroup.
- Support API RemoveLiveMessageGroupBand.
- Support API RemoveTerminals.
- Support API RestartLivePullToPush.
- Support API RestartTranscodeTask.
- Support API SendLiveMessageGroup.
- Support API SendLiveMessageUser.
- Support API SetLiveDomainMultiStreamConfig.
- Support API SetLiveDomainMultiStreamMaster.
- Support API SetLiveDomainMultiStreamOptimalMode.
- Support API SetLiveMpuTaskSei.
- Support API SetLiveStreamBlock.
- Support API SetLiveStreamPreloadTasks.
- Support API SetShowListBackground.
- Support API StartEdgeTranscodeJob.
- Support API StartLiveMPUTask.
- Support API StartRtcCloudRecording.
- Support API StopEdgeTranscodeJob.
- Support API StopLiveMPUTask.
- Support API StopLivePullToPush.
- Support API StopRtcAsrTask.
- Support API StopRtcCloudRecording.
- Support API UnbanLiveMessageGroup.
- Support API UpdateCasterResourceGroup.
- Support API UpdateCustomLiveStreamTranscode.
- Support API UpdateEdgeTranscodeJob.
- Support API UpdateEventSub.
- Support API UpdateLiveAIProduceRules.
- Support API UpdateLiveAISubtitle.
- Support API UpdateLiveAppRecordConfig.
- Support API UpdateLiveCenterTransfer.
- Support API UpdateLiveDelayConfig.
- Support API UpdateLiveMPUTask.
- Support API UpdateLivePackageConfig.
- Support API UpdateLivePullToPush.
- Support API UpdateLiveRecordVodConfig.
- Support API UpdateLiveStreamTranscode.
- Support API UpdateRtcCloudRecording.
- Support API UpdateRtcMPUEventSub.
- Support API UpdateRtsLiveStreamTranscode.
- Update API AddCasterVideoResource: add request parameters ImageId.
- Update API AddCasterVideoResource: add request parameters ImageUrl.
- Update API AddCustomLiveStreamTranscode: add request parameters BitrateWithSource.
- Update API AddCustomLiveStreamTranscode: add request parameters ExtWithSource.
- Update API AddCustomLiveStreamTranscode: add request parameters FpsWithSource.
- Update API AddCustomLiveStreamTranscode: add request parameters Lazy.
- Update API AddCustomLiveStreamTranscode: add request parameters ResWithSource.
- Update API AddLiveAppRecordConfig: add request parameters DelayTime.
- Update API AddLiveDomain: add request parameters ResourceGroupId.
- Update API AddLiveDomain: add request parameters Tag.
- Update API AddLiveRecordVodConfig: add request parameters OnDemand.
- Update API AddLiveStreamWatermark: add request parameters Domain.
- Update API CancelMuteAllGroupUser: add request parameters BroadCastType.
- Update API CreateCaster: add request parameters ResourceGroupId.
- Update API CreateCaster: add request parameters Tag.
- Update API CreateLiveStreamMonitor: add request parameters CallbackUrl.
- Update API CreateLiveStreamMonitor: add request parameters DingTalkWebHookUrl.
- Update API CreateLiveStreamMonitor: add request parameters MonitorConfig.
- Update API CreateLiveStreamRecordIndexFiles: add request parameters EndTimeIncluded.
- Update API DescribeCasterConfig: add response parameters Body.AutoSwitchUrgentConfig.
- Update API DescribeCasterConfig: add response parameters Body.AutoSwitchUrgentOn.
- Update API DescribeCasterConfig: add response parameters Body.UrgentImageId.
- Update API DescribeCasterConfig: add response parameters Body.UrgentImageUrl.
- Update API DescribeCasterConfig: add response parameters Body.RecordConfig.OnDemand.
- Update API DescribeCasterConfig: add response parameters Body.TranscodeConfig.CustomParams.
- Update API DescribeCasterVideoResources: add response parameters Body.VideoResources.$.ImageId.
- Update API DescribeCasterVideoResources: add response parameters Body.VideoResources.$.ImageUrl.
- Update API DescribeCasters: add request parameters ResourceGroupId.
- Update API DescribeCasters: add request parameters Tag.
- Update API DescribeCasters: add response parameters Body.CasterList.$.ClientTokenId.
- Update API DescribeCasters: add response parameters Body.CasterList.$.ResourceGroupId.
- Update API DescribeCasters: add response parameters Body.CasterList.$.Tags.
- Update API DescribeLiveDomainDetail: add response parameters Body.DomainDetail.ResourceGroupId.
- Update API DescribeLiveDomainLimit: add response parameters Body.LiveDomainLimitList.$.CurrentNum.
- Update API DescribeLiveDomainLimit: add response parameters Body.LiveDomainLimitList.$.CurrentTranscodeNum.
- Update API DescribeLiveDomainLimit: add response parameters Body.LiveDomainLimitList.$.CurrentTransferNum.
- Update API DescribeLiveDomainRecordUsageData: add request parameters Interval.
- Update API DescribeLiveDomainRecordUsageData: add request parameters Region.
- Update API DescribeLiveDomainRecordUsageData: add response parameters Body.EndTime.
- Update API DescribeLiveDomainRecordUsageData: add response parameters Body.StartTime.
- Update API DescribeLiveDomainRecordUsageData: add response parameters Body.RecordUsageData.$.Region.
- Update API DescribeLiveDomainStreamTranscodeData: add request parameters Precision.
- Update API DescribeLiveLazyPullStreamConfig: add response parameters Body.LiveLazyPullConfigList.$.PullArgs.
- Update API DescribeLiveLazyPullStreamConfig: add response parameters Body.LiveLazyPullConfigList.$.TranscodeLazy.
- Update API DescribeLiveRecordConfig: add response parameters Body.LiveAppRecordList.$.DelayTime.
- Update API DescribeLiveRecordVodConfigs: add response parameters Body.LiveRecordVodConfigs.$.OnDemand.
- Update API DescribeLiveRecordVodConfigs: add response parameters Body.LiveRecordVodConfigs.$.StorageLocation.
- Update API DescribeLiveStreamMetricDetailData: add response parameters Body.StreamDetailData.$.NewConns.
- Update API DescribeLiveStreamMonitorList: add response parameters Body.LiveStreamMonitorList.$.CallbackUrl.
- Update API DescribeLiveStreamMonitorList: add response parameters Body.LiveStreamMonitorList.$.DingTalkWebHookUrl.
- Update API DescribeLiveStreamMonitorList: add response parameters Body.LiveStreamMonitorList.$.MonitorConfig.
- Update API DescribeLiveStreamRecordIndexFile: add response parameters Body.RecordIndexInfo.Format.
- Update API DescribeLiveStreamRecordIndexFiles: add response parameters Body.RecordIndexInfoList.$.Format.
- Update API DescribeLiveStreamTranscodeInfo: add request parameters AppName.
- Update API DescribeLiveStreamTranscodeInfo: add response parameters Body.DomainTranscodeList.$.CustomTranscodeParameters.BitrateWithSource.
- Update API DescribeLiveStreamTranscodeInfo: add response parameters Body.DomainTranscodeList.$.CustomTranscodeParameters.ExtWithSource.
- Update API DescribeLiveStreamTranscodeInfo: add response parameters Body.DomainTranscodeList.$.CustomTranscodeParameters.FpsWithSource.
- Update API DescribeLiveStreamTranscodeInfo: add response parameters Body.DomainTranscodeList.$.CustomTranscodeParameters.ResWithSource.
- Update API DescribeLiveStreamTranscodeStreamNum: add request parameters SplitType.
- Update API DescribeLiveStreamTranscodeStreamNum: add response parameters Body.TranscodeStreamCountDetails.
- Update API DescribeLiveStreamWatermarkRules: add request parameters Domain.
- Update API DescribeLiveStreamWatermarkRules: add response parameters Body.Total.
- Update API DescribeLiveStreamWatermarks: add request parameters Domain.
- Update API DescribeLiveStreamWatermarks: add request parameters KeyWord.
- Update API DescribeLiveStreamWatermarks: add response parameters Body.Total.
- Update API DescribeLiveStreamWatermarks: add response parameters Body.WatermarkList.$.RuleCount.
- Update API DescribeLiveStreamsNotifyUrlConfig: add response parameters Body.LiveStreamsNotifyConfig.ExceptionNotifyUrl.
- Update API DescribeLiveStreamsOnlineList: add response parameters Body.OnlineInfo.$.AudioDataRate.
- Update API DescribeLiveStreamsOnlineList: add response parameters Body.OnlineInfo.$.VideoDataRate.
- Update API DescribeLiveStreamsPublishList: add response parameters Body.PublishInfo.$.AliInnerErrorFlags.
- Update API DescribeLiveUserDomains: add request parameters ResourceGroupId.
- Update API DescribeLiveUserDomains: add response parameters Body.Domains.$.ResourceGroupId.
- Update API DescribeShowList: add response parameters Body.ShowListInfo.Background.
- Update API ModifyCasterVideoResource: add request parameters ImageId.
- Update API ModifyCasterVideoResource: add request parameters ImageUrl.
- Update API SendMessageToGroup: add request parameters SkipAudit.
- Update API SendMessageToGroupUsers: add request parameters SkipAudit.
- Update API SetCasterConfig: add request parameters AutoSwitchUrgentConfig.
- Update API SetCasterConfig: add request parameters AutoSwitchUrgentOn.
- Update API SetCasterConfig: add request parameters UrgentImageId.
- Update API SetCasterConfig: add request parameters UrgentImageUrl.
- Update API SetLiveLazyPullStreamInfoConfig: add request parameters TranscodeLazy.
- Update API SetLiveStreamsNotifyUrlConfig: add request parameters ExceptionNotifyUrl.
- Update API SetLiveStreamsNotifyUrlConfig: add request parameters SwitchNotifyUrl.
- Update API UpdateCasterSceneAudio: add request parameters AudioLayer.$.Filter.
- Update API UpdateLiveStreamMonitor: add request parameters CallbackUrl.
- Update API UpdateLiveStreamMonitor: add request parameters DingTalkWebHookUrl.
- Update API UpdateLiveStreamMonitor: add request parameters MonitorConfig.


2022-12-05 Version: 1.1.1
- Live sdk update.

2022-12-05 Version: 1.1.0
- Live sdk update.

2022-10-31 Version: 1.0.3
- Live pre sdk test.

2021-05-07 Version: 1.0.2
- Generated python 2016-11-01 for live.

2021-05-07 Version: 0.0.2
- Generated python 2016-11-01 for live.

2021-04-23 Version: 1.0.1
- Generated python 2016-11-01 for live.

2021-01-10 Version: 1.0.0
- Generated python 2016-11-01 for live.

2020-11-16 Version: 0.0.1
- Generated python 2016-11-01 for live.

