# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConfigDeliveryChannelsRequest(DaraModel):
    def __init__(
        self,
        delivery_channel_ids: str = None,
    ):
        # The ID of the delivery channel. Separate multiple IDs with commas (,).
        self.delivery_channel_ids = delivery_channel_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_channel_ids is not None:
            result['DeliveryChannelIds'] = self.delivery_channel_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelIds') is not None:
            self.delivery_channel_ids = m.get('DeliveryChannelIds')

        return self

