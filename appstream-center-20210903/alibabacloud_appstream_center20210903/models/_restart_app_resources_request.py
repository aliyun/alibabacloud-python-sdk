# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RestartAppResourcesRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        biz_region_id: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        resource_ids: List[str] = None,
        session_id: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        self.biz_region_id = biz_region_id
        # This parameter is required.
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
        self.resource_ids = resource_ids
        # This parameter is required.
        self.session_id = session_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

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

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

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

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

