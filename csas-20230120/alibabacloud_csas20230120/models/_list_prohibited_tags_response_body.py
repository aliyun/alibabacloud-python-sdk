# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListProhibitedTagsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[main_models.ListProhibitedTagsResponseBodyTags] = None,
        total_num: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The list of prohibited software tags.
        self.tags = tags
        # The total number of prohibited software tags.
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
                temp_model = main_models.ListProhibitedTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListProhibitedTagsResponseBodyTags(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        is_default: bool = None,
        name: str = None,
        policy_ids: List[str] = None,
        software_ids: List[str] = None,
        tag_id: str = None,
    ):
        # The time when the prohibited software tag was created, in the yyyy-MM-dd HH:mm:ss format. The time is in the UTC+8 time zone.
        self.create_time = create_time
        # The description of the prohibited software tag.
        self.description = description
        # Indicates whether the tag is a system built-in device tag. Valid values:
        # - **true**: A system built-in device tag.
        # - **false**: A user-defined device tag.
        self.is_default = is_default
        # The name of the prohibited software tag.
        self.name = name
        # The collection of software prohibition policy IDs that reference the tag.
        self.policy_ids = policy_ids
        # The collection of prohibited software IDs included in the tag.
        self.software_ids = software_ids
        # The ID of the prohibited software tag.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.software_ids is not None:
            result['SoftwareIds'] = self.software_ids

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SoftwareIds') is not None:
            self.software_ids = m.get('SoftwareIds')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

