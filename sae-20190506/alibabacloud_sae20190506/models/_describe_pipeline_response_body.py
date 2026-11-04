# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribePipelineResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribePipelineResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The API status code or POP error code. Valid values:
        # 
        # - **2xx**: Success.
        # - **3xx**: Redirect.
        # - **4xx**: Request error.
        # - **5xx**: Server error.
        self.code = code
        # The batch information.
        self.data = data
        # The error code. Valid values:
        # 
        # - Successful request: The **ErrorCode** field is not returned.
        # - Failed request: The **ErrorCode** field is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The additional information about the call result.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the batch information was queried successfully. Valid values:
        # 
        # - **true**: The query was successful.
        # - **false**: The query failed.
        self.success = success
        # The trace ID used to accurately query call information.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribePipelineResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribePipelineResponseBodyData(DaraModel):
    def __init__(
        self,
        co_status: str = None,
        current_stage_id: str = None,
        next_pipeline_id: str = None,
        pipeline_id: str = None,
        pipeline_name: str = None,
        pipeline_status: int = None,
        show_batch: bool = None,
        stage_list: List[main_models.DescribePipelineResponseBodyDataStageList] = None,
    ):
        # The status of the change order associated with the batch.
        self.co_status = co_status
        # The ID of the stage being executed in the batch.
        self.current_stage_id = current_stage_id
        # The ID of the next batch.
        self.next_pipeline_id = next_pipeline_id
        # The batch ID.
        self.pipeline_id = pipeline_id
        # The batch name.
        self.pipeline_name = pipeline_name
        # The batch status. Valid values:
        # 
        # - **0**: Ready.
        # - **1**: Running.
        # - **2**: Succeeded.
        # - **3**: Failed.
        # - **6**: Aborted.
        # - **10**: Failed due to a system exception.
        self.pipeline_status = pipeline_status
        # Specifies whether the execution of the next batch can start. Valid values:
        # 
        # - **false**: The execution of the next batch cannot start.
        # - **true**: The execution of the next batch can start.
        self.show_batch = show_batch
        # The list of stages in the batch.
        self.stage_list = stage_list

    def validate(self):
        if self.stage_list:
            for v1 in self.stage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.co_status is not None:
            result['CoStatus'] = self.co_status

        if self.current_stage_id is not None:
            result['CurrentStageId'] = self.current_stage_id

        if self.next_pipeline_id is not None:
            result['NextPipelineId'] = self.next_pipeline_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name

        if self.pipeline_status is not None:
            result['PipelineStatus'] = self.pipeline_status

        if self.show_batch is not None:
            result['ShowBatch'] = self.show_batch

        result['StageList'] = []
        if self.stage_list is not None:
            for k1 in self.stage_list:
                result['StageList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')

        if m.get('CurrentStageId') is not None:
            self.current_stage_id = m.get('CurrentStageId')

        if m.get('NextPipelineId') is not None:
            self.next_pipeline_id = m.get('NextPipelineId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')

        if m.get('PipelineStatus') is not None:
            self.pipeline_status = m.get('PipelineStatus')

        if m.get('ShowBatch') is not None:
            self.show_batch = m.get('ShowBatch')

        self.stage_list = []
        if m.get('StageList') is not None:
            for k1 in m.get('StageList'):
                temp_model = main_models.DescribePipelineResponseBodyDataStageList()
                self.stage_list.append(temp_model.from_map(k1))

        return self

class DescribePipelineResponseBodyDataStageList(DaraModel):
    def __init__(
        self,
        executor_type: int = None,
        stage_id: str = None,
        stage_name: str = None,
        status: int = None,
        task_list: List[main_models.DescribePipelineResponseBodyDataStageListTaskList] = None,
    ):
        # The stage type. Valid values:
        # 
        # - **0**: Serial.
        # - **1**: Parallel.
        self.executor_type = executor_type
        # The stage ID.
        self.stage_id = stage_id
        # The stage name.
        self.stage_name = stage_name
        # The stage status. Valid values:
        # 
        # - **0**: Ready.
        # - **1**: Running.
        # - **2**: Succeeded.
        # - **3**: Failed.
        # - **6**: Aborted.
        self.status = status
        # The list of task status information.
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for v1 in self.task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_type is not None:
            result['ExecutorType'] = self.executor_type

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.status is not None:
            result['Status'] = self.status

        result['TaskList'] = []
        if self.task_list is not None:
            for k1 in self.task_list:
                result['TaskList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorType') is not None:
            self.executor_type = m.get('ExecutorType')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.task_list = []
        if m.get('TaskList') is not None:
            for k1 in m.get('TaskList'):
                temp_model = main_models.DescribePipelineResponseBodyDataStageListTaskList()
                self.task_list.append(temp_model.from_map(k1))

        return self

class DescribePipelineResponseBodyDataStageListTaskList(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_ignore: int = None,
        error_message: str = None,
        message: str = None,
        show_manual_ignore: bool = None,
        stage_id: str = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        # The error code for the task execution failure. This code is not returned if the task succeeds.
        self.error_code = error_code
        # Specifies whether subsequent tasks can be executed after a failure. Valid values:
        # 
        # - **0**: Not supported.
        # - **1**: Supported.
        self.error_ignore = error_ignore
        # The error message for the task execution. This message is not returned if the task succeeds.
        self.error_message = error_message
        # The task execution information.
        self.message = message
        # Specifies whether a running task can be manually skipped. Valid values:
        # - **true**: Supported.
        # - **false**: Not supported.
        self.show_manual_ignore = show_manual_ignore
        # The stage ID.
        self.stage_id = stage_id
        # The task status. Valid values:
        # 
        # - **0**: Ready.
        # - **1**: Running.
        # - **2**: Succeeded.
        # - **3**: Failed.
        # - **5**: Waiting for retry.
        # - **6**: Aborted.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_ignore is not None:
            result['ErrorIgnore'] = self.error_ignore

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.message is not None:
            result['Message'] = self.message

        if self.show_manual_ignore is not None:
            result['ShowManualIgnore'] = self.show_manual_ignore

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorIgnore') is not None:
            self.error_ignore = m.get('ErrorIgnore')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ShowManualIgnore') is not None:
            self.show_manual_ignore = m.get('ShowManualIgnore')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

