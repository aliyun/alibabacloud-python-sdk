# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetMemoryDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        groups: List[main_models.GetMemoryDetailResponseBodyGroups] = None,
        message: str = None,
        profile: main_models.GetMemoryDetailResponseBodyProfile = None,
        request_id: str = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The list of groups for automatically collected memories. If no automatic memories exist, an empty array is returned.
        self.groups = groups
        # The error description.
        self.message = message
        # The manually added memory from profile.md. It includes the full content, existence status, and modification time.
        self.profile = profile
        # The request tracking ID.
        self.request_id = request_id

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.profile:
            self.profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['groups'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.profile is not None:
            result['profile'] = self.profile.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.groups = []
        if m.get('groups') is not None:
            for k1 in m.get('groups'):
                temp_model = main_models.GetMemoryDetailResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('profile') is not None:
            temp_model = main_models.GetMemoryDetailResponseBodyProfile()
            self.profile = temp_model.from_map(m.get('profile'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetMemoryDetailResponseBodyProfile(DaraModel):
    def __init__(
        self,
        content: str = None,
        exists: bool = None,
        gmt_modified: int = None,
    ):
        # The full body of the manual memory. If the memory has never been saved, an empty string is returned.
        self.content = content
        # Indicates whether profile.md exists. If the memory has never been saved, false is returned.
        self.exists = exists
        # The last modification time of profile.md. The value is a UNIX timestamp in seconds. If the file does not exist or its metadata cannot be obtained, null is returned.
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.exists is not None:
            result['exists'] = self.exists

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('exists') is not None:
            self.exists = m.get('exists')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        return self

class GetMemoryDetailResponseBodyGroups(DaraModel):
    def __init__(
        self,
        gmt_modified: int = None,
        items: List[main_models.GetMemoryDetailResponseBodyGroupsItems] = None,
        type: str = None,
    ):
        # The last modification time of the group. The value is a UNIX timestamp in seconds. If no files exist, null is returned.
        self.gmt_modified = gmt_modified
        # The list of automatic memory entries under this type. If no entries exist, an empty array is returned.
        self.items = items
        # The type of the automatic memory. Valid values: user, feedback, reference, and project.
        self.type = type

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetMemoryDetailResponseBodyGroupsItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetMemoryDetailResponseBodyGroupsItems(DaraModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        id: str = None,
        title: str = None,
    ):
        # The body of the automatic memory, excluding the YAML frontmatter.
        self.content = content
        # The additional description of the automatic memory. If no description is available, an empty string is returned.
        self.description = description
        # The unique identifier of the automatic memory entry, which is a relative OSS path.
        self.id = id
        # The title of the automatic memory, which is derived from the file metadata or file name.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

