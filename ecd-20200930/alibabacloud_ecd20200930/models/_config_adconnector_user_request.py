# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigADConnectorUserRequest(DaraModel):
    def __init__(
        self,
        domain_password: str = None,
        domain_user_name: str = None,
        ouname: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # The password of the AD user that has the permissions to join computers to domains.
        # 
        # This parameter is required.
        self.domain_password = domain_password
        # The username of the AD user that has the permissions to join computers to domains.
        # 
        # After the username is configured, the cloud desktops in the same AD workspace are joined to the specified OU.
        # 
        # This parameter is required.
        self.domain_user_name = domain_user_name
        # The name of the OU in the AD domain. You can call the [ListUserAdOrganizationUnits](https://help.aliyun.com/document_detail/311259.html) to obtain the OU name.
        self.ouname = ouname
        # The ID of the AD workspace.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The ID of the region.
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
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password

        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name

        if self.ouname is not None:
            result['OUName'] = self.ouname

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')

        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')

        if m.get('OUName') is not None:
            self.ouname = m.get('OUName')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

