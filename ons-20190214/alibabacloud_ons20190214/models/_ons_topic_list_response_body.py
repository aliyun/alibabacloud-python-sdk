# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsTopicListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsTopicListResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # The ID of the request. This is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
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
            temp_model = main_models.OnsTopicListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsTopicListResponseBodyData(DaraModel):
    def __init__(
        self,
        publish_info_do: List[main_models.OnsTopicListResponseBodyDataPublishInfoDo] = None,
    ):
        self.publish_info_do = publish_info_do

    def validate(self):
        if self.publish_info_do:
            for v1 in self.publish_info_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PublishInfoDo'] = []
        if self.publish_info_do is not None:
            for k1 in self.publish_info_do:
                result['PublishInfoDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.publish_info_do = []
        if m.get('PublishInfoDo') is not None:
            for k1 in m.get('PublishInfoDo'):
                temp_model = main_models.OnsTopicListResponseBodyDataPublishInfoDo()
                self.publish_info_do.append(temp_model.from_map(k1))

        return self

class OnsTopicListResponseBodyDataPublishInfoDo(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        independent_naming: bool = None,
        instance_id: str = None,
        message_type: int = None,
        owner: str = None,
        relation: int = None,
        relation_name: str = None,
        remark: str = None,
        service_status: int = None,
        tags: main_models.OnsTopicListResponseBodyDataPublishInfoDoTags = None,
        topic: str = None,
    ):
        self.create_time = create_time
        self.independent_naming = independent_naming
        self.instance_id = instance_id
        self.message_type = message_type
        self.owner = owner
        self.relation = relation
        self.relation_name = relation_name
        self.remark = remark
        self.service_status = service_status
        self.tags = tags
        self.topic = topic

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

        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.relation is not None:
            result['Relation'] = self.relation

        if self.relation_name is not None:
            result['RelationName'] = self.relation_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        if m.get('RelationName') is not None:
            self.relation_name = m.get('RelationName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        if m.get('Tags') is not None:
            temp_model = main_models.OnsTopicListResponseBodyDataPublishInfoDoTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class OnsTopicListResponseBodyDataPublishInfoDoTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.OnsTopicListResponseBodyDataPublishInfoDoTagsTag] = None,
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
                temp_model = main_models.OnsTopicListResponseBodyDataPublishInfoDoTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class OnsTopicListResponseBodyDataPublishInfoDoTagsTag(DaraModel):
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

