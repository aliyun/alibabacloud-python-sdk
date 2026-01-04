# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetPasswordComplexityConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        password_complexity_configuration: main_models.GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfiguration = None,
        request_id: str = None,
    ):
        # The password complexity configurations.
        self.password_complexity_configuration = password_complexity_configuration
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.password_complexity_configuration:
            self.password_complexity_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_complexity_configuration is not None:
            result['PasswordComplexityConfiguration'] = self.password_complexity_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordComplexityConfiguration') is not None:
            temp_model = main_models.GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfiguration()
            self.password_complexity_configuration = temp_model.from_map(m.get('PasswordComplexityConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfiguration(DaraModel):
    def __init__(
        self,
        password_complexity_rules: List[main_models.GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfigurationPasswordComplexityRules] = None,
        password_min_length: int = None,
    ):
        # The password complexity rules.
        self.password_complexity_rules = password_complexity_rules
        # The minimum number of characters in a password.
        self.password_min_length = password_min_length

    def validate(self):
        if self.password_complexity_rules:
            for v1 in self.password_complexity_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PasswordComplexityRules'] = []
        if self.password_complexity_rules is not None:
            for k1 in self.password_complexity_rules:
                result['PasswordComplexityRules'].append(k1.to_map() if k1 else None)

        if self.password_min_length is not None:
            result['PasswordMinLength'] = self.password_min_length

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.password_complexity_rules = []
        if m.get('PasswordComplexityRules') is not None:
            for k1 in m.get('PasswordComplexityRules'):
                temp_model = main_models.GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfigurationPasswordComplexityRules()
                self.password_complexity_rules.append(temp_model.from_map(k1))

        if m.get('PasswordMinLength') is not None:
            self.password_min_length = m.get('PasswordMinLength')

        return self

class GetPasswordComplexityConfigurationResponseBodyPasswordComplexityConfigurationPasswordComplexityRules(DaraModel):
    def __init__(
        self,
        password_check_type: str = None,
    ):
        # The type of the password check. Valid values:
        # 
        # *   inclusion_upper_case: The password must contain uppercase letters.
        # *   inclusion_lower_case: The password must contain lowercase letters.
        # *   inclusion_special_case: The password must contain one or more of the following special characters: @ % + \\ / \\" ! # $ ^ ? : , ( ) { } [ ] ~ - _ .
        # *   inclusion_number: The password must contain digits.
        # *   exclusion_username: The password cannot contain a username.
        # *   exclusion_email: The password cannot contain an email prefix.
        # *   exclusion_phone_number: The password cannot contain a mobile number.
        # *   exclusion_display_name: The password cannot contain a display name.
        self.password_check_type = password_check_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_check_type is not None:
            result['PasswordCheckType'] = self.password_check_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordCheckType') is not None:
            self.password_check_type = m.get('PasswordCheckType')

        return self

