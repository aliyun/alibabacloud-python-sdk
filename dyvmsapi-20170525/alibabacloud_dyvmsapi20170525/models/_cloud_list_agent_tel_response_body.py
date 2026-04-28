# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudListAgentTelResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudListAgentTelResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CloudListAgentTelResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudListAgentTelResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.CloudListAgentTelResponseBodyDataList] = None,
    ):
        # 座席电话数组
        self.list = list

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.CloudListAgentTelResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        return self

class CloudListAgentTelResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        area_code: str = None,
        cno: str = None,
        create_time: str = None,
        enterprise_id: int = None,
        id: int = None,
        is_bind: int = None,
        is_validity: int = None,
        tel: str = None,
        tel_type: int = None,
    ):
        # 座席id
        self.agent_id = agent_id
        # 区号
        self.area_code = area_code
        # 座席工号
        self.cno = cno
        # 创建时间，格式: yyyy-MM-dd HH:mm:ss
        self.create_time = create_time
        # 企业编号
        self.enterprise_id = enterprise_id
        # 座席电话id
        self.id = id
        # 是否绑定，0:未绑定 1:绑定
        self.is_bind = is_bind
        # 是否验证，0:未验证 1:已验证
        self.is_validity = is_validity
        # 电话号码
        self.tel = tel
        # 电话类型，1:固话 2:手机 3:分机 4:软电话
        self.tel_type = tel_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.area_code is not None:
            result['AreaCode'] = self.area_code

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.id is not None:
            result['Id'] = self.id

        if self.is_bind is not None:
            result['IsBind'] = self.is_bind

        if self.is_validity is not None:
            result['IsValidity'] = self.is_validity

        if self.tel is not None:
            result['Tel'] = self.tel

        if self.tel_type is not None:
            result['TelType'] = self.tel_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsBind') is not None:
            self.is_bind = m.get('IsBind')

        if m.get('IsValidity') is not None:
            self.is_validity = m.get('IsValidity')

        if m.get('Tel') is not None:
            self.tel = m.get('Tel')

        if m.get('TelType') is not None:
            self.tel_type = m.get('TelType')

        return self

