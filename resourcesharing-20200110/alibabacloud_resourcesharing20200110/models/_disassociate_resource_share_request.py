# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class DisassociateResourceShareRequest(DaraModel):
    def __init__(
        self,
        resource_arns: List[str] = None,
        resource_owner: str = None,
        resource_share_id: str = None,
        resources: List[main_models.DisassociateResourceShareRequestResources] = None,
        targets: List[str] = None,
    ):
        self.resource_arns = resource_arns
        # The owner of the resource share. Valid values:
        # 
        # *   Self: The resource share belongs to the current account. This is the default value. For resource sharing within a resource directory, if you are a resource owner and you want to disassociate resources or principals from a resource share, set this parameter to Self.
        # *   OtherAccounts: The resource share belongs to another account. For resource sharing outside a resource directory, if you are a principal and you want to exit a resource share, set this parameter to OtherAccounts.
        self.resource_owner = resource_owner
        # The ID of the resource share.
        # 
        # This parameter is required.
        self.resource_share_id = resource_share_id
        # The information about the resources.
        self.resources = resources
        # The information about the principals.
        self.targets = targets

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
        if self.resource_arns is not None:
            result['ResourceArns'] = self.resource_arns

        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.targets is not None:
            result['Targets'] = self.targets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceArns') is not None:
            self.resource_arns = m.get('ResourceArns')

        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.DisassociateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('Targets') is not None:
            self.targets = m.get('Targets')

        return self

class DisassociateResourceShareRequestResources(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the shared resource.
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
        # >  Resources.N.ResourceId and Resources.N.ResourceType must be used in pairs.
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

