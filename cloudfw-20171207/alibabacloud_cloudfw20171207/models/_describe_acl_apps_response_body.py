# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAclAppsResponseBody(DaraModel):
    def __init__(
        self,
        acl_apps: List[main_models.DescribeAclAppsResponseBodyAclApps] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.acl_apps = acl_apps
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.acl_apps:
            for v1 in self.acl_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AclApps'] = []
        if self.acl_apps is not None:
            for k1 in self.acl_apps:
                result['AclApps'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_apps = []
        if m.get('AclApps') is not None:
            for k1 in m.get('AclApps'):
                temp_model = main_models.DescribeAclAppsResponseBodyAclApps()
                self.acl_apps.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAclAppsResponseBodyAclApps(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        popular: int = None,
        protocols: List[str] = None,
        risk_level: int = None,
        support_fqdn: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.popular = popular
        self.protocols = protocols
        self.risk_level = risk_level
        self.support_fqdn = support_fqdn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.popular is not None:
            result['Popular'] = self.popular

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.support_fqdn is not None:
            result['SupportFqdn'] = self.support_fqdn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Popular') is not None:
            self.popular = m.get('Popular')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SupportFqdn') is not None:
            self.support_fqdn = m.get('SupportFqdn')

        return self

