# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetStreamTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetStreamTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The basic information and running information of the real-time task instance. The fileId can be used to subsequently query operation records and historical running instances.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend response exception.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetStreamTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStreamTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        consume_location_date: str = None,
        engine_version: str = None,
        file_id: str = None,
        name: str = None,
        node_id: str = None,
        operator_id: str = None,
        operator_name: str = None,
        project_id: int = None,
        project_mode: str = None,
        project_name: str = None,
        resource_queue: str = None,
        status: str = None,
        task_id: str = None,
        type: str = None,
    ):
        # The time corresponding to the latest read position. The format is yyyy-MM-dd HH:mm:ss. If no consumption metrics are available, the value is null.
        self.consume_location_date = consume_location_date
        # The database engine version of the compute DPI engine used to run the node.
        self.engine_version = engine_version
        # The ID of the task file. This corresponds to the FileId request parameter in ListStreamOpsRecords and ListStreamInstanceRecords. It is not a nodeId or a template file ID.
        self.file_id = file_id
        # The name of the node to which the real-time task belongs.
        self.name = name
        # The ID of the node. The ID starts with n_ and identifies a development node. It is different from the task file ID.
        self.node_id = node_id
        # The ID of the user who last operated the task.
        self.operator_id = operator_id
        # The display name of the user who last operated the task.
        self.operator_name = operator_name
        # The ID of the Dataphin project to which the task belongs.
        self.project_id = project_id
        # The project mode. Valid values: BASIC for the basic mode, and DEV_PROD for the development-production isolation mode.
        self.project_mode = project_mode
        # The name of the Dataphin project to which the task belongs.
        self.project_name = project_name
        # The display information of the resource queue used by the task, including the queue name and ID.
        self.resource_queue = resource_queue
        # The running status of the task. The original TaskStatusEnum enumeration name is returned. Common real-time statuses include: STREAMING_STARTING (starting), STREAMING_RUNNING (running), STREAMING_PAUSING (pausing), STREAMING_PAUSED (paused), STREAMING_RESUMING (resuming), STREAMING_STOPPING (stopping), STREAMING_STOPPED (stopped), STREAMING_INIT (initial status), STREAMING_FAILED (running exception), STREAMING_START_FAILED (start exception), STREAMING_RESUME_FAILED (resume exception), and STREAMING_FINISHED (completed). Other known statuses also return the original enumeration name. If the status cannot be identified, UNKNOWN is returned. If the original status is empty, null is returned.
        self.status = status
        # Instance ID of the real-time task instance. Instance ID starts with t_ and corresponds to the TaskId request parameter in GetStreamTask.
        self.task_id = task_id
        # The type of the task, such as REAL_TIME_PIPELINE (real-time integration), FLINK_SQL (SQL task), FLINK_TEMPLATE_SQL (template task), and FLINK_DATASTREAM (DataStream task).
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_location_date is not None:
            result['ConsumeLocationDate'] = self.consume_location_date

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_mode is not None:
            result['ProjectMode'] = self.project_mode

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.resource_queue is not None:
            result['ResourceQueue'] = self.resource_queue

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeLocationDate') is not None:
            self.consume_location_date = m.get('ConsumeLocationDate')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectMode') is not None:
            self.project_mode = m.get('ProjectMode')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ResourceQueue') is not None:
            self.resource_queue = m.get('ResourceQueue')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

