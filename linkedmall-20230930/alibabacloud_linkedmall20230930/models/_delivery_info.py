# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeliveryInfo(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        id: str = None,
        post_fee: int = None,
        service_type: int = None,
    ):
        self.display_name = display_name
        self.id = id
        self.post_fee = post_fee
        # serviceType
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.id is not None:
            result['id'] = self.id

        if self.post_fee is not None:
            result['postFee'] = self.post_fee

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('postFee') is not None:
            self.post_fee = m.get('postFee')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        return self

