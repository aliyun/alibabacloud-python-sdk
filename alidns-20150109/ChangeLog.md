2026-01-16 Version: 4.2.0
- Support API SetCloudGtmInstanceConfigLogSwitch.


2026-01-15 Version: 4.1.1
- Update API DescribeCloudGtmGlobalAlert: add response parameters Body.AlertConfig.$.Threshold.
- Update API DescribeInternetDnsLogs: add response parameters Body.Logs.$.Flags.
- Update API DescribeInternetDnsLogs: add response parameters Body.Logs.$.QueryFlags.
- Update API DescribeInternetDnsLogs: add response parameters Body.Logs.$.ResponseTimestamp.
- Update API ListCloudGtmInstanceConfigs: add response parameters Body.InstanceConfigs.$.ConfigLoggingSwitchStatus.
- Update API SearchCloudGtmInstanceConfigs: add response parameters Body.InstanceConfigs.$.ConfigLoggingSwitchStatus.
- Update API UpdateCloudGtmGlobalAlert: add request parameters AlertConfig.$.Threshold.


2025-12-30 Version: 4.1.0
- Support API AddRspDomainServerHoldStatusForGateway.
- Update API DescribePdnsAppKeys: add response parameters Body.AppKeys.$.BindEdgeDnsClusters.


2025-12-30 Version: 4.1.0
- Support API AddRspDomainServerHoldStatusForGateway.
- Update API DescribePdnsAppKeys: add response parameters Body.AppKeys.$.BindEdgeDnsClusters.


2025-12-04 Version: 4.0.0
- Support API RemoveRspDomainServerHoldStatusForGateway.
- Support API UpdateRspDomainServerProhibitStatusForGateway.
- Delete API UpdateRspDomainServerHoldStatusOte.
- Delete API UpdateRspDomainStatusOte.


2025-11-13 Version: 3.7.0
- Support API UpdateRspDomainServerHoldStatusOte.
- Support API UpdateRspDomainStatusOte.


2025-10-14 Version: 3.6.1
- Update API CreateCloudGtmInstanceConfig: add request parameters ChargeType.
- Update API CreateCloudGtmInstanceConfig: add response parameters Body.InstanceId.
- Update API ListCloudGtmInstances: add request parameters ChargeType.
- Update API ListCloudGtmInstances: add response parameters Body.Instances.$.ChargeType.
- Update API SearchCloudGtmInstances: add request parameters ChargeType.
- Update API SearchCloudGtmInstances: add response parameters Body.Instances.$.ChargeType.


2025-09-09 Version: 3.6.0
- Support API AddRecursionRecord.
- Support API AddRecursionZone.
- Support API DeleteRecursionRecord.
- Support API DeleteRecursionZone.
- Support API DescribeRecursionRecord.
- Support API DescribeRecursionZone.
- Support API ListRecursionRecords.
- Support API ListRecursionZones.
- Support API SearchRecursionRecords.
- Support API SearchRecursionZones.
- Support API UpdateRecursionRecord.
- Support API UpdateRecursionRecordEnableStatus.
- Support API UpdateRecursionRecordRemark.
- Support API UpdateRecursionRecordWeight.
- Support API UpdateRecursionRecordWeightEnableStatus.
- Support API UpdateRecursionZoneEffectiveScope.
- Support API UpdateRecursionZoneProxyPattern.
- Support API UpdateRecursionZoneRemark.


2025-07-25 Version: 3.5.10
- Update API DescribeDomainRecords: add response parameters Body.DomainRecords.$.LbaStatus.


2025-06-27 Version: 3.5.9
- Update API DescribeDomains: add response parameters Body.Domains.$.SlaveDnsStatus.
- Update API DescribeInternetDnsLogs: add request parameters RecursionProtocolType.
- Update API DescribePdnsOperateLogs: add request parameters ResourceType.


2025-04-23 Version: 3.5.8
- Update API DescribeCustomLines: add response parameters Body.CustomLines.$.IpSegmentList.


2025-02-10 Version: 3.5.7
- Update API DescribeIspFlushCacheTask: update param TaskId.
- Update API DescribePdnsUserInfo: update response param.


2024-10-18 Version: 3.5.6
- Update API AddDomainRecord: update param Priority.
- Update API CreatePdnsAppKey: add param Remark.
- Update API DescribePdnsAppKey: update response param.
- Update API DescribePdnsAppKeys: update response param.
- Update API DescribePdnsRequestStatistic: add param Type.
- Update API DescribePdnsUdpIpSegments: update response param.
- Update API DescribePdnsUserInfo: update response param.
- Update API UpdateDomainRecord: update param Priority.


2024-08-28 Version: 3.5.5
- Update API DescribePdnsUdpIpSegments: update response param.
- Update API DescribePdnsUserInfo: update response param.


2024-08-20 Version: 3.5.4
- Update API DescribeInternetDnsLogs: update response param.


2024-08-01 Version: 3.5.3
- Update API CreatePdnsUdpIpSegment: add param IpToken.
- Update API ValidatePdnsUdpIpSegment: add param IpToken.


2024-07-30 Version: 3.5.2
- Update API DescribePdnsUdpIpSegments: update response param.


2024-07-19 Version: 3.5.1
- Update API DescribePdnsUserInfo: update response param.
- Update API GetTxtRecordForVerify: update response param.


