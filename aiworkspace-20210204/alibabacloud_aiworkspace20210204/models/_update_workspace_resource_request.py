# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkspaceResourceRequest(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        is_default: bool = None,
        labels: List[main_models.UpdateWorkspaceResourceRequestLabels] = None,
        product_type: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        spec: Dict[str, Any] = None,
    ):
        # The group name.
        self.group_name = group_name
        # Specifies whether the resource is the default resource. This parameter can only be set to true and cannot be set to false.
        self.is_default = is_default
        # The resource tags. If you specify multiple tags, only resources that meet all the specified tag-based filter conditions are returned.
        self.labels = labels
        # **This field is no longer used and will be removed. Use the ResourceType field.
        self.product_type = product_type
        # The resource IDs.
        # 
        # You cannot leave both GroupName and ResourceIds empty. If you specify both the parameters, the value of GroupName of each resource ID in the dataset must be the same.
        self.resource_ids = resource_ids
        # The resource type. Valid values:
        # 
        # *   MaxCompute
        # *   ECS
        # *   Lingjun
        # *   ACS
        # *   FLINK
        self.resource_type = resource_type
        # The specification of the resource.
        self.spec = spec

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.UpdateWorkspaceResourceRequestLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

class UpdateWorkspaceResourceRequestLabels(DaraModel):
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

