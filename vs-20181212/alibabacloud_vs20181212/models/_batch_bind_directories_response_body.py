# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class BatchBindDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.BatchBindDirectoriesResponseBodyResults] = None,
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
                temp_model = main_models.BatchBindDirectoriesResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class BatchBindDirectoriesResponseBodyResults(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        directory_id: str = None,
        error: str = None,
    ):
        self.device_id = device_id
        self.directory_id = directory_id
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.error is not None:
            result['Error'] = self.error

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        return self

