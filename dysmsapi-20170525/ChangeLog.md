2026-01-05 Version: 4.4.0
- Support API CreateSmsAppIcpRecord.
- Support API CreateSmsTrademark.
- Support API GetSmsTemplateList.
- Support API QuerySmsAppIcpRecord.
- Support API QuerySmsTrademark.


2025-12-11 Version: 4.3.1
- Update API CreateSmsSign: add request parameters AppIcpRecordId.
- Update API CreateSmsSign: add request parameters TrademarkId.
- Update API GetSmsSign: add response parameters Body.AppIcpRecordId.
- Update API GetSmsSign: add response parameters Body.TrademarkId.
- Update API QuerySmsSignList: add response parameters Body.SmsSignList.$.AppIcpRecordId.
- Update API QuerySmsSignList: add response parameters Body.SmsSignList.$.TrademarkId.
- Update API UpdateSmsSign: add request parameters AppIcpRecordId.
- Update API UpdateSmsSign: add request parameters TrademarkId.


2025-11-27 Version: 4.3.0
- Support API GetSmsOcrOssInfo.
- Update API QuerySmsTemplateList: add response parameters Body.SmsTemplateList.$.TrafficDriving.


2025-09-17 Version: 4.2.0
- Support API SendLogisticsSms.
- Support API VerifyLogisticsSmsMailNo.


2025-06-30 Version: 4.1.2
- Update API GetSmsSign: add response parameters Body.SignIspRegisterDetailList.


2025-05-27 Version: 4.1.1
- Update API QueryMobilesCardSupport: add request parameters EncryptType.


2025-04-23 Version: 4.1.0
- Support API DeleteSmsQualification.
- Support API QuerySingleSmsQualification.
- Support API QuerySmsQualificationRecord.
- Support API RequiredPhoneCode.
- Support API SubmitSmsQualification.
- Support API UpdateSmsQualification.
- Support API ValidPhoneCode.


2025-04-22 Version: 4.0.0
- Support API ChangeSignatureQualification.
- Support API CreateSmsAuthorizationLetter.
- Support API GetQualificationOssInfo.
- Support API QuerySmsAuthorizationLetter.
- Update API CreateSmsSign: update request parameters AuthorizationLetterId' type has changed.
- Update API CreateSmsSign: update request parameters AuthorizationLetterId' format has changed.
- Update API GetSmsSign: update response parameters Body.AuthorizationLetterId' type has changed.
- Update API GetSmsSign: update response parameters Body.AuthorizationLetterId' format has changed.
- Update API QuerySmsSignList: update response parameters Body.SmsSignList.$.AuthorizationLetterId' type has changed.
- Update API QuerySmsSignList: update response parameters Body.SmsSignList.$.AuthorizationLetterId' format has changed.
- Update API UpdateSmsSign: update request parameters AuthorizationLetterId' type has changed.
- Update API UpdateSmsSign: update request parameters AuthorizationLetterId' format has changed.


2025-04-16 Version: 3.1.3
- Update API CreateSmsSign: add request parameters AuthorizationLetterId.
- Update API GetSmsSign: add response parameters Body.AuthorizationLetterAuditPass.
- Update API GetSmsSign: add response parameters Body.AuthorizationLetterId.
- Update API QuerySmsSignList: add response parameters Body.SmsSignList.$.AuthorizationLetterId.
- Update API QuerySmsSignList: add response parameters Body.SmsSignList.$.authorizationLetterAuditPass.
- Update API UpdateSmsSign: add request parameters AuthorizationLetterId.


2025-03-26 Version: 3.1.2
- Update API GetSmsTemplate: add response parameters Body.VendorAuditStatus.


2025-01-03 Version: 3.1.1
- Update API GetSmsSign: update response param.
- Update API QueryExtCodeSign: update param ExtCode.
- Update API QueryExtCodeSign: update param SignName.


2024-10-24 Version: 3.1.0
- Support API AddExtCodeSign.
- Support API DeleteExtCodeSign.
- Support API GetCardSmsDetails.
- Support API QueryExtCodeSign.
- Support API UpdateExtCodeSign.


2024-06-25 Version: 3.0.0
- Support API CreateSmsSign.
- Support API CreateSmsTemplate.
- Support API GetOSSInfoForUploadFile.
- Support API GetSmsSign.
- Support API GetSmsTemplate.
- Support API UpdateSmsSign.
- Support API UpdateSmsTemplate.
- Update API CreateSmartShortUrl: add param OutId.
- Update API CreateSmartShortUrl: delete param Expiration.
- Update API CreateSmartShortUrl: delete param SourceName.
- Update API CreateSmartShortUrl: update param PhoneNumbers.
- Update API CreateSmartShortUrl: update param SourceUrl.
- Update API QueryPageSmartShortUrlLog: delete param ClickState.
- Update API QueryPageSmartShortUrlLog: delete param EndId.
- Update API QueryPageSmartShortUrlLog: delete param ShortName.
- Update API QueryPageSmartShortUrlLog: delete param StartId.
- Update API QueryPageSmartShortUrlLog: update param CreateDateEnd.
- Update API QueryPageSmartShortUrlLog: update param CreateDateStart.
- Update API QueryPageSmartShortUrlLog: update param PageNo.
- Update API QueryPageSmartShortUrlLog: update param PageSize.


2023-07-04 Version: 2.0.24
- Add CreateSmartShortUrl api.

2022-11-29 Version: 2.0.23
- Add custom content for QueryCardSmsTemplateReport.

2022-10-11 Version: 2.0.22
- Add custom content for QueryCardSmsTemplateReport.

2022-09-30 Version: 2.0.21
- Add custom content for SendBatchSms.

2022-09-29 Version: 2.0.20
- Add outId for SendBatchSms.

2022-09-28 Version: 2.0.19
- Upgrade formdata for CheckMobilesCardTemplateSupport.

2022-08-11 Version: 2.0.18
- Upgrade formdata for SendBatchSms.

2022-08-03 Version: 2.0.17
- Upgrade Service for SmsStatistics.

2022-07-14 Version: 2.0.16
- Upgrade Service for SmsTemplate.

2022-07-06 Version: 2.0.15
- Upgrade Service for SmsSign.

2022-07-06 Version: 2.0.14
- Upgrade Service for SmsSign.

2022-07-04 Version: 2.0.13
- Upgrade Service for CardSms.

2022-06-29 Version: 2.0.12
- Upgrade Service for Template and Sign.

2022-06-17 Version: 2.0.10
- Upgrade Service for CARDSMS.

2022-01-24 Version: 2.0.9
- Generated python 2017-05-25 for Dysmsapi.

2021-11-29 Version: 2.0.8
- Upgrade Service for SMS.

2021-11-16 Version: 2.0.7
- Upgrade Service for SMS.

2021-10-26 Version: 2.0.6
- Support Short Url for SMS.

2021-09-01 Version: 2.0.3
- Generated python 2017-05-25 for Dysmsapi.

2021-03-31 Version: 2.0.2
- Generated python 2017-05-25 for Dysmsapi.

2021-01-04 Version: 2.0.1
- AMP Version Change.

2020-12-29 Version: 2.0.0
- AMP Version Change.

