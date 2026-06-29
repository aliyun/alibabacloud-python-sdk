# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeFileSystemsRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_type: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        tag: List[main_models.DescribeFileSystemsRequestTag] = None,
        vpc_id: str = None,
    ):
        # The file system ID.
        # - General-purpose NAS: 31a8e4****.
        # - Extreme NAS: Must start with extreme-, such as extreme-0015****.
        # - CPFS (locally redundant): Must start with cpfs-, such as cpfs-125487****.
        # - CPFS SE (zone-redundant): Must start with cpfsse-, such as cpfsse-022c71b134****.
        self.file_system_id = file_system_id
        # The file system type.
        # 
        # Valid values:
        # 
        # - all (default): queries all types.
        # - standard: General-purpose NAS.
        # - extreme: Extreme NAS.
        # - cpfs: Cloud Parallel File Storage (CPFS) (locally redundant).
        # - cpfsse: CPFS SE (zone-redundant).
        # 
        # > To query multiple types, separate them with commas (,).
        self.file_system_type = file_system_type
        # The page number of the file system list.
        # 
        # Start value (default value): 1.
        self.page_number = page_number
        # The number of file systems on each page in a paging query.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The resource group ID.
        # 
        # You can view the resource group ID in the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups?).
        self.resource_group_id = resource_group_id
        # The tag information.
        self.tag = tag
        # The virtual private cloud (VPC) ID.
        # 
        # The VPC must be the same as the VPC of the Elastic Computing Service (ECS) server to which you want to mount the file system.
        self.vpc_id = vpc_id

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
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeFileSystemsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeFileSystemsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # Limits:
        # 
        # - Valid values of N: 1 to 20.
        # - The tag key can be up to 128 characters in length.
        # - The tag key cannot start with `aliyun` or `acs:`.
        # - The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # Limits:
        # 
        # - Valid values of N: 1 to 20.
        # - The tag value can be up to 128 characters in length.
        # - The tag value cannot start with `aliyun` or `acs:`.
        # - The tag value cannot contain `http://` or `https://`.
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

