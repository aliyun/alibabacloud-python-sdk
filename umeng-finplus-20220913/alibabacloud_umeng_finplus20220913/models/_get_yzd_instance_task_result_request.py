# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class GetYzdInstanceTaskResultRequest(DaraModel):
    def __init__(
        self,
        body: main_models.GetYzdInstanceTaskResultRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.GetYzdInstanceTaskResultRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class GetYzdInstanceTaskResultRequestBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        range_time_end_time: str = None,
        range_time_start_time: str = None,
    ):
        self.app_id = app_id
        self.range_time_end_time = range_time_end_time
        self.range_time_start_time = range_time_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.range_time_end_time is not None:
            result['rangeTimeEndTime'] = self.range_time_end_time

        if self.range_time_start_time is not None:
            result['rangeTimeStartTime'] = self.range_time_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('rangeTimeEndTime') is not None:
            self.range_time_end_time = m.get('rangeTimeEndTime')

        if m.get('rangeTimeStartTime') is not None:
            self.range_time_start_time = m.get('rangeTimeStartTime')

        return self

