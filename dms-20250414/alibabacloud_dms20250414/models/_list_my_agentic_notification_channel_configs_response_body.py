# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class ListMyAgenticNotificationChannelConfigsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMyAgenticNotificationChannelConfigsResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of notification channel configurations for the current user.
        self.data = data
        # The error code returned when the request fails.
        self.error_code = error_code
        # The error message returned when the request fails.
        self.error_message = error_message
        # The maximum number of records per page used for this query.
        self.max_results = max_results
        # The pagination token for the next page. This parameter is empty if no more data is available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListMyAgenticNotificationChannelConfigsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMyAgenticNotificationChannelConfigsResponseBodyData(DaraModel):
    def __init__(
        self,
        channel: str = None,
        config: Dict[str, str] = None,
        enabled: bool = None,
    ):
        # The notification channel type. Valid values: FEISHU (Lark).
        self.channel = channel
        # The channel configuration information. Both keys and values are strings, which include bound identity information such as openId, mobile, or email. Sensitive values are always displayed as ****** and are not returned in plaintext.
        self.config = config
        # Indicates whether the notification channel is enabled. If the channel has never been configured, false is returned.
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

