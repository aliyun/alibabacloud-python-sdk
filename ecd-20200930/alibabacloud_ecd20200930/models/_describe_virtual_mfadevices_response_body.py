# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeVirtualMFADevicesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        virtual_mfadevices: List[main_models.DescribeVirtualMFADevicesResponseBodyVirtualMFADevices] = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Details of the virtual MFA devices.
        self.virtual_mfadevices = virtual_mfadevices

    def validate(self):
        if self.virtual_mfadevices:
            for v1 in self.virtual_mfadevices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VirtualMFADevices'] = []
        if self.virtual_mfadevices is not None:
            for k1 in self.virtual_mfadevices:
                result['VirtualMFADevices'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.virtual_mfadevices = []
        if m.get('VirtualMFADevices') is not None:
            for k1 in m.get('VirtualMFADevices'):
                temp_model = main_models.DescribeVirtualMFADevicesResponseBodyVirtualMFADevices()
                self.virtual_mfadevices.append(temp_model.from_map(k1))

        return self

class DescribeVirtualMFADevicesResponseBodyVirtualMFADevices(DaraModel):
    def __init__(
        self,
        ad_user: main_models.DescribeVirtualMFADevicesResponseBodyVirtualMFADevicesAdUser = None,
        consecutive_fails: int = None,
        directory_id: str = None,
        end_user_id: str = None,
        gmt_enabled: str = None,
        gmt_unlock: str = None,
        office_site_id: str = None,
        serial_number: str = None,
        status: str = None,
    ):
        self.ad_user = ad_user
        # The number of consecutive failures to bind the virtual MFA device, or the number of failures on the verification of the virtual MFA device.
        self.consecutive_fails = consecutive_fails
        # > This parameter is in invitational preview and is not publicly available.
        self.directory_id = directory_id
        # The name of the AD user who uses the virtual MFA device.
        self.end_user_id = end_user_id
        # The time when the virtual MFA device was started. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_enabled = gmt_enabled
        # The time when a locked virtual MFA device was automatically unlocked. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_unlock = gmt_unlock
        # The ID of the workspace.
        self.office_site_id = office_site_id
        # The serial number of the virtual MFA device, which is a unique identifier.
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

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.gmt_enabled is not None:
            result['GmtEnabled'] = self.gmt_enabled

        if self.gmt_unlock is not None:
            result['GmtUnlock'] = self.gmt_unlock

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdUser') is not None:
            temp_model = main_models.DescribeVirtualMFADevicesResponseBodyVirtualMFADevicesAdUser()
            self.ad_user = temp_model.from_map(m.get('AdUser'))

        if m.get('ConsecutiveFails') is not None:
            self.consecutive_fails = m.get('ConsecutiveFails')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('GmtEnabled') is not None:
            self.gmt_enabled = m.get('GmtEnabled')

        if m.get('GmtUnlock') is not None:
            self.gmt_unlock = m.get('GmtUnlock')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class DescribeVirtualMFADevicesResponseBodyVirtualMFADevicesAdUser(DaraModel):
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

