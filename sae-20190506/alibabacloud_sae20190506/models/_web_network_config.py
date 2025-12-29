# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class WebNetworkConfig(DaraModel):
    def __init__(
        self,
        internet_access: bool = None,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
    ):
        self.internet_access = internet_access
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_access is not None:
            result['InternetAccess'] = self.internet_access

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetAccess') is not None:
            self.internet_access = m.get('InternetAccess')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

