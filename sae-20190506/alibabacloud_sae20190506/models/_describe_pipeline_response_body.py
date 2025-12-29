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
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The batch information.
        self.data = data
        # The error code returned if the request failed. Take note of the following rules:
        # 
        # *   The **ErrorCode** parameter is not returned if the request succeeds.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the "**Error codes**" section of this topic.
        self.error_code = error_code
        # The message returned for the operation.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the batch information was obtained. Valid values:
        # 
        # *   **true**: The information was queried.
        # *   **false**: The image failed to be found.
        self.success = success
        # The trace ID that is used to query the details of the request.
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
        # The status of the change order for the batch.
        self.co_status = co_status
        # The ID of the batch processing stage.
        self.current_stage_id = current_stage_id
        # The ID of the next batch.
        self.next_pipeline_id = next_pipeline_id
        # The ID of the batch.
        self.pipeline_id = pipeline_id
        # The name of the batch.
        self.pipeline_name = pipeline_name
        # The batch status. Valid values:
        # 
        # *   **0**: The batch is prepared for processing.
        # *   **1**: The task is being executed.
        # *   **2**: successful
        # *   **3**: The processing failed in this stage.
        # *   **6**: The batch processing was terminated.
        # *   **10**: The batch could not be processed due to a system exception.
        self.pipeline_status = pipeline_status
        # Indicates whether to start processing the next batch. Valid values:
        # 
        # *   **false**: indicates that the next batch cannot be processed yet.
        # *   **true**: indicates that the next batch can be processed now.
        self.show_batch = show_batch
        # The list of batch processing stages.
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
        # The execution type of the stage. Valid values:
        # 
        # *   **0**: in sequence.
        # *   **1**: in parallel.
        self.executor_type = executor_type
        # The ID of the stage.
        self.stage_id = stage_id
        # The name of the stage.
        self.stage_name = stage_name
        # The status of the batch processing stage. Valid values:
        # 
        # *   **0**: The batch is prepared for this processing stage.
        # *   **1**: The task is being executed.
        # *   **2**: successful
        # *   **3**: The processing failed in this stage.
        # *   **6**: The processing stage was terminated.
        self.status = status
        # The list of task statuses.
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
        # The error code returned when the task could not be executed. If the task is successfully executed, this parameter is not returned.
        self.error_code = error_code
        # Indicates whether to execute the subsequent tasks when the task failed. Valid values:
        # 
        # *   **0**: The subsequent tasks cannot be executed.
        # *   **1**: The subsequent tasks can be executed.
        self.error_ignore = error_ignore
        # The error message returned when the task could not be executed. If the task is successfully executed, this parameter is not returned.
        self.error_message = error_message
        # The returned message indicating the task execution result.
        self.message = message
        # Indicates whether a running task can be manually skipped. Valid values:
        # 
        # *   **true**: The running task can be skipped.
        # *   **false**: The zone does not allow you to change the network type of an ApsaraDB for Redis instance from classic network to VPC.
        self.show_manual_ignore = show_manual_ignore
        # The ID of the stage.
        self.stage_id = stage_id
        # The task status. Valid values:
        # 
        # *   **0**: The task is prepared for execution.
        # *   **1**: The task is being executed.
        # *   **2**: successful
        # *   **3**: The task could not be executed.
        # *   **5**: The task is pending retry.
        # *   **6**: The task was terminated.
        self.status = status
        # The ID of the task.
        self.task_id = task_id
        # The name of the task.
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

