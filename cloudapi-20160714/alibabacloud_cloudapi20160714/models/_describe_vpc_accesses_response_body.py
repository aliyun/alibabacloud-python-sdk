# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcAccessesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpc_access_attributes: main_models.DescribeVpcAccessesResponseBodyVpcAccessAttributes = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count
        # The information about the VPC access authorization. The information is an array consisting of VpcAccessAttribute data.
        self.vpc_access_attributes = vpc_access_attributes

    def validate(self):
        if self.vpc_access_attributes:
            self.vpc_access_attributes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vpc_access_attributes is not None:
            result['VpcAccessAttributes'] = self.vpc_access_attributes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VpcAccessAttributes') is not None:
            temp_model = main_models.DescribeVpcAccessesResponseBodyVpcAccessAttributes()
            self.vpc_access_attributes = temp_model.from_map(m.get('VpcAccessAttributes'))

        return self

class DescribeVpcAccessesResponseBodyVpcAccessAttributes(DaraModel):
    def __init__(
        self,
        vpc_access_attribute: List[main_models.DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute] = None,
    ):
        self.vpc_access_attribute = vpc_access_attribute

    def validate(self):
        if self.vpc_access_attribute:
            for v1 in self.vpc_access_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VpcAccessAttribute'] = []
        if self.vpc_access_attribute is not None:
            for k1 in self.vpc_access_attribute:
                result['VpcAccessAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc_access_attribute = []
        if m.get('VpcAccessAttribute') is not None:
            for k1 in m.get('VpcAccessAttribute'):
                temp_model = main_models.DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute()
                self.vpc_access_attribute.append(temp_model.from_map(k1))

        return self

class DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttribute(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        port: int = None,
        region_id: str = None,
        tags: main_models.DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttributeTags = None,
        vpc_access_id: str = None,
        vpc_id: str = None,
        vpc_target_host_name: str = None,
    ):
        # The time when the authorization was created.
        self.created_time = created_time
        # The description of the VPC access authorization.
        self.description = description
        # The ID of an Elastic Compute Service (ECS) or Server Load Balancer (SLB) instance in the VPC.
        self.instance_id = instance_id
        # The name of the authorization.
        self.name = name
        # The port number that corresponds to the instance.
        self.port = port
        # The region ID.
        self.region_id = region_id
        # The tags.
        self.tags = tags
        # The ID of the VPC access authorization.
        self.vpc_access_id = vpc_access_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The host of the backend service.
        self.vpc_target_host_name = vpc_target_host_name

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.vpc_access_id is not None:
            result['VpcAccessId'] = self.vpc_access_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_target_host_name is not None:
            result['VpcTargetHostName'] = self.vpc_target_host_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttributeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('VpcAccessId') is not None:
            self.vpc_access_id = m.get('VpcAccessId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcTargetHostName') is not None:
            self.vpc_target_host_name = m.get('VpcTargetHostName')

        return self

class DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttributeTags(DaraModel):
    def __init__(
        self,
        tag_info: List[main_models.DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttributeTagsTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for v1 in self.tag_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k1 in self.tag_info:
                result['TagInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k1 in m.get('TagInfo'):
                temp_model = main_models.DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttributeTagsTagInfo()
                self.tag_info.append(temp_model.from_map(k1))

        return self

class DescribeVpcAccessesResponseBodyVpcAccessAttributesVpcAccessAttributeTagsTagInfo(DaraModel):
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

