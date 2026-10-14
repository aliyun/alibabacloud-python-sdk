# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class UnassociateNetworkAclRequest(DaraModel):
    def __init__(
        self,
        network_acl_id: str = None,
        resource: List[main_models.UnassociateNetworkAclRequestResource] = None,
    ):
        # The ID of the network ACL.
        # 
        # This parameter is required.
        self.network_acl_id = network_acl_id
        # The list of resources to disassociate. Valid values of N: 1 to 30. The resources must be associated with the network ACL by calling the AssociateNetworkAcl operation, and the current association status must be BINDED.
        # 
        # This parameter is required.
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.UnassociateNetworkAclRequestResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class UnassociateNetworkAclRequestResource(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the associated resource to disassociate.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the associated resource to disassociate. Valid values:
        # * Network: network.
        # 
        # This parameter is required.
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

