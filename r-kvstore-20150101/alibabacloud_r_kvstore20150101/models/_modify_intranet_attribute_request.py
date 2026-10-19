# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyIntranetAttributeRequest(DaraModel):
    def __init__(
        self,
        band_width: int = None,
        instance_id: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The bandwidth to add, in MB/s. The value must be an integer greater than or equal to 0. Typically, the maximum value is twice the default maximum bandwidth of the current instance type. For bandwidth information about each instance type, see [Instance type navigation](https://help.aliyun.com/document_detail/26350.html). However, the following limits also apply:
        # * The bandwidth of a single instance cannot exceed 75% of the bandwidth of the host on which the instance resides. For information about host specifications and bandwidth, see [Host specification details](https://help.aliyun.com/document_detail/206343.html).
        # * The total bandwidth of all instances on a host cannot exceed 150% of the bandwidth of the host. You can configure overcommitment to meet bandwidth requirements for staggered-peak deployment. For more information, see [Configure cluster overcommitment to reduce costs](https://help.aliyun.com/document_detail/183798.html).
        # 
        # > For instances that use the standard architecture, if you do not specify this parameter, the bandwidth of the instance is doubled based on the current bandwidth.
        self.band_width = band_width
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the data node. You can call [DescribeClusterMemberInfo](https://help.aliyun.com/document_detail/473783.html) to query the ID. Separate multiple IDs with commas (,).
        # > This parameter is available and required only when the instance uses the [Cluster Edition](https://help.aliyun.com/document_detail/52228.html).
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width is not None:
            result['BandWidth'] = self.band_width

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

