# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SearchMediaClipByFaceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        media_clip_list: List[main_models.SearchMediaClipByFaceResponseBodyMediaClipList] = None,
        request_id: str = None,
        success: str = None,
        total: int = None,
    ):
        # The status code returned.
        self.code = code
        # The media asset clips that meet the requirements.
        self.media_clip_list = media_clip_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
        self.success = success
        # The total number of media asset clips that meet the conditions.
        self.total = total

    def validate(self):
        if self.media_clip_list:
            for v1 in self.media_clip_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['MediaClipList'] = []
        if self.media_clip_list is not None:
            for k1 in self.media_clip_list:
                result['MediaClipList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.media_clip_list = []
        if m.get('MediaClipList') is not None:
            for k1 in m.get('MediaClipList'):
                temp_model = main_models.SearchMediaClipByFaceResponseBodyMediaClipList()
                self.media_clip_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class SearchMediaClipByFaceResponseBodyMediaClipList(DaraModel):
    def __init__(
        self,
        category: str = None,
        entity_id: str = None,
        label_name: str = None,
        occurrences_infos: List[main_models.SearchMediaClipByFaceResponseBodyMediaClipListOccurrencesInfos] = None,
        score: float = None,
    ):
        # The type of the character. Valid values: celebrity sensitive politician custom unknown
        self.category = category
        # The ID of the entity, which is the same as the entity ID returned in tag analysis.
        self.entity_id = entity_id
        # The name of the entity.
        self.label_name = label_name
        # The information about clips related to the face.
        self.occurrences_infos = occurrences_infos
        # The score of the clip. The value is of the Float type. The value is in the range of [0,1].
        self.score = score

    def validate(self):
        if self.occurrences_infos:
            for v1 in self.occurrences_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.label_name is not None:
            result['LabelName'] = self.label_name

        result['OccurrencesInfos'] = []
        if self.occurrences_infos is not None:
            for k1 in self.occurrences_infos:
                result['OccurrencesInfos'].append(k1.to_map() if k1 else None)

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')

        self.occurrences_infos = []
        if m.get('OccurrencesInfos') is not None:
            for k1 in m.get('OccurrencesInfos'):
                temp_model = main_models.SearchMediaClipByFaceResponseBodyMediaClipListOccurrencesInfos()
                self.occurrences_infos.append(temp_model.from_map(k1))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

class SearchMediaClipByFaceResponseBodyMediaClipListOccurrencesInfos(DaraModel):
    def __init__(
        self,
        end_time: float = None,
        expression: str = None,
        start_time: float = None,
        track_data: List[main_models.SearchMediaClipByFaceResponseBodyMediaClipListOccurrencesInfosTrackData] = None,
    ):
        # The end time of the clip. Unit: seconds. The value is of the Float type.
        self.end_time = end_time
        self.expression = expression
        # The start time of the clip. Unit: seconds. The value is of the Float type.
        self.start_time = start_time
        # The information about the face in the clip.
        self.track_data = track_data

    def validate(self):
        if self.track_data:
            for v1 in self.track_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['TrackData'] = []
        if self.track_data is not None:
            for k1 in self.track_data:
                result['TrackData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.track_data = []
        if m.get('TrackData') is not None:
            for k1 in m.get('TrackData'):
                temp_model = main_models.SearchMediaClipByFaceResponseBodyMediaClipListOccurrencesInfosTrackData()
                self.track_data.append(temp_model.from_map(k1))

        return self

class SearchMediaClipByFaceResponseBodyMediaClipListOccurrencesInfosTrackData(DaraModel):
    def __init__(
        self,
        box_position: main_models.SearchMediaClipByFaceResponseBodyMediaClipListOccurrencesInfosTrackDataBoxPosition = None,
        timestamp: float = None,
    ):
        # The coordinates of the face.
        self.box_position = box_position
        # The timestamp when the face appears in the clip. Unit: seconds. The value is of the Float type.
        self.timestamp = timestamp

    def validate(self):
        if self.box_position:
            self.box_position.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.box_position is not None:
            result['BoxPosition'] = self.box_position.to_map()

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoxPosition') is not None:
            temp_model = main_models.SearchMediaClipByFaceResponseBodyMediaClipListOccurrencesInfosTrackDataBoxPosition()
            self.box_position = temp_model.from_map(m.get('BoxPosition'))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class SearchMediaClipByFaceResponseBodyMediaClipListOccurrencesInfosTrackDataBoxPosition(DaraModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        # The height of the rectangle frame. Unit: pixels.
        self.h = h
        # The width of the rectangle frame. Unit: pixels.
        self.w = w
        # The x-axis coordinate of the upper-left corner. Unit: pixels.
        self.x = x
        # The y-axis coordinate of the upper-left corner. Unit: pixels.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.h is not None:
            result['H'] = self.h

        if self.w is not None:
            result['W'] = self.w

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')

        if m.get('W') is not None:
            self.w = m.get('W')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

