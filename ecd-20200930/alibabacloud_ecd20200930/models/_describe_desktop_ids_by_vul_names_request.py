# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDesktopIdsByVulNamesRequest(DaraModel):
    def __init__(
        self,
        necessity: str = None,
        office_site_id: str = None,
        region_id: str = None,
        type: str = None,
        vul_name: List[str] = None,
    ):
        # The necessity level for vulnerability fixing, which indicates the urgency of the vulnerability. Valid values:
        # - asap: high
        # - later: medium
        # - nntf: low
        self.necessity = necessity
        # The workspace ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The vulnerability type. Valid values:
        # 
        # - cve: Linux software vulnerability
        # - sys: Windows system vulnerability
        # 
        # This parameter is required.
        self.type = type
        # The array of vulnerability names.
        # 
        # This parameter is required.
        self.vul_name = vul_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        if self.vul_name is not None:
            result['VulName'] = self.vul_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VulName') is not None:
            self.vul_name = m.get('VulName')

        return self

