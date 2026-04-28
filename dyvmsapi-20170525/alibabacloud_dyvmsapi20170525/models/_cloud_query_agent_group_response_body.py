# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CloudQueryAgentGroupResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CloudQueryAgentGroupResponseBodyData = None,
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
            temp_model = main_models.CloudQueryAgentGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CloudQueryAgentGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: str = None,
        enterprise_id: int = None,
        gno: str = None,
        group_name: str = None,
        id: int = None,
        type: int = None,
    ):
        # 描述信息
        self.comment = comment
        # 创建时间，格式: yyyy-MM-dd HH:mm:ss
        self.create_time = create_time
        # 企业编号
        self.enterprise_id = enterprise_id
        # 外呼组编号
        self.gno = gno
        # 外呼组名称
        self.group_name = group_name
        # 外呼组id
        self.id = id
        # 外呼组类型 1：外呼总组 2：外呼组
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.gno is not None:
            result['Gno'] = self.gno

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Gno') is not None:
            self.gno = m.get('Gno')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

