# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class AddStoryFilesResponseBody(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        files: List[main_models.AddStoryFile] = None,
        request_id: str = None,
        story_id: str = None,
    ):
        self.drive_id = drive_id
        self.files = files
        self.request_id = request_id
        self.story_id = story_id

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        result['files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['files'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.story_id is not None:
            result['story_id'] = self.story_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        self.files = []
        if m.get('files') is not None:
            for k1 in m.get('files'):
                temp_model = main_models.AddStoryFile()
                self.files.append(temp_model.from_map(k1))

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')

        return self

