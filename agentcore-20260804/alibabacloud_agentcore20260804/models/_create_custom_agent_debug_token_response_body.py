# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateCustomAgentDebugTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateCustomAgentDebugTokenResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. SUCCESS is returned if the call is successful.
        self.code = code
        # The debug token issued in this request, the token fingerprint, and the corresponding resource and network information.
        self.data = data
        # The HTTP status code of the request.
        self.http_status_code = http_status_code
        # The description of the request processing result.
        self.message = message
        # The unique identifier of the request, which can be used for troubleshooting.
        self.request_id = request_id
        # Indicates whether the request is successful. A value of true indicates success. A value of false indicates failure.
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateCustomAgentDebugTokenResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class CreateCustomAgentDebugTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        bootstrap_token: str = None,
        network_type: str = None,
        token_fingerprint: str = None,
        workspace_id: str = None,
    ):
        # The ID of the high-code agent corresponding to the token.
        self.agent_id = agent_id
        # The token used by the AgentCore SDK for local debugging. Keep the token secure. Do not write it to logs or commit it to code repositories.
        self.bootstrap_token = bootstrap_token
        # The network type used for the token, which is the same as the networkType parameter in the request.
        self.network_type = network_type
        # The fingerprint used to identify the issued token, which can be used to troubleshoot issuance records.
        self.token_fingerprint = token_fingerprint
        # The ID of the workspace corresponding to the token.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.bootstrap_token is not None:
            result['bootstrapToken'] = self.bootstrap_token

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.token_fingerprint is not None:
            result['tokenFingerprint'] = self.token_fingerprint

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('bootstrapToken') is not None:
            self.bootstrap_token = m.get('bootstrapToken')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('tokenFingerprint') is not None:
            self.token_fingerprint = m.get('tokenFingerprint')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

