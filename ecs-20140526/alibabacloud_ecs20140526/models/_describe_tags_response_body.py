# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeTagsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tags: main_models.DescribeTagsResponseBodyTags = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The tags that match all filter conditions.
        self.tags = tags
        # The total number of tags.
        self.total_count = total_count

    def validate(self):
        if self.tags:
            self.tags.validate()

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

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeTagsResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTagsResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeTagsResponseBodyTagsTag] = None,
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
                temp_model = main_models.DescribeTagsResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeTagsResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        resource_type_count: main_models.DescribeTagsResponseBodyTagsTagResourceTypeCount = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The number of resource types.
        self.resource_type_count = resource_type_count
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        if self.resource_type_count:
            self.resource_type_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type_count is not None:
            result['ResourceTypeCount'] = self.resource_type_count.to_map()

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypeCount') is not None:
            temp_model = main_models.DescribeTagsResponseBodyTagsTagResourceTypeCount()
            self.resource_type_count = temp_model.from_map(m.get('ResourceTypeCount'))

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeTagsResponseBodyTagsTagResourceTypeCount(DaraModel):
    def __init__(
        self,
        ddh: int = None,
        disk: int = None,
        eni: int = None,
        image: int = None,
        instance: int = None,
        key_pair: int = None,
        launch_template: int = None,
        reserved_instance: int = None,
        securitygroup: int = None,
        snapshot: int = None,
        snapshot_policy: int = None,
        volume: int = None,
    ):
        # The number of dedicated hosts to which the tag is added.
        self.ddh = ddh
        # The number of disks to which the tag is added.
        self.disk = disk
        # The number of ENIs to which the tag is added.
        self.eni = eni
        # The number of images to which the tag is added.
        self.image = image
        # The number of instances to which the tag is added.
        self.instance = instance
        # The number of key pairs to which the tag is added.
        self.key_pair = key_pair
        # The number of launch templates to which the tag is added.
        self.launch_template = launch_template
        # The number of reserved instances to which the tag is added.
        self.reserved_instance = reserved_instance
        # The number of security groups to which the tag is added.
        self.securitygroup = securitygroup
        # The number of snapshots to which the tag is added.
        self.snapshot = snapshot
        # The number of automatic snapshot policies to which the tag is added.
        self.snapshot_policy = snapshot_policy
        # The number of storage volumes to which the tag is added.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddh is not None:
            result['Ddh'] = self.ddh

        if self.disk is not None:
            result['Disk'] = self.disk

        if self.eni is not None:
            result['Eni'] = self.eni

        if self.image is not None:
            result['Image'] = self.image

        if self.instance is not None:
            result['Instance'] = self.instance

        if self.key_pair is not None:
            result['KeyPair'] = self.key_pair

        if self.launch_template is not None:
            result['LaunchTemplate'] = self.launch_template

        if self.reserved_instance is not None:
            result['ReservedInstance'] = self.reserved_instance

        if self.securitygroup is not None:
            result['Securitygroup'] = self.securitygroup

        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot

        if self.snapshot_policy is not None:
            result['SnapshotPolicy'] = self.snapshot_policy

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ddh') is not None:
            self.ddh = m.get('Ddh')

        if m.get('Disk') is not None:
            self.disk = m.get('Disk')

        if m.get('Eni') is not None:
            self.eni = m.get('Eni')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Instance') is not None:
            self.instance = m.get('Instance')

        if m.get('KeyPair') is not None:
            self.key_pair = m.get('KeyPair')

        if m.get('LaunchTemplate') is not None:
            self.launch_template = m.get('LaunchTemplate')

        if m.get('ReservedInstance') is not None:
            self.reserved_instance = m.get('ReservedInstance')

        if m.get('Securitygroup') is not None:
            self.securitygroup = m.get('Securitygroup')

        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')

        if m.get('SnapshotPolicy') is not None:
            self.snapshot_policy = m.get('SnapshotPolicy')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

