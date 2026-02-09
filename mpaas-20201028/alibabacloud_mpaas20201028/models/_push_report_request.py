# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushReportRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        channel: str = None,
        connect_type: str = None,
        delivery_token: str = None,
        imei: str = None,
        imsi: str = None,
        model: str = None,
        os_type: int = None,
        push_version: str = None,
        tenant_id: str = None,
        third_channel: int = None,
        third_channel_device_token: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.app_version = app_version
        self.channel = channel
        self.connect_type = connect_type
        # This parameter is required.
        self.delivery_token = delivery_token
        self.imei = imei
        self.imsi = imsi
        self.model = model
        # This parameter is required.
        self.os_type = os_type
        self.push_version = push_version
        self.tenant_id = tenant_id
        self.third_channel = third_channel
        self.third_channel_device_token = third_channel_device_token
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.delivery_token is not None:
            result['DeliveryToken'] = self.delivery_token

        if self.imei is not None:
            result['Imei'] = self.imei

        if self.imsi is not None:
            result['Imsi'] = self.imsi

        if self.model is not None:
            result['Model'] = self.model

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.push_version is not None:
            result['PushVersion'] = self.push_version

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.third_channel is not None:
            result['ThirdChannel'] = self.third_channel

        if self.third_channel_device_token is not None:
            result['ThirdChannelDeviceToken'] = self.third_channel_device_token

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('DeliveryToken') is not None:
            self.delivery_token = m.get('DeliveryToken')

        if m.get('Imei') is not None:
            self.imei = m.get('Imei')

        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PushVersion') is not None:
            self.push_version = m.get('PushVersion')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('ThirdChannel') is not None:
            self.third_channel = m.get('ThirdChannel')

        if m.get('ThirdChannelDeviceToken') is not None:
            self.third_channel_device_token = m.get('ThirdChannelDeviceToken')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

