# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class CreateIpamScopeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ipam_id: str = None,
        ipam_scope_description: str = None,
        ipam_scope_name: str = None,
        ipam_scope_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateIpamScopeRequestTag] = None,
    ):
        # The client token used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including invalid AccessKey pairs, unauthorized RAM users, and missing parameter values. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and the actual request. After the request passes the dry run, a 2xx HTTP status code is returned and the IPAM scope is created.
        self.dry_run = dry_run
        # The ID of the IPAM.
        # 
        # This parameter is required.
        self.ipam_id = ipam_id
        # The description of the IPAM scope.
        # 
        # It must be 1 to 256 characters in length. It must start with a letter but cannot start with `http://` or `https://`. This parameter is empty by default.
        self.ipam_scope_description = ipam_scope_description
        # The name of the IPAM scope.
        # 
        # It must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.ipam_scope_name = ipam_scope_name
        # The type of IPAM scope: **private**
        # 
        # 
        # **Usage notes** You can create only private IPAM scopes.
        self.ipam_scope_type = ipam_scope_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the IPAM instance is hosted. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the IPAM scope.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tag list.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id

        if self.ipam_scope_description is not None:
            result['IpamScopeDescription'] = self.ipam_scope_description

        if self.ipam_scope_name is not None:
            result['IpamScopeName'] = self.ipam_scope_name

        if self.ipam_scope_type is not None:
            result['IpamScopeType'] = self.ipam_scope_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')

        if m.get('IpamScopeDescription') is not None:
            self.ipam_scope_description = m.get('IpamScopeDescription')

        if m.get('IpamScopeName') is not None:
            self.ipam_scope_name = m.get('IpamScopeName')

        if m.get('IpamScopeType') is not None:
            self.ipam_scope_type = m.get('IpamScopeType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateIpamScopeRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateIpamScopeRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify at most 20 tag keys. It cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). It must start with a letter but cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. You can specify empty strings as tag values.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

