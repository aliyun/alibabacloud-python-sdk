# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferIntentionOwnerRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        employee_code: str = None,
        person_id: int = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.biz_type = biz_type
        self.employee_code = employee_code
        self.person_id = person_id
        self.remark = remark

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

        if self.employee_code is not None:
            result['EmployeeCode'] = self.employee_code

        if self.person_id is not None:
            result['PersonId'] = self.person_id

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EmployeeCode') is not None:
            self.employee_code = m.get('EmployeeCode')

        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

