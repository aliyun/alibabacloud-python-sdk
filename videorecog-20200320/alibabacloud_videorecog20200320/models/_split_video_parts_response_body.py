# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_videorecog20200320 import models as main_models
from darabonba.model import DaraModel

class SplitVideoPartsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SplitVideoPartsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SplitVideoPartsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SplitVideoPartsResponseBodyData(DaraModel):
    def __init__(
        self,
        elements: List[main_models.SplitVideoPartsResponseBodyDataElements] = None,
        split_video_part_results: List[main_models.SplitVideoPartsResponseBodyDataSplitVideoPartResults] = None,
    ):
        self.elements = elements
        self.split_video_part_results = split_video_part_results

    def validate(self):
        if self.elements:
            for v1 in self.elements:
                 if v1:
                    v1.validate()
        if self.split_video_part_results:
            for v1 in self.split_video_part_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Elements'] = []
        if self.elements is not None:
            for k1 in self.elements:
                result['Elements'].append(k1.to_map() if k1 else None)

        result['SplitVideoPartResults'] = []
        if self.split_video_part_results is not None:
            for k1 in self.split_video_part_results:
                result['SplitVideoPartResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.elements = []
        if m.get('Elements') is not None:
            for k1 in m.get('Elements'):
                temp_model = main_models.SplitVideoPartsResponseBodyDataElements()
                self.elements.append(temp_model.from_map(k1))

        self.split_video_part_results = []
        if m.get('SplitVideoPartResults') is not None:
            for k1 in m.get('SplitVideoPartResults'):
                temp_model = main_models.SplitVideoPartsResponseBodyDataSplitVideoPartResults()
                self.split_video_part_results.append(temp_model.from_map(k1))

        return self

class SplitVideoPartsResponseBodyDataSplitVideoPartResults(DaraModel):
    def __init__(
        self,
        begin_time: float = None,
        by: str = None,
        end_time: float = None,
        theme: str = None,
        type: str = None,
    ):
        self.begin_time = begin_time
        self.by = by
        self.end_time = end_time
        self.theme = theme
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.by is not None:
            result['By'] = self.by

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.theme is not None:
            result['Theme'] = self.theme

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('By') is not None:
            self.by = m.get('By')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Theme') is not None:
            self.theme = m.get('Theme')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SplitVideoPartsResponseBodyDataElements(DaraModel):
    def __init__(
        self,
        begin_time: float = None,
        end_time: float = None,
        index: int = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.index = index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.index is not None:
            result['Index'] = self.index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        return self

