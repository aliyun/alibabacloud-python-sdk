# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetPasswordHistoryConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        password_history_configuration: main_models.GetPasswordHistoryConfigurationResponseBodyPasswordHistoryConfiguration = None,
        request_id: str = None,
    ):
        # The password history configurations.
        self.password_history_configuration = password_history_configuration
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.password_history_configuration:
            self.password_history_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_history_configuration is not None:
            result['PasswordHistoryConfiguration'] = self.password_history_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordHistoryConfiguration') is not None:
            temp_model = main_models.GetPasswordHistoryConfigurationResponseBodyPasswordHistoryConfiguration()
            self.password_history_configuration = temp_model.from_map(m.get('PasswordHistoryConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPasswordHistoryConfigurationResponseBodyPasswordHistoryConfiguration(DaraModel):
    def __init__(
        self,
        password_history_max_retention: int = None,
        password_history_status: str = None,
    ):
        # The maximum number of recent passwords that are retained.
        self.password_history_max_retention = password_history_max_retention
        # Indicates whether the password history feature is enabled. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.password_history_status = password_history_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password_history_max_retention is not None:
            result['PasswordHistoryMaxRetention'] = self.password_history_max_retention

        if self.password_history_status is not None:
            result['PasswordHistoryStatus'] = self.password_history_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PasswordHistoryMaxRetention') is not None:
            self.password_history_max_retention = m.get('PasswordHistoryMaxRetention')

        if m.get('PasswordHistoryStatus') is not None:
            self.password_history_status = m.get('PasswordHistoryStatus')

        return self

