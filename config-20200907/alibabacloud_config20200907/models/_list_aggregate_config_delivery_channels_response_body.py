# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListAggregateConfigDeliveryChannelsResponseBody(DaraModel):
    def __init__(
        self,
        delivery_channels: List[main_models.ListAggregateConfigDeliveryChannelsResponseBodyDeliveryChannels] = None,
        request_id: str = None,
    ):
        self.delivery_channels = delivery_channels
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
                temp_model = main_models.ListAggregateConfigDeliveryChannelsResponseBodyDeliveryChannels()
                self.delivery_channels.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAggregateConfigDeliveryChannelsResponseBodyDeliveryChannels(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_id: str = None,
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
        self.account_id = account_id
        self.aggregator_id = aggregator_id
        self.compliant_snapshot = compliant_snapshot
        self.configuration_item_change_notification = configuration_item_change_notification
        self.configuration_snapshot = configuration_snapshot
        self.delivery_channel_assume_role_arn = delivery_channel_assume_role_arn
        self.delivery_channel_condition = delivery_channel_condition
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.delivery_channel_target_arn = delivery_channel_target_arn
        self.delivery_channel_type = delivery_channel_type
        self.delivery_snapshot_time = delivery_snapshot_time
        self.description = description
        self.non_compliant_notification = non_compliant_notification
        self.oversized_data_osstarget_arn = oversized_data_osstarget_arn
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

        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

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

        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

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

