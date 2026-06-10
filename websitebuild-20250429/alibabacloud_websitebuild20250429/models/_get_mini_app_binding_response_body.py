# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetMiniAppBindingResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMiniAppBindingResponseBodyData = None,
        request_id: str = None,
    ):
        # Request result.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetMiniAppBindingResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMiniAppBindingResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_status: str = None,
        biz_id: str = None,
        icp_filed: bool = None,
        platform_appid: str = None,
        preview_qr_code_url: str = None,
        production_qr_code_url: str = None,
        setting_values: Dict[str, str] = None,
    ):
        # Authorization status
        self.auth_status = auth_status
        # Business ID
        self.biz_id = biz_id
        # ICP filing status
        self.icp_filed = icp_filed
        # Miniapp ID
        self.platform_appid = platform_appid
        # Preview QR code
        self.preview_qr_code_url = preview_qr_code_url
        # Production QR code
        self.production_qr_code_url = production_qr_code_url
        # Extension information
        self.setting_values = setting_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.icp_filed is not None:
            result['IcpFiled'] = self.icp_filed

        if self.platform_appid is not None:
            result['PlatformAppid'] = self.platform_appid

        if self.preview_qr_code_url is not None:
            result['PreviewQrCodeUrl'] = self.preview_qr_code_url

        if self.production_qr_code_url is not None:
            result['ProductionQrCodeUrl'] = self.production_qr_code_url

        if self.setting_values is not None:
            result['SettingValues'] = self.setting_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('IcpFiled') is not None:
            self.icp_filed = m.get('IcpFiled')

        if m.get('PlatformAppid') is not None:
            self.platform_appid = m.get('PlatformAppid')

        if m.get('PreviewQrCodeUrl') is not None:
            self.preview_qr_code_url = m.get('PreviewQrCodeUrl')

        if m.get('ProductionQrCodeUrl') is not None:
            self.production_qr_code_url = m.get('ProductionQrCodeUrl')

        if m.get('SettingValues') is not None:
            self.setting_values = m.get('SettingValues')

        return self

