# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetImageByIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetImageByIdResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of 200 indicates success. If the call fails, the corresponding error code is returned.
        self.code = code
        # The image information returned by the query.
        self.data = data
        # The response message.
        self.message = message
        # The request ID, which is used to locate and troubleshoot the request.
        self.request_id = request_id
        # Indicates whether the API call is successful. Valid values:
        # - true: Successful.
        # - false: Failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetImageByIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetImageByIdResponseBodyData(DaraModel):
    def __init__(
        self,
        adaptor_info_bolist: List[main_models.GetImageByIdResponseBodyDataAdaptorInfoBOList] = None,
        ali_uid: int = None,
        base_image_id: str = None,
        base_image_version: str = None,
        biz_type: int = None,
        bucket_name: str = None,
        description: str = None,
        feature_list: List[str] = None,
        fota_version: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_create_mode: str = None,
        image_extend_info_model: main_models.GetImageByIdResponseBodyDataImageExtendInfoModel = None,
        image_id: str = None,
        image_name: str = None,
        image_region_distribute_list: List[main_models.GetImageByIdResponseBodyDataImageRegionDistributeList] = None,
        image_region_list: List[str] = None,
        image_source: str = None,
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
        property_map: Dict[str, str] = None,
        protocol_type: str = None,
        status: str = None,
        version_id: str = None,
    ):
        # The list of adapted applications for the image version.
        self.adaptor_info_bolist = adaptor_info_bolist
        # The ID of the Alibaba Cloud account to which the image belongs. The account ID for a system image is 0.
        self.ali_uid = ali_uid
        # The ID of the base image.
        self.base_image_id = base_image_id
        # The ID of the base image version.
        self.base_image_version = base_image_version
        # The business line to which the image belongs. Valid values:
        # - 1: basic business
        # - 2: personal edition
        # - 3: cloud office
        # - 4: cloud streaming
        # - 10: standard edition
        self.biz_type = biz_type
        # The name of the OSS bucket where the image files are stored.
        self.bucket_name = bucket_name
        # The description of the image.
        self.description = description
        # The list of feature tags supported by the image.
        self.feature_list = feature_list
        # The FOTA version.
        self.fota_version = fota_version
        # The creation time.
        self.gmt_create = gmt_create
        # The last update time.
        self.gmt_modified = gmt_modified
        # The image creation method. For example, BUILDER_MANUAL indicates manual creation.
        self.image_create_mode = image_create_mode
        # The image extended information, including disk specifications and GPU driver information. For VHD or container images, the extended information of the base image and base version is used.
        self.image_extend_info_model = image_extend_info_model
        # The image ID.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The list of region distribution information for the image version.
        self.image_region_distribute_list = image_region_distribute_list
        # The list of region IDs supported by the image.
        self.image_region_list = image_region_list
        # The source of the image. For example, center indicates the central image service.
        self.image_source = image_source
        # The image type. Valid values:
        # - System: system image
        # - User: custom image
        # - Shared: shared image
        # - Community: community image
        self.image_type = image_type
        # The image language. If the encapsulation type is VHD or Container, this property is inherited from the image with the ECS encapsulation type in the image combination.
        self.language = language
        # The ID of the latest image version.
        self.latest_version_id = latest_version_id
        # Indicates whether the returned version is the active version. Valid values:
        # - true: Yes.
        # - false: No.
        self.online_version = online_version
        # The ID of the current online version of the image.
        self.online_version_id = online_version_id
        # The operating system type of the image. Valid values:
        # - Windows: Windows system
        # - Linux: Linux system
        # - Android: Android system
        # - Unknown: unknown system
        self.os_type = os_type
        # The image package type. Valid values:
        # - Ecs: ECS image.
        # - Vhd: Virtual disk image.
        # - Container: Container image.
        # - Ecs_Container: ECS and container combined image.
        # - K8s_Node: Kubernetes node image.
        self.package_type = package_type
        # The ID of the parent image, which indicates the image inheritance relationship. System images do not have parent images.
        self.parent_image_id = parent_image_id
        # The ID of the parent image version.
        self.parent_image_version = parent_image_version
        # The operating system platform ID. For example, 33 indicates Windows Server 2022.
        self.platform = platform
        # The name of the operating system platform, which corresponds to Platform.
        self.platform_name = platform_name
        # The product type to which the image belongs, such as CloudDesktop (Cloud Desktop), CloudApp (Cloud Application), or WuyingServer (WUYING Workspace Enterprise Edition workstation).
        self.product_type = product_type
        # The extended properties of the image version, in key-value pair format.
        self.property_map = property_map
        # The connection protocol used by the image. Valid values:
        # - ASP: Alibaba Cloud Streaming Protocol
        # - HDX: HDX protocol
        self.protocol_type = protocol_type
        # The image status. Valid values:
        # - INIT: Initialized.
        # - CREATING: Creating.
        # - AVAILABLE: Available.
        # - CREATE_FAILED: Creation failed.
        # - DELETE: Deleted.
        self.status = status
        # The image version ID.
        self.version_id = version_id

    def validate(self):
        if self.adaptor_info_bolist:
            for v1 in self.adaptor_info_bolist:
                 if v1:
                    v1.validate()
        if self.image_extend_info_model:
            self.image_extend_info_model.validate()
        if self.image_region_distribute_list:
            for v1 in self.image_region_distribute_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdaptorInfoBOList'] = []
        if self.adaptor_info_bolist is not None:
            for k1 in self.adaptor_info_bolist:
                result['AdaptorInfoBOList'].append(k1.to_map() if k1 else None)

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.base_image_id is not None:
            result['BaseImageId'] = self.base_image_id

        if self.base_image_version is not None:
            result['BaseImageVersion'] = self.base_image_version

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.description is not None:
            result['Description'] = self.description

        if self.feature_list is not None:
            result['FeatureList'] = self.feature_list

        if self.fota_version is not None:
            result['FotaVersion'] = self.fota_version

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_create_mode is not None:
            result['ImageCreateMode'] = self.image_create_mode

        if self.image_extend_info_model is not None:
            result['ImageExtendInfoModel'] = self.image_extend_info_model.to_map()

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

        if self.image_source is not None:
            result['ImageSource'] = self.image_source

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

        if self.property_map is not None:
            result['PropertyMap'] = self.property_map

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.status is not None:
            result['Status'] = self.status

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.adaptor_info_bolist = []
        if m.get('AdaptorInfoBOList') is not None:
            for k1 in m.get('AdaptorInfoBOList'):
                temp_model = main_models.GetImageByIdResponseBodyDataAdaptorInfoBOList()
                self.adaptor_info_bolist.append(temp_model.from_map(k1))

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('BaseImageId') is not None:
            self.base_image_id = m.get('BaseImageId')

        if m.get('BaseImageVersion') is not None:
            self.base_image_version = m.get('BaseImageVersion')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FeatureList') is not None:
            self.feature_list = m.get('FeatureList')

        if m.get('FotaVersion') is not None:
            self.fota_version = m.get('FotaVersion')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageCreateMode') is not None:
            self.image_create_mode = m.get('ImageCreateMode')

        if m.get('ImageExtendInfoModel') is not None:
            temp_model = main_models.GetImageByIdResponseBodyDataImageExtendInfoModel()
            self.image_extend_info_model = temp_model.from_map(m.get('ImageExtendInfoModel'))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        self.image_region_distribute_list = []
        if m.get('ImageRegionDistributeList') is not None:
            for k1 in m.get('ImageRegionDistributeList'):
                temp_model = main_models.GetImageByIdResponseBodyDataImageRegionDistributeList()
                self.image_region_distribute_list.append(temp_model.from_map(k1))

        if m.get('ImageRegionList') is not None:
            self.image_region_list = m.get('ImageRegionList')

        if m.get('ImageSource') is not None:
            self.image_source = m.get('ImageSource')

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

        if m.get('PropertyMap') is not None:
            self.property_map = m.get('PropertyMap')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetImageByIdResponseBodyDataImageRegionDistributeList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        ecs_image_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        message: str = None,
        progress: str = None,
        region_id: str = None,
        status: str = None,
        unit_image_id: str = None,
        version_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the image belongs. The account ID for a system image is 0.
        self.ali_uid = ali_uid
        # The ID of the ECS image corresponding to the region.
        self.ecs_image_id = ecs_image_id
        # The creation time.
        self.gmt_create = gmt_create
        # The last update time.
        self.gmt_modified = gmt_modified
        # The image ID.
        self.image_id = image_id
        # The processing information reported by the region distribution task.
        self.message = message
        # The distribution progress of the image in the region, expressed as a percentage.
        self.progress = progress
        # The ID of the region where the image is distributed.
        self.region_id = region_id
        # The region distribution status. Valid values:
        # - CREATING: Distributing.
        # - AVAILABLE: Available.
        # - CREATE_FAILED: Distribution failed.
        # - DELETE: Deleted.
        self.status = status
        # The logical ID of the image on the unit side, which can be different from the central image ID.
        self.unit_image_id = unit_image_id
        # The image version ID.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.ecs_image_id is not None:
            result['EcsImageId'] = self.ecs_image_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.message is not None:
            result['Message'] = self.message

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.unit_image_id is not None:
            result['UnitImageId'] = self.unit_image_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('EcsImageId') is not None:
            self.ecs_image_id = m.get('EcsImageId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnitImageId') is not None:
            self.unit_image_id = m.get('UnitImageId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetImageByIdResponseBodyDataImageExtendInfoModel(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        data_disk_size: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        gpu_category: int = None,
        gpu_driver_version: str = None,
        image_id: str = None,
        package_type: str = None,
        system_disk_size: int = None,
        version_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the image belongs. The account ID for a system image is 0.
        self.ali_uid = ali_uid
        # The size of the data cloud disk. Unit: GiB.
        self.data_disk_size = data_disk_size
        # The creation time.
        self.gmt_create = gmt_create
        # The last update time.
        self.gmt_modified = gmt_modified
        # The GPU category.
        self.gpu_category = gpu_category
        # The GPU driver version.
        self.gpu_driver_version = gpu_driver_version
        # The image ID.
        self.image_id = image_id
        # The image package type. Valid values:
        # - Ecs: ECS image.
        # - Vhd: Virtual disk image.
        # - Container: Container image.
        # - Ecs_Container: ECS and container combined image.
        # - K8s_Node: Kubernetes node image.
        self.package_type = package_type
        # The size of the system cloud disk. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The image version ID.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category

        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetImageByIdResponseBodyDataAdaptorInfoBOList(DaraModel):
    def __init__(
        self,
        adaptor_id: str = None,
        adaptor_message: str = None,
        adaptor_mode: str = None,
        adaptor_step: str = None,
        aid: int = None,
        ali_uid: int = None,
        app_icon_url: str = None,
        app_id: str = None,
        app_name: str = None,
        app_script: str = None,
        app_theme_color: str = None,
        app_type: str = None,
        app_version_id: str = None,
        app_version_name: str = None,
        app_version_number: str = None,
        biz_type: int = None,
        bucket_name: str = None,
        category_id: int = None,
        category_type: int = None,
        control_param: str = None,
        disk_id: str = None,
        execute_file_address: str = None,
        extend: str = None,
        file_name: str = None,
        file_path: str = None,
        file_size: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        optimize_param: str = None,
        origin_app_type: str = None,
        os_type: str = None,
        product_type: str = None,
        runtime_env: str = None,
        silence_flag: str = None,
        silence_param: str = None,
        status: str = None,
        sub_app_type: str = None,
    ):
        # The adapter ID.
        self.adaptor_id = adaptor_id
        # The adaptor message.
        self.adaptor_message = adaptor_message
        # The execution mode.
        self.adaptor_mode = adaptor_mode
        # The execution step.
        self.adaptor_step = adaptor_step
        # The numeric ID of the application.
        self.aid = aid
        # The ID of the Alibaba Cloud account to which the application belongs.
        self.ali_uid = ali_uid
        # The application icon.
        self.app_icon_url = app_icon_url
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The application script.
        self.app_script = app_script
        # The theme color.
        self.app_theme_color = app_theme_color
        # The application type.
        self.app_type = app_type
        # The application version ID.
        self.app_version_id = app_version_id
        # The version name.
        self.app_version_name = app_version_name
        # The version number.
        self.app_version_number = app_version_number
        # The ID of the business line to which the application belongs.
        self.biz_type = biz_type
        # The name of the OSS bucket where the application files are stored.
        self.bucket_name = bucket_name
        # The level-2 category of the application.
        self.category_id = category_id
        # The level-1 category of the application.
        self.category_type = category_type
        # The control parameters that can be configured by tenants and administrators.
        self.control_param = control_param
        # The ID of the disk where the application files are stored.
        self.disk_id = disk_id
        # The path of the executable file after the cloud application is installed.
        self.execute_file_address = execute_file_address
        # The extended information of the adapted application.
        self.extend = extend
        # The file name.
        self.file_name = file_name
        # The file path.
        self.file_path = file_path
        # The file size.
        self.file_size = file_size
        # The creation time.
        self.gmt_create = gmt_create
        # The last update time.
        self.gmt_modified = gmt_modified
        # The optimization parameters configured in the administrator backend.
        self.optimize_param = optimize_param
        # The original application type.
        self.origin_app_type = origin_app_type
        # The operating system type supported by the application.
        self.os_type = os_type
        # The product type to which the application belongs.
        self.product_type = product_type
        # The runtime environment.
        self.runtime_env = runtime_env
        # Specifies whether to skip installation. This parameter can be configured by tenants and administrators.
        self.silence_flag = silence_flag
        # The installation parameters that can be configured by tenants and administrators.
        self.silence_param = silence_param
        # The application adaptation status. For example, ADAPT_DONE indicates that the adaptation is complete.
        self.status = status
        # The sub-application type.
        self.sub_app_type = sub_app_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptor_id is not None:
            result['AdaptorId'] = self.adaptor_id

        if self.adaptor_message is not None:
            result['AdaptorMessage'] = self.adaptor_message

        if self.adaptor_mode is not None:
            result['AdaptorMode'] = self.adaptor_mode

        if self.adaptor_step is not None:
            result['AdaptorStep'] = self.adaptor_step

        if self.aid is not None:
            result['Aid'] = self.aid

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.app_icon_url is not None:
            result['AppIconUrl'] = self.app_icon_url

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_script is not None:
            result['AppScript'] = self.app_script

        if self.app_theme_color is not None:
            result['AppThemeColor'] = self.app_theme_color

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id

        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name

        if self.app_version_number is not None:
            result['AppVersionNumber'] = self.app_version_number

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_type is not None:
            result['CategoryType'] = self.category_type

        if self.control_param is not None:
            result['ControlParam'] = self.control_param

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.execute_file_address is not None:
            result['ExecuteFileAddress'] = self.execute_file_address

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.optimize_param is not None:
            result['OptimizeParam'] = self.optimize_param

        if self.origin_app_type is not None:
            result['OriginAppType'] = self.origin_app_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.runtime_env is not None:
            result['RuntimeEnv'] = self.runtime_env

        if self.silence_flag is not None:
            result['SilenceFlag'] = self.silence_flag

        if self.silence_param is not None:
            result['SilenceParam'] = self.silence_param

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_app_type is not None:
            result['SubAppType'] = self.sub_app_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptorId') is not None:
            self.adaptor_id = m.get('AdaptorId')

        if m.get('AdaptorMessage') is not None:
            self.adaptor_message = m.get('AdaptorMessage')

        if m.get('AdaptorMode') is not None:
            self.adaptor_mode = m.get('AdaptorMode')

        if m.get('AdaptorStep') is not None:
            self.adaptor_step = m.get('AdaptorStep')

        if m.get('Aid') is not None:
            self.aid = m.get('Aid')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AppIconUrl') is not None:
            self.app_icon_url = m.get('AppIconUrl')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppScript') is not None:
            self.app_script = m.get('AppScript')

        if m.get('AppThemeColor') is not None:
            self.app_theme_color = m.get('AppThemeColor')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')

        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')

        if m.get('AppVersionNumber') is not None:
            self.app_version_number = m.get('AppVersionNumber')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')

        if m.get('ControlParam') is not None:
            self.control_param = m.get('ControlParam')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('ExecuteFileAddress') is not None:
            self.execute_file_address = m.get('ExecuteFileAddress')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OptimizeParam') is not None:
            self.optimize_param = m.get('OptimizeParam')

        if m.get('OriginAppType') is not None:
            self.origin_app_type = m.get('OriginAppType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RuntimeEnv') is not None:
            self.runtime_env = m.get('RuntimeEnv')

        if m.get('SilenceFlag') is not None:
            self.silence_flag = m.get('SilenceFlag')

        if m.get('SilenceParam') is not None:
            self.silence_param = m.get('SilenceParam')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubAppType') is not None:
            self.sub_app_type = m.get('SubAppType')

        return self

