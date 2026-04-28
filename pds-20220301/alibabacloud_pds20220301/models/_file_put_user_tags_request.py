# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class FilePutUserTagsRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        user_tags: List[main_models.FilePutUserTagsRequestUserTags] = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The tags to be added to the file. You cannot leave this parameter empty. You can specify up to 1,000 tags. You cannot specify tags that have the same name.
        # 
        # This parameter is required.
        self.user_tags = user_tags

    def validate(self):
        if self.user_tags:
            for v1 in self.user_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        result['user_tags'] = []
        if self.user_tags is not None:
            for k1 in self.user_tags:
                result['user_tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        self.user_tags = []
        if m.get('user_tags') is not None:
            for k1 in m.get('user_tags'):
                temp_model = main_models.FilePutUserTagsRequestUserTags()
                self.user_tags.append(temp_model.from_map(k1))

        return self

class FilePutUserTagsRequestUserTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the tag. The tag name cannot be empty and cannot contain number signs (#).
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag. The tag value cannot contain number signs (#).
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

