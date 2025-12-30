# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class DescribeMeterImsEditUsageResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeMeterImsEditUsageResponseBodyData] = None,
        request_id: str = None,
    ):
        # The usage statistics of IMS on VOD editing.
        self.data = data
        # The request ID.
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
                temp_model = main_models.DescribeMeterImsEditUsageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMeterImsEditUsageResponseBodyData(DaraModel):
    def __init__(
        self,
        duration: int = None,
        profile: str = None,
        time: int = None,
    ):
        # The usage duration, in minutes.
        self.duration = duration
        # The video profile.
        self.profile = profile
        # The beginning time of usage. The value is a 10-digit timestamp.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

