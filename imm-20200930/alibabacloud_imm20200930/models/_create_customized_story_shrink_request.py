# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomizedStoryShrinkRequest(DaraModel):
    def __init__(
        self,
        cover_shrink: str = None,
        custom_labels_shrink: str = None,
        dataset_name: str = None,
        files_shrink: str = None,
        project_name: str = None,
        story_name: str = None,
        story_sub_type: str = None,
        story_type: str = None,
    ):
        # The cover image of the story. You can specify an image as the cover image of the custom story.
        # 
        # This parameter is required.
        self.cover_shrink = cover_shrink
        # The custom labels. You can specify labels to help you identify and retrieve the story.
        self.custom_labels_shrink = custom_labels_shrink
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The files of the story. You can specify up to 100 files in a custom story.
        # 
        # This parameter is required.
        self.files_shrink = files_shrink
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The name of the story.
        # 
        # This parameter is required.
        self.story_name = story_name
        # The subtype of the story. For information about valid subtypes, see [Story types and subtypes](https://help.aliyun.com/document_detail/2743998.html).
        # 
        # This parameter is required.
        self.story_sub_type = story_sub_type
        # The type of the story. For information about valid types, see [Story types and subtypes](https://help.aliyun.com/document_detail/2743998.html).
        # 
        # This parameter is required.
        self.story_type = story_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_shrink is not None:
            result['Cover'] = self.cover_shrink

        if self.custom_labels_shrink is not None:
            result['CustomLabels'] = self.custom_labels_shrink

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.files_shrink is not None:
            result['Files'] = self.files_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.story_name is not None:
            result['StoryName'] = self.story_name

        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type

        if self.story_type is not None:
            result['StoryType'] = self.story_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cover') is not None:
            self.cover_shrink = m.get('Cover')

        if m.get('CustomLabels') is not None:
            self.custom_labels_shrink = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')

        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')

        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')

        return self

