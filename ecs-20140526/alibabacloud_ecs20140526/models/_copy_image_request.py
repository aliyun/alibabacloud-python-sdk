# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CopyImageRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        destination_description: str = None,
        destination_image_name: str = None,
        destination_region_id: str = None,
        dry_run: bool = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        image_id: str = None,
        kmskey_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CopyImageRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken parameter can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the copied image. The description must be 2 to 256 characters in length, and cannot start with http:// or https://.
        self.destination_description = destination_description
        # The name of the copied image. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character, and cannot start with aliyun or acs:. It cannot contain http:// or https://. It can contain digits, periods (.), colons (:), underscores (_), and hyphens (-).
        self.destination_image_name = destination_image_name
        # The ID of the destination region.
        self.destination_region_id = destination_region_id
        # Specifies whether to only perform a dry run for this request. Valid values:
        # 
        # - true: performs a dry run. The system checks whether your AccessKey pair is valid, whether the Resource Access Management (RAM) user has authorization, and whether the required parameters are specified. If the request fails the dry run, the corresponding error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # - false: sends a Normal request. If the request passes the dry run, a 2XX HTTP status code is returned and the operation is performed.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # > This parameter is not available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the copied image. Valid values:
        # 
        # - true: Encrypts the image.
        # - false: Does not encrypt the image.
        # - Not specified: The encryption status depends on the backend logic. For more information, see the supplementary description below.
        # 
        # Default value: none.
        self.encrypted = encrypted
        # The ID of the source custom image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The ID of the key used to encrypt the image.
        self.kmskey_id = kmskey_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the source custom image. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the image after replication. If you do not specify this parameter, the image after replication belongs to the default resource group.
        # 
        # > If you invoke this operation as a Resource Access Management (RAM) user and leave ResourceGroupId empty, note that if the Resource Access Management (RAM) user does not have permissions on the default resource group, the operation returns the `Forbidden: User not authorized to operate on the specified resource` error. Update the Settings of ResourceGroupId to the ID of a resource group on which the Resource Access Management (RAM) user has permissions, or use the corresponding Alibaba Cloud account to grant the Resource Access Management (RAM) user permissions on the default resource group, and then invoke this operation again.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of tags.
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

        if self.destination_description is not None:
            result['DestinationDescription'] = self.destination_description

        if self.destination_image_name is not None:
            result['DestinationImageName'] = self.destination_image_name

        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

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

        if m.get('DestinationDescription') is not None:
            self.destination_description = m.get('DestinationDescription')

        if m.get('DestinationImageName') is not None:
            self.destination_image_name = m.get('DestinationImageName')

        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

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
                temp_model = main_models.CopyImageRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CopyImageRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the copied image. Valid values of N: 1 to 20. If you specify this parameter, it cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The value of tag N of the copied image. Valid values of N: 1 to 20. If you specify this parameter, it can be an empty string. The tag value can be up to 128 characters in length. It cannot start with acs:, and cannot contain http:// or https://.
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

