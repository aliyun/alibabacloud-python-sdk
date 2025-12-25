# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateSourceRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        k_8s_source_config: main_models.CreateSourceRequestK8sSourceConfig = None,
        nacos_source_config: main_models.CreateSourceRequestNacosSourceConfig = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        # The gateway instance ID.
        self.gateway_id = gateway_id
        # The source configuration when the source type is K8S.
        self.k_8s_source_config = k_8s_source_config
        # The source configuration when the source type is MSE_NACOS.
        self.nacos_source_config = nacos_source_config
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The source type. Valid values:
        # 
        # *   MSE_NACOS: MSE Nacos
        # *   K8S: Container Service for Kubernetes (ACK)
        self.type = type

    def validate(self):
        if self.k_8s_source_config:
            self.k_8s_source_config.validate()
        if self.nacos_source_config:
            self.nacos_source_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.k_8s_source_config is not None:
            result['k8sSourceConfig'] = self.k_8s_source_config.to_map()

        if self.nacos_source_config is not None:
            result['nacosSourceConfig'] = self.nacos_source_config.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('k8sSourceConfig') is not None:
            temp_model = main_models.CreateSourceRequestK8sSourceConfig()
            self.k_8s_source_config = temp_model.from_map(m.get('k8sSourceConfig'))

        if m.get('nacosSourceConfig') is not None:
            temp_model = main_models.CreateSourceRequestNacosSourceConfig()
            self.nacos_source_config = temp_model.from_map(m.get('nacosSourceConfig'))

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateSourceRequestNacosSourceConfig(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The Nacos instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

class CreateSourceRequestK8sSourceConfig(DaraModel):
    def __init__(
        self,
        authorize_security_group_rules: List[main_models.CreateSourceRequestK8sSourceConfigAuthorizeSecurityGroupRules] = None,
        cluster_id: str = None,
    ):
        # The security group rules.
        self.authorize_security_group_rules = authorize_security_group_rules
        # The ID of the ACK cluster.
        self.cluster_id = cluster_id

    def validate(self):
        if self.authorize_security_group_rules:
            for v1 in self.authorize_security_group_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['authorizeSecurityGroupRules'] = []
        if self.authorize_security_group_rules is not None:
            for k1 in self.authorize_security_group_rules:
                result['authorizeSecurityGroupRules'].append(k1.to_map() if k1 else None)

        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorize_security_group_rules = []
        if m.get('authorizeSecurityGroupRules') is not None:
            for k1 in m.get('authorizeSecurityGroupRules'):
                temp_model = main_models.CreateSourceRequestK8sSourceConfigAuthorizeSecurityGroupRules()
                self.authorize_security_group_rules.append(temp_model.from_map(k1))

        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        return self

class CreateSourceRequestK8sSourceConfigAuthorizeSecurityGroupRules(DaraModel):
    def __init__(
        self,
        description: str = None,
        port_ranges: List[str] = None,
        security_group_id: str = None,
    ):
        # The rule description.
        self.description = description
        # The list of port ranges.
        self.port_ranges = port_ranges
        # The ID of a security group.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.port_ranges is not None:
            result['portRanges'] = self.port_ranges

        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('portRanges') is not None:
            self.port_ranges = m.get('portRanges')

        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        return self

