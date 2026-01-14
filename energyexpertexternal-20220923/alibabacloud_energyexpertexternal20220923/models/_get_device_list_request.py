# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeviceListRequest(DaraModel):
    def __init__(
        self,
        factory_id: str = None,
    ):
        # The ID of the site.
        # 
        # This parameter is required.
        self.factory_id = factory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')

        return self

