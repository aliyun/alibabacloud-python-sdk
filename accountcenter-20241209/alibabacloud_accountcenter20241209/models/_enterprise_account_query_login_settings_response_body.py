# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseAccountQueryLoginSettingsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.EnterpriseAccountQueryLoginSettingsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.EnterpriseAccountQueryLoginSettingsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EnterpriseAccountQueryLoginSettingsResponseBodyData(DaraModel):
    def __init__(
        self,
        ip_mask_dto: main_models.EnterpriseAccountQueryLoginSettingsResponseBodyDataIpMaskDto = None,
        mfa_bind_status: str = None,
        risk_control_dto: main_models.EnterpriseAccountQueryLoginSettingsResponseBodyDataRiskControlDto = None,
        security_mobile_login_status: str = None,
        session_expire_time: int = None,
    ):
        self.ip_mask_dto = ip_mask_dto
        self.mfa_bind_status = mfa_bind_status
        self.risk_control_dto = risk_control_dto
        self.security_mobile_login_status = security_mobile_login_status
        self.session_expire_time = session_expire_time

    def validate(self):
        if self.ip_mask_dto:
            self.ip_mask_dto.validate()
        if self.risk_control_dto:
            self.risk_control_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_mask_dto is not None:
            result['IpMaskDto'] = self.ip_mask_dto.to_map()

        if self.mfa_bind_status is not None:
            result['MfaBindStatus'] = self.mfa_bind_status

        if self.risk_control_dto is not None:
            result['RiskControlDto'] = self.risk_control_dto.to_map()

        if self.security_mobile_login_status is not None:
            result['SecurityMobileLoginStatus'] = self.security_mobile_login_status

        if self.session_expire_time is not None:
            result['SessionExpireTime'] = self.session_expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpMaskDto') is not None:
            temp_model = main_models.EnterpriseAccountQueryLoginSettingsResponseBodyDataIpMaskDto()
            self.ip_mask_dto = temp_model.from_map(m.get('IpMaskDto'))

        if m.get('MfaBindStatus') is not None:
            self.mfa_bind_status = m.get('MfaBindStatus')

        if m.get('RiskControlDto') is not None:
            temp_model = main_models.EnterpriseAccountQueryLoginSettingsResponseBodyDataRiskControlDto()
            self.risk_control_dto = temp_model.from_map(m.get('RiskControlDto'))

        if m.get('SecurityMobileLoginStatus') is not None:
            self.security_mobile_login_status = m.get('SecurityMobileLoginStatus')

        if m.get('SessionExpireTime') is not None:
            self.session_expire_time = m.get('SessionExpireTime')

        return self

class EnterpriseAccountQueryLoginSettingsResponseBodyDataRiskControlDto(DaraModel):
    def __init__(
        self,
        protect_level: str = None,
        risk_control_enabled: bool = None,
        verify_detail: str = None,
        verify_type: str = None,
    ):
        self.protect_level = protect_level
        self.risk_control_enabled = risk_control_enabled
        self.verify_detail = verify_detail
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protect_level is not None:
            result['ProtectLevel'] = self.protect_level

        if self.risk_control_enabled is not None:
            result['RiskControlEnabled'] = self.risk_control_enabled

        if self.verify_detail is not None:
            result['VerifyDetail'] = self.verify_detail

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectLevel') is not None:
            self.protect_level = m.get('ProtectLevel')

        if m.get('RiskControlEnabled') is not None:
            self.risk_control_enabled = m.get('RiskControlEnabled')

        if m.get('VerifyDetail') is not None:
            self.verify_detail = m.get('VerifyDetail')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self

class EnterpriseAccountQueryLoginSettingsResponseBodyDataIpMaskDto(DaraModel):
    def __init__(
        self,
        ip_mask_enabled_status: str = None,
        ip_masks: List[str] = None,
    ):
        self.ip_mask_enabled_status = ip_mask_enabled_status
        self.ip_masks = ip_masks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_mask_enabled_status is not None:
            result['IpMaskEnabledStatus'] = self.ip_mask_enabled_status

        if self.ip_masks is not None:
            result['IpMasks'] = self.ip_masks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpMaskEnabledStatus') is not None:
            self.ip_mask_enabled_status = m.get('IpMaskEnabledStatus')

        if m.get('IpMasks') is not None:
            self.ip_masks = m.get('IpMasks')

        return self

