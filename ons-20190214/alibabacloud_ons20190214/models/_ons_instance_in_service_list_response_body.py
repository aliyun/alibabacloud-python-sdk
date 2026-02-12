# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsInstanceInServiceListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsInstanceInServiceListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.OnsInstanceInServiceListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsInstanceInServiceListResponseBodyData(DaraModel):
    def __init__(
        self,
        instance_vo: List[main_models.OnsInstanceInServiceListResponseBodyDataInstanceVO] = None,
    ):
        self.instance_vo = instance_vo

    def validate(self):
        if self.instance_vo:
            for v1 in self.instance_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceVO'] = []
        if self.instance_vo is not None:
            for k1 in self.instance_vo:
                result['InstanceVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_vo = []
        if m.get('InstanceVO') is not None:
            for k1 in m.get('InstanceVO'):
                temp_model = main_models.OnsInstanceInServiceListResponseBodyDataInstanceVO()
                self.instance_vo.append(temp_model.from_map(k1))

        return self

class OnsInstanceInServiceListResponseBodyDataInstanceVO(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        group_count: int = None,
        independent_naming: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: int = None,
        instance_type: int = None,
        release_time: int = None,
        tags: main_models.OnsInstanceInServiceListResponseBodyDataInstanceVOTags = None,
        topic_count: int = None,
    ):
        self.create_time = create_time
        self.group_count = group_count
        self.independent_naming = independent_naming
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.release_time = release_time
        self.tags = tags
        self.topic_count = topic_count

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.topic_count is not None:
            result['TopicCount'] = self.topic_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('Tags') is not None:
            temp_model = main_models.OnsInstanceInServiceListResponseBodyDataInstanceVOTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TopicCount') is not None:
            self.topic_count = m.get('TopicCount')

        return self

class OnsInstanceInServiceListResponseBodyDataInstanceVOTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.OnsInstanceInServiceListResponseBodyDataInstanceVOTagsTag] = None,
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
                temp_model = main_models.OnsInstanceInServiceListResponseBodyDataInstanceVOTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class OnsInstanceInServiceListResponseBodyDataInstanceVOTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

