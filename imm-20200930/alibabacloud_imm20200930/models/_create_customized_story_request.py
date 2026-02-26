# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateCustomizedStoryRequest(DaraModel):
    def __init__(
        self,
        cover: main_models.CreateCustomizedStoryRequestCover = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        files: List[main_models.CreateCustomizedStoryRequestFiles] = None,
        project_name: str = None,
        story_name: str = None,
        story_sub_type: str = None,
        story_type: str = None,
    ):
        # The cover image of the story. You can specify an image as the cover image of the custom story.
        # 
        # This parameter is required.
        self.cover = cover
        # The custom labels. You can specify labels to help you identify and retrieve the story.
        self.custom_labels = custom_labels
        # The name of the dataset.[](~~478160~~)
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The files of the story. You can specify up to 100 files in a custom story.
        # 
        # This parameter is required.
        self.files = files
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
        if self.cover:
            self.cover.validate()
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.CreateCustomizedStoryRequestCover()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.CreateCustomizedStoryRequestFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')

        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')

        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')

        return self

class CreateCustomizedStoryRequestFiles(DaraModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # The URIs of the files.
        # 
        # This parameter is required.
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

class CreateCustomizedStoryRequestCover(DaraModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # The URI of the cover image.
        # 
        # This parameter is required.
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

