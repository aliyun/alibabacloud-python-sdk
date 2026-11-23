# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qwenb2bchat20261121 import models as main_models
from darabonba.model import DaraModel

class OpenServiceRequest(DaraModel):
    def __init__(
        self,
        communication: main_models.OpenServiceRequestCommunication = None,
        open_benefits: bool = None,
    ):
        # 按凭据的业务身份配置提供；固定用户身份或不要求正文用户身份时可省略。若提供，必须是只含 user_info 的对象，不能为 null 或空对象。测试与真实开通请求执行相同身份检查。
        self.communication = communication
        # 必填 JSON 布尔值，无默认值。false 仅验证接口、鉴权、身份和请求参数，成功返回 TEST_OK，不实际开通。true 发起服务开通；返回 OPENING 时仍在处理中。重复发送 true 仍是开通操作，不是只读状态查询。字符串 true/false 不合法。
        # 
        # This parameter is required.
        self.open_benefits = open_benefits

    def validate(self):
        if self.communication:
            self.communication.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.communication is not None:
            result['communication'] = self.communication.to_map()

        if self.open_benefits is not None:
            result['openBenefits'] = self.open_benefits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('communication') is not None:
            temp_model = main_models.OpenServiceRequestCommunication()
            self.communication = temp_model.from_map(m.get('communication'))

        if m.get('openBenefits') is not None:
            self.open_benefits = m.get('openBenefits')

        return self

class OpenServiceRequestCommunication(DaraModel):
    def __init__(
        self,
        user_info: main_models.OpenServiceRequestCommunicationUserInfo = None,
    ):
        # communication 存在时必填的对象，只包含 user_id，不能为 null 或空对象。
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_info is not None:
            result['user_info'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_info') is not None:
            temp_model = main_models.OpenServiceRequestCommunicationUserInfo()
            self.user_info = temp_model.from_map(m.get('user_info'))

        return self

class OpenServiceRequestCommunicationUserInfo(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # 客户应用内的业务用户标识，须符合凭据身份配置。非空，最多 256 个 UTF-16 代码单元，无首尾空白、控制字符或非法 Unicode。不是阿里云 UID、订单号或 SP 实例 ID。
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

