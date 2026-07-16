# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListAppPublishHistoryResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: main_models.ListAppPublishHistoryResponseBodyModule = None,
        next_token: str = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # Detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # is retry allowed
        self.allow_retry = allow_retry
        # frontend application Name.
        self.app_name = app_name
        # dynamic error code.
        self.dynamic_code = dynamic_code
        # dynamic message, not currently used. Please ignore.
        self.dynamic_message = dynamic_message
        # fault parameters
        self.error_args = error_args
        # Number of results per query.  
        # 
        # Value range: 10 to 100. Default Value: 20.
        self.max_results = max_results
        # Data Table module.  
        # 
        # - ABTest: experiment Data Table  
        # 
        # - ExperimentTool: experiment tool table  
        # 
        # - DataDiagnosis: Data Diagnosis
        self.module = module
        # Token for the start of the next query. It is empty if there is no next query.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # error code
        self.root_error_code = root_error_code
        # abnormal message
        self.root_error_msg = root_error_msg
        # Reserved parameter.
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Module') is not None:
            temp_model = main_models.ListAppPublishHistoryResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListAppPublishHistoryResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_publish_order_id: int = None,
        history: List[main_models.ListAppPublishHistoryResponseBodyModuleHistory] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # Current publish order ID
        self.current_publish_order_id = current_publish_order_id
        # Indicates whether to display the history of applying the alert template to application groups. Valid values:
        # 
        # - true: Display.
        # 
        # - false (default): Do not display.
        self.history = history
        # Page number. Default value is 1.
        self.page_num = page_num
        # Paging size.
        self.page_size = page_size
        # Total count.
        self.total = total

    def validate(self):
        if self.history:
            for v1 in self.history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_publish_order_id is not None:
            result['CurrentPublishOrderId'] = self.current_publish_order_id

        result['History'] = []
        if self.history is not None:
            for k1 in self.history:
                result['History'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPublishOrderId') is not None:
            self.current_publish_order_id = m.get('CurrentPublishOrderId')

        self.history = []
        if m.get('History') is not None:
            for k1 in m.get('History'):
                temp_model = main_models.ListAppPublishHistoryResponseBodyModuleHistory()
                self.history.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListAppPublishHistoryResponseBodyModuleHistory(DaraModel):
    def __init__(
        self,
        can_quick_revert: str = None,
        commit_hash: str = None,
        current_step: str = None,
        deploy_channel: str = None,
        description: str = None,
        error_step: str = None,
        is_finish: bool = None,
        is_success: bool = None,
        msg: str = None,
        order_type: str = None,
        percent: int = None,
        publish_number: str = None,
        publish_order_id: int = None,
        publish_time: str = None,
        steps: List[str] = None,
        subchannel: str = None,
    ):
        # Indicates whether quick rollback is supported.
        self.can_quick_revert = can_quick_revert
        self.commit_hash = commit_hash
        # Current step.
        self.current_step = current_step
        # Deployment channel.
        self.deploy_channel = deploy_channel
        # Application description.
        self.description = description
        # Publishing procedure.
        self.error_step = error_step
        # Indicates whether the process is complete.
        self.is_finish = is_finish
        # Indicates whether resource allocation to the cost center succeeded.
        # - true indicates success.
        # - false indicates failure.
        self.is_success = is_success
        # Error message.
        self.msg = msg
        # Sorting type: ASC or DESC.
        self.order_type = order_type
        # Transcoding progress.
        self.percent = percent
        # Publish number.
        self.publish_number = publish_number
        # Publish order ID.
        self.publish_order_id = publish_order_id
        # Published At.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.publish_time = publish_time
        # Specific widget configuration.
        self.steps = steps
        self.subchannel = subchannel

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_quick_revert is not None:
            result['CanQuickRevert'] = self.can_quick_revert

        if self.commit_hash is not None:
            result['CommitHash'] = self.commit_hash

        if self.current_step is not None:
            result['CurrentStep'] = self.current_step

        if self.deploy_channel is not None:
            result['DeployChannel'] = self.deploy_channel

        if self.description is not None:
            result['Description'] = self.description

        if self.error_step is not None:
            result['ErrorStep'] = self.error_step

        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.publish_number is not None:
            result['PublishNumber'] = self.publish_number

        if self.publish_order_id is not None:
            result['PublishOrderId'] = self.publish_order_id

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.steps is not None:
            result['Steps'] = self.steps

        if self.subchannel is not None:
            result['Subchannel'] = self.subchannel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanQuickRevert') is not None:
            self.can_quick_revert = m.get('CanQuickRevert')

        if m.get('CommitHash') is not None:
            self.commit_hash = m.get('CommitHash')

        if m.get('CurrentStep') is not None:
            self.current_step = m.get('CurrentStep')

        if m.get('DeployChannel') is not None:
            self.deploy_channel = m.get('DeployChannel')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorStep') is not None:
            self.error_step = m.get('ErrorStep')

        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('PublishNumber') is not None:
            self.publish_number = m.get('PublishNumber')

        if m.get('PublishOrderId') is not None:
            self.publish_order_id = m.get('PublishOrderId')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('Steps') is not None:
            self.steps = m.get('Steps')

        if m.get('Subchannel') is not None:
            self.subchannel = m.get('Subchannel')

        return self

