# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigADConnectorTrustRequest(DaraModel):
    def __init__(
        self,
        office_site_id: str = None,
        rds_license_domain: bool = None,
        region_id: str = None,
        trust_key: str = None,
    ):
        # The ID of the enterprise AD office network.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # Specifies whether to configure a trust password for the Remote Desktop Services (RDS) License Domain of the enterprise AD office network.
        # 
        # Valid values:
        # 
        # *   true: configures a trust password for the RDS License Domain of the AD office network.
        # 
        # *   false: configures a trust password for a regular enterprise AD office network.
        self.rds_license_domain = rds_license_domain
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The trust password. You can specify the password when you configure a trust relationship between the AD domain and the ecd.acs domain.
        # 
        # This parameter is required.
        self.trust_key = trust_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.rds_license_domain is not None:
            result['RdsLicenseDomain'] = self.rds_license_domain

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.trust_key is not None:
            result['TrustKey'] = self.trust_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RdsLicenseDomain') is not None:
            self.rds_license_domain = m.get('RdsLicenseDomain')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TrustKey') is not None:
            self.trust_key = m.get('TrustKey')

        return self

