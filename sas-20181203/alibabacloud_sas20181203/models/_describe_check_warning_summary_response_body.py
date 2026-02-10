# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCheckWarningSummaryResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        warning_summarys: List[main_models.DescribeCheckWarningSummaryResponseBodyWarningSummarys] = None,
    ):
        # The number of check items returned on the current page.
        self.count = count
        # The page number of the current page.
        self.current_page = current_page
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of check items.
        self.total_count = total_count
        # The statistics of check items.
        self.warning_summarys = warning_summarys

    def validate(self):
        if self.warning_summarys:
            for v1 in self.warning_summarys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WarningSummarys'] = []
        if self.warning_summarys is not None:
            for k1 in self.warning_summarys:
                result['WarningSummarys'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.warning_summarys = []
        if m.get('WarningSummarys') is not None:
            for k1 in m.get('WarningSummarys'):
                temp_model = main_models.DescribeCheckWarningSummaryResponseBodyWarningSummarys()
                self.warning_summarys.append(temp_model.from_map(k1))

        return self

class DescribeCheckWarningSummaryResponseBodyWarningSummarys(DaraModel):
    def __init__(
        self,
        check_count: int = None,
        check_exploit: bool = None,
        container_risk: bool = None,
        database_risk: bool = None,
        high_warning_count: int = None,
        last_found_time: str = None,
        level: str = None,
        low_warning_count: int = None,
        medium_warning_count: int = None,
        risk_id: int = None,
        risk_name: str = None,
        sub_type_alias: str = None,
        type_alias: str = None,
        warning_machine_count: int = None,
    ):
        # The number of check items.
        self.check_count = check_count
        # Indicates whether the risk item can be exploited. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.check_exploit = check_exploit
        # Indicates  whether the risk item is a container runtime risk item. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.container_risk = container_risk
        # Indicates whether the risk item is a database risk item. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.database_risk = database_risk
        # The number of high-risk items.
        self.high_warning_count = high_warning_count
        # The time when the last baseline check was performed.
        self.last_found_time = last_found_time
        # The risk level of the risk item. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.level = level
        # The number of low-risk items.
        self.low_warning_count = low_warning_count
        # The number of medium-risk items.
        self.medium_warning_count = medium_warning_count
        # The ID of the risk item.
        self.risk_id = risk_id
        # The name of the risk item.
        self.risk_name = risk_name
        # The level-2 type of the risk item.
        self.sub_type_alias = sub_type_alias
        # The level-1 type of the check item. Examples: database, system, weak password, and middleware.
        self.type_alias = type_alias
        # The number of assets on which risk items are detected.
        self.warning_machine_count = warning_machine_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_count is not None:
            result['CheckCount'] = self.check_count

        if self.check_exploit is not None:
            result['CheckExploit'] = self.check_exploit

        if self.container_risk is not None:
            result['ContainerRisk'] = self.container_risk

        if self.database_risk is not None:
            result['DatabaseRisk'] = self.database_risk

        if self.high_warning_count is not None:
            result['HighWarningCount'] = self.high_warning_count

        if self.last_found_time is not None:
            result['LastFoundTime'] = self.last_found_time

        if self.level is not None:
            result['Level'] = self.level

        if self.low_warning_count is not None:
            result['LowWarningCount'] = self.low_warning_count

        if self.medium_warning_count is not None:
            result['MediumWarningCount'] = self.medium_warning_count

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        if self.sub_type_alias is not None:
            result['SubTypeAlias'] = self.sub_type_alias

        if self.type_alias is not None:
            result['TypeAlias'] = self.type_alias

        if self.warning_machine_count is not None:
            result['WarningMachineCount'] = self.warning_machine_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCount') is not None:
            self.check_count = m.get('CheckCount')

        if m.get('CheckExploit') is not None:
            self.check_exploit = m.get('CheckExploit')

        if m.get('ContainerRisk') is not None:
            self.container_risk = m.get('ContainerRisk')

        if m.get('DatabaseRisk') is not None:
            self.database_risk = m.get('DatabaseRisk')

        if m.get('HighWarningCount') is not None:
            self.high_warning_count = m.get('HighWarningCount')

        if m.get('LastFoundTime') is not None:
            self.last_found_time = m.get('LastFoundTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('LowWarningCount') is not None:
            self.low_warning_count = m.get('LowWarningCount')

        if m.get('MediumWarningCount') is not None:
            self.medium_warning_count = m.get('MediumWarningCount')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        if m.get('SubTypeAlias') is not None:
            self.sub_type_alias = m.get('SubTypeAlias')

        if m.get('TypeAlias') is not None:
            self.type_alias = m.get('TypeAlias')

        if m.get('WarningMachineCount') is not None:
            self.warning_machine_count = m.get('WarningMachineCount')

        return self

