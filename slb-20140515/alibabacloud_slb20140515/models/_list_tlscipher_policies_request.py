# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTLSCipherPoliciesRequest(DaraModel):
    def __init__(
        self,
        include_listener: bool = None,
        max_items: int = None,
        name: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tlscipher_policy_id: str = None,
    ):
        # Specifies whether to return the information about the associated listeners. Valid values:
        # 
        # *   **true**: returns the information about the associated listeners.
        # *   **false** (default): does not return the information about the associated listeners.
        self.include_listener = include_listener
        # The maximum number of TLS policies to be queried in this call. Valid values: **1** to **100**. If you do not set this parameter, the default value **20** is used.
        self.max_items = max_items
        # The name of the TLS policy. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the value to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the Classic Load Balancer (CLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the TLS policy.
        self.tlscipher_policy_id = tlscipher_policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_listener is not None:
            result['IncludeListener'] = self.include_listener

        if self.max_items is not None:
            result['MaxItems'] = self.max_items

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if self.tlscipher_policy_id is not None:
            result['TLSCipherPolicyId'] = self.tlscipher_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeListener') is not None:
            self.include_listener = m.get('IncludeListener')

        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

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

        if m.get('TLSCipherPolicyId') is not None:
            self.tlscipher_policy_id = m.get('TLSCipherPolicyId')

        return self

