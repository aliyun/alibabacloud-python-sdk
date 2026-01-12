# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class CredentialRole(DaraModel):
    def __init__(
        self,
        assume_role_for: str = None,
        assume_user_info: main_models.AssumeUserInfo = None,
        policy: str = None,
        role_arn: str = None,
        role_type: str = None,
    ):
        self.assume_role_for = assume_role_for
        self.assume_user_info = assume_user_info
        self.policy = policy
        self.role_arn = role_arn
        self.role_type = role_type

    def validate(self):
        if self.assume_user_info:
            self.assume_user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.assume_user_info is not None:
            result['AssumeUserInfo'] = self.assume_user_info.to_map()

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('AssumeUserInfo') is not None:
            temp_model = main_models.AssumeUserInfo()
            self.assume_user_info = temp_model.from_map(m.get('AssumeUserInfo'))

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

