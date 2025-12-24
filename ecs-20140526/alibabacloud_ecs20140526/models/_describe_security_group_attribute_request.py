# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        direction: str = None,
        max_results: int = None,
        next_token: str = None,
        nic_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
    ):
        # The attributes of the security group. Valid value: snapshotPolicyIds: queries information about snapshot policies associated with a security group.
        self.attribute = attribute
        # The direction in which the security group rule is applied. Valid values:
        # 
        # *   egress: outbound
        # *   ingress: inbound
        # *   all: outbound and inbound
        # 
        # Default value: all.
        self.direction = direction
        # The maximum number of entries per page.
        # 
        # *   Minimum value: 10.
        # *   Maximum value: 1000.
        # 
        # Default value: 500.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The network interface controller (NIC) type of the security group rule.
        # 
        # *   Valid values for rules of security groups in the classic network:
        # 
        #     *   internet (default)
        #     *   intranet
        # 
        #     **
        # 
        #     **Note** You can query security group rules of only one NIC type in a single call. To query security group rules of both NIC types, call the operation twice.
        # 
        # *   When the security group is in a virtual private cloud (VPC), set the value to intranet, which is the default value for rules of security groups in VPCs.
        # 
        #     **
        # 
        #     **Note** If you set this parameter to internet or leave this parameter empty, a value of intranet is automatically used.
        self.nic_type = nic_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the security group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.nic_type is not None:
            result['NicType'] = self.nic_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NicType') is not None:
            self.nic_type = m.get('NicType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

