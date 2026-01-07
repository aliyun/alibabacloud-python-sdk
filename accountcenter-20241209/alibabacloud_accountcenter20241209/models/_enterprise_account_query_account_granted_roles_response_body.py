# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseAccountQueryAccountGrantedRolesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.EnterpriseAccountQueryAccountGrantedRolesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.EnterpriseAccountQueryAccountGrantedRolesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EnterpriseAccountQueryAccountGrantedRolesResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_role_code: str = None,
        biz_role_name: str = None,
    ):
        self.biz_role_code = biz_role_code
        self.biz_role_name = biz_role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_role_code is not None:
            result['BizRoleCode'] = self.biz_role_code

        if self.biz_role_name is not None:
            result['BizRoleName'] = self.biz_role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRoleCode') is not None:
            self.biz_role_code = m.get('BizRoleCode')

        if m.get('BizRoleName') is not None:
            self.biz_role_name = m.get('BizRoleName')

        return self

