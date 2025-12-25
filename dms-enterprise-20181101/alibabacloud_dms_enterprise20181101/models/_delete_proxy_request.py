# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteProxyRequest(DaraModel):
    def __init__(
        self,
        proxy_id: int = None,
        tid: int = None,
    ):
        # The ID of the security protection agent. You can call the [ListProxies](https://www.alibabacloud.com/help/en/data-management-service/latest/listproxies) or [GetProxy](https://www.alibabacloud.com/help/en/data-management-service/latest/getproxy) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.proxy_id = proxy_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://www.alibabacloud.com/help/en/data-management-service/latest/getuseractivetenant) or [ListUserTenants](https://www.alibabacloud.com/help/en/data-management-service/latest/listusertenants) operation to obtain this parameter.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

