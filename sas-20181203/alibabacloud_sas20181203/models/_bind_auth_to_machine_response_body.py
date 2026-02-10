# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAuthToMachineResponseBody(DaraModel):
    def __init__(
        self,
        bind_count: int = None,
        insufficient_core_count: int = None,
        insufficient_ecs_count: int = None,
        request_id: str = None,
        result_code: int = None,
        un_bind_count: int = None,
    ):
        # The number of bound servers.
        self.bind_count = bind_count
        # The shortage in the quota for cores of servers that can be protected.
        self.insufficient_core_count = insufficient_core_count
        # The shortage in the quota for servers that can be protected.
        self.insufficient_ecs_count = insufficient_ecs_count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The status code that indicates the result. Valid values:
        # 
        # *   **0**: The servers are bound to or unbound from Security Center.
        # *   **1**: The values that you specified for the parameters are invalid.
        # *   **2**: The quota for servers that can be protected is insufficient.
        # *   **3**: The quota for cores of servers that can be protected is insufficient.
        self.result_code = result_code
        # The number of unbound servers.
        self.un_bind_count = un_bind_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_count is not None:
            result['BindCount'] = self.bind_count

        if self.insufficient_core_count is not None:
            result['InsufficientCoreCount'] = self.insufficient_core_count

        if self.insufficient_ecs_count is not None:
            result['InsufficientEcsCount'] = self.insufficient_ecs_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.un_bind_count is not None:
            result['UnBindCount'] = self.un_bind_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindCount') is not None:
            self.bind_count = m.get('BindCount')

        if m.get('InsufficientCoreCount') is not None:
            self.insufficient_core_count = m.get('InsufficientCoreCount')

        if m.get('InsufficientEcsCount') is not None:
            self.insufficient_ecs_count = m.get('InsufficientEcsCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('UnBindCount') is not None:
            self.un_bind_count = m.get('UnBindCount')

        return self

