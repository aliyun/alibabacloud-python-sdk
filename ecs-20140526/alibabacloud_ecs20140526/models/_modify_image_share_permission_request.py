# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyImageSharePermissionRequest(DaraModel):
    def __init__(
        self,
        add_account: List[str] = None,
        dry_run: bool = None,
        image_id: str = None,
        is_public: bool = None,
        launch_permission: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remove_account: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The Alibaba Cloud account ID to which you want to grant authorization to share the image. Valid values of N: 1 to 10. If you commit more than 10 Alibaba Cloud accounts at a time, the system processes only the first 10 accounts and ignores the rest.
        self.add_account = add_account
        self.dry_run = dry_run
        # The ID of the custom image to be shared.
        # 
        # >Notice: Sharing images encrypted with a service key is no longer supported. Only images encrypted with a customer master key (CMK) can be shared. An error is returned if you attempt to share an image encrypted with a service key.
        # 
        # This parameter is required.
        self.image_id = image_id
        # Specifies whether to publish or delist the community image. Valid values:
        # 
        # - true: Publishes the image as a community image.
        # - false: Delists the image to a regular image. If the image is already a regular image, no change is made.
        # 
        # Default value: false.
        self.is_public = is_public
        # >This parameter is in invitational preview and is not available for use.
        self.launch_permission = launch_permission
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the custom image. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The Alibaba Cloud account ID from which you want to delete image sharing. Valid values of N: 1 to 10. If you commit more than 10 Alibaba Cloud accounts at a time, the system processes only the first 10 accounts and ignores the rest.
        self.remove_account = remove_account
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_account is not None:
            result['AddAccount'] = self.add_account

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.is_public is not None:
            result['IsPublic'] = self.is_public

        if self.launch_permission is not None:
            result['LaunchPermission'] = self.launch_permission

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remove_account is not None:
            result['RemoveAccount'] = self.remove_account

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccount') is not None:
            self.add_account = m.get('AddAccount')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')

        if m.get('LaunchPermission') is not None:
            self.launch_permission = m.get('LaunchPermission')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoveAccount') is not None:
            self.remove_account = m.get('RemoveAccount')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

