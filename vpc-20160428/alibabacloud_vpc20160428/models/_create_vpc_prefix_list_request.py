# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CreateVpcPrefixListRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ip_version: str = None,
        max_entries: int = None,
        owner_account: str = None,
        owner_id: int = None,
        prefix_list_description: str = None,
        prefix_list_entries: List[main_models.CreateVpcPrefixListRequestPrefixListEntries] = None,
        prefix_list_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateVpcPrefixListRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without creating the prefix list. The system checks the required parameters, request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the check succeeds, an HTTP 2xx status code is returned and the prefix list is created.
        self.dry_run = dry_run
        # The IP version. Valid values:
        # 
        # - **IPv4** (default): IPv4.
        # - **IPv6**: IPv6.
        self.ip_version = ip_version
        # The maximum number of entries for Classless Inter-Domain Routing (CIDR) blocks in the prefix list. Default value: 50.
        self.max_entries = max_entries
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The description of the prefix list.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.prefix_list_description = prefix_list_description
        # The Classless Inter-Domain Routing (CIDR) block information of the prefix list.
        self.prefix_list_entries = prefix_list_entries
        # The name of the prefix list.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.prefix_list_name = prefix_list_name
        # The region ID of the prefix list that you want to create. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the prefix list belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tag = tag

    def validate(self):
        if self.prefix_list_entries:
            for v1 in self.prefix_list_entries:
                 if v1:
                    v1.validate()
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

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.max_entries is not None:
            result['MaxEntries'] = self.max_entries

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prefix_list_description is not None:
            result['PrefixListDescription'] = self.prefix_list_description

        result['PrefixListEntries'] = []
        if self.prefix_list_entries is not None:
            for k1 in self.prefix_list_entries:
                result['PrefixListEntries'].append(k1.to_map() if k1 else None)

        if self.prefix_list_name is not None:
            result['PrefixListName'] = self.prefix_list_name

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

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('MaxEntries') is not None:
            self.max_entries = m.get('MaxEntries')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrefixListDescription') is not None:
            self.prefix_list_description = m.get('PrefixListDescription')

        self.prefix_list_entries = []
        if m.get('PrefixListEntries') is not None:
            for k1 in m.get('PrefixListEntries'):
                temp_model = main_models.CreateVpcPrefixListRequestPrefixListEntries()
                self.prefix_list_entries.append(temp_model.from_map(k1))

        if m.get('PrefixListName') is not None:
            self.prefix_list_name = m.get('PrefixListName')

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
                temp_model = main_models.CreateVpcPrefixListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateVpcPrefixListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

class CreateVpcPrefixListRequestPrefixListEntries(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
    ):
        # The Classless Inter-Domain Routing (CIDR) block of the prefix list.
        self.cidr = cidr
        # The description of the Classless Inter-Domain Routing (CIDR) block in the prefix list.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

