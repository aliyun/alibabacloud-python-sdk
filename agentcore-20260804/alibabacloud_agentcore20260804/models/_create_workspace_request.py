# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        body: main_models.CreateWorkspaceRequestBody = None,
        client_token: str = None,
    ):
        # The request body for creating a workspace.
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
            temp_model = main_models.CreateWorkspaceRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class CreateWorkspaceRequestBody(DaraModel):
    def __init__(
        self,
        name: str = None,
        network_configuration: main_models.CreateWorkspaceRequestBodyNetworkConfiguration = None,
    ):
        # The workspace name.
        # 
        # This parameter is required.
        self.name = name
        # The network configuration of the workspace.
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
            temp_model = main_models.CreateWorkspaceRequestBodyNetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        return self

class CreateWorkspaceRequestBodyNetworkConfiguration(DaraModel):
    def __init__(
        self,
        vpc: main_models.CreateWorkspaceRequestBodyNetworkConfigurationVpc = None,
    ):
        # The VPC network configuration of the user.
        # 
        # This parameter is required.
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            self.vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc is not None:
            result['vpc'] = self.vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpc') is not None:
            temp_model = main_models.CreateWorkspaceRequestBodyNetworkConfigurationVpc()
            self.vpc = temp_model.from_map(m.get('vpc'))

        return self

class CreateWorkspaceRequestBodyNetworkConfigurationVpc(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # Specifies whether to enable VPC networking.
        self.enabled = enabled
        # The list of vSwitch IDs. When VPC networking is enabled, at least one vSwitch must be included, and all vSwitches must belong to the VPC specified by VpcId.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC.
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

