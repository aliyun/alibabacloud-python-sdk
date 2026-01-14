# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyConsumeMessageRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        consumer_group_id: str = None,
    ):
        # The client ID.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the consumer group.
        # 
        # This parameter is required.
        self.consumer_group_id = consumer_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        return self

