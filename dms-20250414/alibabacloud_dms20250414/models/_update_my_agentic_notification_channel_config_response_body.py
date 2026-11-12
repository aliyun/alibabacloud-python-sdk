# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class UpdateMyAgenticNotificationChannelConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateMyAgenticNotificationChannelConfigResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The updated notification channel configuration.
        self.data = data
        # The error code returned when the request fails.
        self.error_code = error_code
        # The error message returned when the request fails.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true: The request is successful. false: The request fails.
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.UpdateMyAgenticNotificationChannelConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateMyAgenticNotificationChannelConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        channel: str = None,
        config: Dict[str, str] = None,
        enabled: bool = None,
    ):
        # The notification channel type. Valid values: FEISHU (Lark).
        self.channel = channel
        # The channel configuration information. Both keys and values are strings, including the bound identity information such as openId, mobile, or email. Sensitive values are always displayed as ******, and plaintext is not returned.
        self.config = config
        # Indicates whether the notification channel is enabled. Returns false if the channel has never been configured.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.config is not None:
            result['Config'] = self.config

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

