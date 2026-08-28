# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetWorkspacePluginResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetWorkspacePluginResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The plug-in details.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message. An error description is returned if the request fails.
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
            temp_model = main_models.GetWorkspacePluginResponseBodyData()
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

class GetWorkspacePluginResponseBodyData(DaraModel):
    def __init__(
        self,
        config: main_models.GetWorkspacePluginResponseBodyDataConfig = None,
        enabled: bool = None,
        plugin_name: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # The user-configurable properties currently in effect for the plug-in. This field is empty if the plug-in is not installed.
        self.config = config
        # Indicates whether the plug-in is enabled. The value is true when the status is ENABLED.
        self.enabled = enabled
        # The plug-in name.
        self.plugin_name = plugin_name
        # The plug-in status. Valid values: DISABLED, ENABLING, ENABLED, ENABLE_FAILED, DISABLING, DISABLE_FAILED.
        self.status = status
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.plugin_name is not None:
            result['pluginName'] = self.plugin_name

        if self.status is not None:
            result['status'] = self.status

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.GetWorkspacePluginResponseBodyDataConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('pluginName') is not None:
            self.plugin_name = m.get('pluginName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class GetWorkspacePluginResponseBodyDataConfig(DaraModel):
    def __init__(
        self,
        agent_loop: main_models.GetWorkspacePluginResponseBodyDataConfigAgentLoop = None,
        network: main_models.GetWorkspacePluginResponseBodyDataConfigNetwork = None,
    ):
        # The AgentLoop plug-in configuration.
        self.agent_loop = agent_loop
        # The network configuration of the plug-in, including public network access configuration and VPC configuration.
        self.network = network

    def validate(self):
        if self.agent_loop:
            self.agent_loop.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_loop is not None:
            result['agentLoop'] = self.agent_loop.to_map()

        if self.network is not None:
            result['network'] = self.network.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentLoop') is not None:
            temp_model = main_models.GetWorkspacePluginResponseBodyDataConfigAgentLoop()
            self.agent_loop = temp_model.from_map(m.get('agentLoop'))

        if m.get('network') is not None:
            temp_model = main_models.GetWorkspacePluginResponseBodyDataConfigNetwork()
            self.network = temp_model.from_map(m.get('network'))

        return self

class GetWorkspacePluginResponseBodyDataConfigNetwork(DaraModel):
    def __init__(
        self,
        internet: main_models.GetWorkspacePluginResponseBodyDataConfigNetworkInternet = None,
        vpc: main_models.GetWorkspacePluginResponseBodyDataConfigNetworkVpc = None,
    ):
        # The public network access configuration.
        self.internet = internet
        # The user VPC configuration.
        self.vpc = vpc

    def validate(self):
        if self.internet:
            self.internet.validate()
        if self.vpc:
            self.vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet is not None:
            result['internet'] = self.internet.to_map()

        if self.vpc is not None:
            result['vpc'] = self.vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internet') is not None:
            temp_model = main_models.GetWorkspacePluginResponseBodyDataConfigNetworkInternet()
            self.internet = temp_model.from_map(m.get('internet'))

        if m.get('vpc') is not None:
            temp_model = main_models.GetWorkspacePluginResponseBodyDataConfigNetworkVpc()
            self.vpc = temp_model.from_map(m.get('vpc'))

        return self

class GetWorkspacePluginResponseBodyDataConfigNetworkVpc(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # Indicates whether VPC network access is enabled for the collaboration plug-in.
        self.enabled = enabled
        # The list of vSwitch IDs used for plug-in deployment.
        self.v_switch_ids = v_switch_ids
        # The VPC ID used for plug-in deployment.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.v_switch_ids is not None:
            result['vSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('vSwitchIds') is not None:
            self.v_switch_ids = m.get('vSwitchIds')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

class GetWorkspacePluginResponseBodyDataConfigNetworkInternet(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Indicates whether public network access is enabled.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class GetWorkspacePluginResponseBodyDataConfigAgentLoop(DaraModel):
    def __init__(
        self,
        agent_space_name: str = None,
        created_at: str = None,
        region_id: str = None,
    ):
        # The AgentSpace name associated with the AgentLoop plug-in.
        self.agent_space_name = agent_space_name
        # The creation time of the AgentSpace in UTC in RFC 3339 format.
        self.created_at = created_at
        # The region ID where the AgentSpace resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space_name is not None:
            result['agentSpaceName'] = self.agent_space_name

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpaceName') is not None:
            self.agent_space_name = m.get('agentSpaceName')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

