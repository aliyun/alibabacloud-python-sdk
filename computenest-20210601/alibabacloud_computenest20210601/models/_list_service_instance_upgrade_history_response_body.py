# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceUpgradeHistoryResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        upgrade_history: List[main_models.ListServiceInstanceUpgradeHistoryResponseBodyUpgradeHistory] = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The upgrade history.
        self.upgrade_history = upgrade_history

    def validate(self):
        if self.upgrade_history:
            for v1 in self.upgrade_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UpgradeHistory'] = []
        if self.upgrade_history is not None:
            for k1 in self.upgrade_history:
                result['UpgradeHistory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.upgrade_history = []
        if m.get('UpgradeHistory') is not None:
            for k1 in m.get('UpgradeHistory'):
                temp_model = main_models.ListServiceInstanceUpgradeHistoryResponseBodyUpgradeHistory()
                self.upgrade_history.append(temp_model.from_map(k1))

        return self

class ListServiceInstanceUpgradeHistoryResponseBodyUpgradeHistory(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        from_version: str = None,
        results: str = None,
        start_time: str = None,
        status: str = None,
        to_version: str = None,
        type: str = None,
        upgrade_history_id: str = None,
    ):
        # The time when the update ended.
        self.end_time = end_time
        # The version before the upgrade.
        self.from_version = from_version
        # The upgrade result.
        self.results = results
        # The time when the update started.
        self.start_time = start_time
        # The state of the update. Valid values:
        # 
        # *   upgrading: The service instance is being upgraded.
        # *   UpgradeSuccessful: The service instance is upgraded.
        # *   UpgradeFailed: The service instance failed to be upgraded.
        self.status = status
        # The version after the upgrade.
        self.to_version = to_version
        # The update type.
        self.type = type
        # The ID of the upgrade record.
        self.upgrade_history_id = upgrade_history_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.from_version is not None:
            result['FromVersion'] = self.from_version

        if self.results is not None:
            result['Results'] = self.results

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.to_version is not None:
            result['ToVersion'] = self.to_version

        if self.type is not None:
            result['Type'] = self.type

        if self.upgrade_history_id is not None:
            result['UpgradeHistoryId'] = self.upgrade_history_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FromVersion') is not None:
            self.from_version = m.get('FromVersion')

        if m.get('Results') is not None:
            self.results = m.get('Results')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ToVersion') is not None:
            self.to_version = m.get('ToVersion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpgradeHistoryId') is not None:
            self.upgrade_history_id = m.get('UpgradeHistoryId')

        return self

