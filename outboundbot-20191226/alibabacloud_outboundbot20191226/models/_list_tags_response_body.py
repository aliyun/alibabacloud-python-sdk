# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListTagsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        tag_groups: List[main_models.ListTagsResponseBodyTagGroups] = None,
        tags: List[main_models.ListTagsResponseBodyTags] = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.tag_groups = tag_groups
        self.tags = tags

    def validate(self):
        if self.tag_groups:
            for v1 in self.tag_groups:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TagGroups'] = []
        if self.tag_groups is not None:
            for k1 in self.tag_groups:
                result['TagGroups'].append(k1.to_map() if k1 else None)

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.tag_groups = []
        if m.get('TagGroups') is not None:
            for k1 in m.get('TagGroups'):
                temp_model = main_models.ListTagsResponseBodyTagGroups()
                self.tag_groups.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListTagsResponseBodyTags(DaraModel):
    def __init__(
        self,
        script_id: str = None,
        tag_group: str = None,
        tag_id: str = None,
        tag_index: int = None,
        tag_name: str = None,
    ):
        self.script_id = script_id
        self.tag_group = tag_group
        self.tag_id = tag_id
        self.tag_index = tag_index
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_index is not None:
            result['TagIndex'] = self.tag_index

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagIndex') is not None:
            self.tag_index = m.get('TagIndex')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class ListTagsResponseBodyTagGroups(DaraModel):
    def __init__(
        self,
        script_id: str = None,
        tag_group: str = None,
        tag_group_id: str = None,
        tag_group_index: int = None,
    ):
        self.script_id = script_id
        self.tag_group = tag_group
        self.tag_group_id = tag_group_id
        self.tag_group_index = tag_group_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group

        if self.tag_group_id is not None:
            result['TagGroupId'] = self.tag_group_id

        if self.tag_group_index is not None:
            result['TagGroupIndex'] = self.tag_group_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')

        if m.get('TagGroupId') is not None:
            self.tag_group_id = m.get('TagGroupId')

        if m.get('TagGroupIndex') is not None:
            self.tag_group_index = m.get('TagGroupIndex')

        return self

