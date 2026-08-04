# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListSubAlbumResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ListSubAlbumResponseBodyResult = None,
    ):
        # Status code
        self.code = code
        # Additional information
        self.message = message
        # Request ID
        self.request_id = request_id
        # Result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListSubAlbumResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListSubAlbumResponseBodyResult(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.ListSubAlbumResponseBodyResultDataList] = None,
        has_next: bool = None,
        total_count: int = None,
        total_page_count: int = None,
    ):
        # Album List
        self.data_list = data_list
        # Indicates whether there is a next page.
        self.has_next = has_next
        # total number of entries
        self.total_count = total_count
        # Total number of pages
        self.total_page_count = total_page_count

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.ListSubAlbumResponseBodyResultDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')

        return self

class ListSubAlbumResponseBodyResultDataList(DaraModel):
    def __init__(
        self,
        album_id: str = None,
        category_id: int = None,
        cover_url: str = None,
        id: int = None,
        is_added: bool = None,
        schedule_info: main_models.ListSubAlbumResponseBodyResultDataListScheduleInfo = None,
        sequence: int = None,
        title: str = None,
        total_episode: int = None,
    ):
        # Album ID
        self.album_id = album_id
        # Album category ID
        self.category_id = category_id
        # Album thumbnail
        self.cover_url = cover_url
        # Record ID
        self.id = id
        # Is subscribed
        self.is_added = is_added
        # Schedule information
        self.schedule_info = schedule_info
        # Sorting
        self.sequence = sequence
        # Album title
        self.title = title
        # Total number of episodes
        self.total_episode = total_episode

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.album_id is not None:
            result['AlbumId'] = self.album_id

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.id is not None:
            result['Id'] = self.id

        if self.is_added is not None:
            result['IsAdded'] = self.is_added

        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.title is not None:
            result['Title'] = self.title

        if self.total_episode is not None:
            result['TotalEpisode'] = self.total_episode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsAdded') is not None:
            self.is_added = m.get('IsAdded')

        if m.get('ScheduleInfo') is not None:
            temp_model = main_models.ListSubAlbumResponseBodyResultDataListScheduleInfo()
            self.schedule_info = temp_model.from_map(m.get('ScheduleInfo'))

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TotalEpisode') is not None:
            self.total_episode = m.get('TotalEpisode')

        return self

class ListSubAlbumResponseBodyResultDataListScheduleInfo(DaraModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
        schedule_id: int = None,
    ):
        # trigger epoch
        self.days_of_week = days_of_week
        # trigger hour
        self.hour = hour
        # trigger minute
        self.minute = minute
        # scheduled task ID
        self.schedule_id = schedule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week

        if self.hour is not None:
            result['Hour'] = self.hour

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')

        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')

        return self

