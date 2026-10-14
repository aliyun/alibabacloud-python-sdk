2026-10-14 Version: 2.0.0
- Support API CancelC2paBucketSignTask.
- Support API CreateC2paBucketSignTask.
- Support API CreateC2paSignTask.
- Support API CreateImageDefectDetectionTask.
- Support API CreateImageIncomeTaxDetectionTask.
- Support API CreateVideoTask.
- Support API CreateWatermarkEmbedTask.
- Support API CreateWatermarkExtractTask.
- Support API GetC2paSignResult.
- Support API GetImageDefectDetectionTaskResult.
- Support API GetImageIncomeTaxDetectionTaskResult.
- Support API GetVideoTaskResult.
- Support API GetWatermarkEmbedTaskResult.
- Support API GetWatermarkExtractTaskResult.
- Support API PauseC2paBucketSignTask.
- Support API ResumeC2paBucketSignTask.
- Update API CreateImageDetectionTask: add request parameters UseTamperSmallModel.
- Update API CreateImageDetectionTask: delete request parameters CredType.
- Update API CreateImageDetectionTask: delete request parameters ObjectKey.
- Update API CreateImageTask: delete request parameters Watermark.
- Update API CreateSensitiveScanTask: delete request parameters ObjectKey.
- Update API DetectAigcImage: delete request parameters ObjectKey.
- Update API DetectImageBasicInfo: delete request parameters ObjectKey.
- Update API GetImageDetectionTaskResult: add response parameters Body.Tamper.AiWatermark.
- Update API GetImageDetectionTaskResult: add response parameters Body.Tamper.FinalConclusion.
- Update API GetImageDetectionTaskResult: add response parameters Body.Tamper.MetadataAiFlag.
- Update API GetImageDetectionTaskResult: add response parameters Body.Tamper.MetadataAiSource.
- Update API GetImageDetectionTaskResult: add response parameters Body.Tamper.RiskLevel.
- Update API GetImageDetectionTaskResult: add response parameters Body.Tamper.BaseResults.Recap.
- Update API GetImageDetectionTaskResult: add response parameters Body.Tamper.BaseResults.Aigc.Risk.
- Update API GetImageDetectionTaskResult: add response parameters Body.Tamper.BaseResults.Aips.Risk.
- Update API GetImageDetectionTaskResult: delete response parameters Body.Tamper.RiskCode.
- Update API GetImageDetectionTaskResult: delete response parameters Body.Tamper.RiskReasons.
- Update API SignUserImage: delete request parameters ObjectKey.
- Update API VerifyImageSignature: delete request parameters ObjectKey.


2026-07-09 Version: 1.0.0
- Generated python 2026-05-11 for AIDeepSign.

