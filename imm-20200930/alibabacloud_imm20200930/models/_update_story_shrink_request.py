# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateStoryShrinkRequest(DaraModel):
    def __init__(
        self,
        cover_shrink: str = None,
        custom_id: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_name: str = None,
    ):
        # The cover image of the story.
        self.cover_shrink = cover_shrink
        # The custom ID.
        self.custom_id = custom_id
        # The custom tags. You can specify up to 100 custom tags.
        self.custom_labels_shrink = custom_labels_shrink
        # The name of the dataset.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The ID of the story.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The name of the project.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The name of the story.
        self.story_name = story_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_shrink is not None:
            result['Cover'] = self.cover_shrink

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.story_name is not None:
            result['StoryName'] = self.story_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            self.cover_shrink = m.get('Cover')

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')

        return self

