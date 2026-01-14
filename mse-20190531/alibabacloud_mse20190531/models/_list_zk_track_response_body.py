# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListZkTrackResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        traces: List[main_models.ListZkTrackResponseBodyTraces] = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count
        # The track data.
        self.traces = traces

    def validate(self):
        if self.traces:
            for v1 in self.traces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Traces'] = []
        if self.traces is not None:
            for k1 in self.traces:
                result['Traces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traces = []
        if m.get('Traces') is not None:
            for k1 in m.get('Traces'):
                temp_model = main_models.ListZkTrackResponseBodyTraces()
                self.traces.append(temp_model.from_map(k1))

        return self

class ListZkTrackResponseBodyTraces(DaraModel):
    def __init__(
        self,
        acl: str = None,
        data_type: str = None,
        event_type: str = None,
        finished: bool = None,
        log_date: str = None,
        multi_size: int = None,
        op_type: str = None,
        path: str = None,
        result: str = None,
        session_id: str = None,
        timestamp: str = None,
        trace_type: str = None,
        ttl: int = None,
        watch: bool = None,
    ):
        # The access control list (ACL).
        self.acl = acl
        # The data type. Valid values:
        # 
        # *   persist
        # *   ephemeral
        self.data_type = data_type
        # The type of the event. For trajectory of the Notify type:
        # 
        # *   NodeCreated
        # *   NodeDeleted
        # *   NodeDataChanged
        # *   NodeChildrenChanged
        self.event_type = event_type
        # Indicates whether the transaction ended.
        self.finished = finished
        # The logging time.
        self.log_date = log_date
        # The transaction size.
        self.multi_size = multi_size
        # The type of the operation. For trajectory of the Push type:
        # 
        # *   Create
        # *   Update
        # *   Delete
        # *   SetAcl
        # *   Multi
        # 
        # For trajectory of the Pull type:
        # 
        # *   GetData
        # *   GetChild
        # *   GetStat
        self.op_type = op_type
        # The path.
        self.path = path
        # The returned result.
        self.result = result
        # The session ID.
        self.session_id = session_id
        # The timestamp. It is not available.
        self.timestamp = timestamp
        # The type of the trajectory. Valid values:
        # 
        # *   Push
        # *   Pull
        # *   Notify
        self.trace_type = trace_type
        # The time to live (TTL).
        self.ttl = ttl
        # Indicates whether the monitoring feature is enabled.
        self.watch = watch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['Acl'] = self.acl

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.finished is not None:
            result['Finished'] = self.finished

        if self.log_date is not None:
            result['LogDate'] = self.log_date

        if self.multi_size is not None:
            result['MultiSize'] = self.multi_size

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.path is not None:
            result['Path'] = self.path

        if self.result is not None:
            result['Result'] = self.result

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.trace_type is not None:
            result['TraceType'] = self.trace_type

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.watch is not None:
            result['Watch'] = self.watch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acl') is not None:
            self.acl = m.get('Acl')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('LogDate') is not None:
            self.log_date = m.get('LogDate')

        if m.get('MultiSize') is not None:
            self.multi_size = m.get('MultiSize')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TraceType') is not None:
            self.trace_type = m.get('TraceType')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Watch') is not None:
            self.watch = m.get('Watch')

        return self

