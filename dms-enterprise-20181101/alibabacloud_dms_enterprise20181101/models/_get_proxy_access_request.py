# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProxyAccessRequest(DaraModel):
    def __init__(
        self,
        proxy_access_id: int = None,
        tid: int = None,
    ):
        # The ID that Data Management (DMS) generates after the user is authorized to enable the secure access proxy feature for an instance. The ID is unique in DMS. You can call the [ListProxyAccesses](https://help.aliyun.com/document_detail/295386.html) operation to query the ID.
        # 
        # This parameter is required.
        self.proxy_access_id = proxy_access_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.proxy_access_id is not None:
            result['ProxyAccessId'] = self.proxy_access_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyAccessId') is not None:
            self.proxy_access_id = m.get('ProxyAccessId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

