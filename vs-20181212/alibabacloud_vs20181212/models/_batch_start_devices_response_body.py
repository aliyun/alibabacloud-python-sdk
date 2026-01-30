# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class BatchStartDevicesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.BatchStartDevicesResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.BatchStartDevicesResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class BatchStartDevicesResponseBodyResults(DaraModel):
    def __init__(
        self,
        id: str = None,
        streams: List[main_models.BatchStartDevicesResponseBodyResultsStreams] = None,
    ):
        self.id = id
        self.streams = streams

    def validate(self):
        if self.streams:
            for v1 in self.streams:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        result['Streams'] = []
        if self.streams is not None:
            for k1 in self.streams:
                result['Streams'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.streams = []
        if m.get('Streams') is not None:
            for k1 in m.get('Streams'):
                temp_model = main_models.BatchStartDevicesResponseBodyResultsStreams()
                self.streams.append(temp_model.from_map(k1))

        return self

class BatchStartDevicesResponseBodyResultsStreams(DaraModel):
    def __init__(
        self,
        error: str = None,
        id: str = None,
        name: str = None,
    ):
        self.error = error
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error is not None:
            result['Error'] = self.error

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

