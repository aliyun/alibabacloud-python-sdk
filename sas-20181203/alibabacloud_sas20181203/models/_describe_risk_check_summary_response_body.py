# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeRiskCheckSummaryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_check_summary: main_models.DescribeRiskCheckSummaryResponseBodyRiskCheckSummary = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The summary information about the check results of cloud service configurations.
        self.risk_check_summary = risk_check_summary

    def validate(self):
        if self.risk_check_summary:
            self.risk_check_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_check_summary is not None:
            result['RiskCheckSummary'] = self.risk_check_summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskCheckSummary') is not None:
            temp_model = main_models.DescribeRiskCheckSummaryResponseBodyRiskCheckSummary()
            self.risk_check_summary = temp_model.from_map(m.get('RiskCheckSummary'))

        return self

class DescribeRiskCheckSummaryResponseBodyRiskCheckSummary(DaraModel):
    def __init__(
        self,
        affected_asset_count: int = None,
        disabled_risk_count: int = None,
        enabled_risk_count: int = None,
        groups: List[main_models.DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroups] = None,
        item_count: int = None,
        previous_count: int = None,
        previous_time: int = None,
        risk_count: int = None,
        risk_level_count: List[main_models.DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryRiskLevelCount] = None,
        risk_rate: float = None,
    ):
        # The number of affected assets.
        self.affected_asset_count = affected_asset_count
        # The number of the check items that failed the check.
        self.disabled_risk_count = disabled_risk_count
        # The number of the check items that passed the check.
        self.enabled_risk_count = enabled_risk_count
        # An array that consists of the statistics for each type of check item.
        self.groups = groups
        # The number of check items.
        self.item_count = item_count
        # The number of risk items detected in the last check.
        self.previous_count = previous_count
        # The timestamp of the last check. Unit: milliseconds.
        self.previous_time = previous_time
        # The number of detected risk items.
        self.risk_count = risk_count
        # An array that consists of the number of check items at each risk level.
        self.risk_level_count = risk_level_count
        # The proportion of risk items to all check items.
        self.risk_rate = risk_rate

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.risk_level_count:
            for v1 in self.risk_level_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_asset_count is not None:
            result['AffectedAssetCount'] = self.affected_asset_count

        if self.disabled_risk_count is not None:
            result['DisabledRiskCount'] = self.disabled_risk_count

        if self.enabled_risk_count is not None:
            result['EnabledRiskCount'] = self.enabled_risk_count

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.item_count is not None:
            result['ItemCount'] = self.item_count

        if self.previous_count is not None:
            result['PreviousCount'] = self.previous_count

        if self.previous_time is not None:
            result['PreviousTime'] = self.previous_time

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        result['RiskLevelCount'] = []
        if self.risk_level_count is not None:
            for k1 in self.risk_level_count:
                result['RiskLevelCount'].append(k1.to_map() if k1 else None)

        if self.risk_rate is not None:
            result['RiskRate'] = self.risk_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedAssetCount') is not None:
            self.affected_asset_count = m.get('AffectedAssetCount')

        if m.get('DisabledRiskCount') is not None:
            self.disabled_risk_count = m.get('DisabledRiskCount')

        if m.get('EnabledRiskCount') is not None:
            self.enabled_risk_count = m.get('EnabledRiskCount')

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('ItemCount') is not None:
            self.item_count = m.get('ItemCount')

        if m.get('PreviousCount') is not None:
            self.previous_count = m.get('PreviousCount')

        if m.get('PreviousTime') is not None:
            self.previous_time = m.get('PreviousTime')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        self.risk_level_count = []
        if m.get('RiskLevelCount') is not None:
            for k1 in m.get('RiskLevelCount'):
                temp_model = main_models.DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryRiskLevelCount()
                self.risk_level_count.append(temp_model.from_map(k1))

        if m.get('RiskRate') is not None:
            self.risk_rate = m.get('RiskRate')

        return self

class DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryRiskLevelCount(DaraModel):
    def __init__(
        self,
        count: int = None,
        key: str = None,
    ):
        # The number of check items at the specified risk level.
        self.count = count
        # The risk level of the check items. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

class DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroups(DaraModel):
    def __init__(
        self,
        count_by_status: List[main_models.DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroupsCountByStatus] = None,
        id: int = None,
        remaining_time: int = None,
        sort: int = None,
        status: str = None,
        title: str = None,
    ):
        # An array that consists of the statistics about check results.
        self.count_by_status = count_by_status
        # The ID of the check item type.
        self.id = id
        # The remaining time before the check is complete.
        self.remaining_time = remaining_time
        # The sequence number of the check item type in the **All Types** drop-down list in the Security Center console.
        self.sort = sort
        # The status of the check. Valid values:
        # 
        # *   **finish**: The check is finished.
        # *   **running**: The check is in progress.
        # *   **waiting**: The check is pending.
        # *   **notStart**: The check is not started.
        self.status = status
        # The name of the check item type.
        self.title = title

    def validate(self):
        if self.count_by_status:
            for v1 in self.count_by_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CountByStatus'] = []
        if self.count_by_status is not None:
            for k1 in self.count_by_status:
                result['CountByStatus'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.remaining_time is not None:
            result['RemainingTime'] = self.remaining_time

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.count_by_status = []
        if m.get('CountByStatus') is not None:
            for k1 in m.get('CountByStatus'):
                temp_model = main_models.DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroupsCountByStatus()
                self.count_by_status.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RemainingTime') is not None:
            self.remaining_time = m.get('RemainingTime')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class DescribeRiskCheckSummaryResponseBodyRiskCheckSummaryGroupsCountByStatus(DaraModel):
    def __init__(
        self,
        count: int = None,
        status: str = None,
    ):
        # The number of detected risk items.
        self.count = count
        # The status of the check item after the check is finished. Valid values:
        # 
        # *   **pass**: The check item passed the check, which indicates that the check item is normal.
        # *   **failed**: The check item failed the check, which indicates that risks are detected based on the check item.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

