# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class CreateAgentResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateAgentResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The agent information and the automatically issued API key returned after the agent is created.
        self.data = data
        # The status code of the request result. A value of success indicates success. A specific error code is returned upon failure.
        self.error_code = error_code
        # The error message returned when the request fails. This parameter is empty when the request succeeds.
        self.error_message = error_message
        # The unique ID of the request. You can use this ID for troubleshooting and tracing.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.CreateAgentResponseBodyData()
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

class CreateAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        agent_type: str = None,
        api_key: main_models.CreateAgentResponseBodyDataApiKey = None,
        created_at: str = None,
        creation_type: str = None,
        description: str = None,
        owner_id: str = None,
        status: str = None,
    ):
        # The globally unique ID of the agent.
        self.agent_id = agent_id
        # The agent name.
        self.agent_name = agent_name
        # The permission inheritance type of the agent. Valid values: HUMAN_BOUND (inherits user permissions), PERMISSION_NARROW (narrows permissions), STANDALONE (operates as an independent identity principal without inheriting permissions from other principals).
        self.agent_type = agent_type
        # The automatically issued API key for the new agent. The plaintext secret is returned only once in this response.
        self.api_key = api_key
        # The time when the agent was created. The value is a time string in RFC 3339 format.
        self.created_at = created_at
        # The creation method of the agent. Valid values: manual (manually created in the console), auto (automatic creation by the system). Agents created by this operation are always manual.
        self.creation_type = creation_type
        # The description of the agent.
        self.description = description
        # The user ID of the agent owner, which is the current user who initiated the creation request.
        self.owner_id = owner_id
        # The status of the agent. Valid values: active (enabled), disabled (disabled), deleted (deleted). A newly created agent is always active.
        self.status = status

    def validate(self):
        if self.api_key:
            self.api_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.api_key is not None:
            result['ApiKey'] = self.api_key.to_map()

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
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('ApiKey') is not None:
            temp_model = main_models.CreateAgentResponseBodyDataApiKey()
            self.api_key = temp_model.from_map(m.get('ApiKey'))

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

class CreateAgentResponseBodyDataApiKey(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        agent_type: str = None,
        created_at: str = None,
        creator_id: str = None,
        creator_name: str = None,
        description: str = None,
        expire_time: str = None,
        id: int = None,
        is_revoked: bool = None,
        key_prefix: str = None,
        last_used_time: str = None,
        name: str = None,
        secret: str = None,
        source: str = None,
    ):
        # The ID of the agent to which the API key belongs.
        self.agent_id = agent_id
        # The name of the agent to which the API key belongs.
        self.agent_name = agent_name
        # The permission inheritance type of the agent to which the API key belongs.
        self.agent_type = agent_type
        # The time when the API key was created. The value is a time string in RFC 3339 format.
        self.created_at = created_at
        # The user ID of the user who created the API key.
        self.creator_id = creator_id
        # The name of the user who created the API key.
        self.creator_name = creator_name
        # The description of the API key.
        self.description = description
        # The expiration time of the API key. The value is a time string in RFC 3339 format.
        self.expire_time = expire_time
        # The primary key ID of the API key.
        self.id = id
        # Indicates whether the API key has been revoked.
        self.is_revoked = is_revoked
        # The non-sensitive visible prefix of the API key plaintext, used to identify the credential. The plaintext secret is not returned again.
        self.key_prefix = key_prefix
        # The time when the API key was last used. The value is a time string in RFC 3339 format. This parameter is empty if the API key has never been used.
        self.last_used_time = last_used_time
        # The name of the API key.
        self.name = name
        # The plaintext secret of the API key. This value is returned only once in this creation response. Store it securely. Subsequent API calls do not return the plaintext secret again.
        self.secret = secret
        # The credential source. Valid values: console (issued from the console), oauth (issued through the OAuth flow), install_token (issued through the install-and-authenticate flow). The API key automatically issued by this operation is always console.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.description is not None:
            result['Description'] = self.description

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.id is not None:
            result['Id'] = self.id

        if self.is_revoked is not None:
            result['IsRevoked'] = self.is_revoked

        if self.key_prefix is not None:
            result['KeyPrefix'] = self.key_prefix

        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time

        if self.name is not None:
            result['Name'] = self.name

        if self.secret is not None:
            result['Secret'] = self.secret

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsRevoked') is not None:
            self.is_revoked = m.get('IsRevoked')

        if m.get('KeyPrefix') is not None:
            self.key_prefix = m.get('KeyPrefix')

        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Secret') is not None:
            self.secret = m.get('Secret')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

