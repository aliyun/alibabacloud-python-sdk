# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitorGroupInstanceAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResources = None,
        success: bool = None,
        total: int = None,
    ):
        # The responses code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The resources that are associated with the application group.
        self.resources = resources
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            temp_model = main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeMonitorGroupInstanceAttributeResponseBodyResources(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResource(DaraModel):
    def __init__(
        self,
        category: str = None,
        desc: str = None,
        dimension: str = None,
        instance_id: str = None,
        instance_name: str = None,
        network_type: str = None,
        region: main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceRegion = None,
        tags: main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceTags = None,
        vpc: main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceVpc = None,
    ):
        # The name of the cloud service.
        self.category = category
        # The resource description.
        self.desc = desc
        # The dimensions of the resource that is associated with the application group.
        self.dimension = dimension
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The network type.
        self.network_type = network_type
        # The region.
        self.region = region
        # The tag of the resource.
        self.tags = tags
        # The VPC description.
        self.vpc = vpc

    def validate(self):
        if self.region:
            self.region.validate()
        if self.tags:
            self.tags.validate()
        if self.vpc:
            self.vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region is not None:
            result['Region'] = self.region.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc is not None:
            result['Vpc'] = self.vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Region') is not None:
            temp_model = main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceRegion()
            self.region = temp_model.from_map(m.get('Region'))

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Vpc') is not None:
            temp_model = main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceVpc()
            self.vpc = temp_model.from_map(m.get('Vpc'))

        return self

class DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceVpc(DaraModel):
    def __init__(
        self,
        vpc_instance_id: str = None,
        vswitch_instance_id: str = None,
    ):
        # The VPC ID.
        self.vpc_instance_id = vpc_instance_id
        # The vSwitch ID.
        self.vswitch_instance_id = vswitch_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        if self.vswitch_instance_id is not None:
            result['VswitchInstanceId'] = self.vswitch_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        if m.get('VswitchInstanceId') is not None:
            self.vswitch_instance_id = m.get('VswitchInstanceId')

        return self

class DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class DescribeMonitorGroupInstanceAttributeResponseBodyResourcesResourceRegion(DaraModel):
    def __init__(
        self,
        availability_zone: str = None,
        region_id: str = None,
    ):
        # The zone.
        self.availability_zone = availability_zone
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

