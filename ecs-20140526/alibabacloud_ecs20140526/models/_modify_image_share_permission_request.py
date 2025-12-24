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
        # The IDs of Alibaba Cloud accounts to which you want to share the custom image. Valid values of N: 1 to 10. If you specify more than 10 Alibaba Cloud account IDs, the system processes only the first 10 account IDs. The excess account IDs are ignored.
        self.add_account = add_account
        self.dry_run = dry_run
        # The ID of the shared custom image.
        # 
        # >  You can share images encrypted by using CMKs but cannot share images encrypted by using service keys. When you share an image encrypted by using a service key, an error is reported.
        # 
        # This parameter is required.
        self.image_id = image_id
        # Specifies whether to publish or unpublish a community image. Valid values:
        # 
        # *   true: publishes the custom image as a community image.
        # *   false: unpublishes a community image. The unpublish operation takes effect only on community images.
        # 
        # Default value: false.
        self.is_public = is_public
        # > This parameter is in invitational preview and is not publicly available.
        self.launch_permission = launch_permission
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the custom image. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of Alibaba Cloud accounts from which you want to unshare the custom image. Valid values of N: 1 to 10. If you specify more than 10 Alibaba Cloud account IDs, the system processes only the first 10 account IDs. The excess account IDs are ignored.
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

