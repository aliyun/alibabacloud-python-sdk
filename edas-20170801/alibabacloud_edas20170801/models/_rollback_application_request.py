# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RollbackApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        batch: int = None,
        batch_wait_time: int = None,
        group_id: str = None,
        history_version: str = None,
    ):
        # The application ID. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/423162.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The number of batches for the rollback. Default value: 1. Valid values: 1 to 5.
        self.batch = batch
        # The wait time between batches. Default value: 0. The default value indicates no wait time. Valid values: 0 to 5. Unit: minutes.
        self.batch_wait_time = batch_wait_time
        # The application group ID. You can call the ListDeployGroup operation to query the application group ID. For more information, see [ListDeployGroup](https://help.aliyun.com/document_detail/423184.html).
        # 
        # If you need to roll back the application in all application groups, set this parameter to `all`.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The historical version to which you want to roll back the application. Call the ListHistoryDeployVersion operation to query the historical versions of the application. Then, set this parameter based on the returned value of `PackageVersion`. For more information, see [ListHistoryDeployVersion](https://help.aliyun.com/document_detail/423163.html).
        # 
        # This parameter is required.
        self.history_version = history_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.batch is not None:
            result['Batch'] = self.batch

        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Batch') is not None:
            self.batch = m.get('Batch')

        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')

        return self

