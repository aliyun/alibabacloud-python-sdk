# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetInstanceTwoFactorResponseBody(DaraModel):
    def __init__(
        self,
        config: main_models.GetInstanceTwoFactorResponseBodyConfig = None,
        request_id: str = None,
    ):
        # The settings of two-factor authentication.
        self.config = config
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.GetInstanceTwoFactorResponseBodyConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInstanceTwoFactorResponseBodyConfig(DaraModel):
    def __init__(
        self,
        enable_two_factor: bool = None,
        skip_two_factor_time: int = None,
        two_factor_methods: List[str] = None,
    ):
        # Indicates whether two-factor authentication is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_two_factor = enable_two_factor
        # The duration within which two-factor authentication is not required after a local user passes two-factor authentication. Valid values: `0 to 168`. Unit: hours.
        # 
        # > If 0 is returned, a local user must pass two-factor authentication every time the local user logs on to the bastion host.
        self.skip_two_factor_time = skip_two_factor_time
        # The two-factor authentication methods.
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

        if self.skip_two_factor_time is not None:
            result['SkipTwoFactorTime'] = self.skip_two_factor_time

        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTwoFactor') is not None:
            self.enable_two_factor = m.get('EnableTwoFactor')

        if m.get('SkipTwoFactorTime') is not None:
            self.skip_two_factor_time = m.get('SkipTwoFactorTime')

        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')

        return self

