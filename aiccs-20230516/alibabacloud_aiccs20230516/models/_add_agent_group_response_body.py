# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class AddAgentGroupResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: main_models.AddAgentGroupResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
        timestamp: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success
        self.timestamp = timestamp

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.AddAgentGroupResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class AddAgentGroupResponseBodyModel(DaraModel):
    def __init__(
        self,
        agent_group_id: int = None,
        agent_group_name: str = None,
        create_time: str = None,
    ):
        # 坐席组ID
        self.agent_group_id = agent_group_id
        # 坐席组名称
        self.agent_group_name = agent_group_name
        # 创建坐席组的时间
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_group_id is not None:
            result['AgentGroupId'] = self.agent_group_id

        if self.agent_group_name is not None:
            result['AgentGroupName'] = self.agent_group_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentGroupId') is not None:
            self.agent_group_id = m.get('AgentGroupId')

        if m.get('AgentGroupName') is not None:
            self.agent_group_name = m.get('AgentGroupName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        return self

