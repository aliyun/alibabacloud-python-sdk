# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ExecuteSparkReplStatementResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ExecuteSparkReplStatementResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ExecuteSparkReplStatementResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ExecuteSparkReplStatementResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_uid: int = None,
        code: str = None,
        code_state: str = None,
        code_type: str = None,
        columns: List[str] = None,
        end_time: int = None,
        error: str = None,
        output: str = None,
        output_type: str = None,
        start_time: int = None,
        statement_id: int = None,
    ):
        # The ID of the Alibaba Cloud account that owns the cluster.
        self.aliyun_uid = aliyun_uid
        # The code that is executed.
        self.code = code
        # The code execution status. Valid values:
        # 
        # *   CANCELLED
        # *   RUNNING
        # *   SUCCEEDED
        # *   ERROR
        self.code_state = code_state
        # The code type. Valid values:
        # 
        # *   SCALA
        # *   PYTHON
        self.code_type = code_type
        # The column names.
        self.columns = columns
        # The end time of the execution. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The error message.
        self.error = error
        # The code execution result, which is a JSON string that conforms to Apache Livy.
        self.output = output
        # The execution result type, which is in the JSON format. Valid values:
        # 
        # *   TEXT: the text content that conforms to Apache Livy.
        # *   TABLE: the table content that conforms to Apache Livy.
        self.output_type = output_type
        # The start time of the execution. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The unique ID of the code block in the Spark job.
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.code is not None:
            result['Code'] = self.code

        if self.code_state is not None:
            result['CodeState'] = self.code_state

        if self.code_type is not None:
            result['CodeType'] = self.code_type

        if self.columns is not None:
            result['Columns'] = self.columns

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.error is not None:
            result['Error'] = self.error

        if self.output is not None:
            result['Output'] = self.output

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statement_id is not None:
            result['StatementId'] = self.statement_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeState') is not None:
            self.code_state = m.get('CodeState')

        if m.get('CodeType') is not None:
            self.code_type = m.get('CodeType')

        if m.get('Columns') is not None:
            self.columns = m.get('Columns')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatementId') is not None:
            self.statement_id = m.get('StatementId')

        return self

