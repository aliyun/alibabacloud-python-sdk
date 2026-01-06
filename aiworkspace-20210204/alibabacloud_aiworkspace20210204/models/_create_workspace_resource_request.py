# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateWorkspaceResourceRequest(DaraModel):
    def __init__(
        self,
        option: str = None,
        resources: List[main_models.CreateWorkspaceResourceRequestResources] = None,
    ):
        # The operation to perform. Valid values:
        # 
        # *   CreateAndAttach: creates resources and associates the resources with a workspace.
        # *   Attach: associates resources with a workspace.
        # 
        # >  MaxCompute supports only the Attach operation.
        self.option = option
        # The resources.
        # 
        # This parameter is required.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option is not None:
            result['Option'] = self.option

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Option') is not None:
            self.option = m.get('Option')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.CreateWorkspaceResourceRequestResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class CreateWorkspaceResourceRequestResources(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        group_name: str = None,
        is_default: bool = None,
        labels: List[main_models.CreateWorkspaceResourceRequestResourcesLabels] = None,
        name: str = None,
        product_type: str = None,
        quotas: List[main_models.CreateWorkspaceResourceRequestResourcesQuotas] = None,
        resource_type: str = None,
        spec: Dict[str, Any] = None,
        workspace_id: str = None,
    ):
        # The environment type. Valid values:
        # 
        # *   dev: development environment
        # *   prod: production environment
        # 
        # This parameter is required.
        self.env_type = env_type
        # The name of the resource group, which is unique within your Alibaba Cloud account. This parameter is required for MaxCompute, Elastic Compute Service (ECS), Lingjun, Alibaba Cloud Container Compute Service (ACS), and Realtime Compute for Apache Flink resources.
        self.group_name = group_name
        # Specifies whether the resource is the default resource. Each type of resources has a default resource. Valid values:
        # 
        # *   false (default)
        # *   true
        self.is_default = is_default
        # The labels added to the resource.
        self.labels = labels
        # The resource name. The name must meet the following requirements:
        # 
        # *   The name must be 3 to 28 characters in length, and can contain only letters, digits, and underscores (_). The name must start with a letter.
        # *   The name must be unique in the region.
        # 
        # This parameter is required.
        self.name = name
        # **This parameter is no longer used and will be removed. Use the ResourceType parameter instead.
        self.product_type = product_type
        # The quotas. Only MaxCompute quotas are available.
        self.quotas = quotas
        # The resource types. Valid values:
        # 
        # *   MaxCompute
        # *   ECS
        # *   Lingjun
        # *   ACS
        # *   FLINK
        self.resource_type = resource_type
        # The resource specifications in the JSON format.
        self.spec = spec
        # The workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.quotas:
            for v1 in self.quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        result['Quotas'] = []
        if self.quotas is not None:
            for k1 in self.quotas:
                result['Quotas'].append(k1.to_map() if k1 else None)

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.CreateWorkspaceResourceRequestResourcesLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.CreateWorkspaceResourceRequestResourcesQuotas()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateWorkspaceResourceRequestResourcesQuotas(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The quota ID. You can call [ListQuotas](https://help.aliyun.com/document_detail/449144.html) to obtain the quota ID.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class CreateWorkspaceResourceRequestResourcesLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The label key.
        self.key = key
        # The label value.
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

