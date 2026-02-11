# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class ListServerlessTopNAppsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListServerlessTopNAppsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListServerlessTopNAppsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListServerlessTopNAppsResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        error: int = None,
        name: str = None,
        pid: str = None,
        region: str = None,
        rt: float = None,
    ):
        self.count = count
        self.error = error
        self.name = name
        self.pid = pid
        self.region = region
        self.rt = rt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.error is not None:
            result['Error'] = self.error

        if self.name is not None:
            result['Name'] = self.name

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region is not None:
            result['Region'] = self.region

        if self.rt is not None:
            result['Rt'] = self.rt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        return self

