# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKmsAssociateResourcesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        kms_resource_id: str = None,
        kms_resource_region_id: str = None,
        kms_resource_type: str = None,
        kms_resource_user: str = None,
        owner_account: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The ID of the KMS resource. Only key IDs are supported.
        # 
        # This parameter is required.
        self.kms_resource_id = kms_resource_id
        # The ID of the region to which the KMS resource belongs.
        self.kms_resource_region_id = kms_resource_region_id
        # The type of the KMS resource. Only key is supported.
        # 
        # This parameter is required.
        self.kms_resource_type = kms_resource_type
        # The ID of the Alibaba Cloud account to which the KMS resource belongs.
        # 
        # This parameter is required.
        self.kms_resource_user = kms_resource_user
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.kms_resource_id is not None:
            result['KmsResourceId'] = self.kms_resource_id

        if self.kms_resource_region_id is not None:
            result['KmsResourceRegionId'] = self.kms_resource_region_id

        if self.kms_resource_type is not None:
            result['KmsResourceType'] = self.kms_resource_type

        if self.kms_resource_user is not None:
            result['KmsResourceUser'] = self.kms_resource_user

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('KmsResourceId') is not None:
            self.kms_resource_id = m.get('KmsResourceId')

        if m.get('KmsResourceRegionId') is not None:
            self.kms_resource_region_id = m.get('KmsResourceRegionId')

        if m.get('KmsResourceType') is not None:
            self.kms_resource_type = m.get('KmsResourceType')

        if m.get('KmsResourceUser') is not None:
            self.kms_resource_user = m.get('KmsResourceUser')

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

        return self

