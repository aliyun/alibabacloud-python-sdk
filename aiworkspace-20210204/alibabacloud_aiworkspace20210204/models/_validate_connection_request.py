# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ValidateConnectionRequest(DaraModel):
    def __init__(
        self,
        configs: Dict[str, str] = None,
        connection_id: str = None,
        connection_type: str = None,
        secrets: Dict[str, str] = None,
        validate_type: str = None,
        workspace_id: str = None,
    ):
        # The configuration of the connection, specified as key-value pairs. The configuration keys vary by connection type. For more information, see the supplementary information about the request parameters of the CreateConnection operation.
        self.configs = configs
        # The connection ID. For more information about how to obtain the connection ID, see [ListConnections](url).
        self.connection_id = connection_id
        # The connection type. Only connection types that support public network access are available. Valid values:
        # 
        # - DashScopeConnection: a service connection for Alibaba Cloud Model Studio.
        # 
        # - DeepSeekConnection: a service connection for DeepSeek.
        # 
        # - FunctionAIMCPConnection: a connection for Function AI MCP.
        # 
        # - CustomMCPConnection: a custom MCP connection.
        self.connection_type = connection_type
        # The key-value pairs to encrypt, such as a database logon password or a model connection key.
        self.secrets = secrets
        # The validation type. Set the value to:
        # 
        # - Connectivity: a connectivity test
        self.validate_type = validate_type
        # The workspace ID. For more information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs is not None:
            result['Configs'] = self.configs

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.secrets is not None:
            result['Secrets'] = self.secrets

        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('Secrets') is not None:
            self.secrets = m.get('Secrets')

        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

