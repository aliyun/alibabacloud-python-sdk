# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableAccessForCloudSiemRequest(DaraModel):
    def __init__(
        self,
        auto_submit: int = None,
        client_token: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # Specifies whether to automatically integrate alert logs from Security Center, Web Application Firewall (WAF), and Cloud Firewall. By default, the logs are automatically integrated.
        self.auto_submit = auto_submit
        # The idempotency token.
        self.client_token = client_token
        # The region where the threat detection and response data management center resides. Select the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: assets in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: assets outside China.
        self.region_id = region_id
        # The ID of the member account to which the administrator switches the view.
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
        if self.auto_submit is not None:
            result['AutoSubmit'] = self.auto_submit

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSubmit') is not None:
            self.auto_submit = m.get('AutoSubmit')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

