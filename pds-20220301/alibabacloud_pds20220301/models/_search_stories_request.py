# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class SearchStoriesRequest(DaraModel):
    def __init__(
        self,
        cover_image_thumbnail_process: str = None,
        cover_video_thumbnail_process: str = None,
        create_time_range: main_models.SearchStoriesRequestCreateTimeRange = None,
        custom_labels: str = None,
        drive_id: str = None,
        face_group_ids: List[str] = None,
        limit: int = None,
        marker: str = None,
        order: str = None,
        sort: str = None,
        story_end_time_range: main_models.SearchStoriesRequestStoryEndTimeRange = None,
        story_id: str = None,
        story_name: str = None,
        story_start_time_range: main_models.SearchStoriesRequestStoryStartTimeRange = None,
        story_type: str = None,
        url_expire_sec: int = None,
        with_empty_stories: bool = None,
    ):
        self.cover_image_thumbnail_process = cover_image_thumbnail_process
        self.cover_video_thumbnail_process = cover_video_thumbnail_process
        self.create_time_range = create_time_range
        self.custom_labels = custom_labels
        # This parameter is required.
        self.drive_id = drive_id
        self.face_group_ids = face_group_ids
        self.limit = limit
        self.marker = marker
        self.order = order
        self.sort = sort
        self.story_end_time_range = story_end_time_range
        self.story_id = story_id
        self.story_name = story_name
        self.story_start_time_range = story_start_time_range
        self.story_type = story_type
        self.url_expire_sec = url_expire_sec
        self.with_empty_stories = with_empty_stories

    def validate(self):
        if self.create_time_range:
            self.create_time_range.validate()
        if self.story_end_time_range:
            self.story_end_time_range.validate()
        if self.story_start_time_range:
            self.story_start_time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_image_thumbnail_process is not None:
            result['cover_image_thumbnail_process'] = self.cover_image_thumbnail_process

        if self.cover_video_thumbnail_process is not None:
            result['cover_video_thumbnail_process'] = self.cover_video_thumbnail_process

        if self.create_time_range is not None:
            result['create_time_range'] = self.create_time_range.to_map()

        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.face_group_ids is not None:
            result['face_group_ids'] = self.face_group_ids

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.order is not None:
            result['order'] = self.order

        if self.sort is not None:
            result['sort'] = self.sort

        if self.story_end_time_range is not None:
            result['story_end_time_range'] = self.story_end_time_range.to_map()

        if self.story_id is not None:
            result['story_id'] = self.story_id

        if self.story_name is not None:
            result['story_name'] = self.story_name

        if self.story_start_time_range is not None:
            result['story_start_time_range'] = self.story_start_time_range.to_map()

        if self.story_type is not None:
            result['story_type'] = self.story_type

        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec

        if self.with_empty_stories is not None:
            result['with_empty_stories'] = self.with_empty_stories

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_image_thumbnail_process') is not None:
            self.cover_image_thumbnail_process = m.get('cover_image_thumbnail_process')

        if m.get('cover_video_thumbnail_process') is not None:
            self.cover_video_thumbnail_process = m.get('cover_video_thumbnail_process')

        if m.get('create_time_range') is not None:
            temp_model = main_models.SearchStoriesRequestCreateTimeRange()
            self.create_time_range = temp_model.from_map(m.get('create_time_range'))

        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('face_group_ids') is not None:
            self.face_group_ids = m.get('face_group_ids')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('sort') is not None:
            self.sort = m.get('sort')

        if m.get('story_end_time_range') is not None:
            temp_model = main_models.SearchStoriesRequestStoryEndTimeRange()
            self.story_end_time_range = temp_model.from_map(m.get('story_end_time_range'))

        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')

        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')

        if m.get('story_start_time_range') is not None:
            temp_model = main_models.SearchStoriesRequestStoryStartTimeRange()
            self.story_start_time_range = temp_model.from_map(m.get('story_start_time_range'))

        if m.get('story_type') is not None:
            self.story_type = m.get('story_type')

        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')

        if m.get('with_empty_stories') is not None:
            self.with_empty_stories = m.get('with_empty_stories')

        return self

class SearchStoriesRequestStoryStartTimeRange(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['end'] = self.end

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

class SearchStoriesRequestStoryEndTimeRange(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['end'] = self.end

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

class SearchStoriesRequestCreateTimeRange(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['end'] = self.end

        if self.start is not None:
            result['start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('start') is not None:
            self.start = m.get('start')

        return self

