# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListCommonLogsResponseBody(DaraModel):
    def __init__(
        self,
        logs: List[main_models.ListCommonLogsResponseBodyLogs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        uid: str = None,
    ):
        # The brief information of operation logs.
        self.logs = logs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count
        # The ID of the Alibaba Cloud account.
        self.uid = uid

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.ListCommonLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class ListCommonLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        log_type: str = None,
        message: str = None,
        operator_uid: str = None,
        request_id: str = None,
        status: str = None,
        target: str = None,
        time: str = None,
    ):
        # The name of the action corresponding to the log.
        self.action = action
        # The cluster ID.
        self.cluster_id = cluster_id
        # The log type.
        self.log_type = log_type
        # The message of the log.
        self.message = message
        # The account ID of the operator.
        self.operator_uid = operator_uid
        # The request ID associated with the action that generated the log.
        self.request_id = request_id
        # The action state in the log. Valid values:
        # 
        # *   InProgress: The action is being performed.
        # *   Finished: The action is completed.
        # *   Failed: The action failed.
        self.status = status
        # The involved resource.
        self.target = target
        # The time when the log was generated.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.message is not None:
            result['Message'] = self.message

        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.target is not None:
            result['Target'] = self.target

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

