# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateEnvironmentRequest(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        bind_resource_id: str = None,
        environment_name: str = None,
        environment_sub_type: str = None,
        environment_type: str = None,
        fee_package: str = None,
        grafana_workspace_id: str = None,
        init_environment: bool = None,
        managed_type: str = None,
        prometheus_instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateEnvironmentRequestTags] = None,
    ):
        # The language. Default value: zh.
        # 
        # Valid values:
        # *   en: English
        # *   zh: Chinese
        self.aliyun_lang = aliyun_lang
        # The ID of the resource bound to the environment, such as the container ID or VPC ID. For a Cloud environment, specify the region ID.
        # 
        # This parameter is required.
        self.bind_resource_id = bind_resource_id
        # The name of the environment.
        # 
        # This parameter is required.
        self.environment_name = environment_name
        # The subtype of the environment. Valid values:
        # 
        # *   CS: Container Service for Kubernetes (ACK) or Distributed Cloud Container Platform for Kubernetes (ACK One)
        # *   ECS: ECS
        # *   Cloud: cloud service
        # 
        # This parameter is required.
        self.environment_sub_type = environment_sub_type
        # The type of the environment. Valid values:
        # 
        # *   CS: Container Service
        # *   ECS: Elastic Compute Service
        # *   Cloud: cloud service
        # 
        # This parameter is required.
        self.environment_type = environment_type
        # The payable resource plan.
        # 
        # *   If the EnvironmentType parameter is set to CS, set the value to CS_Basic or CS_Pro. Default value: CS_Basic.
        # *   Otherwise, leave the parameter empty.
        self.fee_package = fee_package
        # The ID of the Grafana workspace associated with the environment. If this parameter is left empty, the default shared Grafana workspace is used.
        self.grafana_workspace_id = grafana_workspace_id
        # Specifies whether to initialize the environment.
        self.init_environment = init_environment
        # Specifies whether agents or exporters are managed. Valid values:
        # 
        # *   none: No. By default, no managed agents or exporters are provided for ACK clusters.
        # *   agent: Agents are managed. By default, managed agents are provided for ASK clusters, ACS clusters, and ACK One clusters.
        # *   agent-exporter: Agents and exporters are managed. By default, managed agents and exporters are provided for cloud services.
        self.managed_type = managed_type
        # The ID of the Prometheus instance. If no Prometheus instance is created, call the InitEnvironment operation.
        self.prometheus_instance_id = prometheus_instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the instance. You can specify this parameter to manage tags for the instance.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.bind_resource_id is not None:
            result['BindResourceId'] = self.bind_resource_id

        if self.environment_name is not None:
            result['EnvironmentName'] = self.environment_name

        if self.environment_sub_type is not None:
            result['EnvironmentSubType'] = self.environment_sub_type

        if self.environment_type is not None:
            result['EnvironmentType'] = self.environment_type

        if self.fee_package is not None:
            result['FeePackage'] = self.fee_package

        if self.grafana_workspace_id is not None:
            result['GrafanaWorkspaceId'] = self.grafana_workspace_id

        if self.init_environment is not None:
            result['InitEnvironment'] = self.init_environment

        if self.managed_type is not None:
            result['ManagedType'] = self.managed_type

        if self.prometheus_instance_id is not None:
            result['PrometheusInstanceId'] = self.prometheus_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('BindResourceId') is not None:
            self.bind_resource_id = m.get('BindResourceId')

        if m.get('EnvironmentName') is not None:
            self.environment_name = m.get('EnvironmentName')

        if m.get('EnvironmentSubType') is not None:
            self.environment_sub_type = m.get('EnvironmentSubType')

        if m.get('EnvironmentType') is not None:
            self.environment_type = m.get('EnvironmentType')

        if m.get('FeePackage') is not None:
            self.fee_package = m.get('FeePackage')

        if m.get('GrafanaWorkspaceId') is not None:
            self.grafana_workspace_id = m.get('GrafanaWorkspaceId')

        if m.get('InitEnvironment') is not None:
            self.init_environment = m.get('InitEnvironment')

        if m.get('ManagedType') is not None:
            self.managed_type = m.get('ManagedType')

        if m.get('PrometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('PrometheusInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateEnvironmentRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateEnvironmentRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

