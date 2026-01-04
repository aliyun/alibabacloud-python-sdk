# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeReservedResourceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        images: main_models.DescribeReservedResourceResponseBodyImages = None,
        request_id: str = None,
        support_resources: main_models.DescribeReservedResourceResponseBodySupportResources = None,
    ):
        # The returned service code. 0 indicates that the request was successful.
        self.code = code
        # The information about the image.
        self.images = images
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.support_resources = support_resources

    def validate(self):
        if self.images:
            self.images.validate()
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.images is not None:
            result['Images'] = self.images.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Images') is not None:
            temp_model = main_models.DescribeReservedResourceResponseBodyImages()
            self.images = temp_model.from_map(m.get('Images'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportResources') is not None:
            temp_model = main_models.DescribeReservedResourceResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m.get('SupportResources'))

        return self

class DescribeReservedResourceResponseBodySupportResources(DaraModel):
    def __init__(
        self,
        support_resource: List[main_models.DescribeReservedResourceResponseBodySupportResourcesSupportResource] = None,
    ):
        self.support_resource = support_resource

    def validate(self):
        if self.support_resource:
            for v1 in self.support_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k1 in self.support_resource:
                result['SupportResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.support_resource = []
        if m.get('SupportResource') is not None:
            for k1 in m.get('SupportResource'):
                temp_model = main_models.DescribeReservedResourceResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k1))

        return self

class DescribeReservedResourceResponseBodySupportResourcesSupportResource(DaraModel):
    def __init__(
        self,
        data_disk_sizes: main_models.DescribeReservedResourceResponseBodySupportResourcesSupportResourceDataDiskSizes = None,
        ens_region_id: str = None,
        instance_spec: str = None,
        support_resources_count: str = None,
        system_disk_sizes: main_models.DescribeReservedResourceResponseBodySupportResourcesSupportResourceSystemDiskSizes = None,
    ):
        # The sizes of data disks.
        self.data_disk_sizes = data_disk_sizes
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The specifications of instances.
        self.instance_spec = instance_spec
        # The number of resources that you can purchase.
        self.support_resources_count = support_resources_count
        # The sizes of system disks.
        self.system_disk_sizes = system_disk_sizes

    def validate(self):
        if self.data_disk_sizes:
            self.data_disk_sizes.validate()
        if self.system_disk_sizes:
            self.system_disk_sizes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_sizes is not None:
            result['DataDiskSizes'] = self.data_disk_sizes.to_map()

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.support_resources_count is not None:
            result['SupportResourcesCount'] = self.support_resources_count

        if self.system_disk_sizes is not None:
            result['SystemDiskSizes'] = self.system_disk_sizes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSizes') is not None:
            temp_model = main_models.DescribeReservedResourceResponseBodySupportResourcesSupportResourceDataDiskSizes()
            self.data_disk_sizes = temp_model.from_map(m.get('DataDiskSizes'))

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('SupportResourcesCount') is not None:
            self.support_resources_count = m.get('SupportResourcesCount')

        if m.get('SystemDiskSizes') is not None:
            temp_model = main_models.DescribeReservedResourceResponseBodySupportResourcesSupportResourceSystemDiskSizes()
            self.system_disk_sizes = temp_model.from_map(m.get('SystemDiskSizes'))

        return self

class DescribeReservedResourceResponseBodySupportResourcesSupportResourceSystemDiskSizes(DaraModel):
    def __init__(
        self,
        system_disk_size: List[str] = None,
    ):
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

class DescribeReservedResourceResponseBodySupportResourcesSupportResourceDataDiskSizes(DaraModel):
    def __init__(
        self,
        data_disk_size: List[str] = None,
    ):
        self.data_disk_size = data_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        return self

class DescribeReservedResourceResponseBodyImages(DaraModel):
    def __init__(
        self,
        image: List[main_models.DescribeReservedResourceResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for v1 in self.image:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Image'] = []
        if self.image is not None:
            for k1 in self.image:
                result['Image'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k1 in m.get('Image'):
                temp_model = main_models.DescribeReservedResourceResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k1))

        return self

class DescribeReservedResourceResponseBodyImagesImage(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
    ):
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        return self

