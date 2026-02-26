# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class GetDeliveryChannelStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        delivery_channel_statistics: main_models.GetDeliveryChannelStatisticsResponseBodyDeliveryChannelStatistics = None,
        request_id: str = None,
    ):
        # The statistics of the delivery channel.
        self.delivery_channel_statistics = delivery_channel_statistics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.delivery_channel_statistics:
            self.delivery_channel_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_channel_statistics is not None:
            result['DeliveryChannelStatistics'] = self.delivery_channel_statistics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelStatistics') is not None:
            temp_model = main_models.GetDeliveryChannelStatisticsResponseBodyDeliveryChannelStatistics()
            self.delivery_channel_statistics = temp_model.from_map(m.get('DeliveryChannelStatistics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDeliveryChannelStatisticsResponseBodyDeliveryChannelStatistics(DaraModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        latest_change_delivery_time: str = None,
        latest_snapshot_delivery_time: str = None,
    ):
        # The ID of the delivery channel.
        self.delivery_channel_id = delivery_channel_id
        # The name of the delivery channel.
        self.delivery_channel_name = delivery_channel_name
        # The last time a resource configuration change was delivered.
        self.latest_change_delivery_time = latest_change_delivery_time
        # The last time a scheduled resource snapshot was delivered.
        self.latest_snapshot_delivery_time = latest_snapshot_delivery_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id

        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name

        if self.latest_change_delivery_time is not None:
            result['LatestChangeDeliveryTime'] = self.latest_change_delivery_time

        if self.latest_snapshot_delivery_time is not None:
            result['LatestSnapshotDeliveryTime'] = self.latest_snapshot_delivery_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')

        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')

        if m.get('LatestChangeDeliveryTime') is not None:
            self.latest_change_delivery_time = m.get('LatestChangeDeliveryTime')

        if m.get('LatestSnapshotDeliveryTime') is not None:
            self.latest_snapshot_delivery_time = m.get('LatestSnapshotDeliveryTime')

        return self

