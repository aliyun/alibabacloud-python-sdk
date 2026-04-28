# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudInterruptIvrRequest(DaraModel):
    def __init__(
        self,
        check_name: str = None,
        check_value: str = None,
        enterprise_id: int = None,
        unique_id: str = None,
        user_field: str = None,
    ):
        # 根据变量名去通道变量中取对应的变量值
        self.check_name = check_name
        # 当checkName代表的变量值与checkValue一致，才打断
        self.check_value = check_value
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 通话唯一标识；从通道唯一标识
        # 
        # This parameter is required.
        self.unique_id = unique_id
        # 自定义字段；json字符串
        self.user_field = user_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_name is not None:
            result['CheckName'] = self.check_name

        if self.check_value is not None:
            result['CheckValue'] = self.check_value

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        if self.user_field is not None:
            result['UserField'] = self.user_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckName') is not None:
            self.check_name = m.get('CheckName')

        if m.get('CheckValue') is not None:
            self.check_value = m.get('CheckValue')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        if m.get('UserField') is not None:
            self.user_field = m.get('UserField')

        return self

