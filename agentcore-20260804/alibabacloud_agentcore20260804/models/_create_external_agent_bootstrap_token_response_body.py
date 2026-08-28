# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateExternalAgentBootstrapTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateExternalAgentBootstrapTokenResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value SUCCESS indicates success.
        self.code = code
        # The Bootstrap Token and CMS configuration required for connecting the external agent.
        self.data = data
        # The HTTP status code. The value 200 indicates success.
        self.http_status_code = http_status_code
        # The message indicating the request processing result.
        self.message = message
        # The request ID.
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
            temp_model = main_models.CreateExternalAgentBootstrapTokenResponseBodyData()
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

class CreateExternalAgentBootstrapTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        bootstrap_token: str = None,
        cms: main_models.CreateExternalAgentBootstrapTokenResponseBodyDataCms = None,
        network_type: str = None,
        token_fingerprint: str = None,
        workspace_id: str = None,
    ):
        # The external agent ID.
        self.agent_id = agent_id
        # The Bootstrap Token used for connecting the external agent.
        self.bootstrap_token = bootstrap_token
        # The CMS configuration used for connecting the external agent.
        self.cms = cms
        # The network type for connection. Valid values:
        # - INTERNET: public network
        # - INTRANET: internal network
        self.network_type = network_type
        # The fingerprint of the Bootstrap Token.
        self.token_fingerprint = token_fingerprint
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.cms:
            self.cms.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.bootstrap_token is not None:
            result['bootstrapToken'] = self.bootstrap_token

        if self.cms is not None:
            result['cms'] = self.cms.to_map()

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

        if m.get('cms') is not None:
            temp_model = main_models.CreateExternalAgentBootstrapTokenResponseBodyDataCms()
            self.cms = temp_model.from_map(m.get('cms'))

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('tokenFingerprint') is not None:
            self.token_fingerprint = m.get('tokenFingerprint')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CreateExternalAgentBootstrapTokenResponseBodyDataCms(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        license_key: str = None,
        workspace: str = None,
    ):
        # The CMS reporting endpoint.
        self.endpoint = endpoint
        # The license key used for CMS connection.
        self.license_key = license_key
        # The CMS workspace name.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.license_key is not None:
            result['licenseKey'] = self.license_key

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

