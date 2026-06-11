# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HiMarketPortalDeployConfig(DaraModel):
    def __init__(
        self,
        message: str = None,
        platform: str = None,
        sae_config: main_models.HiMarketPortalDeployConfigSaeConfig = None,
        status: str = None,
    ):
        # Additional information about the deployment status, such as error details.
        self.message = message
        # The target deployment platform. For example, set this to `SAE` to deploy on Serverless App Engine.
        self.platform = platform
        # Configuration settings for deploying to Serverless App Engine (SAE). This object is required when the `platform` is `SAE`.
        self.sae_config = sae_config
        # The current status of the deployment. Possible values include `succeeded`, `failed`, and `in_progress`.
        self.status = status

    def validate(self):
        if self.sae_config:
            self.sae_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.platform is not None:
            result['platform'] = self.platform

        if self.sae_config is not None:
            result['saeConfig'] = self.sae_config.to_map()

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('saeConfig') is not None:
            temp_model = main_models.HiMarketPortalDeployConfigSaeConfig()
            self.sae_config = temp_model.from_map(m.get('saeConfig'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class HiMarketPortalDeployConfigSaeConfig(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        namespace_id: str = None,
        oidc_role_name: str = None,
        region_id: str = None,
        replicas: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of the application in Serverless App Engine.
        self.app_id = app_id
        # The ID of the namespace that logically isolates the application.
        self.namespace_id = namespace_id
        # The name of the OIDC role that grants permissions to the application.
        self.oidc_role_name = oidc_role_name
        # The ID of the region in which to deploy the application.
        self.region_id = region_id
        # The desired number of application replicas.
        self.replicas = replicas
        # The ID of the security group to apply to the application instances. A security group acts as a virtual firewall.
        self.security_group_id = security_group_id
        # The ID of the vSwitch within the specified VPC. Serverless App Engine launches application instances in the vSwitch\\"s zone.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to connect the application to.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.namespace_id is not None:
            result['namespaceId'] = self.namespace_id

        if self.oidc_role_name is not None:
            result['oidcRoleName'] = self.oidc_role_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.replicas is not None:
            result['replicas'] = self.replicas

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('namespaceId') is not None:
            self.namespace_id = m.get('namespaceId')

        if m.get('oidcRoleName') is not None:
            self.oidc_role_name = m.get('oidcRoleName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('replicas') is not None:
            self.replicas = m.get('replicas')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

