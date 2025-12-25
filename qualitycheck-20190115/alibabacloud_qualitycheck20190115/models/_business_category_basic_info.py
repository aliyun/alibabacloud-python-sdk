# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BusinessCategoryBasicInfo(DaraModel):
    def __init__(
        self,
        bid: int = None,
        name: str = None,
        original_id: int = None,
        service_type: int = None,
    ):
        self.bid = bid
        self.name = name
        self.original_id = original_id
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['Bid'] = self.bid

        if self.name is not None:
            result['Name'] = self.name

        if self.original_id is not None:
            result['OriginalId'] = self.original_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OriginalId') is not None:
            self.original_id = m.get('OriginalId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self

