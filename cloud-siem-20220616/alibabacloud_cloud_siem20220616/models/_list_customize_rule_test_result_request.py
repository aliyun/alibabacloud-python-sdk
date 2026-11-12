# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomizeRuleTestResultRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        detection_rule_id: str = None,
        end_time: int = None,
        id: int = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        start_time: int = None,
        verify_type: str = None,
    ):
        # The current page number. The value must be greater than or equal to 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The ID of the custom rule. You can obtain the rule ID by calling the rule list API operation.
        self.detection_rule_id = detection_rule_id
        # The end time. The value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The ID of the custom rule.
        self.id = id
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region where the data management center of Threat Analysis is located. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the user whose view the administrator switches to.
        self.role_for = role_for
        # The view type. Valid values:
        # - 0: the view of the current Alibaba Cloud account
        # - 1: the view of all accounts in the enterprise
        self.role_type = role_type
        # The start time. The value is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The verification result of the accuracy of alert fields based on the alert template. Valid values:
        # - true: Passed. Alerts from enabled rules can be synchronized to the product side.
        # - false: Failed. Alerts cannot pass the product-side verification.
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.detection_rule_id is not None:
            result['DetectionRuleId'] = self.detection_rule_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DetectionRuleId') is not None:
            self.detection_rule_id = m.get('DetectionRuleId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self

