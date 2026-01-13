# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrepaidRecord(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        code_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        remain_quota: int = None,
        status: str = None,
        total_quota: int = None,
        used_quota: int = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.code_type = code_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.remain_quota = remain_quota
        self.status = status
        self.total_quota = total_quota
        self.used_quota = used_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.account_name is not None:
            result['accountName'] = self.account_name

        if self.code_type is not None:
            result['codeType'] = self.code_type

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.remain_quota is not None:
            result['remainQuota'] = self.remain_quota

        if self.status is not None:
            result['status'] = self.status

        if self.total_quota is not None:
            result['totalQuota'] = self.total_quota

        if self.used_quota is not None:
            result['usedQuota'] = self.used_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')

        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('remainQuota') is not None:
            self.remain_quota = m.get('remainQuota')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalQuota') is not None:
            self.total_quota = m.get('totalQuota')

        if m.get('usedQuota') is not None:
            self.used_quota = m.get('usedQuota')

        return self

