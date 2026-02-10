# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCheckSummaryResponseBody(DaraModel):
    def __init__(
        self,
        overall_item_statistic: main_models.GetCheckSummaryResponseBodyOverallItemStatistic = None,
        overall_statistic: main_models.GetCheckSummaryResponseBodyOverallStatistic = None,
        request_id: str = None,
        summarys: List[main_models.GetCheckSummaryResponseBodySummarys] = None,
    ):
        # The statistics about the number of check items.
        self.overall_item_statistic = overall_item_statistic
        # The overall risk statistics.
        self.overall_statistic = overall_statistic
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The summary information about the configuration checks on cloud services.
        self.summarys = summarys

    def validate(self):
        if self.overall_item_statistic:
            self.overall_item_statistic.validate()
        if self.overall_statistic:
            self.overall_statistic.validate()
        if self.summarys:
            for v1 in self.summarys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overall_item_statistic is not None:
            result['OverallItemStatistic'] = self.overall_item_statistic.to_map()

        if self.overall_statistic is not None:
            result['OverallStatistic'] = self.overall_statistic.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Summarys'] = []
        if self.summarys is not None:
            for k1 in self.summarys:
                result['Summarys'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallItemStatistic') is not None:
            temp_model = main_models.GetCheckSummaryResponseBodyOverallItemStatistic()
            self.overall_item_statistic = temp_model.from_map(m.get('OverallItemStatistic'))

        if m.get('OverallStatistic') is not None:
            temp_model = main_models.GetCheckSummaryResponseBodyOverallStatistic()
            self.overall_statistic = temp_model.from_map(m.get('OverallStatistic'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.summarys = []
        if m.get('Summarys') is not None:
            for k1 in m.get('Summarys'):
                temp_model = main_models.GetCheckSummaryResponseBodySummarys()
                self.summarys.append(temp_model.from_map(k1))

        return self

class GetCheckSummaryResponseBodySummarys(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        pass_count: int = None,
        standards: List[main_models.GetCheckSummaryResponseBodySummarysStandards] = None,
        type: str = None,
        type_statistic: main_models.GetCheckSummaryResponseBodySummarysTypeStatistic = None,
    ):
        # The number of detected risk items.
        self.fail_count = fail_count
        # The number of check items that pass the check.
        self.pass_count = pass_count
        # The information about the check items.
        self.standards = standards
        # The type of the check item. Valid values:
        # 
        # *   **COMPLIANCE**
        # *   **RISK**
        # *   **IDENTITY_PERMISSION**
        self.type = type
        # The risk statistics by type.
        self.type_statistic = type_statistic

    def validate(self):
        if self.standards:
            for v1 in self.standards:
                 if v1:
                    v1.validate()
        if self.type_statistic:
            self.type_statistic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.pass_count is not None:
            result['PassCount'] = self.pass_count

        result['Standards'] = []
        if self.standards is not None:
            for k1 in self.standards:
                result['Standards'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.type_statistic is not None:
            result['TypeStatistic'] = self.type_statistic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')

        self.standards = []
        if m.get('Standards') is not None:
            for k1 in m.get('Standards'):
                temp_model = main_models.GetCheckSummaryResponseBodySummarysStandards()
                self.standards.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeStatistic') is not None:
            temp_model = main_models.GetCheckSummaryResponseBodySummarysTypeStatistic()
            self.type_statistic = temp_model.from_map(m.get('TypeStatistic'))

        return self

class GetCheckSummaryResponseBodySummarysTypeStatistic(DaraModel):
    def __init__(
        self,
        not_check_count: int = None,
        not_check_high_count: int = None,
        not_check_low_count: int = None,
        not_check_medium_count: int = None,
        not_pass_count: int = None,
        not_pass_high_count: int = None,
        not_pass_low_count: int = None,
        not_pass_medium_count: int = None,
        pass_count: int = None,
        pass_high_count: int = None,
        pass_low_count: int = None,
        pass_medium_count: int = None,
    ):
        # The number of unchecked check items.
        self.not_check_count = not_check_count
        # The number of unchecked high-risk check items.
        self.not_check_high_count = not_check_high_count
        # The number of unchecked low-risk check items.
        self.not_check_low_count = not_check_low_count
        # The number of unchecked medium-risk check items.
        self.not_check_medium_count = not_check_medium_count
        # The number of check items that failed to pass the check.
        self.not_pass_count = not_pass_count
        # The number of high-risk check items that failed to pass the check.
        self.not_pass_high_count = not_pass_high_count
        # The number of low-risk check items that failed to pass the check.
        self.not_pass_low_count = not_pass_low_count
        # The number of medium-risk check items that failed to pass the check.
        self.not_pass_medium_count = not_pass_medium_count
        # The number of check items that pass the check.
        self.pass_count = pass_count
        # The number of high-risk check items that pass the check.
        self.pass_high_count = pass_high_count
        # The number of low-risk check items that pass the check.
        self.pass_low_count = pass_low_count
        # The number of medium-risk check items that pass the check.
        self.pass_medium_count = pass_medium_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_check_count is not None:
            result['NotCheckCount'] = self.not_check_count

        if self.not_check_high_count is not None:
            result['NotCheckHighCount'] = self.not_check_high_count

        if self.not_check_low_count is not None:
            result['NotCheckLowCount'] = self.not_check_low_count

        if self.not_check_medium_count is not None:
            result['NotCheckMediumCount'] = self.not_check_medium_count

        if self.not_pass_count is not None:
            result['NotPassCount'] = self.not_pass_count

        if self.not_pass_high_count is not None:
            result['NotPassHighCount'] = self.not_pass_high_count

        if self.not_pass_low_count is not None:
            result['NotPassLowCount'] = self.not_pass_low_count

        if self.not_pass_medium_count is not None:
            result['NotPassMediumCount'] = self.not_pass_medium_count

        if self.pass_count is not None:
            result['PassCount'] = self.pass_count

        if self.pass_high_count is not None:
            result['PassHighCount'] = self.pass_high_count

        if self.pass_low_count is not None:
            result['PassLowCount'] = self.pass_low_count

        if self.pass_medium_count is not None:
            result['PassMediumCount'] = self.pass_medium_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotCheckCount') is not None:
            self.not_check_count = m.get('NotCheckCount')

        if m.get('NotCheckHighCount') is not None:
            self.not_check_high_count = m.get('NotCheckHighCount')

        if m.get('NotCheckLowCount') is not None:
            self.not_check_low_count = m.get('NotCheckLowCount')

        if m.get('NotCheckMediumCount') is not None:
            self.not_check_medium_count = m.get('NotCheckMediumCount')

        if m.get('NotPassCount') is not None:
            self.not_pass_count = m.get('NotPassCount')

        if m.get('NotPassHighCount') is not None:
            self.not_pass_high_count = m.get('NotPassHighCount')

        if m.get('NotPassLowCount') is not None:
            self.not_pass_low_count = m.get('NotPassLowCount')

        if m.get('NotPassMediumCount') is not None:
            self.not_pass_medium_count = m.get('NotPassMediumCount')

        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')

        if m.get('PassHighCount') is not None:
            self.pass_high_count = m.get('PassHighCount')

        if m.get('PassLowCount') is not None:
            self.pass_low_count = m.get('PassLowCount')

        if m.get('PassMediumCount') is not None:
            self.pass_medium_count = m.get('PassMediumCount')

        return self

class GetCheckSummaryResponseBodySummarysStandards(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        id: int = None,
        pass_count: int = None,
        risk_level_high_count: int = None,
        risk_level_low_count: int = None,
        risk_level_medium_count: int = None,
        show_name: str = None,
        standard_statistic: main_models.GetCheckSummaryResponseBodySummarysStandardsStandardStatistic = None,
    ):
        # The number of check items that failed to pass the check.
        self.fail_count = fail_count
        # The ID of the check item.
        self.id = id
        # The number of check items that pass the check.
        self.pass_count = pass_count
        # The number of **high-risk** items.
        self.risk_level_high_count = risk_level_high_count
        # The number of **low-risk** items.
        self.risk_level_low_count = risk_level_low_count
        # The number of **medium-risk** items.
        self.risk_level_medium_count = risk_level_medium_count
        # The name of the check item.
        self.show_name = show_name
        # The standard statistics of the check items.
        self.standard_statistic = standard_statistic

    def validate(self):
        if self.standard_statistic:
            self.standard_statistic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.id is not None:
            result['Id'] = self.id

        if self.pass_count is not None:
            result['PassCount'] = self.pass_count

        if self.risk_level_high_count is not None:
            result['RiskLevelHighCount'] = self.risk_level_high_count

        if self.risk_level_low_count is not None:
            result['RiskLevelLowCount'] = self.risk_level_low_count

        if self.risk_level_medium_count is not None:
            result['RiskLevelMediumCount'] = self.risk_level_medium_count

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.standard_statistic is not None:
            result['StandardStatistic'] = self.standard_statistic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')

        if m.get('RiskLevelHighCount') is not None:
            self.risk_level_high_count = m.get('RiskLevelHighCount')

        if m.get('RiskLevelLowCount') is not None:
            self.risk_level_low_count = m.get('RiskLevelLowCount')

        if m.get('RiskLevelMediumCount') is not None:
            self.risk_level_medium_count = m.get('RiskLevelMediumCount')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('StandardStatistic') is not None:
            temp_model = main_models.GetCheckSummaryResponseBodySummarysStandardsStandardStatistic()
            self.standard_statistic = temp_model.from_map(m.get('StandardStatistic'))

        return self

class GetCheckSummaryResponseBodySummarysStandardsStandardStatistic(DaraModel):
    def __init__(
        self,
        not_check_count: int = None,
        not_check_high_count: int = None,
        not_check_low_count: int = None,
        not_check_medium_count: int = None,
        not_pass_count: int = None,
        not_pass_high_count: int = None,
        not_pass_low_count: int = None,
        not_pass_medium_count: int = None,
        pass_count: int = None,
        pass_high_count: int = None,
        pass_low_count: int = None,
        pass_medium_count: int = None,
    ):
        # The number of unchecked check items.
        self.not_check_count = not_check_count
        # The number of unchecked high-risk check items.
        self.not_check_high_count = not_check_high_count
        # The number of unchecked low-risk check items.
        self.not_check_low_count = not_check_low_count
        # The number of unchecked medium-risk check items.
        self.not_check_medium_count = not_check_medium_count
        # The number of check items that failed to pass the check.
        self.not_pass_count = not_pass_count
        # The number of high-risk check items that failed to pass the check.
        self.not_pass_high_count = not_pass_high_count
        # The number of low-risk check items that failed to pass the check.
        self.not_pass_low_count = not_pass_low_count
        # The number of medium-risk check items that failed to pass the check.
        self.not_pass_medium_count = not_pass_medium_count
        # The number of check items that pass the check.
        self.pass_count = pass_count
        # The number of high-risk check items that pass the check.
        self.pass_high_count = pass_high_count
        # The number of low-risk check items that pass the check.
        self.pass_low_count = pass_low_count
        # The number of medium-risk check items that pass the check.
        self.pass_medium_count = pass_medium_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_check_count is not None:
            result['NotCheckCount'] = self.not_check_count

        if self.not_check_high_count is not None:
            result['NotCheckHighCount'] = self.not_check_high_count

        if self.not_check_low_count is not None:
            result['NotCheckLowCount'] = self.not_check_low_count

        if self.not_check_medium_count is not None:
            result['NotCheckMediumCount'] = self.not_check_medium_count

        if self.not_pass_count is not None:
            result['NotPassCount'] = self.not_pass_count

        if self.not_pass_high_count is not None:
            result['NotPassHighCount'] = self.not_pass_high_count

        if self.not_pass_low_count is not None:
            result['NotPassLowCount'] = self.not_pass_low_count

        if self.not_pass_medium_count is not None:
            result['NotPassMediumCount'] = self.not_pass_medium_count

        if self.pass_count is not None:
            result['PassCount'] = self.pass_count

        if self.pass_high_count is not None:
            result['PassHighCount'] = self.pass_high_count

        if self.pass_low_count is not None:
            result['PassLowCount'] = self.pass_low_count

        if self.pass_medium_count is not None:
            result['PassMediumCount'] = self.pass_medium_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotCheckCount') is not None:
            self.not_check_count = m.get('NotCheckCount')

        if m.get('NotCheckHighCount') is not None:
            self.not_check_high_count = m.get('NotCheckHighCount')

        if m.get('NotCheckLowCount') is not None:
            self.not_check_low_count = m.get('NotCheckLowCount')

        if m.get('NotCheckMediumCount') is not None:
            self.not_check_medium_count = m.get('NotCheckMediumCount')

        if m.get('NotPassCount') is not None:
            self.not_pass_count = m.get('NotPassCount')

        if m.get('NotPassHighCount') is not None:
            self.not_pass_high_count = m.get('NotPassHighCount')

        if m.get('NotPassLowCount') is not None:
            self.not_pass_low_count = m.get('NotPassLowCount')

        if m.get('NotPassMediumCount') is not None:
            self.not_pass_medium_count = m.get('NotPassMediumCount')

        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')

        if m.get('PassHighCount') is not None:
            self.pass_high_count = m.get('PassHighCount')

        if m.get('PassLowCount') is not None:
            self.pass_low_count = m.get('PassLowCount')

        if m.get('PassMediumCount') is not None:
            self.pass_medium_count = m.get('PassMediumCount')

        return self

class GetCheckSummaryResponseBodyOverallStatistic(DaraModel):
    def __init__(
        self,
        not_check_count: int = None,
        not_check_high_count: int = None,
        not_check_low_count: int = None,
        not_check_medium_count: int = None,
        not_pass_count: int = None,
        not_pass_high_count: int = None,
        not_pass_low_count: int = None,
        not_pass_medium_count: int = None,
        pass_count: int = None,
        pass_high_count: int = None,
        pass_low_count: int = None,
        pass_medium_count: int = None,
    ):
        # The number of unchecked check items.
        self.not_check_count = not_check_count
        # The number of unchecked high-risk check items.
        self.not_check_high_count = not_check_high_count
        # The number of unchecked low-risk check items.
        self.not_check_low_count = not_check_low_count
        # The number of unchecked medium-risk check items.
        self.not_check_medium_count = not_check_medium_count
        # The number of check items that failed to pass the check.
        self.not_pass_count = not_pass_count
        # The number of high-risk check items that failed to pass the check.
        self.not_pass_high_count = not_pass_high_count
        # The number of low-risk check items that failed to pass the check.
        self.not_pass_low_count = not_pass_low_count
        # The number of medium-risk check items that failed to pass the check.
        self.not_pass_medium_count = not_pass_medium_count
        # The number of check items that pass the check.
        self.pass_count = pass_count
        # The number of high-risk check items that pass the check.
        self.pass_high_count = pass_high_count
        # The number of low-risk check items that pass the check.
        self.pass_low_count = pass_low_count
        # The number of medium-risk check items that pass the check.
        self.pass_medium_count = pass_medium_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_check_count is not None:
            result['NotCheckCount'] = self.not_check_count

        if self.not_check_high_count is not None:
            result['NotCheckHighCount'] = self.not_check_high_count

        if self.not_check_low_count is not None:
            result['NotCheckLowCount'] = self.not_check_low_count

        if self.not_check_medium_count is not None:
            result['NotCheckMediumCount'] = self.not_check_medium_count

        if self.not_pass_count is not None:
            result['NotPassCount'] = self.not_pass_count

        if self.not_pass_high_count is not None:
            result['NotPassHighCount'] = self.not_pass_high_count

        if self.not_pass_low_count is not None:
            result['NotPassLowCount'] = self.not_pass_low_count

        if self.not_pass_medium_count is not None:
            result['NotPassMediumCount'] = self.not_pass_medium_count

        if self.pass_count is not None:
            result['PassCount'] = self.pass_count

        if self.pass_high_count is not None:
            result['PassHighCount'] = self.pass_high_count

        if self.pass_low_count is not None:
            result['PassLowCount'] = self.pass_low_count

        if self.pass_medium_count is not None:
            result['PassMediumCount'] = self.pass_medium_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotCheckCount') is not None:
            self.not_check_count = m.get('NotCheckCount')

        if m.get('NotCheckHighCount') is not None:
            self.not_check_high_count = m.get('NotCheckHighCount')

        if m.get('NotCheckLowCount') is not None:
            self.not_check_low_count = m.get('NotCheckLowCount')

        if m.get('NotCheckMediumCount') is not None:
            self.not_check_medium_count = m.get('NotCheckMediumCount')

        if m.get('NotPassCount') is not None:
            self.not_pass_count = m.get('NotPassCount')

        if m.get('NotPassHighCount') is not None:
            self.not_pass_high_count = m.get('NotPassHighCount')

        if m.get('NotPassLowCount') is not None:
            self.not_pass_low_count = m.get('NotPassLowCount')

        if m.get('NotPassMediumCount') is not None:
            self.not_pass_medium_count = m.get('NotPassMediumCount')

        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')

        if m.get('PassHighCount') is not None:
            self.pass_high_count = m.get('PassHighCount')

        if m.get('PassLowCount') is not None:
            self.pass_low_count = m.get('PassLowCount')

        if m.get('PassMediumCount') is not None:
            self.pass_medium_count = m.get('PassMediumCount')

        return self

class GetCheckSummaryResponseBodyOverallItemStatistic(DaraModel):
    def __init__(
        self,
        release_count: int = None,
        result_count: int = None,
    ):
        # The number of check items supported by the system.
        self.release_count = release_count
        # The number of check items available to you.
        self.result_count = result_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release_count is not None:
            result['ReleaseCount'] = self.release_count

        if self.result_count is not None:
            result['ResultCount'] = self.result_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseCount') is not None:
            self.release_count = m.get('ReleaseCount')

        if m.get('ResultCount') is not None:
            self.result_count = m.get('ResultCount')

        return self

