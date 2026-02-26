# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class ListDeliveryChannelsResponseBody(DaraModel):
    def __init__(
        self,
        delivery_channels: List[main_models.ListDeliveryChannelsResponseBodyDeliveryChannels] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The delivery channels.
        self.delivery_channels = delivery_channels
        # The maximum number of entries per page.
        self.max_results = max_results
        # A pagination token.
        # 
        # This parameter is required.
        self.next_token = next_token
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_channels = []
        if m.get('DeliveryChannels') is not None:
            for k1 in m.get('DeliveryChannels'):
                temp_model = main_models.ListDeliveryChannelsResponseBodyDeliveryChannels()
                self.delivery_channels.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDeliveryChannelsResponseBodyDeliveryChannels(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        delivery_channel_description: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
    ):
        # The time when the delivery channel was created.
        self.create_time = create_time
        # The description of the delivery channel.
        self.delivery_channel_description = delivery_channel_description
        # The ID of the delivery channel.
        self.delivery_channel_id = delivery_channel_id
        # The name of the delivery channel.
        self.delivery_channel_name = delivery_channel_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description

        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id

        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')

        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')

        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')

        return self

