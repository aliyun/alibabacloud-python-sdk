# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class UpdateStoryRequest(DaraModel):
    def __init__(
        self,
        cover: main_models.UpdateStoryRequestCover = None,
        custom_labels: Dict[str, str] = None,
        drive_id: str = None,
        story_id: str = None,
        story_name: str = None,
    ):
        self.cover = cover
        self.custom_labels = custom_labels
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.story_id = story_id
        self.story_name = story_name

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover is not None:
            result['cover'] = self.cover.to_map()

        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.story_id is not None:
            result['story_id'] = self.story_id

        if self.story_name is not None:
            result['story_name'] = self.story_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover') is not None:
            temp_model = main_models.UpdateStoryRequestCover()
            self.cover = temp_model.from_map(m.get('cover'))

        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')

        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')

        return self

class UpdateStoryRequestCover(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        revision_id: str = None,
    ):
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

