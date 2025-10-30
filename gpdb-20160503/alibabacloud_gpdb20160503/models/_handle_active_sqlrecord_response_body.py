# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class HandleActiveSQLRecordResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        request_id: str = None,
        results: List[main_models.HandleActiveSQLRecordResponseBodyResults] = None,
        status: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The request ID.
        self.request_id = request_id
        # The processing result of the active query.
        self.results = results
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.status = status

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.HandleActiveSQLRecordResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class HandleActiveSQLRecordResponseBodyResults(DaraModel):
    def __init__(
        self,
        pid: str = None,
        status: str = None,
    ):
        # The process ID, which is a unique identifier of the query.
        self.pid = pid
        # Indicates whether the processing was successful. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pid is not None:
            result['Pid'] = self.pid

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

