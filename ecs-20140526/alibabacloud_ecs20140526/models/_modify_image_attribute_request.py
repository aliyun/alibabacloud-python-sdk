# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyImageAttributeRequest(DaraModel):
    def __init__(
        self,
        boot_mode: str = None,
        description: str = None,
        dry_run: bool = None,
        features: main_models.ModifyImageAttributeRequestFeatures = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        license_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
    ):
        # The boot mode of the image. Valid values:
        # 
        # - `BIOS`: BIOS boot mode.
        # 
        # - `UEFI`: UEFI boot mode.
        # 
        # - `UEFI-Preferred`: UEFI-preferred boot mode.
        # 
        # >Notice: 
        # 
        # To prevent startup failures, verify the boot modes that the image supports before you change its boot mode. For more information, see [Boot modes](~~2244655#b9caa9b8bb1wf~~).
        self.boot_mode = boot_mode
        # The new description of the custom image. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # If you do not specify this parameter, the original description is retained.
        self.description = description
        # Specifies whether to perform a dry run to check whether the request is valid. Valid values:
        # 
        # - `true`: performs a dry run to check the request for validity, syntax, and required permissions. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - `false` (default): sends the request. If the request passes the validation checks, the operation is performed.
        self.dry_run = dry_run
        # The features of the image.
        self.features = features
        # The name of the image family. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character. The name cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`. It can contain digits, periods (.), colons (:), underscores (_), and hyphens (-).
        # 
        # By default, this parameter is empty.
        self.image_family = image_family
        # The ID of the custom image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The name of the custom image. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character. The name cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`. It can contain digits, periods (.), colons (:), underscores (_), and hyphens (-).
        # 
        # If you do not specify this parameter, the original name is retained.
        self.image_name = image_name
        # The license type for activating the operating system after you import the image. The only valid value is `BYOL`.
        # 
        # `BYOL`: Bring Your Own License. If you use the BYOL license type, you must ensure that your license key is supported for use on Alibaba Cloud.
        self.license_type = license_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the custom image is located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The image status. Valid values:
        # 
        # - `Deprecated`: Deprecates the image. If a custom image that you want to deprecate is shared, you must unshare it first. You cannot share or copy a deprecated image. However, you can use the image to create an instance or replace a system disk.
        # 
        # - `Available`: Makes the image available. You can change the status of a deprecated image to `Available`.
        # 
        # > However, if this is the only available custom image in the image family, deprecating it prevents the creation of instances from any image in that family. Use this option with caution.
        self.status = status

    def validate(self):
        if self.features:
            self.features.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_mode is not None:
            result['BootMode'] = self.boot_mode

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.features is not None:
            result['Features'] = self.features.to_map()

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

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

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Features') is not None:
            temp_model = main_models.ModifyImageAttributeRequestFeatures()
            self.features = temp_model.from_map(m.get('Features'))

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ModifyImageAttributeRequestFeatures(DaraModel):
    def __init__(
        self,
        imds_support: str = None,
        nvme_support: str = None,
    ):
        # The metadata access mode of the image. Valid values:
        # 
        # - `v1`: When you create an ECS instance from this image, you cannot set the metadata access mode to `enforced mode`.
        # 
        # - `v2`: When you create an ECS instance from this image, you can set the metadata access mode to `enforced mode`.
        # 
        #   >Notice: 
        # 
        #   You cannot change the value of `ImdsSupport` from `v2` to `v1`. To use the `v1` mode, create a new image from a snapshot that is associated with the image and set `ImdsSupport` to `v1`.
        self.imds_support = imds_support
        # Specifies whether the image supports NVMe. Valid values:
        # 
        # - `supported`: The image supports NVMe. Instances that you create from this image support the NVMe protocol.
        # 
        # - `unsupported`: The image does not support NVMe. Instances that you create from this image do not support the NVMe protocol.
        self.nvme_support = nvme_support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.imds_support is not None:
            result['ImdsSupport'] = self.imds_support

        if self.nvme_support is not None:
            result['NvmeSupport'] = self.nvme_support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImdsSupport') is not None:
            self.imds_support = m.get('ImdsSupport')

        if m.get('NvmeSupport') is not None:
            self.nvme_support = m.get('NvmeSupport')

        return self

