# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Story(DaraModel):
    def __init__(
        self,
        addresses: List[main_models.Address] = None,
        cover: main_models.File = None,
        create_time: str = None,
        custom_id: str = None,
        custom_labels: Dict[str, Any] = None,
        dataset_name: str = None,
        figure_cluster_ids: List[str] = None,
        files: List[main_models.File] = None,
        object_id: str = None,
        object_type: str = None,
        owner_id: str = None,
        project_name: str = None,
        story_end_time: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        update_time: str = None,
    ):
        # The addresses.
        self.addresses = addresses
        # The story cover.
        self.cover = cover
        # The time when the story was created.
        self.create_time = create_time
        # The custom ID.
        self.custom_id = custom_id
        # The custom labels.
        self.custom_labels = custom_labels
        # The name of the dataset.
        self.dataset_name = dataset_name
        # The fluster IDs.
        self.figure_cluster_ids = figure_cluster_ids
        # The story files.
        self.files = files
        # The ID of the story object.
        self.object_id = object_id
        # The type of the object.
        self.object_type = object_type
        # The ID of the owner to which the story belongs.
        self.owner_id = owner_id
        # The name of the project.
        self.project_name = project_name
        # The time when the story ends.
        self.story_end_time = story_end_time
        # The name of the story.
        self.story_name = story_name
        # The time when the story starts.
        self.story_start_time = story_start_time
        # The subtype of the story.
        self.story_sub_type = story_sub_type
        # The story type.
        self.story_type = story_type
        # The time when the story was updated.
        self.update_time = update_time

    def validate(self):
        if self.addresses:
            for v1 in self.addresses:
                 if v1:
                    v1.validate()
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
        result['Addresses'] = []
        if self.addresses is not None:
            for k1 in self.addresses:
                result['Addresses'].append(k1.to_map() if k1 else None)

        if self.cover is not None:
            result['Cover'] = self.cover.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_id is not None:
            result['CustomId'] = self.custom_id

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.figure_cluster_ids is not None:
            result['FigureClusterIds'] = self.figure_cluster_ids

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.story_end_time is not None:
            result['StoryEndTime'] = self.story_end_time

        if self.story_name is not None:
            result['StoryName'] = self.story_name

        if self.story_start_time is not None:
            result['StoryStartTime'] = self.story_start_time

        if self.story_sub_type is not None:
            result['StorySubType'] = self.story_sub_type

        if self.story_type is not None:
            result['StoryType'] = self.story_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addresses = []
        if m.get('Addresses') is not None:
            for k1 in m.get('Addresses'):
                temp_model = main_models.Address()
                self.addresses.append(temp_model.from_map(k1))

        if m.get('Cover') is not None:
            temp_model = main_models.File()
            self.cover = temp_model.from_map(m.get('Cover'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomId') is not None:
            self.custom_id = m.get('CustomId')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('FigureClusterIds') is not None:
            self.figure_cluster_ids = m.get('FigureClusterIds')

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.File()
                self.files.append(temp_model.from_map(k1))

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('StoryEndTime') is not None:
            self.story_end_time = m.get('StoryEndTime')

        if m.get('StoryName') is not None:
            self.story_name = m.get('StoryName')

        if m.get('StoryStartTime') is not None:
            self.story_start_time = m.get('StoryStartTime')

        if m.get('StorySubType') is not None:
            self.story_sub_type = m.get('StorySubType')

        if m.get('StoryType') is not None:
            self.story_type = m.get('StoryType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