2024-05-28 Version: 3.5.0
- Support API CreateCloudGtmAddress.
- Support API CreateCloudGtmAddressPool.
- Support API CreateCloudGtmInstanceConfig.
- Support API CreateCloudGtmMonitorTemplate.
- Support API DeleteCloudGtmAddress.
- Support API DeleteCloudGtmAddressPool.
- Support API DeleteCloudGtmInstanceConfig.
- Support API DeleteCloudGtmMonitorTemplate.
- Support API DescribeCloudGtmAddress.
- Support API DescribeCloudGtmAddressPoolReference.
- Support API DescribeCloudGtmAddressReference.
- Support API DescribeCloudGtmGlobalAlert.
- Support API DescribeCloudGtmInstanceConfigAlert.
- Support API DescribeCloudGtmInstanceConfigFullInfo.
- Support API DescribeCloudGtmMonitorTemplate.
- Support API DescribeCloudGtmSummary.
- Support API DescribeCloudGtmSystemLines.
- Support API ListCloudGtmAddressPools.
- Support API ListCloudGtmAddresses.
- Support API ListCloudGtmAlertLogs.
- Support API ListCloudGtmAvailableAlertGroups.
- Support API ListCloudGtmInstanceConfigs.
- Support API ListCloudGtmInstances.
- Support API ListCloudGtmMonitorNodes.
- Support API ListCloudGtmMonitorTemplates.
- Support API ReplaceCloudGtmAddressPoolAddress.
- Support API ReplaceCloudGtmInstanceConfigAddressPool.
- Support API SearchCloudGtmAddressPools.
- Support API SearchCloudGtmAddresses.
- Support API SearchCloudGtmInstanceConfigs.
- Support API SearchCloudGtmInstances.
- Support API SearchCloudGtmMonitorTemplates.
- Support API UpdateCloudGtmAddress.
- Support API UpdateCloudGtmAddressEnableStatus.
- Support API UpdateCloudGtmAddressManualAvailableStatus.
- Support API UpdateCloudGtmAddressPoolBasicConfig.
- Support API UpdateCloudGtmAddressPoolEnableStatus.
- Support API UpdateCloudGtmAddressPoolLbStrategy.
- Support API UpdateCloudGtmAddressPoolRemark.
- Support API UpdateCloudGtmAddressRemark.
- Support API UpdateCloudGtmGlobalAlert.
- Support API UpdateCloudGtmInstanceConfigAlert.
- Support API UpdateCloudGtmInstanceConfigBasic.
- Support API UpdateCloudGtmInstanceConfigEnableStatus.
- Support API UpdateCloudGtmInstanceConfigLbStrategy.
- Support API UpdateCloudGtmInstanceConfigRemark.
- Support API UpdateCloudGtmInstanceName.
- Support API UpdateCloudGtmMonitorTemplate.
- Support API UpdateCloudGtmMonitorTemplateRemark.


2024-05-27 Version: 3.4.0
- Support API DescribeCloudGtmAddressPool.
- Support API DescribeInternetDnsLogs.
- Update API DescribePdnsAppKey: add param AuthCode.
- Update API DescribePdnsAppKey: update response param.
- Update API DescribePdnsAppKeys: update response param.


2024-05-22 Version: 3.3.0
- Support API DescribeInternetDnsLogs.
- Update API DescribePdnsAppKey: add param AuthCode.
- Update API DescribePdnsAppKey: update response param.
- Update API DescribePdnsAppKeys: update response param.


2024-03-13 Version: 3.2.0
- Support API DescribeInternetDnsLogs.
- Update API DescribePdnsAppKey: add param AuthCode.
- Update API DescribePdnsAppKey: update response param.
- Update API DescribePdnsAppKeys: update response param.


2024-03-01 Version: 3.1.0
- Support API DescribeInternetDnsLogs.


2024-01-29 Version: 3.0.13
- Generated python 2015-01-09 for Alidns.

2024-01-18 Version: 3.0.12
- Generated python 2015-01-09 for Alidns.

2024-01-17 Version: 3.0.11
- Generated python 2015-01-09 for Alidns.

2023-11-23 Version: 3.0.10
- Generated python 2015-01-09 for Alidns.

2023-10-12 Version: 3.0.9
- Generated python 2015-01-09 for Alidns.

2023-09-22 Version: 3.0.8
- Generated python 2015-01-09 for Alidns.

2023-05-11 Version: 3.0.7
- Supported sorting for DescribeDnsProduceInstances.

2023-04-04 Version: 3.0.3
- New Resolve Statistic Summary API.

2023-04-03 Version: 3.0.2
- New Resolve Statistic Summary API.

2022-11-23 Version: 3.0.1
- Api DescribeSubDomainRecords add Remark field.

2022-08-18 Version: 3.0.0
- Bump version.

2021-03-30 Version: 2.0.2
- Generated python 2015-01-09 for Alidns.

2021-02-08 Version: 2.0.1
- Generated python 2015-01-09 for Alidns.

2021-02-03 Version: 1.0.2
- Generated python 2015-01-09 for Alidns.

2021-02-03 Version: 1.0.1
- Generated python 2015-01-09 for Alidns.

2020-12-29 Version: 2.0.0
- AMP Version Change.

