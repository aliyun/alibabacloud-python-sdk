# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class BuilderImageByParentShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_type: int = None,
        data_disk_size: int = None,
        description: str = None,
        distro: str = None,
        driver_id_list: List[str] = None,
        image_create_mode: str = None,
        image_name: str = None,
        language: str = None,
        node_instance_type: str = None,
        office_site_id: str = None,
        package_type: str = None,
        parent_image_id: str = None,
        performance_type: str = None,
        product_type: str = None,
        property_map_shrink: str = None,
        resource_list: List[main_models.BuilderImageByParentShrinkRequestResourceList] = None,
        run_mode: str = None,
        source_region: str = None,
        system_disk_size: int = None,
        v_switch_id_list: List[str] = None,
        version_name: str = None,
    ):
        # The business type to which the image belongs. **Required**. Valid values:
        # 
        # - **1**: Basic product.
        # - **2**: Personal cloud.
        # - **3**: Cloud office.
        # - **4**: Cloud Flow.
        # - **10**: Personal edition.
        # - **20**: Business edition.
        # - **60**: Linggou team edition.
        self.biz_type = biz_type
        # The capacity of the data cloud disk in the creation environment. Unit: GiB. Specify this parameter when a data cloud disk is required, and ensure that it meets the disk requirements of the selected resource specifications.
        self.data_disk_size = data_disk_size
        # The description of the new image, which facilitates subsequent queries and differentiation of images.
        self.description = description
        # The operating system distribution information of the image. Enter the distribution identifier that is consistent with the parent image used.
        self.distro = distro
        # The list of driver IDs used when creating the image. A maximum of 200 items are supported. When you need to specify drivers, enter the IDs of existing drivers that are applicable to the target image.
        # 
        # **If PropertyMap.DRIVER_LIST is also specified, this parameter overwrites the driver list in it.**
        self.driver_id_list = driver_id_list
        # The image creation mode. Use the following mode:
        # 
        # - **BUILDER_MANUAL**: Manually enter the creation environment to install applications and configure the image.
        # 
        # This parameter is required.
        self.image_create_mode = image_create_mode
        # The name of the new image. **Required**. The name must start with a letter or a Chinese character, and can contain letters, digits, Chinese characters, colons (:), underscores (_), periods (.), and hyphens (-). It cannot start with http:// or https://. The length is calculated as 3 for each Chinese character and 1 for each other character. The total length must be 2 to 64 characters.
        self.image_name = image_name
        # The language of the image. Valid values:
        # 
        # - **zh-CN**: Simplified Chinese.
        # - **zh-HK**: Traditional Chinese (Hong Kong).
        # - **en-US**: English.
        # - **ja-JP**: Japanese.
        # - **CN**: Compatible value for Simplified Chinese.
        # - **EN**: Compatible value for English.
        # - **JP**: Compatible value for Japanese.
        # - **CN-HK**: Compatible value for Traditional Chinese (Hong Kong).
        self.language = language
        # The ID of the node specifications for the creation resources. You can invoke ListNodeInstanceType to query the ID. Select a specification that is active in the creation region and under the associated product, and meets the CPU or GPU computing requirements.
        self.node_instance_type = node_instance_type
        # The ID of the office network used by the creation resources. Specify this parameter when a specific office network is required, and ensure that it is consistent with the creation region.
        self.office_site_id = office_site_id
        # The package type of the image. Keep it consistent with the selected parent image and creation scenario. Valid values:
        # 
        # - **Ecs**: ECS instance image.
        # - **Vhd**: VHD application image.
        # - **Container**: Container image.
        # - **Ecs_Container**: ECS and container combined image.
        # - **K8s_Node**: Kubernetes node image.
        # 
        # **This operation does not provide the BaseImageId parameter. You cannot explicitly specify the Vhd or Container type that requires a base image to be configured separately.**
        self.package_type = package_type
        # The ID of the parent image used to create the new image. **Required**. You can call ListImage to query the ID. An available distribution record of the parent image must exist in the region where the image is created.
        # 
        # This parameter is required.
        self.parent_image_id = parent_image_id
        # The computing type of the creation resources.
        # 
        # - **CPU**: Uses CPU compute resources.
        # - **GPU**: Uses GPU compute resources.
        # 
        # This parameter is required.
        self.performance_type = performance_type
        # The product to which the image belongs. **Required**. Use an activated product and keep it consistent with the selected parent image. Valid values:
        # 
        # - **CloudGame**: Cloud game.
        # - **CloudApp**: Wuying Cloud App.
        # - **CloudBrowser**: Secure browser.
        # - **CloudDesktop**: Wuying Cloud Computer.
        # - **ImageBuilder**: Image creation resource.
        # - **ImageValidate**: Image validation resource.
        # - **AndroidCloud**: Android cloud.
        # - **GpuRender**: GPU rendering.
        # - **AndroidGpuRender**: Android cloud GPU rendering.
        # - **WuyingServer**: Enterprise edition workstation.
        # - **GpuProxy**: GPU remote rendering proxy.
        # - **GpuCache**: GPU remote rendering cache.
        # - **AIAgent**: AI agent service.
        # - **HostedDesktop**: Hosted computer.
        # - **WuyingWorkstation**: Personal edition container workstation.
        # - **WuyingWorkstationBusiness**: Business edition container workstation.
        # - **WuyingWorkstationTeam**: Linggou container workstation team edition.
        self.product_type = product_type
        # The extended properties of the image. Both keys and values are strings. This parameter can be omitted when no extended configuration is required.
        # 
        # The property key for the driver list is DRIVER_LIST, and the value is a JSON string of an array of driver IDs. We recommend that you specify drivers by using DriverIdList. **If both DriverIdList and PropertyMap.DRIVER_LIST are specified, DriverIdList takes precedence.** Specify other extended properties only when their purposes and values are confirmed.
        self.property_map_shrink = property_map_shrink
        # The list of resources required for image creation, such as the download URLs of applications to be installed. A maximum of 100 items are supported. The ResourceType and Resource of each item must correspond to each other.
        self.resource_list = resource_list
        # The running mode of the image creation environment. Valid values:
        # 
        # - **NORMAL**: Normal running mode.
        # - **COMPATIBLE**: Compatible running mode.
        self.run_mode = run_mode
        # The ID of the region where the image is created. The selected parent image must have been distributed to this region. Available regions are also affected by the region configurations of the account and product.
        self.source_region = source_region
        # The capacity of the system cloud disk in the creation environment. Unit: GiB. The capacity cannot be smaller than the system cloud disk capacity required by the parent image, and must meet the disk requirements of the selected resource specifications.
        # 
        # This parameter is required.
        self.system_disk_size = system_disk_size
        # The list of vSwitch IDs used by the creation resources. A maximum of 100 items are supported. The vSwitches must belong to the selected office network and be located in the creation region.
        self.v_switch_id_list = v_switch_id_list
        # The display name of the new image version, which is used to differentiate different versions of the same image.
        self.version_name = version_name

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.description is not None:
            result['Description'] = self.description

        if self.distro is not None:
            result['Distro'] = self.distro

        if self.driver_id_list is not None:
            result['DriverIdList'] = self.driver_id_list

        if self.image_create_mode is not None:
            result['ImageCreateMode'] = self.image_create_mode

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.language is not None:
            result['Language'] = self.language

        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.parent_image_id is not None:
            result['ParentImageId'] = self.parent_image_id

        if self.performance_type is not None:
            result['PerformanceType'] = self.performance_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.property_map_shrink is not None:
            result['PropertyMap'] = self.property_map_shrink

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.v_switch_id_list is not None:
            result['VSwitchIdList'] = self.v_switch_id_list

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Distro') is not None:
            self.distro = m.get('Distro')

        if m.get('DriverIdList') is not None:
            self.driver_id_list = m.get('DriverIdList')

        if m.get('ImageCreateMode') is not None:
            self.image_create_mode = m.get('ImageCreateMode')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('ParentImageId') is not None:
            self.parent_image_id = m.get('ParentImageId')

        if m.get('PerformanceType') is not None:
            self.performance_type = m.get('PerformanceType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('PropertyMap') is not None:
            self.property_map_shrink = m.get('PropertyMap')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.BuilderImageByParentShrinkRequestResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list = m.get('VSwitchIdList')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class BuilderImageByParentShrinkRequestResourceList(DaraModel):
    def __init__(
        self,
        resource: str = None,
        resource_type: str = None,
    ):
        # The resource content corresponding to ResourceType. For the URL type, enter or return an accessible resource URL.
        self.resource = resource
        # The provision method of the resource content. Valid values:
        # 
        # - **HOSTED**: Hosted resource.
        # - **TEXT**: Text resource.
        # - **URL**: Resource provided through a URL.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource is not None:
            result['Resource'] = self.resource

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

