# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NeuronBizUserTokenCreateCmd(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        biz_id: str = None,
        permission: str = None,
    ):
        self.account_id = account_id
        # This parameter is required.
        self.biz_id = biz_id
        self.permission = permission

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.permission is not None:
            result['permission'] = self.permission

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('permission') is not None:
            self.permission = m.get('permission')

        return self

