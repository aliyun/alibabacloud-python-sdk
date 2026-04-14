# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        app_instance_persistent_id: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        session_id: str = None,
        tenant_id: int = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.app_instance_persistent_id = app_instance_persistent_id
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.login_region_id = login_region_id
        # This parameter is required.
        self.login_token = login_token
        # This parameter is required.
        self.product_type = product_type
        # This parameter is required.
        self.session_id = session_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.client_os is not None:
            result['ClientOS'] = self.client_os

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

