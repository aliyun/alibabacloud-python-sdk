# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportImageRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        image_format: str = None,
        image_id: str = None,
        ossbucket: str = None,
        ossprefix: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_name: str = None,
    ):
        # Specifies whether to perform a dry run to check the request\\"s validity without actually exporting the image. Valid values:
        # 
        # - `true`: Performs a dry run. If the check succeeds, the `DryRunOperation` error code is returned. If the check fails, an error is returned.
        # - `false`: Sends a normal request. If the check succeeds, the image is exported.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # The format of the exported image file. Valid values:
        # 
        # - raw.
        # 
        # - vhd.
        # 
        # - qcow2.
        # 
        # - vmdk.
        # 
        # - vdi.
        # 
        # Default value: raw.
        self.image_format = image_format
        # The ID of the custom image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The destination OSS bucket for the exported image.
        # 
        # This parameter is required.
        self.ossbucket = ossbucket
        # The prefix for the OSS object. The prefix must be 1 to 30 characters in length and can consist of letters and digits.
        self.ossprefix = ossprefix
        self.owner_id = owner_id
        # The region ID of the custom image. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the RAM role used to export the image.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.image_format is not None:
            result['ImageFormat'] = self.image_format

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.ossprefix is not None:
            result['OSSPrefix'] = self.ossprefix

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSPrefix') is not None:
            self.ossprefix = m.get('OSSPrefix')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

