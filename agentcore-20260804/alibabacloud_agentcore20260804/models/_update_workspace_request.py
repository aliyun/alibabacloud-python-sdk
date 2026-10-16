# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateWorkspaceRequestBody = None,
        client_token: str = None,
    ):
        # The request body for updating a workspace.
        self.body = body
        # The client token used to ensure idempotence.
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
            temp_model = main_models.UpdateWorkspaceRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateWorkspaceRequestBody(DaraModel):
    def __init__(
        self,
        name: str = None,
        network_configuration: main_models.UpdateWorkspaceRequestBodyNetworkConfiguration = None,
    ):
        # The updated name of the workspace.
        self.name = name
        # The updated network configuration of the workspace.
        self.network_configuration = network_configuration

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.UpdateWorkspaceRequestBodyNetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        return self

class UpdateWorkspaceRequestBodyNetworkConfiguration(DaraModel):
    def __init__(
        self,
        public_egress_enabled: bool = None,
        public_ingress_enabled: bool = None,
        vpc: main_models.UpdateWorkspaceRequestBodyNetworkConfigurationVpc = None,
    ):
        # Specifies whether to allow public egress access from the platform. If this parameter is not specified, the original value is retained. Disabling this feature asynchronously cascades to disable the public network switch for agents. Re-enabling this feature does not automatically restore the agent switch. This parameter only controls whether the latest versions of managed and custom agents use the public egress of the platform. It does not control fixed historical versions, model or MCP proxy egress, or the public egress of the user VPC.
        self.public_egress_enabled = public_egress_enabled
        # Specifies whether to allow public ingress access. If this parameter is not specified, the original value is retained. This parameter can be modified together with PublicEgressEnabled and takes effect asynchronously through a unified task. After this feature is disabled, the public ingress for all agent endpoints in the workspace is closed. After this feature is re-enabled, the original public ingress is restored. INNER_DIRECT and user VPC ingress are not affected. Collaboration and Element Web ingress are not controlled by this parameter.
        self.public_ingress_enabled = public_ingress_enabled
        # The VPC network configuration of the user.
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            self.vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.public_egress_enabled is not None:
            result['publicEgressEnabled'] = self.public_egress_enabled

        if self.public_ingress_enabled is not None:
            result['publicIngressEnabled'] = self.public_ingress_enabled

        if self.vpc is not None:
            result['vpc'] = self.vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publicEgressEnabled') is not None:
            self.public_egress_enabled = m.get('publicEgressEnabled')

        if m.get('publicIngressEnabled') is not None:
            self.public_ingress_enabled = m.get('publicIngressEnabled')

        if m.get('vpc') is not None:
            temp_model = main_models.UpdateWorkspaceRequestBodyNetworkConfigurationVpc()
            self.vpc = temp_model.from_map(m.get('vpc'))

        return self

class UpdateWorkspaceRequestBodyNetworkConfigurationVpc(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # Specifies whether to enable the VPC network.
        self.enabled = enabled
        # The list of vSwitch IDs. When the VPC network is enabled, the list must contain at least one vSwitch, and all vSwitches must belong to the VPC specified by VpcId.
        self.v_switch_ids = v_switch_ids
        # The ID of the user VPC.
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

