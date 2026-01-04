# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableResourceInfoResponseBody(DaraModel):
    def __init__(
        self,
        images: main_models.DescribeAvailableResourceInfoResponseBodyImages = None,
        request_id: str = None,
        support_resources: main_models.DescribeAvailableResourceInfoResponseBodySupportResources = None,
    ):
        # The information about the image.
        self.images = images
        # The request ID.
        self.request_id = request_id
        # The specifications of resources that you can purchase.
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
        if self.images is not None:
            result['Images'] = self.images.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Images') is not None:
            temp_model = main_models.DescribeAvailableResourceInfoResponseBodyImages()
            self.images = temp_model.from_map(m.get('Images'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SupportResources') is not None:
            temp_model = main_models.DescribeAvailableResourceInfoResponseBodySupportResources()
            self.support_resources = temp_model.from_map(m.get('SupportResources'))

        return self

class DescribeAvailableResourceInfoResponseBodySupportResources(DaraModel):
    def __init__(
        self,
        support_resource: List[main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResource] = None,
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
                temp_model = main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResource(DaraModel):
    def __init__(
        self,
        bandwidth_types: main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceBandwidthTypes = None,
        data_disk_max_size: int = None,
        data_disk_min_size: int = None,
        ens_region_ids: main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIds = None,
        ens_region_ids_extends: main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtends = None,
        instance_speces: main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceInstanceSpeces = None,
        isp: main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceIsp = None,
        system_disk_max_size: int = None,
        system_disk_min_size: int = None,
    ):
        # Bandwidth billing method.
        self.bandwidth_types = bandwidth_types
        # The maximum capacity of a data disk. Unit: GB.
        self.data_disk_max_size = data_disk_max_size
        # The minimum data disk size. Unit: GiB.
        self.data_disk_min_size = data_disk_min_size
        # node ID
        self.ens_region_ids = ens_region_ids
        # The supplementary information about the edge nodes.
        self.ens_region_ids_extends = ens_region_ids_extends
        self.instance_speces = instance_speces
        # Operator
        self.isp = isp
        # The maximum size of the system disk. Unit: GiB.
        self.system_disk_max_size = system_disk_max_size
        # The minimum capacity of a system disk. Unit: GB.
        self.system_disk_min_size = system_disk_min_size

    def validate(self):
        if self.bandwidth_types:
            self.bandwidth_types.validate()
        if self.ens_region_ids:
            self.ens_region_ids.validate()
        if self.ens_region_ids_extends:
            self.ens_region_ids_extends.validate()
        if self.instance_speces:
            self.instance_speces.validate()
        if self.isp:
            self.isp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_types is not None:
            result['BandwidthTypes'] = self.bandwidth_types.to_map()

        if self.data_disk_max_size is not None:
            result['DataDiskMaxSize'] = self.data_disk_max_size

        if self.data_disk_min_size is not None:
            result['DataDiskMinSize'] = self.data_disk_min_size

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids.to_map()

        if self.ens_region_ids_extends is not None:
            result['EnsRegionIdsExtends'] = self.ens_region_ids_extends.to_map()

        if self.instance_speces is not None:
            result['InstanceSpeces'] = self.instance_speces.to_map()

        if self.isp is not None:
            result['Isp'] = self.isp.to_map()

        if self.system_disk_max_size is not None:
            result['SystemDiskMaxSize'] = self.system_disk_max_size

        if self.system_disk_min_size is not None:
            result['SystemDiskMinSize'] = self.system_disk_min_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthTypes') is not None:
            temp_model = main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceBandwidthTypes()
            self.bandwidth_types = temp_model.from_map(m.get('BandwidthTypes'))

        if m.get('DataDiskMaxSize') is not None:
            self.data_disk_max_size = m.get('DataDiskMaxSize')

        if m.get('DataDiskMinSize') is not None:
            self.data_disk_min_size = m.get('DataDiskMinSize')

        if m.get('EnsRegionIds') is not None:
            temp_model = main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIds()
            self.ens_region_ids = temp_model.from_map(m.get('EnsRegionIds'))

        if m.get('EnsRegionIdsExtends') is not None:
            temp_model = main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtends()
            self.ens_region_ids_extends = temp_model.from_map(m.get('EnsRegionIdsExtends'))

        if m.get('InstanceSpeces') is not None:
            temp_model = main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceInstanceSpeces()
            self.instance_speces = temp_model.from_map(m.get('InstanceSpeces'))

        if m.get('Isp') is not None:
            temp_model = main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceIsp()
            self.isp = temp_model.from_map(m.get('Isp'))

        if m.get('SystemDiskMaxSize') is not None:
            self.system_disk_max_size = m.get('SystemDiskMaxSize')

        if m.get('SystemDiskMinSize') is not None:
            self.system_disk_min_size = m.get('SystemDiskMinSize')

        return self

class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceIsp(DaraModel):
    def __init__(
        self,
        isp: List[str] = None,
    ):
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isp is not None:
            result['Isp'] = self.isp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        return self

class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceInstanceSpeces(DaraModel):
    def __init__(
        self,
        instance_spec: List[str] = None,
    ):
        self.instance_spec = instance_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        return self

class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtends(DaraModel):
    def __init__(
        self,
        ens_region_id: List[main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtendsEnsRegionId] = None,
    ):
        self.ens_region_id = ens_region_id

    def validate(self):
        if self.ens_region_id:
            for v1 in self.ens_region_id:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnsRegionId'] = []
        if self.ens_region_id is not None:
            for k1 in self.ens_region_id:
                result['EnsRegionId'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_region_id = []
        if m.get('EnsRegionId') is not None:
            for k1 in m.get('EnsRegionId'):
                temp_model = main_models.DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtendsEnsRegionId()
                self.ens_region_id.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIdsExtendsEnsRegionId(DaraModel):
    def __init__(
        self,
        area: str = None,
        en_name: str = None,
        ens_region_id: str = None,
        isp: str = None,
        name: str = None,
        province: str = None,
    ):
        # The region.
        self.area = area
        # The name. This parameter is empty by default.
        self.en_name = en_name
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The information about the Internet service provider (ISP).
        self.isp = isp
        # The name of the edge node.
        self.name = name
        # The province.
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.en_name is not None:
            result['EnName'] = self.en_name

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.name is not None:
            result['Name'] = self.name

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceEnsRegionIds(DaraModel):
    def __init__(
        self,
        ens_region_id: List[str] = None,
    ):
        self.ens_region_id = ens_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        return self

class DescribeAvailableResourceInfoResponseBodySupportResourcesSupportResourceBandwidthTypes(DaraModel):
    def __init__(
        self,
        bandwidth_type: List[str] = None,
    ):
        self.bandwidth_type = bandwidth_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        return self

class DescribeAvailableResourceInfoResponseBodyImages(DaraModel):
    def __init__(
        self,
        image: List[main_models.DescribeAvailableResourceInfoResponseBodyImagesImage] = None,
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
                temp_model = main_models.DescribeAvailableResourceInfoResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceInfoResponseBodyImagesImage(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        image_size: int = None,
    ):
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The size of the image. Unit: GB.
        self.image_size = image_size

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

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        return self

