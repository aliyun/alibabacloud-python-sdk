# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeConfigHistoryResponseBody(DaraModel):
    def __init__(
        self,
        config_history_items: List[main_models.DescribeConfigHistoryResponseBodyConfigHistoryItems] = None,
        request_id: str = None,
    ):
        # The change records of the configuration parameters.
        self.config_history_items = config_history_items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config_history_items:
            for v1 in self.config_history_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigHistoryItems'] = []
        if self.config_history_items is not None:
            for k1 in self.config_history_items:
                result['ConfigHistoryItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_history_items = []
        if m.get('ConfigHistoryItems') is not None:
            for k1 in m.get('ConfigHistoryItems'):
                temp_model = main_models.DescribeConfigHistoryResponseBodyConfigHistoryItems()
                self.config_history_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeConfigHistoryResponseBodyConfigHistoryItems(DaraModel):
    def __init__(
        self,
        change_id: str = None,
        owner_id: str = None,
        reason: str = None,
        success: bool = None,
        time: str = None,
    ):
        # The ID of the change record.
        self.change_id = change_id
        # The user ID (UID) of the Alibaba Cloud account.
        self.owner_id = owner_id
        # The reason for the setting modification of the configuration parameters.
        self.reason = reason
        # Indicates whether the setting modification of the configuration parameters took effect. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The time when the values of the configuration parameters were changed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_id is not None:
            result['ChangeId'] = self.change_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.success is not None:
            result['Success'] = self.success

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

