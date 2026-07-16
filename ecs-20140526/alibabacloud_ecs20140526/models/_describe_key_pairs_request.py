# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeKeyPairsRequest(DaraModel):
    def __init__(
        self,
        include_public_key: bool = None,
        key_pair_finger_print: str = None,
        key_pair_name: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeKeyPairsRequestTag] = None,
    ):
        # Specifies whether to include PublicKey in the response.
        # Default value: false.
        self.include_public_key = include_public_key
        # The fingerprint of the key pair. The fingerprint uses the message-digest algorithm 5 (MD5) based on the public key fingerprint format defined in RFC 4716. For more information, see [RFC 4716](https://tools.ietf.org/html/rfc4716).
        self.key_pair_finger_print = key_pair_finger_print
        # The name of the key pair. You can use regular expressions for fuzzy search, with the asterisk (*) to match child table expressions. Examples:
        # 
        # - `*SshKey`: searches for key pair names that end with SshKey, including SshKey.
        # - `SshKey*`: searches for key pair names that start with SshKey, including SshKey.
        # - `*SshKey*`: searches for key pair names that contain SshKey, including SshKey.
        # - `SshKey`: exact match of SshKey.
        self.key_pair_name = key_pair_name
        self.owner_id = owner_id
        # The page number of the key pair list. Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page in paging queries. Settings: Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the key pairs. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the key pairs belong. When you use this parameter to filter resources, the resource count cannot exceed 1000.
        # 
        # >Filtering by the default resource group is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
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
        if self.include_public_key is not None:
            result['IncludePublicKey'] = self.include_public_key

        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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
        if m.get('IncludePublicKey') is not None:
            self.include_public_key = m.get('IncludePublicKey')

        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

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
                temp_model = main_models.DescribeKeyPairsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeKeyPairsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the key pair. Valid values of N: 1 to 20.
        # 
        # If you use a single tag to filter resources, the resource count with the specified tag cannot exceed 1000. If you use multiple tags to filter resources, the resource count of resources that are attached with all specified tags cannot exceed 1000. If the resource count exceeds 1000, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query resources.
        self.key = key
        # The tag value of the key pair. Valid values of N: 1 to 20.
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

