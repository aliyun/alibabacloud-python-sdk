2026-01-16 Version: 1.8.2
- Update API BatchSendMail: add request parameters DomainAuth.
- Update API SingleSendMail: add request parameters DomainAuth.


2025-12-22 Version: 1.8.1
- Update API SingleSendMail: add request parameters BccAddress.


2025-12-19 Version: 1.8.0
- Support API ListValidateFile.
- Update API GetValidateFileStatus: add response parameters Body.FileId.


2025-11-20 Version: 1.7.2
- Update API ValidateEmail: add request parameters CheckGraylist.


2025-10-29 Version: 1.7.1
- Generated python 2015-11-23 for Dm.

2025-10-23 Version: 1.7.0
- Support API CheckDisposable.
- Support API ConfigSetCancelRelationFromAddress.
- Support API ConfigSetCreate.
- Support API ConfigSetDelete.
- Support API ConfigSetDetail.
- Support API ConfigSetList.
- Support API ConfigSetRelationFromAddress.
- Support API ConfigSetUpdate.
- Support API DeleteValidateFile.
- Support API DescTemplate.
- Support API GetValidateFile.
- Support API GetValidateFileStatus.
- Support API GetValidationQuota.
- Support API QueryTemplateByParam.
- Support API SendValidateFile.
- Support API ValidateEmail.
- Update API SaveReceiverDetail: add request parameters CustomDetail.
- Update API SaveReceiverDetail: add response parameters Body.Data.$.ErrMessage.
- Update API SendTestByTemplate: add request parameters TemplateParams.
- Update API SingleSendMail: add request parameters Template.


2025-09-03 Version: 1.6.2
- Update API DedicatedIpPoolList: add request parameters All.
- Update API GetTrackList: add request parameters ConfigSetId.
- Update API GetTrackListByMailFromAndTagName: add request parameters ConfigSetId.
- Update API QueryMailAddressByParam: add response parameters Body.data.$.ConfigSetId.
- Update API QueryMailAddressByParam: add response parameters Body.data.$.ConfigSetName.
- Update API QueryTaskByParam: add response parameters Body.data.$.ConfigSetId.
- Update API QueryTaskByParam: add response parameters Body.data.$.ConfigSetName.
- Update API SenderStatisticsDetailByParam: add request parameters ConfigSetId.
- Update API SenderStatisticsDetailByParam: add request parameters IpPoolId.
- Update API SenderStatisticsDetailByParam: add response parameters Body.data.$.ConfigSetId.
- Update API SenderStatisticsDetailByParam: add response parameters Body.data.$.ConfigSetName.
- Update API SenderStatisticsDetailByParam: add response parameters Body.data.$.IpPoolId.
- Update API SenderStatisticsDetailByParam: add response parameters Body.data.$.IpPoolName.


2025-08-06 Version: 1.6.1
- Update API DedicatedIpList: add response parameters Body.Ips.$.ZoneId.
- Update API DedicatedIpNonePoolList: add response parameters Body.Ips.$.ZoneId.
- Update API DedicatedIpPoolList: add response parameters Body.IpPools.$.Ips.$.ZoneId.


2025-08-05 Version: 1.6.0
- Support API GetDedicatedIpWarmUpDetail.
- Support API GetDedicatedIpWarmUpInfo.
- Update API DedicatedIpList: add response parameters Body.Ips.$.IpExt.LastWarmUpTypeChangedTime.


2025-07-28 Version: 1.5.0
- Support API ListBlockSending.
- Update API DescAccountSummary: add response parameters Body.IpChannelType.


2025-07-21 Version: 1.4.0
- Support API DedicatedIpAutoRenewal.
- Support API DedicatedIpChangeWarmupType.
- Support API DedicatedIpList.
- Support API DedicatedIpNonePoolList.
- Support API DedicatedIpPoolCreate.
- Support API DedicatedIpPoolDelete.
- Support API DedicatedIpPoolList.
- Support API DedicatedIpPoolUpdate.
- Support API UnblockSending.


2025-06-23 Version: 1.3.0
- Support API ChangeDomainDkimRecord.
- Update API DescDomain: add response parameters Body.DkimRsaLength.


2025-06-20 Version: 1.2.7
- Update API SingleSendMail: add request parameters Attachments.


2025-06-17 Version: 1.2.6
- Update API BatchSendMail: add request parameters IpPoolId.
- Update API QueryTaskByParam: add response parameters Body.data.$.IpPoolId.
- Update API QueryTaskByParam: add response parameters Body.data.$.IpPoolName.
- Update API SingleSendMail: add request parameters IpPoolId.


