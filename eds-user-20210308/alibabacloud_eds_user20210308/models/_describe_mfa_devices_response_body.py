# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class DescribeMfaDevicesResponseBody(DaraModel):
    def __init__(
        self,
        mfa_devices: List[main_models.DescribeMfaDevicesResponseBodyMfaDevices] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about the virtual MFA devices.
        self.mfa_devices = mfa_devices
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.mfa_devices:
            for v1 in self.mfa_devices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MfaDevices'] = []
        if self.mfa_devices is not None:
            for k1 in self.mfa_devices:
                result['MfaDevices'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mfa_devices = []
        if m.get('MfaDevices') is not None:
            for k1 in m.get('MfaDevices'):
                temp_model = main_models.DescribeMfaDevicesResponseBodyMfaDevices()
                self.mfa_devices.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMfaDevicesResponseBodyMfaDevices(DaraModel):
    def __init__(
        self,
        ad_user: main_models.DescribeMfaDevicesResponseBodyMfaDevicesAdUser = None,
        consecutive_fails: int = None,
        device_type: str = None,
        email: str = None,
        end_user_id: str = None,
        gmt_enabled: str = None,
        gmt_unlock: str = None,
        id: int = None,
        serial_number: str = None,
        status: str = None,
    ):
        self.ad_user = ad_user
        # The number of consecutive failures to bind the virtual MFA device, or the number of authentication failures based on the virtual MFA device.
        self.consecutive_fails = consecutive_fails
        # The type of the virtual MFA device. The value can only be `TOTP_VIRTUAL`. This value indicates that the virtual MFA device follows the Time-based One-time Password (TOTP) algorithm.
        self.device_type = device_type
        # >  This parameter is not publicly available.
        self.email = email
        # The username of the convenience account that uses the virtual MFA device.
        self.end_user_id = end_user_id
        # The time when the virtual MFA device was enabled. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.gmt_enabled = gmt_enabled
        # The time when the locked virtual MFA device was automatically unlocked. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.gmt_unlock = gmt_unlock
        # The ID of the virtual MFA device.
        self.id = id
        # The serial number of the virtual MFA device.
        self.serial_number = serial_number
        # The status of the virtual MFA device.
        # 
        # Valid values:
        # 
        # *   LOCKED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   UNBOUND
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NORMAL
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status

    def validate(self):
        if self.ad_user:
            self.ad_user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_user is not None:
            result['AdUser'] = self.ad_user.to_map()

        if self.consecutive_fails is not None:
            result['ConsecutiveFails'] = self.consecutive_fails

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.gmt_enabled is not None:
            result['GmtEnabled'] = self.gmt_enabled

        if self.gmt_unlock is not None:
            result['GmtUnlock'] = self.gmt_unlock

        if self.id is not None:
            result['Id'] = self.id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdUser') is not None:
            temp_model = main_models.DescribeMfaDevicesResponseBodyMfaDevicesAdUser()
            self.ad_user = temp_model.from_map(m.get('AdUser'))

        if m.get('ConsecutiveFails') is not None:
            self.consecutive_fails = m.get('ConsecutiveFails')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('GmtEnabled') is not None:
            self.gmt_enabled = m.get('GmtEnabled')

        if m.get('GmtUnlock') is not None:
            self.gmt_unlock = m.get('GmtUnlock')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeMfaDevicesResponseBodyMfaDevicesAdUser(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        display_name_new: str = None,
        end_user: str = None,
        user_principal_name: str = None,
    ):
        self.display_name = display_name
        self.display_name_new = display_name_new
        self.end_user = end_user
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.display_name_new is not None:
            result['DisplayNameNew'] = self.display_name_new

        if self.end_user is not None:
            result['EndUser'] = self.end_user

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DisplayNameNew') is not None:
            self.display_name_new = m.get('DisplayNameNew')

        if m.get('EndUser') is not None:
            self.end_user = m.get('EndUser')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

