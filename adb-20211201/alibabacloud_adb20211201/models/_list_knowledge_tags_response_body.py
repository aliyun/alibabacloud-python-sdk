# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeTagsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListKnowledgeTagsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request
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
            temp_model = main_models.ListKnowledgeTagsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListKnowledgeTagsResponseBodyData(DaraModel):
    def __init__(
        self,
        file_location: str = None,
        message: str = None,
        success: bool = None,
        tags: List[main_models.ListKnowledgeTagsResponseBodyDataTags] = None,
    ):
        # The location of the knowledge base file.
        self.file_location = file_location
        # The prompt message.
        self.message = message
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success
        # The list details.
        self.tags = tags

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
        if self.file_location is not None:
            result['FileLocation'] = self.file_location

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileLocation') is not None:
            self.file_location = m.get('FileLocation')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListKnowledgeTagsResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListKnowledgeTagsResponseBodyDataTags(DaraModel):
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

