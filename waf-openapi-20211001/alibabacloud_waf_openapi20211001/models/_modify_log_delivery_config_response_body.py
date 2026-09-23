# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLogDeliveryConfigResponseBody(DaraModel):
    def __init__(
        self,
        delivery_name: str = None,
        request_id: str = None,
    ):
        # The name of the log delivery configuration.
        self.delivery_name = delivery_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_name is not None:
            result['DeliveryName'] = self.delivery_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryName') is not None:
            self.delivery_name = m.get('DeliveryName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

