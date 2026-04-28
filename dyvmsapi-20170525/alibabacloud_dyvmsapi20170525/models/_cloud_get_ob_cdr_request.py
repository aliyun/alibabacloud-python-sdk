# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudGetObCdrRequest(DaraModel):
    def __init__(
        self,
        enterprise_id: int = None,
        unique_id: str = None,
    ):
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 电话唯一标识；对应座席外呼通话记录的uniqueId
        # 
        # This parameter is required.
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        return self

