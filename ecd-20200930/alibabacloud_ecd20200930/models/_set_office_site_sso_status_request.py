# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetOfficeSiteSsoStatusRequest(DaraModel):
    def __init__(
        self,
        enable_sso: bool = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable or shutdown single sign-on (SSO) logon.
        # 
        # This parameter is required.
        self.enable_sso = enable_sso
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_sso is not None:
            result['EnableSso'] = self.enable_sso

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSso') is not None:
            self.enable_sso = m.get('EnableSso')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

