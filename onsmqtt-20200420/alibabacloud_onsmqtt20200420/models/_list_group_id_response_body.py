# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class ListGroupIdResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListGroupIdResponseBodyData] = None,
        request_id: str = None,
    ):
        # The details of the returned group IDs.
        self.data = data
        # The unique ID for the request. This is a common parameter.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListGroupIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGroupIdResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        group_id: str = None,
        independent_naming: bool = None,
        instance_id: str = None,
        tags: List[main_models.ListGroupIdResponseBodyDataTags] = None,
        update_time: int = None,
    ):
        # The creation timestamp of the group ID.
        self.create_time = create_time
        # The group ID.
        self.group_id = group_id
        # Indicates whether the instance has an independent namespace. Valid values:
        # 
        # - **true**: The instance has an independent namespace. In this case, resource names must be unique within the instance, but they can be the same as resource names in other instances.
        # 
        # - **false**: The instance does not have an independent namespace. In this case, resource names must be globally unique across all instances.
        self.independent_naming = independent_naming
        # The ID of the instance to which the group ID belongs.
        self.instance_id = instance_id
        # The tags attached to the group ID.
        self.tags = tags
        # The timestamp of the last update for the group ID.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListGroupIdResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListGroupIdResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

