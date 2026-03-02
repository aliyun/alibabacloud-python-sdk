# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetTpsByTimeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetTpsByTimeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTpsByTimeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTpsByTimeResponseBodyData(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        max_tps: int = None,
        start_time: int = None,
        tps_list: List[int] = None,
    ):
        self.end_time = end_time
        self.max_tps = max_tps
        self.start_time = start_time
        self.tps_list = tps_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tps_list is not None:
            result['tpsList'] = self.tps_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('tpsList') is not None:
            self.tps_list = m.get('tpsList')

        return self

