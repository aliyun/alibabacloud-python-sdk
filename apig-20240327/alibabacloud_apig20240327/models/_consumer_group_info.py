# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConsumerGroupInfo(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        gateway_type: str = None,
        name: str = None,
    ):
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The gateway type. Valid values: API or AI.
        self.gateway_type = gateway_type
        # The consumer group name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

