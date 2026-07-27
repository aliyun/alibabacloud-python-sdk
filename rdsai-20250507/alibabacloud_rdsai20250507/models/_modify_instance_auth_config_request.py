# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceAuthConfigRequest(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        config_list: List[main_models.ModifyInstanceAuthConfigRequestConfigList] = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.branch_name = branch_name
        # The list of authentication configurations.
        self.config_list = config_list
        # The instance ID of the AI application.
        self.instance_name = instance_name
        # The region.
        self.region_id = region_id

    def validate(self):
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.ModifyInstanceAuthConfigRequestConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyInstanceAuthConfigRequestConfigList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The configuration item name. Valid values:
        # 
        # - **GOTRUE_EXTERNAL_EMAIL_ENABLED**: specifies whether to allow external email addresses.
        # - **GOTRUE_SITE_URL**: the website URL displayed when the AI application sends emails.
        # - **GOTRUE_SMTP_PORT**: the port of the SMTP provider.
        # - **GOTRUE_SMTP_SENDER_NAME**: the name of the email sender.
        # - **GOTRUE_SMTP_USER**: the username of the SMTP provider.
        # - **GOTRUE_SMTP_PASS**: the secret key of the SMTP provider.
        # - **GOTRUE_SMTP_ADMIN_EMAIL**: the email address of the SMTP provider.
        # - **GOTRUE_SMTP_HOST**: the host address of the SMTP provider.
        # - **GOTRUE_MAILER_AUTOCONFIRM**: specifies whether to enable automatic confirmation.
        # - **GOTRUE_MAILER_OTP_EXP**: the validity period of the one-time password (OTP). Unit: seconds.
        # - **GOTRUE_MAILER_OTP_LENGTH**: the length of the one-time password (OTP) verification code. The value must be an integer greater than or equal to 6.
        self.name = name
        # The value of the configuration item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