2025-06-13 Version: 1.2.5
- Update API GetTrackList: add request parameters DedicatedIp.
- Update API GetTrackList: add request parameters DedicatedIpPoolId.
- Update API GetTrackList: add request parameters Esp.
- Update API GetTrackList: add response parameters Body.TotalPages.
- Update API GetTrackListByMailFromAndTagName: add request parameters DedicatedIp.
- Update API GetTrackListByMailFromAndTagName: add request parameters DedicatedIpPoolId.
- Update API GetTrackListByMailFromAndTagName: add request parameters Esp.
- Update API GetTrackListByMailFromAndTagName: add response parameters Body.TotalPages.
- Update API SenderStatisticsByTagNameAndBatchID: add request parameters DedicatedIp.
- Update API SenderStatisticsByTagNameAndBatchID: add request parameters DedicatedIpPoolId.
- Update API SenderStatisticsByTagNameAndBatchID: add request parameters Esp.


2025-05-26 Version: 1.2.4
- Update API CreateDomain: add request parameters dkimSelector.


2025-01-10 Version: 1.2.3
- Update API BatchSendMail: add param Headers.
- Update API SingleSendMail: add param Headers.
- Update API SingleSendMail: update param ResourceOwnerAccount.


2024-07-31 Version: 1.2.2
- Update API DescAccountSummary: update response param.


2024-07-16 Version: 1.2.1
- Update API GetTrackList: add param AccountName.
- Update API GetTrackList: add param TagName.


2024-05-30 Version: 1.2.0
- Support API GetUser.
- Support API UpdateUser.


2024-05-20 Version: 1.1.2
- Generated python 2015-11-23 for Dm.

2024-05-15 Version: 1.1.1
- Generated python 2015-11-23 for Dm.

2024-04-22 Version: 1.1.0
- Support API CreateUserSuppression.
- Support API GetSuppressionListLevel.
- Support API ListUserSuppression.
- Support API RemoveUserSuppression.
- Support API SetSuppressionListLevel.
- Update API BatchSendMail: add param UnSubscribeFilterLevel.
- Update API BatchSendMail: add param UnSubscribeLinkType.
- Update API SenderStatisticsDetailByParam: update response param.
- Update API SingleSendMail: add param UnSubscribeFilterLevel.
- Update API SingleSendMail: add param UnSubscribeLinkType.


2024-03-13 Version: 1.0.12
- Update API BatchSendMail: add param UnSubscribeFilterLevel.
- Update API BatchSendMail: add param UnSubscribeLinkType.
- Update API SenderStatisticsDetailByParam: update response param.
- Update API SingleSendMail: add param UnSubscribeFilterLevel.
- Update API SingleSendMail: add param UnSubscribeLinkType.


2024-02-20 Version: 1.0.11
- Update API BatchSendMail: add param UnSubscribeFilterLevel.
- Update API BatchSendMail: add param UnSubscribeLinkType.
- Update API SingleSendMail: add param UnSubscribeFilterLevel.
- Update API SingleSendMail: add param UnSubscribeLinkType.


2024-01-15 Version: 1.0.10
- Generated python 2015-11-23 for Dm.

2023-12-12 Version: 1.0.9
- Generated python 2015-11-23 for Dm.

2023-09-13 Version: 1.0.8
- Generated python 2015-11-23 for Dm.

2023-08-29 Version: 1.0.7
- Generated python 2015-11-23 for Dm.

2023-07-27 Version: 1.0.6
- Fix bugs for GetTrackList and GetTrackListByMailFromAndTagName.
- Fixed bugs for GetTrackListByMailFromAndTagName.
- Add field SpfRecordV2, DkimRR, DkimPublicKey, DkimAuthStatus.

2022-09-29 Version: 1.0.5
- Automatically generate sdk tasks.

2022-08-02 Version: 1.0.4
- The input parameter IpProtection of UpdateIpProtection API  is corrected to be required. 

2022-05-20 Version: 1.0.3
- Ip related APIs are changed to visiable and QPM is set as 60 .

2022-04-21 Version: 1.0.2
- Some APIs are changed to invisiable.
- Wrong type of SenderStatisticsDetailByParam reponse fields is fixed.

2022-04-13 Version: 1.0.1
- Some APIs are changed to invisiable.
- Wrong type of QueryInvalidAddress reponse fields is fixed.

2020-12-30 Version: 1.0.0
- AMP Version Change.

