# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConfigDeliveryChannelRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        compliant_snapshot: bool = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_condition: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
    ):
        # A client token. It is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests.
        # 
        # `ClientToken` can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Specifies whether to deliver compliance snapshots. Cloud Config delivers the compliance and non-compliance information of resources to SLS. Valid values:
        # 
        # - true: Deliver compliance snapshots.
        # 
        # - false: Do not deliver compliance snapshots.
        self.compliant_snapshot = compliant_snapshot
        # Specifies whether to deliver resource configuration histories. When the configuration of a resource changes, Cloud Config delivers the resource configuration history to OSS, SLS, or MNS. Valid values:
        # 
        # - true: Deliver resource configuration histories.
        # 
        # - false (default): Do not deliver resource configuration histories.
        # 
        # > * If the delivery channel is OSS, you must set at least one of `ConfigurationSnapshot` (scheduled resource snapshots) and `ConfigurationItemChangeNotification` (resource configuration histories) to true.
        # 
        # > - If the delivery channel is SLS, you must set at least one of `ConfigurationSnapshot` (scheduled resource snapshots), `CompliantSnapshot` (compliance snapshots), `ConfigurationItemChangeNotification` (resource configuration histories), and `NonCompliantNotification` (non-compliant events) to true.
        # 
        # > - If the delivery channel is MNS, you must set at least one of `ConfigurationItemChangeNotification` (resource configuration histories) and `NonCompliantNotification` (non-compliant events) to true.
        self.configuration_item_change_notification = configuration_item_change_notification
        # Specifies whether to deliver scheduled resource snapshots. Cloud Config delivers scheduled resource snapshots to OSS or SLS at `04:00Z` and `16:00Z` (UTC) every day. Valid values:
        # 
        # - true: Deliver scheduled resource snapshots.
        # 
        # - false (default): Do not deliver scheduled resource snapshots.
        # 
        # > * If the delivery channel is OSS, you must set at least one of `ConfigurationSnapshot` (scheduled resource snapshots) and `ConfigurationItemChangeNotification` (resource configuration histories) to true.
        # 
        # > - If the delivery channel is SLS, you must set at least one of `ConfigurationSnapshot` (scheduled resource snapshots), `ConfigurationItemChangeNotification` (resource configuration histories), `CompliantSnapshot` (compliance snapshots), and `NonCompliantNotification` (non-compliant events) to true.
        self.configuration_snapshot = configuration_snapshot
        # An additional rule for the delivery channel. Use this rule to specify filter conditions for subscriptions.
        # 
        # - If you subscribe to compliance events, you can specify the minimum risk level and resource types as follows:
        # 
        #   - To specify the minimum risk level of events, use `{"filterType":"RuleRiskLevel","value":"1","multiple":false}`.
        # 
        #     `value` specifies the risk level to filter. Valid values: 1 for high, 2 for medium, and 3 for low.
        # 
        #     `multiple` specifies whether the filter supports multiple values. The risk level filter supports only a single value. Therefore, set `multiple` to `false` when you deliver compliance events.
        # 
        #   - To specify the resource types of events, use `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #     `values` specifies the resource types to which you want to subscribe. The value is a JSON array of resource types.
        #     Example:
        #     `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        # 
        #     `multiple` specifies whether the filter supports multiple values. The resource type filter supports multiple values. If you select multiple resource types, set `multiple` to `true`.
        # 
        #   - You can also specify a risk level and resource types at the same time. Example:
        #     `[{"filterType":"RuleRiskLevel","value":"2","multiple":false},{"filterType":"ResourceType","values":["ACS::CDN::Domain","ACS::ActionTrail::Trail"],"multiple":true}]`
        # 
        # - If you subscribe to resource configuration deliveries, you can specify the resource types as `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #   `values` specifies the resource types that you want to deliver. The value is a JSON array of resource types.
        #   Example:
        #   `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        self.delivery_channel_condition = delivery_channel_condition
        # The name of the delivery channel.
        # 
        # > If you do not set this parameter, the value is left empty.
        self.delivery_channel_name = delivery_channel_name
        # The ARN of the delivery destination. Valid values:
        # 
        # - If the delivery channel is OSS, the value is in the format of `acs:oss:{RegionId}:{accountId}:{bucketName}`. Example: `acs:oss:cn-shanghai:100931896542****:new-bucket`.
        # 
        # - If the delivery channel is MNS, the value is in the format of `acs:mns:{RegionId}:{accountId}:/topics/{topicName}`. Example: `acs:mns:cn-shanghai:100931896542****:/topics/topic1`.
        # 
        # - If the delivery channel is SLS, the value is in the format of `acs:log:{RegionId}:{accountId}:project/{projectName}/logstore/{logstoreName}`. Example: `acs:log:cn-shanghai:100931896542****:project/project1/logstore/logstore1`.
        # 
        # This parameter is required.
        self.delivery_channel_target_arn = delivery_channel_target_arn
        # The type of the delivery channel. Valid values:
        # 
        # - OSS: Object Storage Service.
        # 
        # - MNS: Simple Message Queue (formerly MNS).
        # 
        # - SLS: Simple Log Service.
        # 
        # This parameter is required.
        self.delivery_channel_type = delivery_channel_type
        # The time when Cloud Config starts to deliver scheduled resource snapshots every day.
        # 
        # The value must be in the `HH:mmZ` format (UTC).
        # 
        # > When you enable scheduled resource snapshot delivery, you can use this parameter to customize the delivery time. If you do not set this parameter, the snapshots are delivered at `04:00Z` and `16:00Z` (UTC) by default.
        self.delivery_snapshot_time = delivery_snapshot_time
        # The description of the delivery channel.
        self.description = description
        # Specifies whether to deliver non-compliant events. When a resource is evaluated as non-compliant, Cloud Config delivers the non-compliant event to SLS or MNS. Valid values:
        # 
        # - true: Deliver non-compliant events.
        # 
        # - false (default): Do not deliver non-compliant events.
        # 
        # > * If the delivery channel is SLS, you must set at least one of `ConfigurationSnapshot` (scheduled resource snapshots), `CompliantSnapshot` (compliance snapshots), `ConfigurationItemChangeNotification` (resource configuration histories), and `NonCompliantNotification` (non-compliant events) to true.
        # 
        # > - If the delivery channel is MNS, you must set at least one of `ConfigurationItemChangeNotification` (resource configuration histories) and `NonCompliantNotification` (non-compliant events) to true.
        self.non_compliant_notification = non_compliant_notification
        # The ARN of the OSS bucket to which the oversized data is delivered when the size of the data exceeds the limit of the delivery channel. The format is `acs:oss:{RegionId}:{accountId}:{bucketName}`.
        # 
        # If you do not set this parameter, Cloud Config delivers only the summary of the data.
        # 
        # > This parameter is supported only for SLS and MNS delivery channels. The delivery channel limit for SLS is 1 MB. The delivery channel limit for MNS is 64 KB.
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compliant_snapshot is not None:
            result['CompliantSnapshot'] = self.compliant_snapshot

        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification

        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot

        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition

        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name

        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn

        if self.delivery_channel_type is not None:
            result['DeliveryChannelType'] = self.delivery_channel_type

        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time

        if self.description is not None:
            result['Description'] = self.description

        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification

        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CompliantSnapshot') is not None:
            self.compliant_snapshot = m.get('CompliantSnapshot')

        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')

        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')

        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')

        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')

        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')

        if m.get('DeliveryChannelType') is not None:
            self.delivery_channel_type = m.get('DeliveryChannelType')

        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')

        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')

        return self

