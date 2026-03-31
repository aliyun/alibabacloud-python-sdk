# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyResourceLogDeliveryStatusResponseBody(DaraModel):
    def __init__(
        self,
        delivery_name: str = None,
        delivery_type: str = None,
        request_id: str = None,
        status: bool = None,
    ):
        self.delivery_name = delivery_name
        self.delivery_type = delivery_type
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delivery_name is not None:
            result['DeliveryName'] = self.delivery_name

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryName') is not None:
            self.delivery_name = m.get('DeliveryName')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

