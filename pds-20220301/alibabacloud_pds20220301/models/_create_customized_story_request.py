# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CreateCustomizedStoryRequest(DaraModel):
    def __init__(
        self,
        custom_labels: Dict[str, str] = None,
        drive_id: str = None,
        story_cover: main_models.CreateCustomizedStoryRequestStoryCover = None,
        story_files: List[main_models.CreateCustomizedStoryRequestStoryFiles] = None,
        story_name: str = None,
        story_sub_type: str = None,
        story_type: str = None,
    ):
        self.custom_labels = custom_labels
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.story_cover = story_cover
        # This parameter is required.
        self.story_files = story_files
        # This parameter is required.
        self.story_name = story_name
        # This parameter is required.
        self.story_sub_type = story_sub_type
        # This parameter is required.
        self.story_type = story_type

    def validate(self):
        if self.story_cover:
            self.story_cover.validate()
        if self.story_files:
            for v1 in self.story_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.story_cover is not None:
            result['story_cover'] = self.story_cover.to_map()

        result['story_files'] = []
        if self.story_files is not None:
            for k1 in self.story_files:
                result['story_files'].append(k1.to_map() if k1 else None)

        if self.story_name is not None:
            result['story_name'] = self.story_name

        if self.story_sub_type is not None:
            result['story_sub_type'] = self.story_sub_type

        if self.story_type is not None:
            result['story_type'] = self.story_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('story_cover') is not None:
            temp_model = main_models.CreateCustomizedStoryRequestStoryCover()
            self.story_cover = temp_model.from_map(m.get('story_cover'))

        self.story_files = []
        if m.get('story_files') is not None:
            for k1 in m.get('story_files'):
                temp_model = main_models.CreateCustomizedStoryRequestStoryFiles()
                self.story_files.append(temp_model.from_map(k1))

        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')

        if m.get('story_sub_type') is not None:
            self.story_sub_type = m.get('story_sub_type')

        if m.get('story_type') is not None:
            self.story_type = m.get('story_type')

        return self

class CreateCustomizedStoryRequestStoryFiles(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        revision_id: str = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        return self

class CreateCustomizedStoryRequestStoryCover(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        revision_id: str = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.revision_id is not None:
            result['revision_id'] = self.revision_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')

        return self

