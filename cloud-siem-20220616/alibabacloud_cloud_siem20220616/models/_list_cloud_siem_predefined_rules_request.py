# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCloudSiemPredefinedRulesRequest(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        att_ck: str = None,
        current_page: int = None,
        end_time: int = None,
        event_transfer_type: str = None,
        id: str = None,
        log_source: str = None,
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
        # The ATT\\&CK technique.
        self.att_ck = att_ck
        # The page number. The value must be greater than or equal to 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. This value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The event generation method. Valid values:
        # 
        # - default: the default built-in method
        # 
        # - singleToSingle: An event is generated for each alert.
        # 
        # - allToSingle: An event is generated for all alerts in an epoch.
        self.event_transfer_type = event_transfer_type
        # The rule ID.
        self.id = id
        # The log source.
        self.log_source = log_source
        # The sort order. Valid values:
        # 
        # - desc: descending
        # 
        # - asc: ascending
        self.order = order
        # The field to sort the rules by. Valid values:
        # 
        # - GmtModified: Sorts by modification time.
        # 
        # - Id: Sorts by rule ID. This is the default value.
        self.order_field = order_field
        # The number of entries per page. The maximum value is 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region where the Data Management center of the threat analysis feature is located. Select the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: assets in the Chinese mainland or China (Hong Kong)
        # 
        # - ap-southeast-1: assets outside China
        self.region_id = region_id
        # The user ID that the administrator uses to switch to the perspective of a member.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # 
        # - 1: the view of all accounts in the enterprise.
        self.role_type = role_type
        # The rule name. The name can contain only letters, digits, underscores (_), and periods (.).
        self.rule_name = rule_name
        # The rule type. Valid values:
        # 
        # - predefine: predefined
        # 
        # - customize: custom
        self.rule_type = rule_type
        # The start of the time range to query. This value is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The rule status. Valid values:
        # 
        # - 0: initial
        # 
        # - 10: testing with simulated data
        # 
        # - 15: testing with production data
        # 
        # - 20: testing with production data is complete
        # 
        # - 100: published
        self.status = status
        # The threat level. The value is a JSON array. Valid values:
        # 
        # - serious: high
        # 
        # - suspicious: medium
        # 
        # - remind: low
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

        if self.att_ck is not None:
            result['AttCk'] = self.att_ck

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_transfer_type is not None:
            result['EventTransferType'] = self.event_transfer_type

        if self.id is not None:
            result['Id'] = self.id

        if self.log_source is not None:
            result['LogSource'] = self.log_source

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

        if m.get('AttCk') is not None:
            self.att_ck = m.get('AttCk')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventTransferType') is not None:
            self.event_transfer_type = m.get('EventTransferType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')

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

