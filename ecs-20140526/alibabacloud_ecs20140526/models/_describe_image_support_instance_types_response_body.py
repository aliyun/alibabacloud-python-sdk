# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImageSupportInstanceTypesResponseBody(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        instance_types: main_models.DescribeImageSupportInstanceTypesResponseBodyInstanceTypes = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # The key of filter N. Only the image ID can be used to filter instance types. Valid values:
        # 
        # *   imagId: image ID
        # *   filter: image ID
        self.image_id = image_id
        # {
        #     "RequestId": "CF661E2D-4AFE-4BCD-959A-A65E14416B44",
        #     "RegionId": "cn-hangzhou",
        #     "ImageId": "ubuntu_16_0402_64_20G_alibase_20180409.vhd",
        #     "InstanceTypes": {
        #         "InstanceType": [{
        #             "InstanceTypeId": "ecs.t1.xsmall",
        #             "CpuCoreCount": 1,
        #             "MemorySize": 0.5,
        #             "InstanceTypeFamily": "ecs.t1"
        #         },
        #         {
        #             "InstanceTypeId": "ecs.t1.small",
        #             "CpuCoreCount": 1,
        #             "MemorySize": 1,
        #             "InstanceTypeFamily": "ecs.t1"
        #         }]
        #     }
        # }
        self.instance_types = instance_types
        # {
        #     "RequestId": "CF661E2D-4AFE-4BCD-959A-A65E14416B44",
        #     "RegionId": "cn-hangzhou",
        #     "ImageId": "ubuntu_16_0402_64_20G_alibase_20180409.vhd",
        #     "InstanceTypes": {
        #         "InstanceType": [{
        #             "InstanceTypeId": "ecs.t1.xsmall",
        #             "CpuCoreCount": 1,
        #             "MemorySize": 0.5,
        #             "InstanceTypeFamily": "ecs.t1"
        #         },
        #         {
        #             "InstanceTypeId": "ecs.t1.small",
        #             "CpuCoreCount": 1,
        #             "MemorySize": 1,
        #             "InstanceTypeFamily": "ecs.t1"
        #         }]
        #     }
        # }
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceTypes') is not None:
            temp_model = main_models.DescribeImageSupportInstanceTypesResponseBodyInstanceTypes()
            self.instance_types = temp_model.from_map(m.get('InstanceTypes'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageSupportInstanceTypesResponseBodyInstanceTypes(DaraModel):
    def __init__(
        self,
        instance_type: List[main_models.DescribeImageSupportInstanceTypesResponseBodyInstanceTypesInstanceType] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type:
            for v1 in self.instance_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k1 in self.instance_type:
                result['InstanceType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k1 in m.get('InstanceType'):
                temp_model = main_models.DescribeImageSupportInstanceTypesResponseBodyInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k1))

        return self

class DescribeImageSupportInstanceTypesResponseBodyInstanceTypesInstanceType(DaraModel):
    def __init__(
        self,
        cpu_core_count: int = None,
        instance_type_family: str = None,
        instance_type_id: str = None,
        memory_size: float = None,
    ):
        # The number of vCPUs of the instance type.
        self.cpu_core_count = cpu_core_count
        # DescribeImageSupportInstanceTypes
        self.instance_type_family = instance_type_family
        # Queries the instance types supported by an image.
        self.instance_type_id = instance_type_id
        # The memory size of the instance type. Unit: GiB.
        self.memory_size = memory_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_core_count is not None:
            result['CpuCoreCount'] = self.cpu_core_count

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.instance_type_id is not None:
            result['InstanceTypeId'] = self.instance_type_id

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCoreCount') is not None:
            self.cpu_core_count = m.get('CpuCoreCount')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('InstanceTypeId') is not None:
            self.instance_type_id = m.get('InstanceTypeId')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        return self

