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
        # - BIOS: BIOS boot mode.
        # - UEFI: UEFI boot mode.
        # - UEFI-Preferred: Dual boot mode.
        # 
        # 
        # <notice>
        # 
        #    To prevent instances from failing to start due to an unsupported boot mode, make sure that you understand the boot modes supported by the target image before you modify the boot mode. For more information about image boot modes, see [Image boot modes](~~2244655#b9caa9b8bb1wf~~).
        # 
        # </notice>
        self.boot_mode = boot_mode
        # The description of the custom image. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        # 
        # Default value: empty. The original description is retained.
        self.description = description
        # Specifies whether to only precheck the request. Valid values:
        # 
        # - true: A precheck request is sent, and the image attributes are not modified. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - false: A normal request is sent, and the image attributes are modified if the request passes the check.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # The feature-related attributes of the image.
        self.features = features
        # The name of the image family. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with aliyun or acs:. It cannot contain http:// or https://. It can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-).
        # 
        # Default value: empty.
        self.image_family = image_family
        # The ID of the custom image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The name of the custom image. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with aliyun or acs:. It cannot contain http:// or https://. It can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-).
        # 
        # Default value: empty. The original name is retained.
        self.image_name = image_name
        # The license type used to activate the operating system after the image is imported. Only BYOL is supported.
        # 
        # BYOL: The license provided with the source operating system. If you use BYOL, you must ensure that your license key is supported on Alibaba Cloud.
        self.license_type = license_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the custom image. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the image. Valid values:
        # 
        # - Deprecated: Sets the image to the deprecated state. If the custom image is shared, you must unshare it before you can set it to the deprecated state. You cannot share or copy a deprecated image. However, you can use the image to create instances or replace system disks.
        # - Available: Sets the image to the available state. You can restore a deprecated image to the available state.
        # 
        # > If you want to roll back a custom image in an image family to the previous version, you can set the latest available custom image to the deprecated state. However, if the image is the only available custom image in the image family, deprecating the image leaves the image family without any available custom images for creating instances. Proceed with caution.
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
        # - v1: When you create an ECS instance from this image, you cannot set the metadata access mode to enforced.
        # - v2: When you create an ECS instance from this image, you can set the metadata access mode to enforced.
        # <notice>
        # 
        #   You cannot change ImdsSupport from v2 to v1. To change the value, create a new image from a snapshot associated with this image and set the value to v1.
        # 
        # </notice>
        self.imds_support = imds_support
        # Modifies the NVMe support attribute of the image. If this parameter is not specified, the original value is retained.
        # >Notice: Before you enable this feature, ensure that the NVMe driver is pre-installed in the operating system. Recommended procedure: install the driver on an instance, create a custom image, and then call this operation. Forcibly enabling this feature without the driver causes the instance to fail to start.
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

