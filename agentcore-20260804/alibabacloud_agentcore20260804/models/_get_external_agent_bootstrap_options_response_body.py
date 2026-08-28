# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetExternalAgentBootstrapOptionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetExternalAgentBootstrapOptionsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value SUCCESS indicates success.
        self.code = code
        # The available network access information for the external agent.
        self.data = data
        # The HTTP status code. The value 200 indicates success.
        self.http_status_code = http_status_code
        # The result message of the request.
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
            temp_model = main_models.GetExternalAgentBootstrapOptionsResponseBodyData()
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

class GetExternalAgentBootstrapOptionsResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        network_options: List[main_models.GetExternalAgentBootstrapOptionsResponseBodyDataNetworkOptions] = None,
        workspace_id: str = None,
    ):
        # The external agent ID.
        self.agent_id = agent_id
        # The list of available network access options.
        self.network_options = network_options
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.network_options:
            for v1 in self.network_options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        result['networkOptions'] = []
        if self.network_options is not None:
            for k1 in self.network_options:
                result['networkOptions'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        self.network_options = []
        if m.get('networkOptions') is not None:
            for k1 in m.get('networkOptions'):
                temp_model = main_models.GetExternalAgentBootstrapOptionsResponseBodyDataNetworkOptions()
                self.network_options.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetExternalAgentBootstrapOptionsResponseBodyDataNetworkOptions(DaraModel):
    def __init__(
        self,
        available: bool = None,
        network_type: str = None,
    ):
        # Indicates whether the network access type is available.
        self.available = available
        # The network type. Valid values:
        # - INTRANET: internal network.
        # - INTERNET: public network.
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['available'] = self.available

        if self.network_type is not None:
            result['networkType'] = self.network_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        return self

