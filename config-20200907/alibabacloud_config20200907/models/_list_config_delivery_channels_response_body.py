# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListConfigDeliveryChannelsResponseBody(DaraModel):
    def __init__(
        self,
        delivery_channels: List[main_models.ListConfigDeliveryChannelsResponseBodyDeliveryChannels] = None,
        request_id: str = None,
    ):
        # A list of delivery channels.
        self.delivery_channels = delivery_channels
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.delivery_channels:
            for v1 in self.delivery_channels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeliveryChannels'] = []
        if self.delivery_channels is not None:
            for k1 in self.delivery_channels:
                result['DeliveryChannels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_channels = []
        if m.get('DeliveryChannels') is not None:
            for k1 in m.get('DeliveryChannels'):
                temp_model = main_models.ListConfigDeliveryChannelsResponseBodyDeliveryChannels()
                self.delivery_channels.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConfigDeliveryChannelsResponseBodyDeliveryChannels(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        compliant_snapshot: bool = None,
        configuration_item_change_notification: bool = None,
        configuration_snapshot: bool = None,
        delivery_channel_assume_role_arn: str = None,
        delivery_channel_condition: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        delivery_channel_target_arn: str = None,
        delivery_channel_type: str = None,
        delivery_snapshot_time: str = None,
        description: str = None,
        non_compliant_notification: bool = None,
        oversized_data_osstarget_arn: str = None,
        status: int = None,
    ):
        # The ID of the current Alibaba Cloud account.
        self.account_id = account_id
        # Specifies whether to receive compliance snapshots. Cloud Config delivers resource compliance and non-compliance information to SLS. Valid values:
        # 
        # - true: Receive compliance snapshots.
        # 
        # - false: Do not receive compliance snapshots.
        self.compliant_snapshot = compliant_snapshot
        # Specifies whether to receive the resource configuration history. When a resource configuration changes, Cloud Config delivers the resource configuration history to OSS, SLS, or MNS. Valid values:
        # 
        # - true: Receive the resource configuration history.
        # 
        # - false: Do not receive the resource configuration history.
        self.configuration_item_change_notification = configuration_item_change_notification
        # Specifies whether to receive scheduled resource snapshots. Cloud Config delivers scheduled resource snapshots to OSS or SLS at `04:00Z` and `16:00Z` (UTC) every day. Valid values:
        # 
        # - true: Receive scheduled resource snapshots.
        # 
        # - false: Do not receive scheduled resource snapshots.
        self.configuration_snapshot = configuration_snapshot
        # The ARN of the role that is assumed by the delivery channel.
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        # The rule attached to the delivery channel. This parameter is supported for MNS channels and for snapshot delivery to SLS channels.
        # 
        # - To subscribe to MNS events, specify the minimum risk level and resource types:
        # 
        #   - Minimum risk level of subscribed events: `{"filterType":"RuleRiskLevel","value":"1","multiple":false}`.
        # 
        #     \\`value\\` specifies the risk level. Valid values: 1 (high risk), 2 (medium risk), and 3 (low risk).
        # 
        #   - Resource types of subscribed events: `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #     \\`values\\` is a JSON array of the resource types.
        #     Example:
        #     `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        # 
        # - To deliver snapshots to SLS, specify the resource types: `{"filterType":"ResourceType","values":["ACS::ACK::Cluster","ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage"],"multiple":true}`.
        # 
        #   \\`values\\` is a JSON array of the resource types.
        #   Example:
        #   `[{"filterType":"ResourceType","values":["ACS::ActionTrail::Trail","ACS::CBWP::CommonBandwidthPackage","ACS::CDN::Domain","ACS::CEN::CenBandwidthPackage","ACS::CEN::CenInstance","ACS::CEN::Flowlog","ACS::DdosCoo::Instance"],"multiple":true}]`
        self.delivery_channel_condition = delivery_channel_condition
        # The ID of the delivery channel.
        self.delivery_channel_id = delivery_channel_id
        # The name of the delivery channel.
        self.delivery_channel_name = delivery_channel_name
        # The Alibaba Cloud Resource Name (ARN) of the delivery destination.
        # 
        # - If \\`DeliveryChannelType\\` is \\`OSS\\`, this parameter is the ARN of an OSS bucket.
        # 
        # - If \\`DeliveryChannelType\\` is \\`MNS\\`, this parameter is the ARN of an MNS topic.
        # 
        # - If \\`DeliveryChannelType\\` is \\`SLS\\`, this parameter is the ARN of an SLS Logstore.
        self.delivery_channel_target_arn = delivery_channel_target_arn
        # The type of the delivery channel. Valid values:
        # 
        # - OSS: Object Storage Service (OSS).
        # 
        # - MNS: Simple Message Queue (formerly MNS).
        # 
        # - SLS: Simple Log Service (SLS).
        self.delivery_channel_type = delivery_channel_type
        # The time when scheduled resource snapshots start to be delivered every day.
        # 
        # The format is `HH:mmZ` (UTC).
        self.delivery_snapshot_time = delivery_snapshot_time
        # The description of the delivery channel.
        self.description = description
        # Specifies whether to receive resource non-compliance events. When a resource becomes non-compliant, Cloud Config delivers a resource non-compliance event to SLS or MNS. Valid values:
        # 
        # - true: Receive resource non-compliance events.
        # 
        # - false: Do not receive resource non-compliance events.
        self.non_compliant_notification = non_compliant_notification
        # The destination OSS bucket to which the data is transferred when the size of the data exceeds the limit of the delivery channel.
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
        # The status of the delivery channel. Valid values:
        # 
        # - 0: The delivery channel is disabled.
        # 
        # - 1: The delivery channel is enabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.compliant_snapshot is not None:
            result['CompliantSnapshot'] = self.compliant_snapshot

        if self.configuration_item_change_notification is not None:
            result['ConfigurationItemChangeNotification'] = self.configuration_item_change_notification

        if self.configuration_snapshot is not None:
            result['ConfigurationSnapshot'] = self.configuration_snapshot

        if self.delivery_channel_assume_role_arn is not None:
            result['DeliveryChannelAssumeRoleArn'] = self.delivery_channel_assume_role_arn

        if self.delivery_channel_condition is not None:
            result['DeliveryChannelCondition'] = self.delivery_channel_condition

        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id

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

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CompliantSnapshot') is not None:
            self.compliant_snapshot = m.get('CompliantSnapshot')

        if m.get('ConfigurationItemChangeNotification') is not None:
            self.configuration_item_change_notification = m.get('ConfigurationItemChangeNotification')

        if m.get('ConfigurationSnapshot') is not None:
            self.configuration_snapshot = m.get('ConfigurationSnapshot')

        if m.get('DeliveryChannelAssumeRoleArn') is not None:
            self.delivery_channel_assume_role_arn = m.get('DeliveryChannelAssumeRoleArn')

        if m.get('DeliveryChannelCondition') is not None:
            self.delivery_channel_condition = m.get('DeliveryChannelCondition')

        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

