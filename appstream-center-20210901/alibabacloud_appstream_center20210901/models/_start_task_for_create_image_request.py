# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class StartTaskForCreateImageRequest(DaraModel):
    def __init__(
        self,
        image_create_mode: str = None,
        image_id: str = None,
        instance_id: str = None,
        jump_step: str = None,
        performance_type: str = None,
        product_type: str = None,
        resource_list: List[main_models.StartTaskForCreateImageRequestResourceList] = None,
        retry_type: str = None,
        run_mode: str = None,
        source_region: str = None,
        sub_instance_id: str = None,
        system_disk_size: int = None,
        version_id: str = None,
    ):
        # The image creation mode. Currently, use the following mode:
        # 
        # - **BUILDER_MANUAL**: Manually enter the creation environment to install applications and configure the image.
        self.image_create_mode = image_create_mode
        # The ID of the image. This parameter is not exposed by default.
        self.image_id = image_id
        # The WUYING instance ID. The instance can be a cloud desktop instance or a workstation instance. To ensure data consistency in the image, stop the instance before initiating image creation.
        self.instance_id = instance_id
        # The step to jump to.
        self.jump_step = jump_step
        # The resource type.
        self.performance_type = performance_type
        # The product type. Set this parameter to the following fixed value when you call the operation:
        # 
        # - CloudApp: WUYING Cloud App.
        self.product_type = product_type
        # The list of resources required for image creation, such as the download URLs of applications to be installed. You can specify up to 100 items. The ResourceType and Resource of each item must correspond to each other.
        self.resource_list = resource_list
        # The retry type.
        self.retry_type = retry_type
        # The running mode of the image creation environment. Valid values:
        # 
        # - **NORMAL**: Normal running mode.
        # - **COMPATIBLE**: Compatible running mode.
        self.run_mode = run_mode
        # The source region where the image is created. If you do not specify this parameter, a region is randomly selected.
        self.source_region = source_region
        # The sub-instance ID. This parameter is not applicable to cloud desktop scenarios. In workstation scenarios, pass the persistent session ID to ensure that a specific instance is located.
        self.sub_instance_id = sub_instance_id
        # The size of the system cloud disk. Unit: GB.
        self.system_disk_size = system_disk_size
        # The image version. This parameter is currently not exposed.
        self.version_id = version_id

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
        if self.image_create_mode is not None:
            result['ImageCreateMode'] = self.image_create_mode

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.jump_step is not None:
            result['JumpStep'] = self.jump_step

        if self.performance_type is not None:
            result['PerformanceType'] = self.performance_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        if self.retry_type is not None:
            result['RetryType'] = self.retry_type

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.sub_instance_id is not None:
            result['SubInstanceId'] = self.sub_instance_id

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageCreateMode') is not None:
            self.image_create_mode = m.get('ImageCreateMode')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JumpStep') is not None:
            self.jump_step = m.get('JumpStep')

        if m.get('PerformanceType') is not None:
            self.performance_type = m.get('PerformanceType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.StartTaskForCreateImageRequestResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        if m.get('RetryType') is not None:
            self.retry_type = m.get('RetryType')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SubInstanceId') is not None:
            self.sub_instance_id = m.get('SubInstanceId')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class StartTaskForCreateImageRequestResourceList(DaraModel):
    def __init__(
        self,
        resource: str = None,
        resource_type: str = None,
    ):
        # The resource information.
        self.resource = resource
        # The resource type.
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

