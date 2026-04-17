# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetTopicListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        topic_list: main_models.GetTopicListResponseBodyTopicList = None,
        total: int = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        # The page number of the returned page.
        self.current_page = current_page
        # The message returned.
        self.message = message
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        self.topic_list = topic_list
        # The number of topics.
        self.total = total

    def validate(self):
        if self.topic_list:
            self.topic_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.topic_list is not None:
            result['TopicList'] = self.topic_list.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TopicList') is not None:
            temp_model = main_models.GetTopicListResponseBodyTopicList()
            self.topic_list = temp_model.from_map(m.get('TopicList'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetTopicListResponseBodyTopicList(DaraModel):
    def __init__(
        self,
        topic_vo: List[main_models.GetTopicListResponseBodyTopicListTopicVO] = None,
    ):
        self.topic_vo = topic_vo

    def validate(self):
        if self.topic_vo:
            for v1 in self.topic_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TopicVO'] = []
        if self.topic_vo is not None:
            for k1 in self.topic_vo:
                result['TopicVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topic_vo = []
        if m.get('TopicVO') is not None:
            for k1 in m.get('TopicVO'):
                temp_model = main_models.GetTopicListResponseBodyTopicListTopicVO()
                self.topic_vo.append(temp_model.from_map(k1))

        return self

class GetTopicListResponseBodyTopicListTopicVO(DaraModel):
    def __init__(
        self,
        auto_create: bool = None,
        compact_topic: bool = None,
        create_time: int = None,
        instance_id: str = None,
        local_topic: bool = None,
        partition_num: int = None,
        region_id: str = None,
        remark: str = None,
        status: int = None,
        status_name: str = None,
        tags: main_models.GetTopicListResponseBodyTopicListTopicVOTags = None,
        topic: str = None,
        topic_config: str = None,
    ):
        self.auto_create = auto_create
        self.compact_topic = compact_topic
        self.create_time = create_time
        self.instance_id = instance_id
        self.local_topic = local_topic
        self.partition_num = partition_num
        self.region_id = region_id
        self.remark = remark
        self.status = status
        self.status_name = status_name
        self.tags = tags
        self.topic = topic
        self.topic_config = topic_config

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create is not None:
            result['AutoCreate'] = self.auto_create

        if self.compact_topic is not None:
            result['CompactTopic'] = self.compact_topic

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.local_topic is not None:
            result['LocalTopic'] = self.local_topic

        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.topic_config is not None:
            result['TopicConfig'] = self.topic_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreate') is not None:
            self.auto_create = m.get('AutoCreate')

        if m.get('CompactTopic') is not None:
            self.compact_topic = m.get('CompactTopic')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LocalTopic') is not None:
            self.local_topic = m.get('LocalTopic')

        if m.get('PartitionNum') is not None:
            self.partition_num = m.get('PartitionNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        if m.get('Tags') is not None:
            temp_model = main_models.GetTopicListResponseBodyTopicListTopicVOTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TopicConfig') is not None:
            self.topic_config = m.get('TopicConfig')

        return self

class GetTopicListResponseBodyTopicListTopicVOTags(DaraModel):
    def __init__(
        self,
        tag_vo: List[main_models.GetTopicListResponseBodyTopicListTopicVOTagsTagVO] = None,
    ):
        self.tag_vo = tag_vo

    def validate(self):
        if self.tag_vo:
            for v1 in self.tag_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagVO'] = []
        if self.tag_vo is not None:
            for k1 in self.tag_vo:
                result['TagVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_vo = []
        if m.get('TagVO') is not None:
            for k1 in m.get('TagVO'):
                temp_model = main_models.GetTopicListResponseBodyTopicListTopicVOTagsTagVO()
                self.tag_vo.append(temp_model.from_map(k1))

        return self

class GetTopicListResponseBodyTopicListTopicVOTagsTagVO(DaraModel):
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

