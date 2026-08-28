# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class InstallWorkspacePluginRequest(DaraModel):
    def __init__(
        self,
        body: main_models.InstallWorkspacePluginRequestBody = None,
        client_token: str = None,
    ):
        # The request body for installing a plugin.
        self.body = body
        # The client idempotency token.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.InstallWorkspacePluginRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class InstallWorkspacePluginRequestBody(DaraModel):
    def __init__(
        self,
        config: main_models.InstallWorkspacePluginRequestBodyConfig = None,
    ):
        # The plugin-specific configuration. The configuration structure is determined by pluginName. Currently, the collaboration plugin supports network.
        self.config = config

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.InstallWorkspacePluginRequestBodyConfig()
            self.config = temp_model.from_map(m.get('config'))

        return self

class InstallWorkspacePluginRequestBodyConfig(DaraModel):
    def __init__(
        self,
        network: main_models.InstallWorkspacePluginRequestBodyConfigNetwork = None,
    ):
        # The network configuration used by the collaboration plugin. If not specified, the server uses the existing network configuration of the workspace.
        self.network = network

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network is not None:
            result['network'] = self.network.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('network') is not None:
            temp_model = main_models.InstallWorkspacePluginRequestBodyConfigNetwork()
            self.network = temp_model.from_map(m.get('network'))

        return self

class InstallWorkspacePluginRequestBodyConfigNetwork(DaraModel):
    def __init__(
        self,
        internet: main_models.InstallWorkspacePluginRequestBodyConfigNetworkInternet = None,
        vpc: main_models.InstallWorkspacePluginRequestBodyConfigNetworkVpc = None,
    ):
        # Controls whether the collaboration component is allowed to access the public network. This configuration only controls public network access capability and does not expose the component service to the public network.
        self.internet = internet
        # The user VPC and vSwitch list used for deploying the collaboration plugin. The zones corresponding to the vSwitches are queried by the server and do not need to be provided by the user.
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
            temp_model = main_models.InstallWorkspacePluginRequestBodyConfigNetworkInternet()
            self.internet = temp_model.from_map(m.get('internet'))

        if m.get('vpc') is not None:
            temp_model = main_models.InstallWorkspacePluginRequestBodyConfigNetworkVpc()
            self.vpc = temp_model.from_map(m.get('vpc'))

        return self

class InstallWorkspacePluginRequestBodyConfigNetworkVpc(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # Specifies whether the collaboration plugin uses VPC networking. If set to false, vpcId and vSwitchIds are ignored. If set to true, you must provide both vpcId and at least two vSwitchIds.
        self.enabled = enabled
        # The list of vSwitch IDs. The collaboration plugin requires that the vSwitches cover at least two different zones, and all vSwitches must belong to the VPC specified by vpcId.
        # 
        # This parameter is required.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
        # 
        # This parameter is required.
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

class InstallWorkspacePluginRequestBodyConfigNetworkInternet(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to enable public network access. If set to true without a VPC specified, PUB_NET is used. If set to true with a VPC specified, PRIVATE_PUBNET is used. If only a VPC is specified, PRIVATE_NET is used. At least one of public network or VPC must be configured.
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

