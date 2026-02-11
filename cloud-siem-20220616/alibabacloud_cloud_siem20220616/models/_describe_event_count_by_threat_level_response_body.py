# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeEventCountByThreatLevelResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeEventCountByThreatLevelResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.DescribeEventCountByThreatLevelResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeEventCountByThreatLevelResponseBodyData(DaraModel):
    def __init__(
        self,
        event_daily_num: List[main_models.DescribeEventCountByThreatLevelResponseBodyDataEventDailyNum] = None,
        event_num: int = None,
        high_level_event_num: int = None,
        info_level_event_num: int = None,
        low_level_event_num: int = None,
        medium_level_event_num: int = None,
        serious_level_event_num: int = None,
        undeal_event_num: int = None,
    ):
        self.event_daily_num = event_daily_num
        # The total number of events.
        self.event_num = event_num
        # The number of high-risk events.
        self.high_level_event_num = high_level_event_num
        self.info_level_event_num = info_level_event_num
        # The number of low-risk events.
        self.low_level_event_num = low_level_event_num
        # The number of medium-risk events.
        self.medium_level_event_num = medium_level_event_num
        self.serious_level_event_num = serious_level_event_num
        # The number of unhandled events.
        self.undeal_event_num = undeal_event_num

    def validate(self):
        if self.event_daily_num:
            for v1 in self.event_daily_num:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventDailyNum'] = []
        if self.event_daily_num is not None:
            for k1 in self.event_daily_num:
                result['EventDailyNum'].append(k1.to_map() if k1 else None)

        if self.event_num is not None:
            result['EventNum'] = self.event_num

        if self.high_level_event_num is not None:
            result['HighLevelEventNum'] = self.high_level_event_num

        if self.info_level_event_num is not None:
            result['InfoLevelEventNum'] = self.info_level_event_num

        if self.low_level_event_num is not None:
            result['LowLevelEventNum'] = self.low_level_event_num

        if self.medium_level_event_num is not None:
            result['MediumLevelEventNum'] = self.medium_level_event_num

        if self.serious_level_event_num is not None:
            result['SeriousLevelEventNum'] = self.serious_level_event_num

        if self.undeal_event_num is not None:
            result['UndealEventNum'] = self.undeal_event_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_daily_num = []
        if m.get('EventDailyNum') is not None:
            for k1 in m.get('EventDailyNum'):
                temp_model = main_models.DescribeEventCountByThreatLevelResponseBodyDataEventDailyNum()
                self.event_daily_num.append(temp_model.from_map(k1))

        if m.get('EventNum') is not None:
            self.event_num = m.get('EventNum')

        if m.get('HighLevelEventNum') is not None:
            self.high_level_event_num = m.get('HighLevelEventNum')

        if m.get('InfoLevelEventNum') is not None:
            self.info_level_event_num = m.get('InfoLevelEventNum')

        if m.get('LowLevelEventNum') is not None:
            self.low_level_event_num = m.get('LowLevelEventNum')

        if m.get('MediumLevelEventNum') is not None:
            self.medium_level_event_num = m.get('MediumLevelEventNum')

        if m.get('SeriousLevelEventNum') is not None:
            self.serious_level_event_num = m.get('SeriousLevelEventNum')

        if m.get('UndealEventNum') is not None:
            self.undeal_event_num = m.get('UndealEventNum')

        return self

class DescribeEventCountByThreatLevelResponseBodyDataEventDailyNum(DaraModel):
    def __init__(
        self,
        date: str = None,
        event_num: int = None,
        undeal_event_num: int = None,
    ):
        self.date = date
        self.event_num = event_num
        self.undeal_event_num = undeal_event_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.event_num is not None:
            result['EventNum'] = self.event_num

        if self.undeal_event_num is not None:
            result['UndealEventNum'] = self.undeal_event_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('EventNum') is not None:
            self.event_num = m.get('EventNum')

        if m.get('UndealEventNum') is not None:
            self.undeal_event_num = m.get('UndealEventNum')

        return self

