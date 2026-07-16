# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListImageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.ListImageResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The total number of entries.
        self.count = count
        # The returned data object.
        self.data = data
        # The message returned for the API request.
        self.message = message
        # The page number of the returned data.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListImageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListImageResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_list: List[main_models.ListImageResponseBodyDataAppList] = None,
        base_image_id: str = None,
        base_image_version: str = None,
        biz_type: int = None,
        compatible_mode: bool = None,
        data_disk_size: int = None,
        description: str = None,
        distro: str = None,
        driver_list: List[str] = None,
        environment_id: str = None,
        feature_list: List[str] = None,
        fota_channel: str = None,
        fota_version: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_create_mode: str = None,
        image_icon_url: str = None,
        image_id: str = None,
        image_name: str = None,
        image_region_distribute_list: List[main_models.ListImageResponseBodyDataImageRegionDistributeList] = None,
        image_region_list: List[str] = None,
        image_type: str = None,
        language: str = None,
        latest_version_id: str = None,
        online_version: bool = None,
        online_version_id: str = None,
        os_type: str = None,
        package_type: str = None,
        parent_image_id: str = None,
        parent_image_version: str = None,
        platform: int = None,
        platform_name: str = None,
        product_type: str = None,
        protocol_type: str = None,
        rating: int = None,
        resource_instance_category: str = None,
        scene: str = None,
        session_type: str = None,
        snapshot_list: List[main_models.ListImageResponseBodyDataSnapshotList] = None,
        status: str = None,
        supported_language_list: List[str] = None,
        system_disk_size: int = None,
        tag_list: List[main_models.ListImageResponseBodyDataTagList] = None,
        version_id: str = None,
        version_name: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        # The tenant ID.
        self.ali_uid = ali_uid
        # The application configurations.
        self.app_list = app_list
        # The base image ID.
        self.base_image_id = base_image_id
        # The base image version.
        self.base_image_version = base_image_version
        # The business type.
        self.biz_type = biz_type
        # Indicates whether the compatibility mode is enabled.
        self.compatible_mode = compatible_mode
        # The data cloud disk size. Unit: GiB.
        self.data_disk_size = data_disk_size
        # The image description.
        self.description = description
        # The distribution name.
        self.distro = distro
        # The list of driver information.
        self.driver_list = driver_list
        self.environment_id = environment_id
        # The list of image feature tags.
        self.feature_list = feature_list
        # > This parameter is not publicly available.
        self.fota_channel = fota_channel
        # The FOTA version.
        self.fota_version = fota_version
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The image creation type.
        self.image_create_mode = image_create_mode
        self.image_icon_url = image_icon_url
        # The image ID. System image IDs are meaningful, while custom image IDs are automatically generated.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The effective region information for overlay layers.
        self.image_region_distribute_list = image_region_distribute_list
        # The regions.
        self.image_region_list = image_region_list
        # The image type.
        self.image_type = image_type
        # The image language. If the package type is VHD or Container, this property is inherited from the ECS-packaged image in the image combination.
        self.language = language
        # The latest sub-version of the image. An image consists of multiple sub-versions.
        self.latest_version_id = latest_version_id
        # Indicates whether the current version is the active version.
        self.online_version = online_version
        # The sub-version from which the current image reads the primary image information. An image consists of multiple sub-versions.
        self.online_version_id = online_version_id
        # The image type.
        self.os_type = os_type
        # The image package type.
        self.package_type = package_type
        # The parent image ID. This parameter indicates only the inheritance relationship. System images do not have a parent image.
        self.parent_image_id = parent_image_id
        # The parent image version.
        self.parent_image_version = parent_image_version
        # The operating system platform of the image.
        # 
        # > If the package type is VHD or Container, this property is inherited from the ECS-packaged image in the image combination.
        self.platform = platform
        # The system platform name.
        self.platform_name = platform_name
        # The product type.
        self.product_type = product_type
        # The protocol type.
        self.protocol_type = protocol_type
        self.rating = rating
        # The resource type supported by the image.
        self.resource_instance_category = resource_instance_category
        self.scene = scene
        # The session type.
        self.session_type = session_type
        self.snapshot_list = snapshot_list
        # The image status.
        self.status = status
        # The list of supported languages.
        self.supported_language_list = supported_language_list
        # The system cloud disk size. Unit: GiB.
        # 
        # > The system cloud disk size cannot be smaller than the image file.
        self.system_disk_size = system_disk_size
        self.tag_list = tag_list
        # The image version.
        self.version_id = version_id
        # The version name.
        self.version_name = version_name
        # Indicates whether cloud disk encryption is enabled.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The KMS key ID used when cloud disk encryption is enabled.
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        if self.app_list:
            for v1 in self.app_list:
                 if v1:
                    v1.validate()
        if self.image_region_distribute_list:
            for v1 in self.image_region_distribute_list:
                 if v1:
                    v1.validate()
        if self.snapshot_list:
            for v1 in self.snapshot_list:
                 if v1:
                    v1.validate()
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        result['AppList'] = []
        if self.app_list is not None:
            for k1 in self.app_list:
                result['AppList'].append(k1.to_map() if k1 else None)

        if self.base_image_id is not None:
            result['BaseImageId'] = self.base_image_id

        if self.base_image_version is not None:
            result['BaseImageVersion'] = self.base_image_version

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.compatible_mode is not None:
            result['CompatibleMode'] = self.compatible_mode

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.description is not None:
            result['Description'] = self.description

        if self.distro is not None:
            result['Distro'] = self.distro

        if self.driver_list is not None:
            result['DriverList'] = self.driver_list

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.feature_list is not None:
            result['FeatureList'] = self.feature_list

        if self.fota_channel is not None:
            result['FotaChannel'] = self.fota_channel

        if self.fota_version is not None:
            result['FotaVersion'] = self.fota_version

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_create_mode is not None:
            result['ImageCreateMode'] = self.image_create_mode

        if self.image_icon_url is not None:
            result['ImageIconUrl'] = self.image_icon_url

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        result['ImageRegionDistributeList'] = []
        if self.image_region_distribute_list is not None:
            for k1 in self.image_region_distribute_list:
                result['ImageRegionDistributeList'].append(k1.to_map() if k1 else None)

        if self.image_region_list is not None:
            result['ImageRegionList'] = self.image_region_list

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.language is not None:
            result['Language'] = self.language

        if self.latest_version_id is not None:
            result['LatestVersionId'] = self.latest_version_id

        if self.online_version is not None:
            result['OnlineVersion'] = self.online_version

        if self.online_version_id is not None:
            result['OnlineVersionId'] = self.online_version_id

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.parent_image_id is not None:
            result['ParentImageId'] = self.parent_image_id

        if self.parent_image_version is not None:
            result['ParentImageVersion'] = self.parent_image_version

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.rating is not None:
            result['Rating'] = self.rating

        if self.resource_instance_category is not None:
            result['ResourceInstanceCategory'] = self.resource_instance_category

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        result['SnapshotList'] = []
        if self.snapshot_list is not None:
            for k1 in self.snapshot_list:
                result['SnapshotList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.supported_language_list is not None:
            result['SupportedLanguageList'] = self.supported_language_list

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        self.app_list = []
        if m.get('AppList') is not None:
            for k1 in m.get('AppList'):
                temp_model = main_models.ListImageResponseBodyDataAppList()
                self.app_list.append(temp_model.from_map(k1))

        if m.get('BaseImageId') is not None:
            self.base_image_id = m.get('BaseImageId')

        if m.get('BaseImageVersion') is not None:
            self.base_image_version = m.get('BaseImageVersion')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CompatibleMode') is not None:
            self.compatible_mode = m.get('CompatibleMode')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Distro') is not None:
            self.distro = m.get('Distro')

        if m.get('DriverList') is not None:
            self.driver_list = m.get('DriverList')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('FeatureList') is not None:
            self.feature_list = m.get('FeatureList')

        if m.get('FotaChannel') is not None:
            self.fota_channel = m.get('FotaChannel')

        if m.get('FotaVersion') is not None:
            self.fota_version = m.get('FotaVersion')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageCreateMode') is not None:
            self.image_create_mode = m.get('ImageCreateMode')

        if m.get('ImageIconUrl') is not None:
            self.image_icon_url = m.get('ImageIconUrl')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        self.image_region_distribute_list = []
        if m.get('ImageRegionDistributeList') is not None:
            for k1 in m.get('ImageRegionDistributeList'):
                temp_model = main_models.ListImageResponseBodyDataImageRegionDistributeList()
                self.image_region_distribute_list.append(temp_model.from_map(k1))

        if m.get('ImageRegionList') is not None:
            self.image_region_list = m.get('ImageRegionList')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LatestVersionId') is not None:
            self.latest_version_id = m.get('LatestVersionId')

        if m.get('OnlineVersion') is not None:
            self.online_version = m.get('OnlineVersion')

        if m.get('OnlineVersionId') is not None:
            self.online_version_id = m.get('OnlineVersionId')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('ParentImageId') is not None:
            self.parent_image_id = m.get('ParentImageId')

        if m.get('ParentImageVersion') is not None:
            self.parent_image_version = m.get('ParentImageVersion')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Rating') is not None:
            self.rating = m.get('Rating')

        if m.get('ResourceInstanceCategory') is not None:
            self.resource_instance_category = m.get('ResourceInstanceCategory')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        self.snapshot_list = []
        if m.get('SnapshotList') is not None:
            for k1 in m.get('SnapshotList'):
                temp_model = main_models.ListImageResponseBodyDataSnapshotList()
                self.snapshot_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportedLanguageList') is not None:
            self.supported_language_list = m.get('SupportedLanguageList')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.ListImageResponseBodyDataTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        return self

class ListImageResponseBodyDataTagList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class ListImageResponseBodyDataSnapshotList(DaraModel):
    def __init__(
        self,
        bind_type: str = None,
        disk_category: str = None,
        disk_sub_type: str = None,
        disk_type: str = None,
        size: int = None,
        snapshot_id: str = None,
        version_id: str = None,
    ):
        self.bind_type = bind_type
        self.disk_category = disk_category
        self.disk_sub_type = disk_sub_type
        self.disk_type = disk_type
        self.size = size
        self.snapshot_id = snapshot_id
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_type is not None:
            result['BindType'] = self.bind_type

        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        if self.disk_sub_type is not None:
            result['DiskSubType'] = self.disk_sub_type

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindType') is not None:
            self.bind_type = m.get('BindType')

        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        if m.get('DiskSubType') is not None:
            self.disk_sub_type = m.get('DiskSubType')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class ListImageResponseBodyDataImageRegionDistributeList(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        progress: str = None,
        region_id: str = None,
        status: str = None,
        version_id: str = None,
    ):
        # The image ID. System image IDs are meaningful, while custom image IDs are automatically generated.
        self.image_id = image_id
        # The progress percentage.
        self.progress = progress
        # The supported region.
        self.region_id = region_id
        # The status.
        self.status = status
        # The image version.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class ListImageResponseBodyDataAppList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

