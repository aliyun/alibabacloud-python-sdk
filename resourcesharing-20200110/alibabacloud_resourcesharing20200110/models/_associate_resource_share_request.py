# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class AssociateResourceShareRequest(DaraModel):
    def __init__(
        self,
        permission_names: List[str] = None,
        resource_arns: List[str] = None,
        resource_properties: List[main_models.AssociateResourceShareRequestResourceProperties] = None,
        resource_share_id: str = None,
        resources: List[main_models.AssociateResourceShareRequestResources] = None,
        target_properties: List[main_models.AssociateResourceShareRequestTargetProperties] = None,
        targets: List[str] = None,
    ):
        # The information about the permissions. If you do not configure this parameter, the system automatically associates the default permission for the specified resource type with the resource share. For more information, see [Permission library](https://help.aliyun.com/document_detail/465474.html).
        self.permission_names = permission_names
        self.resource_arns = resource_arns
        self.resource_properties = resource_properties
        # The ID of the resource share.
        # 
        # This parameter is required.
        self.resource_share_id = resource_share_id
        # The information about the resources.
        self.resources = resources
        # The properties of the principal.
        # 
        # >  This parameter is available only when you specify an Alibaba Cloud service as a principal.
        self.target_properties = target_properties
        # The information about the principals.
        self.targets = targets

    def validate(self):
        if self.resource_properties:
            for v1 in self.resource_properties:
                 if v1:
                    v1.validate()
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()
        if self.target_properties:
            for v1 in self.target_properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission_names is not None:
            result['PermissionNames'] = self.permission_names

        if self.resource_arns is not None:
            result['ResourceArns'] = self.resource_arns

        result['ResourceProperties'] = []
        if self.resource_properties is not None:
            for k1 in self.resource_properties:
                result['ResourceProperties'].append(k1.to_map() if k1 else None)

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        result['TargetProperties'] = []
        if self.target_properties is not None:
            for k1 in self.target_properties:
                result['TargetProperties'].append(k1.to_map() if k1 else None)

        if self.targets is not None:
            result['Targets'] = self.targets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionNames') is not None:
            self.permission_names = m.get('PermissionNames')

        if m.get('ResourceArns') is not None:
            self.resource_arns = m.get('ResourceArns')

        self.resource_properties = []
        if m.get('ResourceProperties') is not None:
            for k1 in m.get('ResourceProperties'):
                temp_model = main_models.AssociateResourceShareRequestResourceProperties()
                self.resource_properties.append(temp_model.from_map(k1))

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.AssociateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k1))

        self.target_properties = []
        if m.get('TargetProperties') is not None:
            for k1 in m.get('TargetProperties'):
                temp_model = main_models.AssociateResourceShareRequestTargetProperties()
                self.target_properties.append(temp_model.from_map(k1))

        if m.get('Targets') is not None:
            self.targets = m.get('Targets')

        return self

class AssociateResourceShareRequestTargetProperties(DaraModel):
    def __init__(
        self,
        property: str = None,
        target_id: str = None,
    ):
        # The property parameter of the principal. For example, you can specify a parameter that indicates the time range for resource sharing. Valid values of `timeRangeType`:
        # 
        # *   timeRange: a specific time range
        # *   day: all day
        # 
        # >  `TargetProperties.N.TargetId` and `TargetProperties.N.Property` must be used in pairs.
        self.property = property
        # The ID of the principal.
        # 
        # >  `TargetProperties.N.TargetId` and `TargetProperties.N.Property` must be used in pairs.
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property is not None:
            result['Property'] = self.property

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        return self

class AssociateResourceShareRequestResources(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # >  Resources.N.ResourceId and Resources.N.ResourceType must be used in pairs.
        self.resource_id = resource_id
        # The type of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](https://help.aliyun.com/document_detail/450526.html).
        # 
        # >  `Resources.N.ResourceId` and `Resources.N.ResourceType` must be used in pairs.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class AssociateResourceShareRequestResourceProperties(DaraModel):
    def __init__(
        self,
        property: str = None,
        resource_arn: str = None,
    ):
        self.property = property
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property is not None:
            result['Property'] = self.property

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        return self

