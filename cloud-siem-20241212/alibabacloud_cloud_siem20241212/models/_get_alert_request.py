# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAlertRequest(DaraModel):
    def __init__(
        self,
        alert_uuid: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The ID of the alert that is associated with the incident.
        self.alert_uuid = alert_uuid
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The region in which the threat detection and response data management center resides. Specify this parameter based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside outside China.
        self.region_id = region_id
        # The ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # - 1: the view of all accounts in the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

