# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWhiteRuleListRequest(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_type: str = None,
        current_page: int = None,
        incident_uuid: str = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The alert name.
        self.alert_name = alert_name
        # The alerting type.
        self.alert_type = alert_type
        # The current page number. The value must be greater than or equal to 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The globally unique UUID of the incident.
        self.incident_uuid = incident_uuid
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region where the data management center of Threat Analysis is located. You must select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets are located outside China.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for
        # The view type. Valid values:
        # - 0: the view of the current Alibaba Cloud account
        # - 1: the view of all accounts in the enterprise
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

