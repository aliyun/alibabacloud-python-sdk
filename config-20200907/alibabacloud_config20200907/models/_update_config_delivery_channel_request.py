# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConfigDeliveryChannelRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        compliant_snapshot: bool = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_condition: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
        status: int = None,
    ):
        # A client token used to ensure the idempotence of the request. Use a client to generate the token, and make sure that the token is unique among different requests.
        # 
        # The `ClientToken` parameter can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Specifies whether to deliver resource compliance snapshots. Cloud Config delivers resource compliance and non-compliance information to SLS. Valid values:
        # 
        # - true: The resource compliance snapshots are delivered.
        # 
        # - false: The resource compliance snapshots are not delivered.
        self.compliant_snapshot = compliant_snapshot
        # Specifies whether to deliver the resource configuration history. Cloud Config delivers the resource configuration history to OSS, SLS, or MNS when the configuration of a resource changes. Valid values:
        # 
        # - true: The resource configuration history is delivered.
        # 
        # - false (default): The resource configuration history is not delivered.
        # 
        # > This parameter is available for delivery channels of the OSS, SLS, and MNS types.
        self.configuration_item_change_notification = configuration_item_change_notification
        # Specifies whether to deliver scheduled resource snapshots. Cloud Config delivers scheduled resource snapshots to OSS or SLS at `04:00Z` and `16:00Z` (UTC) every day. Valid values:
        # 
        # - true: The scheduled resource snapshots are delivered.
        # 
        # - false (default): The scheduled resource snapshots are not delivered.
        self.configuration_snapshot = configuration_snapshot
        # The rule that is attached to the delivery channel. This parameter is applicable to all deliveries to MNS and snapshot deliveries to SLS.
        # 
        # - If you specify the minimum risk level of events and the resource types for an MNS subscription, use the following formats:
        # 
        #   - The minimum risk level of the subscribed events: `{"filterType":"RuleRiskLevel","value":"1","multiple":false}`.
        # 
        #     `value` specifies the risk level. Valid values: 1 (high risk), 2 (medium risk), and 3 (low risk).
        # 
        #   - The resource types of the subscribed events: `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #     `values` specifies the resource types of the subscribed events. The value is a JSON array.
        #     Example:
        #     `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        # 
        # - If you specify the resource types of snapshots delivered to SLS, use the following format: `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #   `values` specifies the resource types of the snapshots to deliver. The value is a JSON array.
        #   Example:
        #   `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        self.delivery_channel_condition = delivery_channel_condition
        # The ID of the delivery channel.
        # 
        # For more information about how to obtain the delivery channel ID, see [ListConfigDeliveryChannels](https://help.aliyun.com/document_detail/429841.html).
        # 
        # This parameter is required.
        self.delivery_channel_id = delivery_channel_id
        # The name of the delivery channel.
        self.delivery_channel_name = delivery_channel_name
        # The Alibaba Cloud Resource Name (ARN) of the delivery destination. Valid values:
        # 
        # - If the delivery channel is Object Storage Service (OSS), the value is in the format of `acs:oss:{RegionId}:{accountId}:{bucketName}`. Example: `acs:oss:cn-shanghai:100931896542****:new-bucket`.
        # 
        # - If the delivery channel is MNS, the value is in the format of `acs:mns:{RegionId}:{accountId}:/topics/{topicName}`. Example: `acs:mns:cn-shanghai:100931896542****:/topics/topic1`.
        # 
        # - If the delivery channel is Simple Log Service (SLS), the value is in the format of `acs:log:{RegionId}:{accountId}:project/{projectName}/logstore/{logstoreName}`. Example: `acs:log:cn-shanghai:100931896542****:project/project1/logstore/logstore1`.
        self.delivery_channel_target_arn = delivery_channel_target_arn
        # The time of day when the scheduled resource snapshot is delivered.
        # 
        # The value is in the `HH:mmZ` format. The time is in UTC.
        # 
        # > If you enable scheduled delivery of resource snapshots, use this parameter to specify a delivery time. If you do not specify this parameter, Cloud Config delivers the scheduled resource snapshots at `04:00Z` and `16:00Z` by default.
        self.delivery_snapshot_time = delivery_snapshot_time
        # The description of the delivery channel.
        self.description = description
        # Specifies whether to deliver resource non-compliance events. Cloud Config delivers resource non-compliance events to SLS or MNS when a resource is evaluated as non-compliant. Valid values:
        # 
        # - true: The resource non-compliance events are delivered.
        # 
        # - false (default): The resource non-compliance events are not delivered.
        # 
        # > This parameter is available only for delivery channels of the SLS and MNS types.
        self.non_compliant_notification = non_compliant_notification
        # The ARN of the OSS bucket where data is delivered when the data size exceeds the limit of the delivery channel. The value is in the format of `acs:oss:{RegionId}:{accountId}:{bucketName}`.
        # 
        # If you do not specify this parameter, Cloud Config delivers only the summary of the data.
        # 
        # > This parameter is available only for delivery channels of the SLS and MNS types. The maximum size of data that can be delivered to SLS is 1 MB. The maximum size of data that can be delivered to MNS is 64 KB.
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        # The status of the delivery channel. Valid values:
        # 
        # - 0: The delivery channel is disabled. Cloud Config retains the most recent delivery configuration and stops delivering resource data.
        # 
        # - 1 (default): The delivery channel is enabled.
        self.status = status

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

        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id

        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name

        if self.delivery_channel_target_arn is not None:
            result['DeliveryChannelTargetArn'] = self.delivery_channel_target_arn

        if self.delivery_snapshot_time is not None:
            result['DeliverySnapshotTime'] = self.delivery_snapshot_time

        if self.description is not None:
            result['Description'] = self.description

        if self.non_compliant_notification is not None:
            result['NonCompliantNotification'] = self.non_compliant_notification

        if self.oversized_data_osstarget_arn is not None:
            result['OversizedDataOSSTargetArn'] = self.oversized_data_osstarget_arn

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')

        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')

        if m.get('DeliveryChannelTargetArn') is not None:
            self.delivery_channel_target_arn = m.get('DeliveryChannelTargetArn')

        if m.get('DeliverySnapshotTime') is not None:
            self.delivery_snapshot_time = m.get('DeliverySnapshotTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NonCompliantNotification') is not None:
            self.non_compliant_notification = m.get('NonCompliantNotification')

        if m.get('OversizedDataOSSTargetArn') is not None:
            self.oversized_data_osstarget_arn = m.get('OversizedDataOSSTargetArn')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

