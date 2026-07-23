# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetAgenticAgentByInstallTokenResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAgenticAgentByInstallTokenResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetAgenticAgentByInstallTokenResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAgenticAgentByInstallTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        active_api_key_prefixes: List[str] = None,
        agent_id: str = None,
        agent_name: str = None,
        agent_type: str = None,
        created_at: str = None,
        creation_type: str = None,
        description: str = None,
        owner_id: str = None,
        status: str = None,
    ):
        self.active_api_key_prefixes = active_api_key_prefixes
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.agent_type = agent_type
        self.created_at = created_at
        self.creation_type = creation_type
        self.description = description
        self.owner_id = owner_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_api_key_prefixes is not None:
            result['ActiveApiKeyPrefixes'] = self.active_api_key_prefixes

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.creation_type is not None:
            result['CreationType'] = self.creation_type

        if self.description is not None:
            result['Description'] = self.description

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveApiKeyPrefixes') is not None:
            self.active_api_key_prefixes = m.get('ActiveApiKeyPrefixes')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

