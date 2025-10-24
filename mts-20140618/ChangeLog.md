2025-10-24 Version: 6.0.1
- Update API QueryMediaInfoJobList: add response parameters Body.MediaInfoJobList.$.Properties.FileMd5.
- Update API QueryMediaInfoJobList: add response parameters Body.MediaInfoJobList.$.Properties.Streams.AudioStreamList.$.DurationInaccurate.
- Update API QueryMediaInfoJobList: add response parameters Body.MediaInfoJobList.$.Properties.Streams.VideoStreamList.$.DurationInaccurate.
- Update API SubmitMediaInfoJob: add request parameters Config.
- Update API SubmitMediaInfoJob: add response parameters Body.MediaInfoJob.Properties.MD5.
- Update API SubmitMediaInfoJob: add response parameters Body.MediaInfoJob.Properties.Streams.AudioStreamList.$.DurationInaccurate.
- Update API SubmitMediaInfoJob: add response parameters Body.MediaInfoJob.Properties.Streams.VideoStreamList.$.DurationInaccurate.


2025-05-14 Version: 6.0.0
- Update API SubmitCopyrightJob: update request parameters StartTime' type has changed.
- Update API SubmitCopyrightJob: update request parameters StartTime' format has changed.
- Update API SubmitCopyrightJob: update request parameters TotalTime' type has changed.
- Update API SubmitCopyrightJob: update request parameters TotalTime' format has changed.
- Update API SubmitTraceAbJob: update request parameters StartTime' type has changed.
- Update API SubmitTraceAbJob: update request parameters StartTime' format has changed.
- Update API SubmitTraceAbJob: update request parameters TotalTime' type has changed.
- Update API SubmitTraceAbJob: update request parameters TotalTime' format has changed.


2025-05-12 Version: 5.0.3
- Update API AddSmarttagTemplate: add request parameters TemplateConfig.
- Update API UpdateSmarttagTemplate: add request parameters TemplateConfig.


2025-03-17 Version: 5.0.2
- Update API AddSmarttagTemplate: add param LabelCustomCategoryIds.
- Update API AddSmarttagTemplate: add param LabelCustomParamsConfig.
- Update API RegisterCustomView: add param LabelPrompt.
- Update API RegisterCustomView: update param ImageUrl.


2024-10-16 Version: 5.0.1
- Update API QuerySmarttagJob: update param AccessKeyId.
- Update API QuerySmarttagJob: update response param.
- Update API RegisterCustomFace: add param PersonName.
- Update API RegisterCustomFace: update param AccessKeyId.
- Update API SubmitMediaCensorJob: update param PipelineId.


2024-07-23 Version: 5.0.0
- Update API SubmitCopyrightJob: update param Level.
- Update API SubmitImageCopyright: update param Output.
- Update API SubmitImageCopyright: update param Params.
- Update API SubmitTraceAbJob: update param Level.
- Update API SubmitTraceM3u8Job: update param MediaId.
- Update API SubmitTraceM3u8Job: update param Output.
- Update API SubmitTraceM3u8Job: update param Trace.


2024-07-11 Version: 4.2.0
- Support API SubmitImageCopyright.


2024-07-10 Version: 4.1.0
- Support API QueryCopyrightExtractJob.
- Support API QueryCopyrightJob.
- Support API QueryTraceAbJob.
- Support API QueryTraceExtractJob.
- Support API QueryTraceM3u8Job.
- Support API SubmitCopyrightExtractJob.
- Support API SubmitCopyrightJob.
- Support API SubmitTraceAbJob.
- Support API SubmitTraceExtractJob.
- Support API SubmitTraceM3u8Job.


2024-07-05 Version: 4.0.0
- Delete API QuerySnapshotJobListV2.
- Delete API QueryVideoQualityJob.
- Delete API ReportFpShotJobResult.
- Delete API SubmitVideoQualityJob.
- Update API AddPipeline: delete param ExtendConfig.
- Update API AddPipeline: update response param.
- Update API AddTemplate: update response param.
- Update API QueryJobList: delete param IncludePipelineInfo.
- Update API QueryJobList: update response param.
- Update API QueryMediaCensorJobDetail: update response param.
- Update API QueryMediaCensorJobList: update response param.
- Update API QuerySnapshotJobList: update response param.
- Update API QueryTemplateList: update response param.
- Update API SearchPipeline: update response param.
- Update API SearchTemplate: add param NamePrefix.
- Update API SearchTemplate: update response param.
- Update API SubmitSmarttagJob: add param Priority.
- Update API SubmitSnapshotJob: update response param.
- Update API UpdateMediaWorkflow: add param Name.
- Update API UpdateMediaWorkflow: add param TriggerMode.
- Update API UpdatePipeline: update response param.
- Update API UpdateTemplate: update response param.


2023-02-27 Version: 3.3.42
- Add CreateCustomGroup api sdk.

2022-07-14 Version: 3.3.41
- AMP version.

2021-12-30 Version: 3.3.40
- Add faceCustomParamsConfig params for AddSmarttagTemplate,UpdateSmarttagTemplate,QuerySmarttagTemplateList interface.

2021-12-09 Version: 3.3.39
- Support params for QuerySmarttagJob Api.
- Support params for AddSmarttagTemplate,UpdateSmarttagTemplate,QuerySmarttagTemplateList Api.

2021-09-14 Version: 3.3.28
- Add URL for SubmitCensorJob.

2021-09-01 Version: 3.3.25
- SubmitURLUploadJob, support S3 Storage.

2021-08-11 Version: 3.3.23
- SubmitURLUploadJob.
- GetJobInfo.

2021-03-31 Version: 1.0.2
- Generated python 2014-06-18 for Mts.

2021-03-16 Version: 1.0.1
- Generated python 2014-06-18 for Mts.

2021-01-10 Version: 1.0.0
- Generated python 2014-06-18 for Mts.

