# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudAgentSetUserDataRequest(DaraModel):
    def __init__(
        self,
        cno: str = None,
        direction: int = None,
        enterprise_id: int = None,
        user_data: str = None,
    ):
        # 座席工号；取值3-10位正整数
        # 
        # This parameter is required.
        self.cno = cno
        # 随路数据方向；取值说明：1： 座席侧，2： 非座席侧
        # 
        # This parameter is required.
        self.direction = direction
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # json格式字符串,传入的值会打入通道变量,格式：json字符串{"key":"value"} 随路数据数据格式：key=value,不支持数组，嵌套。
        # 
        # This parameter is required.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cno is not None:
            result['Cno'] = self.cno

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

