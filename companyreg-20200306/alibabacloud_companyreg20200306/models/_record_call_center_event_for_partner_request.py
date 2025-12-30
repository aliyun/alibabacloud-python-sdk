# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecordCallCenterEventForPartnerRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        call_action: str = None,
        callee: str = None,
        caller: str = None,
        conn_id: str = None,
        contact_id: str = None,
        employee_code: str = None,
        job_id: str = None,
        related_id: int = None,
        secret_mobile: str = None,
        skill_type: int = None,
        tenant_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.call_action = call_action
        self.callee = callee
        self.caller = caller
        self.conn_id = conn_id
        self.contact_id = contact_id
        self.employee_code = employee_code
        self.job_id = job_id
        # RequestId
        self.related_id = related_id
        self.secret_mobile = secret_mobile
        self.skill_type = skill_type
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.call_action is not None:
            result['CallAction'] = self.call_action

        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.conn_id is not None:
            result['ConnId'] = self.conn_id

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.employee_code is not None:
            result['EmployeeCode'] = self.employee_code

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.related_id is not None:
            result['RelatedId'] = self.related_id

        if self.secret_mobile is not None:
            result['SecretMobile'] = self.secret_mobile

        if self.skill_type is not None:
            result['SkillType'] = self.skill_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CallAction') is not None:
            self.call_action = m.get('CallAction')

        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('ConnId') is not None:
            self.conn_id = m.get('ConnId')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('EmployeeCode') is not None:
            self.employee_code = m.get('EmployeeCode')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')

        if m.get('SecretMobile') is not None:
            self.secret_mobile = m.get('SecretMobile')

        if m.get('SkillType') is not None:
            self.skill_type = m.get('SkillType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

