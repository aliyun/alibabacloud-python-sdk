# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCloudSiemCustomizeRulesRequest(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        current_page: int = None,
        end_time: int = None,
        id: str = None,
        order: str = None,
        order_field: str = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        rule_name: str = None,
        rule_type: str = None,
        start_time: int = None,
        status: int = None,
        threat_level: List[str] = None,
    ):
        # The alert type.
        self.alert_type = alert_type
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time
        # The ID of the custom rule.
        self.id = id
        # The sort method. Valid values:
        # 
        # *   desc: descending order.
        # *   asc: ascending order.
        self.order = order
        # The field that is used to sort the rules. Valid values:
        # 
        # *   GmtModified: The rules are sorted based on the modification time.
        # *   Id (default): The rules are sorted based on the rule ID.
        self.order_field = order_field
        # The number of entries per page. The value can be up to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The data management center of the threat analysis feature. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   **cn-hangzhou**: Your assets reside in regions in China.
        # *   **ap-southeast-1**: Your assets reside in regions outside China.
        self.region_id = region_id
        # The ID of the destination account to which you switch the view from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # 
        # *   0: view of the current Alibaba Cloud account.
        # *   1: view of all accounts for the enterprise.
        self.role_type = role_type
        # The name of the rule. The name can contain letters, digits, underscores (_), and periods (.).
        self.rule_name = rule_name
        # The type of the rule. Valid values:
        # 
        # *   **predefine**
        # *   **customize**
        self.rule_type = rule_type
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time
        # The status of the rule. Valid values:
        # 
        # *   **0**: The rule is in the initial state.
        # *   **10**: The simulation data is tested.
        # *   **15**: The business data is being tested.
        # *   **20**: The business data test is complete.
        # *   **100**: The rule is in effect.
        self.status = status
        # The threat level. The value must be a JSON array. Valid values:
        # 
        # *   **serious**: high-risk.
        # *   **suspicious**: medium-risk.
        # *   **remind**: low-risk.
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.order is not None:
            result['Order'] = self.order

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        return self

