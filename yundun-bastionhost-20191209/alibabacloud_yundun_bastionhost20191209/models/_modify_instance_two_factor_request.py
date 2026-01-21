# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceTwoFactorRequest(DaraModel):
    def __init__(
        self,
        enable_two_factor: str = None,
        instance_id: str = None,
        region_id: str = None,
        skip_two_factor_time: str = None,
        two_factor_methods: str = None,
    ):
        # Specifies whether to enable two-factor authentication. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.enable_two_factor = enable_two_factor
        # The ID of the bastion host.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The duration within which two-factor authentication is not required after a user passes two-factor authentication. Valid values: 0 to 168. Unit: hours. If you set this parameter to 0, the user must pass two-factor authentication every time the user logs on to the bastion host.
        self.skip_two_factor_time = skip_two_factor_time
        # The method used to send a verification code for two-factor authentication. If EnableTwoFactor is set to true, you must specify at least one method. Valid values:
        # 
        # *   **sms:** text message.
        # *   **email**: email.
        # *   **dingtalk**: notice in DingTalk.
        # *   **totp**: one-time password (OTP) token.
        # *   **gmusbkey**: SM-based USB key.
        self.two_factor_methods = two_factor_methods

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_two_factor is not None:
            result['EnableTwoFactor'] = self.enable_two_factor

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.skip_two_factor_time is not None:
            result['SkipTwoFactorTime'] = self.skip_two_factor_time

        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTwoFactor') is not None:
            self.enable_two_factor = m.get('EnableTwoFactor')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SkipTwoFactorTime') is not None:
            self.skip_two_factor_time = m.get('SkipTwoFactorTime')

        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')

        return self

