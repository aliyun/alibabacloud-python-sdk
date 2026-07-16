# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetHoneypotAttackStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHoneypotAttackStatisticsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result code. A value of **200** indicates success. Any other value indicates failure. You can use this field to determine the cause of the failure.
        self.code = code
        # The statistics information data.
        self.data = data
        # The HTTP status code of the response.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # - **true**: The call was successful.
        # - **false**: The call failed.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetHoneypotAttackStatisticsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHoneypotAttackStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        honeypot_attack_statistics: List[main_models.GetHoneypotAttackStatisticsResponseBodyDataHoneypotAttackStatistics] = None,
        statistics_type: str = None,
    ):
        # The number of entries returned on the current page in a paged query.
        self.count = count
        # The list of statistics information.
        self.honeypot_attack_statistics = honeypot_attack_statistics
        # The type of attack source statistics information. Valid values:
        # 
        # - **TOP_ATTACKED_AGENT**: the top 5 probes by number of attacks.
        # - **TOP_ATTACKED_IP**: the top 5 IP addresses by number of attacks.
        # - **ATTACK_EVENT_TYPE**: the intrusion event type.
        # - **ATTACK_HONEYPOT_TYPE**: the type of the compromised honeypot.
        self.statistics_type = statistics_type

    def validate(self):
        if self.honeypot_attack_statistics:
            for v1 in self.honeypot_attack_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['HoneypotAttackStatistics'] = []
        if self.honeypot_attack_statistics is not None:
            for k1 in self.honeypot_attack_statistics:
                result['HoneypotAttackStatistics'].append(k1.to_map() if k1 else None)

        if self.statistics_type is not None:
            result['StatisticsType'] = self.statistics_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.honeypot_attack_statistics = []
        if m.get('HoneypotAttackStatistics') is not None:
            for k1 in m.get('HoneypotAttackStatistics'):
                temp_model = main_models.GetHoneypotAttackStatisticsResponseBodyDataHoneypotAttackStatistics()
                self.honeypot_attack_statistics.append(temp_model.from_map(k1))

        if m.get('StatisticsType') is not None:
            self.statistics_type = m.get('StatisticsType')

        return self

class GetHoneypotAttackStatisticsResponseBodyDataHoneypotAttackStatistics(DaraModel):
    def __init__(
        self,
        statistics_count: int = None,
        statistics_value: str = None,
    ):
        # The count of the statistics value.
        self.statistics_count = statistics_count
        # The statistics value.
        self.statistics_value = statistics_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.statistics_count is not None:
            result['StatisticsCount'] = self.statistics_count

        if self.statistics_value is not None:
            result['StatisticsValue'] = self.statistics_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatisticsCount') is not None:
            self.statistics_count = m.get('StatisticsCount')

        if m.get('StatisticsValue') is not None:
            self.statistics_value = m.get('StatisticsValue')

        return self

