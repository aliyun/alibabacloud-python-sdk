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
        # The HTTP status code or POP error code. Valid values:
        # 
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: The request was redirected.
        # 
        # - **4xx**: A client-side error occurred.
        # 
        # - **5xx**: A server-side error occurred.
        self.code = code
        # The details of the change order.
        self.data = data
        # The error code.
        # 
        # - If the request is successful, this parameter is not returned.
        # 
        # - If the request fails, this parameter is returned. For more information, see the **error codes** section of this topic.
        self.error_code = error_code
        # The message returned for the request.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success
        # The trace ID of the request. This ID is used for troubleshooting.
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
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # Indicates whether gray tag routing is enabled.
        self.application_enable_grey_tag_route = application_enable_grey_tag_route
        # The update strategy for the application.
        self.application_update_strategy = application_update_strategy
        # The approval ID for the operation.
        self.approval_id = approval_id
        # Indicates whether to automatically release the change in batches. Valid values:
        # 
        # - **true**: The change is automatically released.
        # 
        # - **false**: The change is not automatically released.
        self.auto = auto
        # The number of batches.
        self.batch_count = batch_count
        # The release mode for batches. Valid values:
        # 
        # - **auto**: Automatic release.
        # 
        # - **manual**: Manual release.
        self.batch_type = batch_type
        # The wait time, in minutes, between batches in an automatic release.
        self.batch_wait_time = batch_wait_time
        # The change order ID.
        self.change_order_id = change_order_id
        # The change type. This parameter is a description of `CoTypeCode`.
        self.co_type = co_type
        # The change type code. Valid values:
        # 
        # - **CoBindSlb**: Binds an SLB instance.
        # 
        # - **CoUnbindSlb**: Unbinds an SLB instance.
        # 
        # - **CoCreateApp**: Creates an application.
        # 
        # - **CoDeleteApp**: Deletes an application.
        # 
        # - **CoDeploy**: Deploys an application.
        # 
        # - **CoRestartApplication**: Restarts an application.
        # 
        # - **CoRollback**: Rolls back an application.
        # 
        # - **CoScaleIn**: Scales in an application.
        # 
        # - **CoScaleOut**: Scales out an application.
        # 
        # - **CoStart**: Starts an application.
        # 
        # - **CoStop**: Stops an application.
        # 
        # - **CoRescaleApplicationVertically**: Modifies instance specifications.
        # 
        # - **CoDeployHistroy**: Rolls back to a historical version.
        # 
        # - **CoBindNas**: Binds a NAS file system.
        # 
        # - **CoUnbindNas**: Unbinds a NAS file system.
        # 
        # - **CoBatchStartApplication**: Starts applications in batches.
        # 
        # - **CoBatchStopApplication**: Stops applications in batches.
        # 
        # - **CoRestartInstances**: Restarts instances.
        # 
        # - **CoDeleteInstances**: Deletes instances.
        # 
        # - **CoScaleInAppWithInstances**: Scales in an application by specifying instances.
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
        # - **0**: Preparing
        # 
        # - **1**: In progress
        # 
        # - **2**: Succeeded
        # 
        # - **3**: Failed
        # 
        # - **6**: Terminated
        # 
        # - **8**: Awaiting manual confirmation
        # 
        # - **9**: Awaiting automatic confirmation
        # 
        # - **10**: Failed due to a system error
        # 
        # - **11**: Pending approval
        # 
        # - **12**: Approved and pending execution
        self.status = status
        # The substatus of the release order. This parameter indicates whether an exception occurred during the release. Valid values:
        # 
        # - **0**: Normal.
        # 
        # - **1**: Abnormal. For example, if a batch release fails, you must manually perform a rollback, leaving the release order in the In Progress state.
        self.sub_status = sub_status
        # Indicates whether rollback is supported. Valid values:
        # 
        # - **true**: Rollback is supported.
        # 
        # - **false**: Rollback is not supported.
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
        # The batch ID.
        self.pipeline_id = pipeline_id
        # The batch name.
        self.pipeline_name = pipeline_name
        # The start time of the batch.
        self.start_time = start_time
        # The status of the batch. Valid values:
        # 
        # - **0**: Preparing
        # 
        # - **1**: In progress
        # 
        # - **2**: Succeeded
        # 
        # - **3**: Failed
        # 
        # - **6**: Terminated
        # 
        # - **8**: Awaiting manual confirmation
        # 
        # - **9**: Awaiting automatic confirmation
        # 
        # - **10**: Failed due to a system error
        # 
        # - **11**: Pending approval
        # 
        # - **12**: Approved and pending execution
        self.status = status
        # The time when the batch was last updated.
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

