# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class Story(DaraModel):
    def __init__(
        self,
        cover_file_id: str = None,
        cover_file_thumbnail_url: str = None,
        created_at: str = None,
        custom_labels: Dict[str, Any] = None,
        face_group_ids: List[str] = None,
        story_end_time: str = None,
        story_file_list: List[main_models.File] = None,
        story_id: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        updated_at: str = None,
    ):
        # The ID of the story cover file.
        self.cover_file_id = cover_file_id
        # The URL of thumbnail of the story cover file.
        self.cover_file_thumbnail_url = cover_file_thumbnail_url
        # The time when the story was created. The time follows the RFC3339 standard.
        self.created_at = created_at
        # The custom tags. You can specify key-value pairs based on your business requirements to search for stories by calling the FindStories operation.
        self.custom_labels = custom_labels
        # The information about face-based groups. This parameter is valid only if story_type is set to PeopleMemory. This parameter is invalid for stories of other types or custom stories.
        self.face_group_ids = face_group_ids
        # The time when the story ends. The time follows the RFC3339 standard.
        self.story_end_time = story_end_time
        # The story files.
        self.story_file_list = story_file_list
        # The story ID.
        self.story_id = story_id
        # The name of the story.
        self.story_name = story_name
        # The time when the story starts. The time follows the RFC3339 standard.
        self.story_start_time = story_start_time
        # The subtype of the story. It is specified when the story is created.
        self.story_sub_type = story_sub_type
        # The type of the story. It is specified when the story is created.
        self.story_type = story_type
        # The time when the story was updated. The time follows the RFC3339 standard.
        self.updated_at = updated_at

    def validate(self):
        if self.story_file_list:
            for v1 in self.story_file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id

        if self.cover_file_thumbnail_url is not None:
            result['cover_file_thumbnail_url'] = self.cover_file_thumbnail_url

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels

        if self.face_group_ids is not None:
            result['face_group_ids'] = self.face_group_ids

        if self.story_end_time is not None:
            result['story_end_time'] = self.story_end_time

        result['story_file_list'] = []
        if self.story_file_list is not None:
            for k1 in self.story_file_list:
                result['story_file_list'].append(k1.to_map() if k1 else None)

        if self.story_id is not None:
            result['story_id'] = self.story_id

        if self.story_name is not None:
            result['story_name'] = self.story_name

        if self.story_start_time is not None:
            result['story_start_time'] = self.story_start_time

        if self.story_sub_type is not None:
            result['story_sub_type'] = self.story_sub_type

        if self.story_type is not None:
            result['story_type'] = self.story_type

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')

        if m.get('cover_file_thumbnail_url') is not None:
            self.cover_file_thumbnail_url = m.get('cover_file_thumbnail_url')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')

        if m.get('face_group_ids') is not None:
            self.face_group_ids = m.get('face_group_ids')

        if m.get('story_end_time') is not None:
            self.story_end_time = m.get('story_end_time')

        self.story_file_list = []
        if m.get('story_file_list') is not None:
            for k1 in m.get('story_file_list'):
                temp_model = main_models.File()
                self.story_file_list.append(temp_model.from_map(k1))

        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')

        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')

        if m.get('story_start_time') is not None:
            self.story_start_time = m.get('story_start_time')

        if m.get('story_sub_type') is not None:
            self.story_sub_type = m.get('story_sub_type')

        if m.get('story_type') is not None:
            self.story_type = m.get('story_type')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

