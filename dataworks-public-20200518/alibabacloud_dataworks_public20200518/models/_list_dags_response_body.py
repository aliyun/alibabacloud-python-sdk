# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListDagsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDagsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of DAGs.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDagsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDagsResponseBodyData(DaraModel):
    def __init__(
        self,
        dags: List[main_models.ListDagsResponseBodyDataDags] = None,
    ):
        # The entities returned.
        self.dags = dags

    def validate(self):
        if self.dags:
            for v1 in self.dags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dags'] = []
        if self.dags is not None:
            for k1 in self.dags:
                result['Dags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dags = []
        if m.get('Dags') is not None:
            for k1 in m.get('Dags'):
                temp_model = main_models.ListDagsResponseBodyDataDags()
                self.dags.append(temp_model.from_map(k1))

        return self

class ListDagsResponseBodyDataDags(DaraModel):
    def __init__(
        self,
        bizdate: int = None,
        create_time: int = None,
        create_user: str = None,
        dag_id: int = None,
        finish_time: int = None,
        gmtdate: int = None,
        modify_time: int = None,
        name: str = None,
        op_seq: int = None,
        project_id: int = None,
        start_time: int = None,
        status: str = None,
        type: str = None,
    ):
        # The data timestamp.
        self.bizdate = bizdate
        # The creation time.
        self.create_time = create_time
        # The creator.
        self.create_user = create_user
        # The DAG ID.
        self.dag_id = dag_id
        # The end time.
        self.finish_time = finish_time
        # The actual running time.
        self.gmtdate = gmtdate
        # The modification time.
        self.modify_time = modify_time
        # The name of the DAG.
        self.name = name
        # The sequence number of the operation.
        self.op_seq = op_seq
        # The workspace ID.
        self.project_id = project_id
        # The start time.
        self.start_time = start_time
        # The status of the DAG. Valid values:
        # 
        # *   CREATED
        # *   RUNNING
        # *   FAILURE
        # *   SUCCESS
        self.status = status
        # The type of the DAG. Valid values:
        # 
        # *   MANUAL: DAG for a manually triggered workflow
        # *   SMOKE_TEST: DAG for a smoke testing workflow
        # *   SUPPLY_DATA: DAG for a data backfill instance
        # *   BUSINESS_PROCESS_DAG: DAG for a one-time workflow
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.gmtdate is not None:
            result['Gmtdate'] = self.gmtdate

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.op_seq is not None:
            result['OpSeq'] = self.op_seq

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Gmtdate') is not None:
            self.gmtdate = m.get('Gmtdate')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpSeq') is not None:
            self.op_seq = m.get('OpSeq')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

