# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityStatInfoResponseBody(DaraModel):
    def __init__(
        self,
        attack_event: main_models.DescribeSecurityStatInfoResponseBodyAttackEvent = None,
        health_check: main_models.DescribeSecurityStatInfoResponseBodyHealthCheck = None,
        request_id: str = None,
        security_event: main_models.DescribeSecurityStatInfoResponseBodySecurityEvent = None,
        success: bool = None,
        vulnerability: main_models.DescribeSecurityStatInfoResponseBodyVulnerability = None,
    ):
        # The statistics of attack events.
        self.attack_event = attack_event
        # The statistics of baseline issues.
        self.health_check = health_check
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The statistics of pending security alerts.
        self.security_event = security_event
        # Indicates whether the query is successful. Valid values:
        # - **true**: Successful.
        # - **false**: Failed.
        self.success = success
        # The statistics information of unfixed vulnerabilities.
        self.vulnerability = vulnerability

    def validate(self):
        if self.attack_event:
            self.attack_event.validate()
        if self.health_check:
            self.health_check.validate()
        if self.security_event:
            self.security_event.validate()
        if self.vulnerability:
            self.vulnerability.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_event is not None:
            result['AttackEvent'] = self.attack_event.to_map()

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_event is not None:
            result['SecurityEvent'] = self.security_event.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.vulnerability is not None:
            result['Vulnerability'] = self.vulnerability.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackEvent') is not None:
            temp_model = main_models.DescribeSecurityStatInfoResponseBodyAttackEvent()
            self.attack_event = temp_model.from_map(m.get('AttackEvent'))

        if m.get('HealthCheck') is not None:
            temp_model = main_models.DescribeSecurityStatInfoResponseBodyHealthCheck()
            self.health_check = temp_model.from_map(m.get('HealthCheck'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityEvent') is not None:
            temp_model = main_models.DescribeSecurityStatInfoResponseBodySecurityEvent()
            self.security_event = temp_model.from_map(m.get('SecurityEvent'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Vulnerability') is not None:
            temp_model = main_models.DescribeSecurityStatInfoResponseBodyVulnerability()
            self.vulnerability = temp_model.from_map(m.get('Vulnerability'))

        return self

class DescribeSecurityStatInfoResponseBodyVulnerability(DaraModel):
    def __init__(
        self,
        asap_count: int = None,
        asap_list: List[str] = None,
        date_array: List[str] = None,
        later_count: int = None,
        later_list: List[str] = None,
        levels_on: List[str] = None,
        nntf_count: int = None,
        nntf_list: List[str] = None,
        time_array: List[str] = None,
        total_count: int = None,
        value_array: List[str] = None,
    ):
        # The number of unfixed vulnerabilities with **high** priority on the current day.
        self.asap_count = asap_count
        # The collection of high-priority unfixed vulnerability counts at each statistical time point.
        self.asap_list = asap_list
        # The collection of statistical time points in the unfixed vulnerability trend chart.
        self.date_array = date_array
        # The number of unfixed vulnerabilities with **medium** priority on the current day.
        self.later_count = later_count
        # The collection of medium-priority unfixed vulnerability counts at each statistical time point.
        self.later_list = later_list
        # The collection of vulnerability priority levels included in the statistics for unfixed vulnerabilities.
        self.levels_on = levels_on
        # The number of unfixed vulnerabilities with **low** priority on the current day.
        self.nntf_count = nntf_count
        # The collection of low-priority unfixed vulnerability counts at each statistical time point.
        self.nntf_list = nntf_list
        # The collection of statistical time periods for unfixed vulnerabilities.
        self.time_array = time_array
        # The number of unfixed vulnerabilities on the current day.
        self.total_count = total_count
        # The collection of unfixed vulnerability counts at each statistical time point.
        self.value_array = value_array

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count

        if self.asap_list is not None:
            result['AsapList'] = self.asap_list

        if self.date_array is not None:
            result['DateArray'] = self.date_array

        if self.later_count is not None:
            result['LaterCount'] = self.later_count

        if self.later_list is not None:
            result['LaterList'] = self.later_list

        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on

        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count

        if self.nntf_list is not None:
            result['NntfList'] = self.nntf_list

        if self.time_array is not None:
            result['TimeArray'] = self.time_array

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.value_array is not None:
            result['ValueArray'] = self.value_array

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')

        if m.get('AsapList') is not None:
            self.asap_list = m.get('AsapList')

        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')

        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')

        if m.get('LaterList') is not None:
            self.later_list = m.get('LaterList')

        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')

        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')

        if m.get('NntfList') is not None:
            self.nntf_list = m.get('NntfList')

        if m.get('TimeArray') is not None:
            self.time_array = m.get('TimeArray')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')

        return self

class DescribeSecurityStatInfoResponseBodySecurityEvent(DaraModel):
    def __init__(
        self,
        date_array: List[str] = None,
        levels_on: List[str] = None,
        remind_count: int = None,
        remind_list: List[str] = None,
        serious_count: int = None,
        serious_list: List[str] = None,
        suspicious_count: int = None,
        suspicious_list: List[str] = None,
        time_array: List[str] = None,
        total_count: int = None,
        value_array: List[str] = None,
    ):
        # The collection of statistical time points in the pending alert trend chart.
        self.date_array = date_array
        # The collection of alert severity levels included in the statistics for pending alerts.
        self.levels_on = levels_on
        # The number of alerts with the **Reminder** severity level detected on the current day.
        self.remind_count = remind_count
        # The collection of Reminder-level alert counts at each statistical time point.
        self.remind_list = remind_list
        # The number of alerts with the **Urgent** severity level on the current day.
        self.serious_count = serious_count
        # The collection of Urgent-level alert counts at each statistical time point.
        self.serious_list = serious_list
        # The number of alerts with the **Suspicious** severity level on the current day.
        self.suspicious_count = suspicious_count
        # The collection of Suspicious-level alert counts at each statistical time point.
        self.suspicious_list = suspicious_list
        # The collection of statistical time periods for alerts.
        self.time_array = time_array
        # The total number of pending alerts on the current day.
        self.total_count = total_count
        # The collection of pending alert counts at each statistical time point.
        self.value_array = value_array

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_array is not None:
            result['DateArray'] = self.date_array

        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on

        if self.remind_count is not None:
            result['RemindCount'] = self.remind_count

        if self.remind_list is not None:
            result['RemindList'] = self.remind_list

        if self.serious_count is not None:
            result['SeriousCount'] = self.serious_count

        if self.serious_list is not None:
            result['SeriousList'] = self.serious_list

        if self.suspicious_count is not None:
            result['SuspiciousCount'] = self.suspicious_count

        if self.suspicious_list is not None:
            result['SuspiciousList'] = self.suspicious_list

        if self.time_array is not None:
            result['TimeArray'] = self.time_array

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.value_array is not None:
            result['ValueArray'] = self.value_array

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')

        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')

        if m.get('RemindCount') is not None:
            self.remind_count = m.get('RemindCount')

        if m.get('RemindList') is not None:
            self.remind_list = m.get('RemindList')

        if m.get('SeriousCount') is not None:
            self.serious_count = m.get('SeriousCount')

        if m.get('SeriousList') is not None:
            self.serious_list = m.get('SeriousList')

        if m.get('SuspiciousCount') is not None:
            self.suspicious_count = m.get('SuspiciousCount')

        if m.get('SuspiciousList') is not None:
            self.suspicious_list = m.get('SuspiciousList')

        if m.get('TimeArray') is not None:
            self.time_array = m.get('TimeArray')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')

        return self

class DescribeSecurityStatInfoResponseBodyHealthCheck(DaraModel):
    def __init__(
        self,
        date_array: List[str] = None,
        high_count: int = None,
        high_list: List[str] = None,
        levels_on: List[str] = None,
        low_count: int = None,
        low_list: List[str] = None,
        medium_count: int = None,
        medium_list: List[str] = None,
        time_array: List[str] = None,
        total_count: int = None,
        value_array: List[str] = None,
    ):
        # The collection of statistical time points in the baseline issue trend chart.
        self.date_array = date_array
        # The number of high-risk baseline issues on the current day.
        self.high_count = high_count
        # The collection of high-risk baseline counts at each statistical time point.
        self.high_list = high_list
        # The collection of baseline risk levels included in the statistics.
        self.levels_on = levels_on
        # The number of low-risk baseline issues on the current day.
        self.low_count = low_count
        # The collection of low-risk baseline issue counts at each statistical time point.
        self.low_list = low_list
        # The number of medium-risk baseline issues on the current day.
        self.medium_count = medium_count
        # The collection of medium-risk baseline issue counts at each statistical time point.
        self.medium_list = medium_list
        # The collection of statistical time periods for baselines.
        self.time_array = time_array
        # The total number of baseline issues on the current day.
        self.total_count = total_count
        # The collection of total baseline counts at each statistical time point.
        self.value_array = value_array

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_array is not None:
            result['DateArray'] = self.date_array

        if self.high_count is not None:
            result['HighCount'] = self.high_count

        if self.high_list is not None:
            result['HighList'] = self.high_list

        if self.levels_on is not None:
            result['LevelsOn'] = self.levels_on

        if self.low_count is not None:
            result['LowCount'] = self.low_count

        if self.low_list is not None:
            result['LowList'] = self.low_list

        if self.medium_count is not None:
            result['MediumCount'] = self.medium_count

        if self.medium_list is not None:
            result['MediumList'] = self.medium_list

        if self.time_array is not None:
            result['TimeArray'] = self.time_array

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.value_array is not None:
            result['ValueArray'] = self.value_array

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')

        if m.get('HighCount') is not None:
            self.high_count = m.get('HighCount')

        if m.get('HighList') is not None:
            self.high_list = m.get('HighList')

        if m.get('LevelsOn') is not None:
            self.levels_on = m.get('LevelsOn')

        if m.get('LowCount') is not None:
            self.low_count = m.get('LowCount')

        if m.get('LowList') is not None:
            self.low_list = m.get('LowList')

        if m.get('MediumCount') is not None:
            self.medium_count = m.get('MediumCount')

        if m.get('MediumList') is not None:
            self.medium_list = m.get('MediumList')

        if m.get('TimeArray') is not None:
            self.time_array = m.get('TimeArray')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')

        return self

class DescribeSecurityStatInfoResponseBodyAttackEvent(DaraModel):
    def __init__(
        self,
        date_array: List[str] = None,
        total_count: int = None,
        value_array: List[str] = None,
    ):
        # The collection of statistical time points in the attack count trend chart.
        self.date_array = date_array
        # The number of attacks on the current day.
        self.total_count = total_count
        # The collection of attack counts at each statistical time point.
        self.value_array = value_array

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_array is not None:
            result['DateArray'] = self.date_array

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.value_array is not None:
            result['ValueArray'] = self.value_array

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateArray') is not None:
            self.date_array = m.get('DateArray')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('ValueArray') is not None:
            self.value_array = m.get('ValueArray')

        return self

