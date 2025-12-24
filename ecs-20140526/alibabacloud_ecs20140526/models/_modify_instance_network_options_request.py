# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceNetworkOptionsRequest(DaraModel):
    def __init__(
        self,
        bandwidth_weighting: str = None,
        instance_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The bandwidth weight.
        # 
        # The supported values vary with instance types. You can query the bandwidth weights supported by the current instance type by using the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html).
        # 
        # Valid values:
        # 
        # *   Vpc-L1: Vpc-L1.
        # *   Vpc-L2: Vpc-L2.
        # *   Ebs-L1: Ebs-L1.
        # *   Ebs-L2: Ebs-L2.
        # *   Default: the Default.
        self.bandwidth_weighting = bandwidth_weighting
        # The ID of the instance whose network bandwidth weight is to be modified.
        self.instance_id = instance_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_weighting is not None:
            result['BandwidthWeighting'] = self.bandwidth_weighting

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthWeighting') is not None:
            self.bandwidth_weighting = m.get('BandwidthWeighting')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

