# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAITaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbcluster_id: str = None,
        request_id: str = None,
        status: str = None,
        status_name: str = None,
    ):
        # The name of the database account that is used to connect to the AI nodes in the cluster.
        self.account_name = account_name
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id
        # The status of the PolarDB for AI feature. Valid values:
        # 
        # *   **1**: enabled.
        # *   **2**: disabled.
        self.status = status
        # The description of the status of the PolarDB for AI feature.
        self.status_name = status_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        return self

