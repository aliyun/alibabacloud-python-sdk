# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAggregateConfigDeliveryChannelResponseBody(DaraModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        # The ID of the delivery channel.
        self.delivery_channel_id = delivery_channel_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

