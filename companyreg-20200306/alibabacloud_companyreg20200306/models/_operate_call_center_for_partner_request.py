# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateCallCenterForPartnerRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        call_action: str = None,
        employee_code: str = None,
        request: str = None,
        tenant_id: str = None,
    ):
        self.biz_type = biz_type
        self.call_action = call_action
        self.employee_code = employee_code
        self.request = request
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.call_action is not None:
            result['CallAction'] = self.call_action

        if self.employee_code is not None:
            result['EmployeeCode'] = self.employee_code

        if self.request is not None:
            result['Request'] = self.request

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CallAction') is not None:
            self.call_action = m.get('CallAction')

        if m.get('EmployeeCode') is not None:
            self.employee_code = m.get('EmployeeCode')

        if m.get('Request') is not None:
            self.request = m.get('Request')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

