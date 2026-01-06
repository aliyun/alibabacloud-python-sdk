# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListResourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[main_models.ListResourcesResponseBodyResources] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.resources = resources
        # The number of resources that meet the filter conditions.
        self.total_count = total_count

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ListResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        encryption: main_models.ListResourcesResponseBodyResourcesEncryption = None,
        env_type: str = None,
        executor: main_models.ListResourcesResponseBodyResourcesExecutor = None,
        gmt_create_time: str = None,
        group_name: str = None,
        id: str = None,
        is_default: bool = None,
        labels: List[main_models.ListResourcesResponseBodyResourcesLabels] = None,
        name: str = None,
        product_type: str = None,
        quotas: List[main_models.ListResourcesResponseBodyResourcesQuotas] = None,
        resource_type: str = None,
        spec: Dict[str, Any] = None,
        workspace_id: str = None,
    ):
        # The encryption information, which is valid only for MaxCompute resources.
        self.encryption = encryption
        # The environment type. Valid values:
        # 
        # *   dev: development environment
        # *   prod: production environment
        self.env_type = env_type
        # This parameter is invalid and deprecated.
        self.executor = executor
        # The time when the resource group is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The name of the resource group, which is unique within the Alibaba Cloud account.
        self.group_name = group_name
        # The resource ID.
        self.id = id
        # Indicates whether the resource is the default resource. Each type of resources has a default resource. Valid values:
        # 
        # *   true
        # *   false
        self.is_default = is_default
        # The tags.
        self.labels = labels
        # The resource name.
        self.name = name
        # **This field is no longer used and will be removed. Use the ResourceType field.
        self.product_type = product_type
        # The quotas.
        self.quotas = quotas
        # The resource type. Valid values:
        # 
        # *   MaxCompute
        # *   DLC
        # *   FLINK
        self.resource_type = resource_type
        # The resource specification.
        self.spec = spec
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.executor:
            self.executor.validate()
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
        if self.encryption is not None:
            result['Encryption'] = self.encryption.to_map()

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.executor is not None:
            result['Executor'] = self.executor.to_map()

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

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
        if m.get('Encryption') is not None:
            temp_model = main_models.ListResourcesResponseBodyResourcesEncryption()
            self.encryption = temp_model.from_map(m.get('Encryption'))

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Executor') is not None:
            temp_model = main_models.ListResourcesResponseBodyResourcesExecutor()
            self.executor = temp_model.from_map(m.get('Executor'))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ListResourcesResponseBodyResourcesLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.ListResourcesResponseBodyResourcesQuotas()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ListResourcesResponseBodyResourcesQuotas(DaraModel):
    def __init__(
        self,
        card_type: str = None,
        display_name: str = None,
        id: str = None,
        mode: str = None,
        name: str = None,
        product_code: str = None,
        quota_type: str = None,
        specs: List[main_models.ListResourcesResponseBodyResourcesQuotasSpecs] = None,
    ):
        # The resource group type. Valid values:
        # 
        # *   CPU
        # *   GPU
        self.card_type = card_type
        # The alias of the quota.
        self.display_name = display_name
        # The quota ID.
        self.id = id
        # The billing method. Valid values:
        # 
        # *   isolate: subscription
        # *   share: pay-as-you-go
        self.mode = mode
        # The quota name.
        self.name = name
        # The product code. Valid values:
        # 
        # *   PAI_isolate: CPU subscription resource groups of PAI
        # *   PAI_share: GPU pay-as-you-go resource groups of PAI
        # *   MaxCompute_share: pay-as-you-go resource groups of MaxCompute
        # *   MaxCompute_isolate: subscription resource groups of MaxCompute
        # *   DataWorks_isolate: subscription resource groups of DataWorks
        # *   DataWorks_share: pay-as-you-go resource groups of DataWorks
        # *   DLC_share: pay-as-you-go resource groups of Deep Learning Containers (DLC)
        self.product_code = product_code
        # The quota type. Valid values:
        # 
        # *   PAI
        # *   MaxCompute
        # *   DLC
        self.quota_type = quota_type
        # The quota specifications.
        self.specs = specs

    def validate(self):
        if self.specs:
            for v1 in self.specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_type is not None:
            result['CardType'] = self.card_type

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        result['Specs'] = []
        if self.specs is not None:
            for k1 in self.specs:
                result['Specs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        self.specs = []
        if m.get('Specs') is not None:
            for k1 in m.get('Specs'):
                temp_model = main_models.ListResourcesResponseBodyResourcesQuotasSpecs()
                self.specs.append(temp_model.from_map(k1))

        return self

class ListResourcesResponseBodyResourcesQuotasSpecs(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The specification name.
        self.name = name
        # The specification description.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListResourcesResponseBodyResourcesLabels(DaraModel):
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

class ListResourcesResponseBodyResourcesExecutor(DaraModel):
    def __init__(
        self,
        owner_id: str = None,
    ):
        # This parameter is invalid and deprecated.
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

class ListResourcesResponseBodyResourcesEncryption(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        enabled: bool = None,
        key: str = None,
    ):
        # The encryption algorithm.
        self.algorithm = algorithm
        # Indicates whether the resources are encrypted.
        self.enabled = enabled
        # The primary key for the encryption.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

