# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListTimedViewAttitudeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListTimedViewAttitudeResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListTimedViewAttitudeResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTimedViewAttitudeResponseBodyData(DaraModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        pub_time: str = None,
        ratio: str = None,
        source: str = None,
        title: str = None,
        url: str = None,
        view_points: List[main_models.ListTimedViewAttitudeResponseBodyDataViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.pub_time = pub_time
        self.ratio = ratio
        self.source = source
        self.title = title
        self.url = url
        self.view_points = view_points

    def validate(self):
        if self.view_points:
            for v1 in self.view_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attitude is not None:
            result['Attitude'] = self.attitude

        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        result['ViewPoints'] = []
        if self.view_points is not None:
            for k1 in self.view_points:
                result['ViewPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')

        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k1 in m.get('ViewPoints'):
                temp_model = main_models.ListTimedViewAttitudeResponseBodyDataViewPoints()
                self.view_points.append(temp_model.from_map(k1))

        return self

class ListTimedViewAttitudeResponseBodyDataViewPoints(DaraModel):
    def __init__(
        self,
        outlines: List[main_models.ListTimedViewAttitudeResponseBodyDataViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.point is not None:
            result['Point'] = self.point

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.ListTimedViewAttitudeResponseBodyDataViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class ListTimedViewAttitudeResponseBodyDataViewPointsOutlines(DaraModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outline is not None:
            result['Outline'] = self.outline

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

