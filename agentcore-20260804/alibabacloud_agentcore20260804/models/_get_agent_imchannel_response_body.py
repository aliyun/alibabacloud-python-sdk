# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetAgentIMChannelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAgentIMChannelResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value SUCCESS indicates success.
        self.code = code
        # The IM channel details.
        self.data = data
        # The HTTP status code. The value 200 indicates success.
        self.http_status_code = http_status_code
        # The request processing result message.
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
            temp_model = main_models.GetAgentIMChannelResponseBodyData()
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

class GetAgentIMChannelResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        channel_config: main_models.GetAgentIMChannelResponseBodyDataChannelConfig = None,
        channel_type: str = None,
        create_time: str = None,
        credential_summary: main_models.GetAgentIMChannelResponseBodyDataCredentialSummary = None,
        enabled: bool = None,
        endpoint_url: str = None,
        im_channel_id: str = None,
        service_endpoint_id: str = None,
        status: str = None,
        status_reason: str = None,
        update_time: str = None,
        workspace_id: str = None,
    ):
        # The agent ID.
        self.agent_id = agent_id
        # The channel behavior configuration.
        self.channel_config = channel_config
        # The IM channel type. Valid values:
        # - DINGTALK: DingTalk.
        # - FEISHU: Lark.
        # - WECOM: WeCom.
        self.channel_type = channel_type
        # The creation time in RFC 3339 format.
        self.create_time = create_time
        # The channel credential summary. Only non-sensitive fields and configured secret field names are returned. Secret values are not returned.
        self.credential_summary = credential_summary
        # Specifies whether the IM channel is enabled. Default value: true.
        self.enabled = enabled
        # The public network access URL of the attached ServiceEndpoint.
        self.endpoint_url = endpoint_url
        # The IM channel ID.
        self.im_channel_id = im_channel_id
        # The ID of the bound ServiceEndpoint. The endpoint must belong to the specified agent and its current version, be in the ready state, and have a public network address.
        self.service_endpoint_id = service_endpoint_id
        # The IM channel status. Valid values:
        # - CREATING: Being created.
        # - READY: Ready.
        # - UPDATING: Being updated.
        # - FAILED: Failed.
        # - DELETING: Being deleted.
        # - DELETE_FAILED: Deletion failed.
        self.status = status
        # The reason for the current IM channel status.
        self.status_reason = status_reason
        # The update time in RFC 3339 format.
        self.update_time = update_time
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.channel_config:
            self.channel_config.validate()
        if self.credential_summary:
            self.credential_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.channel_config is not None:
            result['channelConfig'] = self.channel_config.to_map()

        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.credential_summary is not None:
            result['credentialSummary'] = self.credential_summary.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.endpoint_url is not None:
            result['endpointUrl'] = self.endpoint_url

        if self.im_channel_id is not None:
            result['imChannelId'] = self.im_channel_id

        if self.service_endpoint_id is not None:
            result['serviceEndpointId'] = self.service_endpoint_id

        if self.status is not None:
            result['status'] = self.status

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('channelConfig') is not None:
            temp_model = main_models.GetAgentIMChannelResponseBodyDataChannelConfig()
            self.channel_config = temp_model.from_map(m.get('channelConfig'))

        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('credentialSummary') is not None:
            temp_model = main_models.GetAgentIMChannelResponseBodyDataCredentialSummary()
            self.credential_summary = temp_model.from_map(m.get('credentialSummary'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('endpointUrl') is not None:
            self.endpoint_url = m.get('endpointUrl')

        if m.get('imChannelId') is not None:
            self.im_channel_id = m.get('imChannelId')

        if m.get('serviceEndpointId') is not None:
            self.service_endpoint_id = m.get('serviceEndpointId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetAgentIMChannelResponseBodyDataCredentialSummary(DaraModel):
    def __init__(
        self,
        configured_secret_fields: List[str] = None,
        non_secret_fields: Dict[str, str] = None,
    ):
        # The list of configured secret field names. Secret values are not included.
        self.configured_secret_fields = configured_secret_fields
        # The non-sensitive credential fields and their values.
        self.non_secret_fields = non_secret_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configured_secret_fields is not None:
            result['configuredSecretFields'] = self.configured_secret_fields

        if self.non_secret_fields is not None:
            result['nonSecretFields'] = self.non_secret_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuredSecretFields') is not None:
            self.configured_secret_fields = m.get('configuredSecretFields')

        if m.get('nonSecretFields') is not None:
            self.non_secret_fields = m.get('nonSecretFields')

        return self

class GetAgentIMChannelResponseBodyDataChannelConfig(DaraModel):
    def __init__(
        self,
        show_thinking: bool = None,
        show_tool_calls: bool = None,
    ):
        # Specifies whether to display the thinking process in IM messages. Default value: false.
        self.show_thinking = show_thinking
        # Specifies whether to display the tool calling process in IM messages. Default value: false.
        self.show_tool_calls = show_tool_calls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.show_thinking is not None:
            result['showThinking'] = self.show_thinking

        if self.show_tool_calls is not None:
            result['showToolCalls'] = self.show_tool_calls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('showThinking') is not None:
            self.show_thinking = m.get('showThinking')

        if m.get('showToolCalls') is not None:
            self.show_tool_calls = m.get('showToolCalls')

        return self

