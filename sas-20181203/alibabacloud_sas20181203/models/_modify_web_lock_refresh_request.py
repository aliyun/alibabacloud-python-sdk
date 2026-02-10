# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebLockRefreshRequest(DaraModel):
    def __init__(
        self,
        uuid: str = None,
    ):
        # The UUID of the server for which you want to refresh the status of the web tamper proofing feature.
        # 
        # >  You can call the [DescribeWebLockBindList](~~DescribeWebLockBindList~~) operation to query the servers for which the web tamper proofing feature is enabled.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

