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
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must ensure that the token is unique among different requests.
        # 
        # The `token` can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Specifies whether to deliver scheduled compliant snapshots. Cloud Config delivers scheduled compliant snapshots at `04:00Z` and `16:00Z` to  Log Service every day. The time is displayed in UTC. Valid values:
        # 
        # *   true: Cloud Config delivers compliant snapshots.
        # *   false (default): Cloud Config does not deliver scheduled compliant snapshots.
        self.compliant_snapshot = compliant_snapshot
        # Specifies whether to deliver resource change logs. If you set this parameter to true, Cloud Config delivers resource change logs to OSS, Log Service, or MNS when the configurations of the resources change. Valid values:
        # 
        # *   true: Cloud Config delivers resource change logs.
        # *   false (default): Cloud Config does not deliver resource change logs.
        # 
        # > This parameter is available for delivery channels of the OSS, SLS, and MNS types.
        self.configuration_item_change_notification = configuration_item_change_notification
        # Specifies whether to deliver scheduled resource snapshots. Cloud Config delivers scheduled resource snapshots at `04:00Z` and `16:00Z` to OSS, MNS, or Log Service every day. The time is displayed in UTC. Valid values:
        # 
        # *   true: Cloud Config delivers scheduled resource snapshots.
        # *   false (default): Cloud Config does not deliver scheduled resource snapshots.
        self.configuration_snapshot = configuration_snapshot
        # The rule that you want to attach to the delivery channel. This parameter is available when you deliver data of all types to MNS or deliver snapshots to Log Service.
        # 
        # *   If the value of the DeliveryChannelType parameter is MNS, take note of the following settings of the lowest risk level and resource types of the events to which you subscribed:
        # 
        #     *   The setting of the lowest risk level for the events to which you want to subscribe is in the following format: `{"filterType":"RuleRiskLevel","value":"1","multiple":false}`.
        # 
        #         The `value` field indicates the lowest risk level of the events to which you want to subscribe. Valid values: 1, 2, and 3. The value 1 indicates the high risk level, the value 2 indicates the medium risk level, and the value 3 indicates the low risk level.
        # 
        #     *   The setting of the resource types of the events to which you want to subscribe is in the following format: `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #         The `values` field indicates the resource types of the events to which you want to subscribe. The value of the field is a JSON array. Examples:
        # 
        # `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        # 
        # *   If you set the DeliveryChannelType parameter to SLS, the setting of the resource types of the snapshots to which you want to deliver is in the following format: `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #     The `values` field specifies the resource types of the snapshots to which you want to deliver. The value of the field is a JSON array. Examples:
        # 
        # `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        self.delivery_channel_condition = delivery_channel_condition
        # The ID of the delivery channel.
        # 
        # For more information about how to obtain the ID of a delivery channel, see [DescribeDeliveryChannels](https://help.aliyun.com/document_detail/429841.html).
        # 
        # This parameter is required.
        self.delivery_channel_id = delivery_channel_id
        # The name of the delivery channel.
        self.delivery_channel_name = delivery_channel_name
        # The Alibaba Cloud Resource Name (ARN) of the delivery destination. Valid values:
        # 
        # *   `acs:oss:{RegionId}:{accountId}:{bucketName}` if your delivery destination is an OSS bucket. Example: `acs:oss:cn-shanghai:100931896542****:new-bucket`.
        # *   `acs:mns:{RegionId}:{accountId}:/topics/{topicName}` if your delivery destination is an MNS topic. Example: `acs:mns:cn-shanghai:100931896542****:/topics/topic1`.
        # *   `acs:log:{RegionId}:{accountId}:project/{projectName}/logstore/{logstoreName}` if your delivery destination is a Log Service Logstore. Example: `acs:log:cn-shanghai:100931896542****:project/project1/logstore/logstore1`.
        self.delivery_channel_target_arn = delivery_channel_target_arn
        # The time when you want Cloud Config to deliver scheduled resource snapshots every day.
        # 
        # Format: `HH:mmZ`. This time is displayed in UTC.
        # 
        # > When you enable the scheduled resource delivery feature, you can configure this parameter to specify a custom delivery time. If you do not configure this parameter, Cloud Config automatically delivers scheduled resource snapshots at `04:00Z` and `16:00Z` every day.
        self.delivery_snapshot_time = delivery_snapshot_time
        # The description of the delivery channel.
        self.description = description
        # Specifies whether to deliver resource non-compliance events. If you set this parameter to true, Cloud Config delivers resource non-compliance events to Log Service or MNS when resources are considered non-compliant. Valid values:
        # 
        # *   true: Cloud Config delivers resource non-compliance events.
        # *   false (default): Cloud Config does not deliver resource non-compliance events.
        # 
        # > This parameter is available only for delivery channels of the SLS or MNS type.
        self.non_compliant_notification = non_compliant_notification
        # The ARN of the OSS bucket to which you want to transfer the delivery data when the size of the data exceeds the specified upper limit of the delivery channel. Format: `acs:oss:{RegionId}:{accountId}:{bucketName}`.
        # 
        # If you do not configure this parameter, Cloud Config delivers only summary data.
        # 
        # > This parameter is available only for delivery channels of the SLS or MNS type. The maximum storage size of delivery channels of the SLS type is 1 MB, and the maximum storage size of delivery channels of the MNS type is 64 KB.
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        # Specifies whether to enable the delivery channel. Valid values:
        # 
        # *   0: Cloud Config disables the delivery channel. Cloud Config retains the most recent delivery configuration and stops resource data delivery.
        # *   1 (default): Cloud Config enables the delivery channel.
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

