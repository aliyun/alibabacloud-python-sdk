# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSQLReviewOptimizeDetailRequest(DaraModel):
    def __init__(
        self,
        sqlreview_query_key: str = None,
        tid: int = None,
    ):
        # The key that is used to query the details of optimization suggestions. You can call the [ListSQLReviewOriginSQL](https://help.aliyun.com/document_detail/257870.html) operation to query the key.
        # 
        # This parameter is required.
        self.sqlreview_query_key = sqlreview_query_key
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the ID of the tenant.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sqlreview_query_key is not None:
            result['SQLReviewQueryKey'] = self.sqlreview_query_key

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SQLReviewQueryKey') is not None:
            self.sqlreview_query_key = m.get('SQLReviewQueryKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

