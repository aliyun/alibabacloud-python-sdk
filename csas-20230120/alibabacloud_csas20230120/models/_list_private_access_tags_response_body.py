# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListPrivateAccessTagsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[main_models.ListPrivateAccessTagsResponseBodyTags] = None,
        total_num: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The internal access tags.
        self.tags = tags
        # The total number of internal access tags.
        self.total_num = total_num

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPrivateAccessTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListPrivateAccessTagsResponseBodyTags(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        policy_ids: List[str] = None,
        tag_id: str = None,
        tag_type: str = None,
    ):
        # The IDs of the internal access applications.
        self.application_ids = application_ids
        # The time when the internal access tag was created.
        self.create_time = create_time
        # The description of the internal access tag.
        self.description = description
        # The name of the internal access tag.
        self.name = name
        # The IDs of the internal access policies.
        self.policy_ids = policy_ids
        # The ID of the internal access tag.
        self.tag_id = tag_id
        # The type of the internal access tag. Valid values:
        # 
        # *   **Default**
        # *   **Custom**
        self.tag_type = tag_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_type is not None:
            result['TagType'] = self.tag_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagType') is not None:
            self.tag_type = m.get('TagType')

        return self

