# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mns_open20220119 import models as main_models
from darabonba.model import DaraModel

class ListTopicRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        tag: List[main_models.ListTopicRequestTag] = None,
        topic_name: str = None,
        topic_type: str = None,
    ):
        # The page number of the results to return.
        # Valid values: 1 to 100000000.
        # If you set this parameter to a value less than 1, the system uses 1 by default. If you set this parameter to a value greater than 100000000, the system uses 100000000 by default.
        self.page_num = page_num
        # The number of results to return on each page.
        # Valid values: 10 to 50.
        # If you set this parameter to a value less than 10, the system uses 10 by default. If you set this parameter to a value greater than 50, the system uses 50 by default.
        self.page_size = page_size
        # The list of tags.
        self.tag = tag
        # The name of the topic.
        self.topic_name = topic_name
        # The type of the topic. Valid values:
        #    * normal: normal topic
        #    * fifo: FIFO topic
        self.topic_type = topic_type

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
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.topic_type is not None:
            result['TopicType'] = self.topic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListTopicRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')

        return self

class ListTopicRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

