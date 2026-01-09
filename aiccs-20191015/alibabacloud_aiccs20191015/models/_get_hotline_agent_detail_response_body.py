# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetHotlineAgentDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHotlineAgentDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('Data') is not None:
            temp_model = main_models.GetHotlineAgentDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHotlineAgentDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_status: int = None,
        agent_status_code: str = None,
        assigned: bool = None,
        rest_type: int = None,
        tenant_id: int = None,
        token: str = None,
    ):
        self.agent_id = agent_id
        self.agent_status = agent_status
        self.agent_status_code = agent_status_code
        self.assigned = assigned
        self.rest_type = rest_type
        self.tenant_id = tenant_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.agent_status_code is not None:
            result['AgentStatusCode'] = self.agent_status_code

        if self.assigned is not None:
            result['Assigned'] = self.assigned

        if self.rest_type is not None:
            result['RestType'] = self.rest_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('AgentStatusCode') is not None:
            self.agent_status_code = m.get('AgentStatusCode')

        if m.get('Assigned') is not None:
            self.assigned = m.get('Assigned')

        if m.get('RestType') is not None:
            self.rest_type = m.get('RestType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

