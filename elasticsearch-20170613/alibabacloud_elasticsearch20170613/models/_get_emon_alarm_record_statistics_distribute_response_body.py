# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class GetEmonAlarmRecordStatisticsDistributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetEmonAlarmRecordStatisticsDistributeResponseBodyResult(DaraModel):
    def __init__(
        self,
        alarm_group: str = None,
        alarm_group_total: List[main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultAlarmGroupTotal] = None,
        channel_total: List[main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultChannelTotal] = None,
        count: int = None,
        level_total: List[main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultLevelTotal] = None,
        receiver_total: List[main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultReceiverTotal] = None,
        statistics: List[main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultStatistics] = None,
    ):
        self.alarm_group = alarm_group
        self.alarm_group_total = alarm_group_total
        self.channel_total = channel_total
        self.count = count
        self.level_total = level_total
        self.receiver_total = receiver_total
        self.statistics = statistics

    def validate(self):
        if self.alarm_group_total:
            for v1 in self.alarm_group_total:
                 if v1:
                    v1.validate()
        if self.channel_total:
            for v1 in self.channel_total:
                 if v1:
                    v1.validate()
        if self.level_total:
            for v1 in self.level_total:
                 if v1:
                    v1.validate()
        if self.receiver_total:
            for v1 in self.receiver_total:
                 if v1:
                    v1.validate()
        if self.statistics:
            for v1 in self.statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_group is not None:
            result['alarmGroup'] = self.alarm_group

        result['alarmGroupTotal'] = []
        if self.alarm_group_total is not None:
            for k1 in self.alarm_group_total:
                result['alarmGroupTotal'].append(k1.to_map() if k1 else None)

        result['channelTotal'] = []
        if self.channel_total is not None:
            for k1 in self.channel_total:
                result['channelTotal'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['count'] = self.count

        result['levelTotal'] = []
        if self.level_total is not None:
            for k1 in self.level_total:
                result['levelTotal'].append(k1.to_map() if k1 else None)

        result['receiverTotal'] = []
        if self.receiver_total is not None:
            for k1 in self.receiver_total:
                result['receiverTotal'].append(k1.to_map() if k1 else None)

        result['statistics'] = []
        if self.statistics is not None:
            for k1 in self.statistics:
                result['statistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmGroup') is not None:
            self.alarm_group = m.get('alarmGroup')

        self.alarm_group_total = []
        if m.get('alarmGroupTotal') is not None:
            for k1 in m.get('alarmGroupTotal'):
                temp_model = main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultAlarmGroupTotal()
                self.alarm_group_total.append(temp_model.from_map(k1))

        self.channel_total = []
        if m.get('channelTotal') is not None:
            for k1 in m.get('channelTotal'):
                temp_model = main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultChannelTotal()
                self.channel_total.append(temp_model.from_map(k1))

        if m.get('count') is not None:
            self.count = m.get('count')

        self.level_total = []
        if m.get('levelTotal') is not None:
            for k1 in m.get('levelTotal'):
                temp_model = main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultLevelTotal()
                self.level_total.append(temp_model.from_map(k1))

        self.receiver_total = []
        if m.get('receiverTotal') is not None:
            for k1 in m.get('receiverTotal'):
                temp_model = main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultReceiverTotal()
                self.receiver_total.append(temp_model.from_map(k1))

        self.statistics = []
        if m.get('statistics') is not None:
            for k1 in m.get('statistics'):
                temp_model = main_models.GetEmonAlarmRecordStatisticsDistributeResponseBodyResultStatistics()
                self.statistics.append(temp_model.from_map(k1))

        return self

class GetEmonAlarmRecordStatisticsDistributeResponseBodyResultStatistics(DaraModel):
    def __init__(
        self,
        alarm_group: str = None,
        compare: str = None,
        count: int = None,
        level: str = None,
        receiver: str = None,
        time: int = None,
        today: int = None,
        type: str = None,
        yesterday: int = None,
    ):
        self.alarm_group = alarm_group
        self.compare = compare
        self.count = count
        self.level = level
        self.receiver = receiver
        self.time = time
        self.today = today
        self.type = type
        self.yesterday = yesterday

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_group is not None:
            result['alarmGroup'] = self.alarm_group

        if self.compare is not None:
            result['compare'] = self.compare

        if self.count is not None:
            result['count'] = self.count

        if self.level is not None:
            result['level'] = self.level

        if self.receiver is not None:
            result['receiver'] = self.receiver

        if self.time is not None:
            result['time'] = self.time

        if self.today is not None:
            result['today'] = self.today

        if self.type is not None:
            result['type'] = self.type

        if self.yesterday is not None:
            result['yesterday'] = self.yesterday

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmGroup') is not None:
            self.alarm_group = m.get('alarmGroup')

        if m.get('compare') is not None:
            self.compare = m.get('compare')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('receiver') is not None:
            self.receiver = m.get('receiver')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('today') is not None:
            self.today = m.get('today')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('yesterday') is not None:
            self.yesterday = m.get('yesterday')

        return self

class GetEmonAlarmRecordStatisticsDistributeResponseBodyResultReceiverTotal(DaraModel):
    def __init__(
        self,
        alarm_group: str = None,
        compare: str = None,
        count: int = None,
        level: str = None,
        receiver: str = None,
        time: int = None,
        today: int = None,
        type: str = None,
        yesterday: int = None,
    ):
        self.alarm_group = alarm_group
        self.compare = compare
        self.count = count
        self.level = level
        self.receiver = receiver
        self.time = time
        self.today = today
        self.type = type
        self.yesterday = yesterday

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_group is not None:
            result['alarmGroup'] = self.alarm_group

        if self.compare is not None:
            result['compare'] = self.compare

        if self.count is not None:
            result['count'] = self.count

        if self.level is not None:
            result['level'] = self.level

        if self.receiver is not None:
            result['receiver'] = self.receiver

        if self.time is not None:
            result['time'] = self.time

        if self.today is not None:
            result['today'] = self.today

        if self.type is not None:
            result['type'] = self.type

        if self.yesterday is not None:
            result['yesterday'] = self.yesterday

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmGroup') is not None:
            self.alarm_group = m.get('alarmGroup')

        if m.get('compare') is not None:
            self.compare = m.get('compare')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('receiver') is not None:
            self.receiver = m.get('receiver')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('today') is not None:
            self.today = m.get('today')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('yesterday') is not None:
            self.yesterday = m.get('yesterday')

        return self

class GetEmonAlarmRecordStatisticsDistributeResponseBodyResultLevelTotal(DaraModel):
    def __init__(
        self,
        alarm_group: str = None,
        compare: str = None,
        count: int = None,
        level: str = None,
        receiver: str = None,
        time: int = None,
        today: int = None,
        type: str = None,
        yesterday: int = None,
    ):
        self.alarm_group = alarm_group
        self.compare = compare
        self.count = count
        self.level = level
        self.receiver = receiver
        self.time = time
        self.today = today
        self.type = type
        self.yesterday = yesterday

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_group is not None:
            result['alarmGroup'] = self.alarm_group

        if self.compare is not None:
            result['compare'] = self.compare

        if self.count is not None:
            result['count'] = self.count

        if self.level is not None:
            result['level'] = self.level

        if self.receiver is not None:
            result['receiver'] = self.receiver

        if self.time is not None:
            result['time'] = self.time

        if self.today is not None:
            result['today'] = self.today

        if self.type is not None:
            result['type'] = self.type

        if self.yesterday is not None:
            result['yesterday'] = self.yesterday

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmGroup') is not None:
            self.alarm_group = m.get('alarmGroup')

        if m.get('compare') is not None:
            self.compare = m.get('compare')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('receiver') is not None:
            self.receiver = m.get('receiver')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('today') is not None:
            self.today = m.get('today')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('yesterday') is not None:
            self.yesterday = m.get('yesterday')

        return self

class GetEmonAlarmRecordStatisticsDistributeResponseBodyResultChannelTotal(DaraModel):
    def __init__(
        self,
        alarm_group: str = None,
        compare: str = None,
        count: int = None,
        level: str = None,
        receiver: str = None,
        time: int = None,
        today: int = None,
        type: str = None,
        yesterday: int = None,
    ):
        self.alarm_group = alarm_group
        self.compare = compare
        self.count = count
        self.level = level
        self.receiver = receiver
        self.time = time
        self.today = today
        self.type = type
        self.yesterday = yesterday

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_group is not None:
            result['alarmGroup'] = self.alarm_group

        if self.compare is not None:
            result['compare'] = self.compare

        if self.count is not None:
            result['count'] = self.count

        if self.level is not None:
            result['level'] = self.level

        if self.receiver is not None:
            result['receiver'] = self.receiver

        if self.time is not None:
            result['time'] = self.time

        if self.today is not None:
            result['today'] = self.today

        if self.type is not None:
            result['type'] = self.type

        if self.yesterday is not None:
            result['yesterday'] = self.yesterday

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmGroup') is not None:
            self.alarm_group = m.get('alarmGroup')

        if m.get('compare') is not None:
            self.compare = m.get('compare')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('receiver') is not None:
            self.receiver = m.get('receiver')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('today') is not None:
            self.today = m.get('today')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('yesterday') is not None:
            self.yesterday = m.get('yesterday')

        return self

class GetEmonAlarmRecordStatisticsDistributeResponseBodyResultAlarmGroupTotal(DaraModel):
    def __init__(
        self,
        alarm_group: str = None,
        compare: str = None,
        count: int = None,
        level: str = None,
        receiver: str = None,
        time: int = None,
        today: int = None,
        type: str = None,
        yesterday: int = None,
    ):
        self.alarm_group = alarm_group
        self.compare = compare
        self.count = count
        self.level = level
        self.receiver = receiver
        self.time = time
        self.today = today
        self.type = type
        self.yesterday = yesterday

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_group is not None:
            result['alarmGroup'] = self.alarm_group

        if self.compare is not None:
            result['compare'] = self.compare

        if self.count is not None:
            result['count'] = self.count

        if self.level is not None:
            result['level'] = self.level

        if self.receiver is not None:
            result['receiver'] = self.receiver

        if self.time is not None:
            result['time'] = self.time

        if self.today is not None:
            result['today'] = self.today

        if self.type is not None:
            result['type'] = self.type

        if self.yesterday is not None:
            result['yesterday'] = self.yesterday

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmGroup') is not None:
            self.alarm_group = m.get('alarmGroup')

        if m.get('compare') is not None:
            self.compare = m.get('compare')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('receiver') is not None:
            self.receiver = m.get('receiver')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('today') is not None:
            self.today = m.get('today')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('yesterday') is not None:
            self.yesterday = m.get('yesterday')

        return self

