# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEpnInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        epninstance_id: str = None,
    ):
        # The ID of the EPN instance.
        # 
        # This parameter is required.
        self.epninstance_id = epninstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')

        return self

