# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qwenb2bmed20261121 import models as main_models
from darabonba.model import DaraModel

class OpenServiceRequest(DaraModel):
    def __init__(
        self,
        communication: main_models.OpenServiceRequestCommunication = None,
        open_benefits: bool = None,
    ):
        # 按接入时约定填写业务用户信息。如果当前业务凭据无需提供用户信息，可省略整个对象。字段名为 user_info 和 user_id。
        self.communication = communication
        # 必填 JSON 布尔值。false 只验证本次调用，成功返回 TEST_OK；true 提交服务开通申请。
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
        # 业务用户信息对象。提供时必须填写其中的 user_id。
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
        # 非空字符串，填写你自己的应用中用于识别该用户的 ID。
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

