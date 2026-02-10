# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCheckItemWarningSummaryResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListCheckItemWarningSummaryResponseBodyList] = None,
        page_info: main_models.ListCheckItemWarningSummaryResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # List of check item risk statistics.
        self.list = list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListCheckItemWarningSummaryResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCheckItemWarningSummaryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCheckItemWarningSummaryResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCheckItemWarningSummaryResponseBodyList(DaraModel):
    def __init__(
        self,
        advice: str = None,
        affiliated_risk_types: List[str] = None,
        affiliated_risks: List[str] = None,
        alias: str = None,
        check_id: int = None,
        check_item: str = None,
        check_level: str = None,
        check_type: str = None,
        container_check_item: bool = None,
        description: str = None,
        enable_risks: List[str] = None,
        risk_type: str = None,
        status: int = None,
        warning_machine_count: int = None,
    ):
        # The suggestion on the check item.
        self.advice = advice
        # The types of the baselines to which the check item belongs.
        self.affiliated_risk_types = affiliated_risk_types
        # The baselines to which the check item belongs.
        self.affiliated_risks = affiliated_risks
        # The alias of the baseline type.
        self.alias = alias
        # The ID of the check item.
        self.check_id = check_id
        # The description of the check item.
        self.check_item = check_item
        # The risk level of the check item. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.check_level = check_level
        # The type of the check item.
        self.check_type = check_type
        # Indicates whether the check item belongs to the container runtime type. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.container_check_item = container_check_item
        # The description of the check item.
        self.description = description
        # The baselines in which the check item is enabled.
        self.enable_risks = enable_risks
        # The type of the baseline.
        self.risk_type = risk_type
        # Risk status of check items. Valid values:
        # 
        # *   **1**: failed
        # *   **3**: passed
        # *   **6**: whitelisted
        # *   **8**: fixed
        self.status = status
        # The number of servers that are affected by the check item.
        self.warning_machine_count = warning_machine_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice is not None:
            result['Advice'] = self.advice

        if self.affiliated_risk_types is not None:
            result['AffiliatedRiskTypes'] = self.affiliated_risk_types

        if self.affiliated_risks is not None:
            result['AffiliatedRisks'] = self.affiliated_risks

        if self.alias is not None:
            result['Alias'] = self.alias

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_item is not None:
            result['CheckItem'] = self.check_item

        if self.check_level is not None:
            result['CheckLevel'] = self.check_level

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.container_check_item is not None:
            result['ContainerCheckItem'] = self.container_check_item

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_risks is not None:
            result['EnableRisks'] = self.enable_risks

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        if self.status is not None:
            result['Status'] = self.status

        if self.warning_machine_count is not None:
            result['WarningMachineCount'] = self.warning_machine_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')

        if m.get('AffiliatedRiskTypes') is not None:
            self.affiliated_risk_types = m.get('AffiliatedRiskTypes')

        if m.get('AffiliatedRisks') is not None:
            self.affiliated_risks = m.get('AffiliatedRisks')

        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')

        if m.get('CheckLevel') is not None:
            self.check_level = m.get('CheckLevel')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('ContainerCheckItem') is not None:
            self.container_check_item = m.get('ContainerCheckItem')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableRisks') is not None:
            self.enable_risks = m.get('EnableRisks')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WarningMachineCount') is not None:
            self.warning_machine_count = m.get('WarningMachineCount')

        return self

