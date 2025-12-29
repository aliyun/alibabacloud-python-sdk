# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeChangeOrderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeChangeOrderResponseBodyData = None,
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
        # The details of the change order.
        self.data = data
        # The error code. Valid values:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the information of the change order was queried. Valid values:
        # 
        # *   **true**: The information was queried.
        # *   **false**: The information failed to be queried.
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
            temp_model = main_models.DescribeChangeOrderResponseBodyData()
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

class DescribeChangeOrderResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        application_enable_grey_tag_route: bool = None,
        application_update_strategy: str = None,
        approval_id: str = None,
        auto: bool = None,
        batch_count: int = None,
        batch_type: str = None,
        batch_wait_time: int = None,
        change_order_id: str = None,
        co_type: str = None,
        co_type_code: str = None,
        create_time: str = None,
        current_pipeline_id: str = None,
        description: str = None,
        error_message: str = None,
        pipelines: List[main_models.DescribeChangeOrderResponseBodyDataPipelines] = None,
        status: int = None,
        sub_status: int = None,
        support_rollback: bool = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        self.application_enable_grey_tag_route = application_enable_grey_tag_route
        self.application_update_strategy = application_update_strategy
        # The approval ID of the change order.
        self.approval_id = approval_id
        # Indicates whether SAE automatically releases the batches. Valid values:
        # 
        # *   **true**: SAE automatically releases the batches.
        # *   **false**: SAE does not automatically release the batches.
        self.auto = auto
        # The number of release batches.
        self.batch_count = batch_count
        # The processing method for the batches. Valid values:
        # 
        # *   **auto**: SAE automatically releases the batches.
        # *   **Manual**: You must manually release the batches.
        self.batch_type = batch_type
        # The interval between batches in a phased release. SAE automatically releases batches at the specified interval. Unit: minutes.
        self.batch_wait_time = batch_wait_time
        # The ID of the change order.
        self.change_order_id = change_order_id
        # The change type, which corresponds to the **CoTypeCode** parameter.
        self.co_type = co_type
        # The code of the change type. Valid values:
        # 
        # *   **CoBindSlb**: associates a Sever Load Balancer (SLB) instance with the application.
        # *   **CoUnbindSlb**: disassociates the SLB instance from the application.
        # *   **CoCreateApp**: creates the application.
        # *   **CoDeleteApp**: deletes the application.
        # *   **CoDeploy**: deploys the application.
        # *   **CoRestartApplication**: restarts the application.
        # *   **CoRollback**: rolls back the application.
        # *   **CoScaleIn**: scales in the application.
        # *   **CoScaleOut**: scales out the application.
        # *   **CoStart**: starts the application.
        # *   **CoStop**: stops the application.
        # *   **CoRescaleApplicationVertically**: modifies the instance type.
        # *   **CoDeployHistroy**: rolls back the application to a historical version.
        # *   **CoBindNas**: associates a NAS file system with the application.
        # *   **CoUnbindNas**: disassociates the NAS file system from the application.
        # *   **CoBatchStartApplication**: starts multiple applications concurrently.
        # *   **CoBatchStopApplication**: stops multiple applications concurrently.
        # *   **CoRestartInstances**: restarts the instances.
        # *   **CoDeleteInstances**: deletes the instances.
        # *   **CoScaleInAppWithInstances**: reduces the specified number of application instances.
        self.co_type_code = co_type_code
        # The time when the change order was created.
        self.create_time = create_time
        # The ID of the current batch.
        self.current_pipeline_id = current_pipeline_id
        # The description of the change order.
        self.description = description
        # The error message.
        self.error_message = error_message
        # The batch information.
        self.pipelines = pipelines
        # The status of the change order. Valid values:
        # 
        # *   **0**: The change order is being prepared.
        # *   **1**: The change order is being executed.
        # *   **2**: The change order was executed.
        # *   **3**: The change order failed to be executed.
        # *   **6**: The change order was terminated.
        # *   **8**: The execution process is pending. You must manually release the batches.
        # *   **9**: The execution process is pending. SAE will automatically release the batches.
        # *   **10**: The execution failed due to a system exception.
        # *   **11**: The change order is pending approval.
        # *   **12**: The change order is approved and is pending execution.
        self.status = status
        # The substatus of the change order. This parameter indicates whether an exception occurred while the change order was being executed. Valid values:
        # 
        # *   **0**: No exception occurred.
        # *   **1**: An exception occurred. For example, if an error occurs during a phased release, you must manually roll back the application. In this case, the change order cannot be completed, so the Status parameter is still displayed as "1", which indicates that the change order is being executed. You can check the value of this parameter to determine whether an exception occurs.
        self.sub_status = sub_status
        # Indicates whether the application can be rolled back. Valid values:
        # 
        # *   **true**: The application can be rolled back.
        # *   **false**: The application cannot be rolled back.
        self.support_rollback = support_rollback

    def validate(self):
        if self.pipelines:
            for v1 in self.pipelines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.application_enable_grey_tag_route is not None:
            result['ApplicationEnableGreyTagRoute'] = self.application_enable_grey_tag_route

        if self.application_update_strategy is not None:
            result['ApplicationUpdateStrategy'] = self.application_update_strategy

        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id

        if self.auto is not None:
            result['Auto'] = self.auto

        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count

        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time

        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.co_type is not None:
            result['CoType'] = self.co_type

        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.current_pipeline_id is not None:
            result['CurrentPipelineId'] = self.current_pipeline_id

        if self.description is not None:
            result['Description'] = self.description

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['Pipelines'] = []
        if self.pipelines is not None:
            for k1 in self.pipelines:
                result['Pipelines'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        if self.support_rollback is not None:
            result['SupportRollback'] = self.support_rollback

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ApplicationEnableGreyTagRoute') is not None:
            self.application_enable_grey_tag_route = m.get('ApplicationEnableGreyTagRoute')

        if m.get('ApplicationUpdateStrategy') is not None:
            self.application_update_strategy = m.get('ApplicationUpdateStrategy')

        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')

        if m.get('Auto') is not None:
            self.auto = m.get('Auto')

        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')

        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')

        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')

        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentPipelineId') is not None:
            self.current_pipeline_id = m.get('CurrentPipelineId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.pipelines = []
        if m.get('Pipelines') is not None:
            for k1 in m.get('Pipelines'):
                temp_model = main_models.DescribeChangeOrderResponseBodyDataPipelines()
                self.pipelines.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        if m.get('SupportRollback') is not None:
            self.support_rollback = m.get('SupportRollback')

        return self

class DescribeChangeOrderResponseBodyDataPipelines(DaraModel):
    def __init__(
        self,
        batch_type: int = None,
        parallel_count: int = None,
        pipeline_id: str = None,
        pipeline_name: str = None,
        start_time: int = None,
        status: int = None,
        update_time: int = None,
    ):
        # The batch type.
        self.batch_type = batch_type
        # The number of parallel tasks in a batch.
        self.parallel_count = parallel_count
        # The ID of the batch.
        self.pipeline_id = pipeline_id
        # The name of the batch.
        self.pipeline_name = pipeline_name
        # The time when the batch processing started.
        self.start_time = start_time
        # The status of the batch. Valid values:
        # 
        # *   **0**: The batch is being prepared.
        # *   **1**: The batch is being processed.
        # *   **2**: The batch was processed.
        # *   **3**: The batch failed to be processed.
        # *   **6**: The batch processing was terminated.
        # *   **8**: The execution process is pending. You must manually release the batch.
        # *   **9**: The execution process is pending. SAE will automatically release the batch.
        # *   **10**: The batch failed to be processed due to a system exception.
        # *   **11**: The batch is pending approval.
        # *   **12**: The batch is approved and is pending execution.
        self.status = status
        # The time when the batch information was last modified.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.parallel_count is not None:
            result['ParallelCount'] = self.parallel_count

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('ParallelCount') is not None:
            self.parallel_count = m.get('ParallelCount')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

