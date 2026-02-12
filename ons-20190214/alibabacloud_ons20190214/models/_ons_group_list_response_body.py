# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsGroupListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsGroupListResponseBodyData = None,
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
            temp_model = main_models.OnsGroupListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsGroupListResponseBodyData(DaraModel):
    def __init__(
        self,
        subscribe_info_do: List[main_models.OnsGroupListResponseBodyDataSubscribeInfoDo] = None,
    ):
        self.subscribe_info_do = subscribe_info_do

    def validate(self):
        if self.subscribe_info_do:
            for v1 in self.subscribe_info_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubscribeInfoDo'] = []
        if self.subscribe_info_do is not None:
            for k1 in self.subscribe_info_do:
                result['SubscribeInfoDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscribe_info_do = []
        if m.get('SubscribeInfoDo') is not None:
            for k1 in m.get('SubscribeInfoDo'):
                temp_model = main_models.OnsGroupListResponseBodyDataSubscribeInfoDo()
                self.subscribe_info_do.append(temp_model.from_map(k1))

        return self

class OnsGroupListResponseBodyDataSubscribeInfoDo(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        group_id: str = None,
        group_type: str = None,
        independent_naming: bool = None,
        instance_id: str = None,
        owner: str = None,
        remark: str = None,
        tags: main_models.OnsGroupListResponseBodyDataSubscribeInfoDoTags = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.group_id = group_id
        self.group_type = group_type
        self.independent_naming = independent_naming
        self.instance_id = instance_id
        self.owner = owner
        self.remark = remark
        self.tags = tags
        self.update_time = update_time

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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Tags') is not None:
            temp_model = main_models.OnsGroupListResponseBodyDataSubscribeInfoDoTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class OnsGroupListResponseBodyDataSubscribeInfoDoTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.OnsGroupListResponseBodyDataSubscribeInfoDoTagsTag] = None,
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
                temp_model = main_models.OnsGroupListResponseBodyDataSubscribeInfoDoTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class OnsGroupListResponseBodyDataSubscribeInfoDoTagsTag(DaraModel):
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

