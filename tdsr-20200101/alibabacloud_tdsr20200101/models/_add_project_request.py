# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddProjectRequest(DaraModel):
    def __init__(
        self,
        business_id: int = None,
        name: str = None,
    ):
        self.business_id = business_id
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

