# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class UpdateStoryRequest(DaraModel):
    def __init__(
        self,
        cover: main_models.UpdateStoryRequestCover = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        object_id: str = None,
        project_name: str = None,
        story_name: str = None,
    ):
        # The cover image of the story.
        self.cover = cover
        # The custom ID.
        self.custom_id = custom_id
        # The custom tags. You can specify up to 100 custom tags.
        self.custom_labels = custom_labels
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
        if self.cover:
            self.cover.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

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
            temp_model = main_models.UpdateStoryRequestCover()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')

        return self

class UpdateStoryRequestCover(DaraModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # The URI of the cover image.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

