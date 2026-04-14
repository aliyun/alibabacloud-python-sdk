# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopAppRequest(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_type: str = None,
        app_id: str = None,
        app_instance_group_id: str = None,
        app_instance_id: str = None,
        biz_region_id: str = None,
        client_channel: str = None,
        client_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        force_stop: bool = None,
        idp_id: str = None,
        login_region_id: str = None,
        login_token: str = None,
        product_type: str = None,
        region_id: str = None,
        session_id: str = None,
        uuid: str = None,
        wy_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.api_type = api_type
        self.app_id = app_id
        self.app_instance_group_id = app_instance_group_id
        self.app_instance_id = app_instance_id
        self.biz_region_id = biz_region_id
        self.client_channel = client_channel
        self.client_id = client_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.end_user_id = end_user_id
        self.force_stop = force_stop
        self.idp_id = idp_id
        self.login_region_id = login_region_id
        self.login_token = login_token
        self.product_type = product_type
        self.region_id = region_id
        self.session_id = session_id
        self.uuid = uuid
        self.wy_id = wy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.client_channel is not None:
            result['ClientChannel'] = self.client_channel

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

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.idp_id is not None:
            result['IdpId'] = self.idp_id

        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.wy_id is not None:
            result['WyId'] = self.wy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ClientChannel') is not None:
            self.client_channel = m.get('ClientChannel')

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

        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')

        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

