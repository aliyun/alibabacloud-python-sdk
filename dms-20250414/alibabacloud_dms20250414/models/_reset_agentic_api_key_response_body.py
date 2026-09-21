# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ResetAgenticApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ResetAgenticApiKeyResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The Access Token information returned after a successful reset. The Secret field contains the new plaintext Secret, which is returned only once in this response.
        self.data = data
        # The error code returned when the request fails. You can use this code to programmatically determine the failure type. This value is empty when the request succeeds.
        self.error_code = error_code
        # The error message returned when the request fails. This message helps you locate the issue. This value is empty when the request succeeds.
        self.error_message = error_message
        # The unique request ID, which is used for troubleshooting and log correlation.
        self.request_id = request_id
        # Indicates whether the request was successful. A value of true indicates that the reset was successful. A value of false indicates a failure. In this case, check ErrorCode and ErrorMessage to identify the cause.
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
            temp_model = main_models.ResetAgenticApiKeyResponseBodyData()
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

class ResetAgenticApiKeyResponseBodyData(DaraModel):
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
        warning: str = None,
    ):
        # The ID of the Agent to which the Access Token belongs.
        self.agent_id = agent_id
        # The name of the Agent to which the Access Token belongs.
        self.agent_name = agent_name
        # The type of the Agent to which the Access Token belongs. Valid values:
        # - HUMAN_BOUND: fully inherits the permissions of the associated user.
        # - PERMISSION_NARROW: narrows the permissions based on the associated user\\"s permission baseline.
        # - AGENT_BOUND: inherits the permissions of the parent Agent.
        # - STANDALONE: holds permissions as an independent identity principal.
        self.agent_type = agent_type
        # The time when the Access Token was created, in the yyyy-MM-dd HH:mm:ss format (UTC+8). This value remains unchanged after the reset.
        self.created_at = created_at
        # The user ID of the Access Token creator.
        self.creator_id = creator_id
        # The display name of the Access Token creator.
        self.creator_name = creator_name
        # The description of the Access Token. This value remains unchanged after the reset.
        self.description = description
        # The expiration time of the Access Token, in the yyyy-MM-dd HH:mm:ss format (UTC+8). If ExpireAfterSeconds is specified, the expiration time is recalculated from the time of the reset. If ExpireAfterSeconds is not specified, the original expiration time is retained.
        self.expire_time = expire_time
        # The ID of the reset Access Token. This value remains unchanged after the reset.
        self.id = id
        # Indicates whether the Access Token has been revoked. An Access Token returned after a successful reset is always in the non-revoked state (false).
        self.is_revoked = is_revoked
        # The visible prefix of the Access Token, which is used to identify the Access Token without exposing the full Secret. This value remains unchanged after the reset.
        self.key_prefix = key_prefix
        # The time when the Access Token was last used, in the yyyy-MM-dd HH:mm:ss format (UTC+8). This value is empty if the Access Token has never been used.
        self.last_used_time = last_used_time
        # The name of the Access Token. This value remains unchanged after the reset.
        self.name = name
        # The new plaintext Secret generated by this reset. This value is returned only once in this response and will not be returned by any subsequent operation. Store it securely right away. The old Secret becomes invalid immediately after the reset.
        self.secret = secret
        # The credential source of the Access Token. The reset operation supports only Access Tokens issued by the console. Therefore, the value is always console.
        self.source = source
        # The reminder information related to this reset, such as a notice that the new Secret is returned only once and must be stored immediately. This value is empty if no reminder exists.
        self.warning = warning

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

        if self.warning is not None:
            result['Warning'] = self.warning

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

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

