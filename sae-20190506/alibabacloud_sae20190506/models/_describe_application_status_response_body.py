# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeApplicationStatusResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: The request was successful.
        # 
        # - **3xx**: The request was redirected.
        # 
        # - **4xx**: The request was invalid.
        # 
        # - **5xx**: A server error occurred.
        self.code = code
        # The response data.
        self.data = data
        # The error code.
        # 
        # - If the request is successful, this parameter is not returned.
        # 
        # - If the request fails, this parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The response message.
        # 
        # - If the call is successful, **success** is returned.
        # 
        # - If the call fails, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the application status was obtained. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        self.success = success
        # The trace ID that is used to query the details of a request.
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
            temp_model = main_models.DescribeApplicationStatusResponseBodyData()
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

class DescribeApplicationStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        arms_advanced_enabled: str = None,
        arms_apm_info: str = None,
        create_time: str = None,
        current_status: str = None,
        enable_agent: bool = None,
        file_size_limit: int = None,
        last_change_order_id: str = None,
        last_change_order_running: bool = None,
        last_change_order_status: str = None,
        running_instances: int = None,
        sub_status: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # Indicates whether ARMS Advanced Edition is enabled. Valid values:
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.arms_advanced_enabled = arms_advanced_enabled
        # The metadata of the application in ARMS.
        self.arms_apm_info = arms_apm_info
        # The time when the application was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The current status of the application. Valid values:
        # 
        # - **RUNNING**: The application is running.
        # 
        # - **STOPPED**: The application is stopped.
        # 
        # - **UNKNOWN**: The application status is unknown.
        self.current_status = current_status
        # Indicates whether the SAE agent is enabled. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        self.enable_agent = enable_agent
        # The file size limit. Unit: KB. Valid values: 0 to 10240.
        self.file_size_limit = file_size_limit
        # The ID of the most recently executed change order. This parameter is empty if no change order was executed or if the information about the change order has expired.
        self.last_change_order_id = last_change_order_id
        # Indicates whether the most recent change order is being executed. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        self.last_change_order_running = last_change_order_running
        # The status of the most recent change order. Valid values:
        # 
        # - **READY**: The change order is ready.
        # 
        # - **RUNNING**: The change order is being executed.
        # 
        # - **SUCCESS**: The change order was successful.
        # 
        # - **FAIL**: The change order failed.
        # 
        # - **ABORT**: The change order was aborted.
        # 
        # - **WAIT_BATCH_CONFIRM**: The change order is waiting for manual confirmation for the next batch.
        # 
        # - **AUTO_BATCH_WAIT**: The change order is in a waiting state for an automatic batch.
        # 
        # - **SYSTEM_FAIL**: A system error occurred.
        # 
        # - **WAIT_APPROVAL**: The change order is pending approval.
        # 
        # - **APPROVED**: The change order is approved and is pending execution.
        self.last_change_order_status = last_change_order_status
        # The number of running instances of the application.
        self.running_instances = running_instances
        # The substatus of the change order. This parameter is used to determine whether an exception occurs during the release process. Valid values:
        # 
        # - **NORMAL**: The release is normal.
        # 
        # - **RUNNING_BUT_HAS_ERROR**: The release is abnormal. For example, if an error occurs during a phased release, you must manually roll back the release. In this case, the change order cannot be completed and the status of the change order remains **RUNNING**.
        self.sub_status = sub_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.arms_advanced_enabled is not None:
            result['ArmsAdvancedEnabled'] = self.arms_advanced_enabled

        if self.arms_apm_info is not None:
            result['ArmsApmInfo'] = self.arms_apm_info

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status

        if self.enable_agent is not None:
            result['EnableAgent'] = self.enable_agent

        if self.file_size_limit is not None:
            result['FileSizeLimit'] = self.file_size_limit

        if self.last_change_order_id is not None:
            result['LastChangeOrderId'] = self.last_change_order_id

        if self.last_change_order_running is not None:
            result['LastChangeOrderRunning'] = self.last_change_order_running

        if self.last_change_order_status is not None:
            result['LastChangeOrderStatus'] = self.last_change_order_status

        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances

        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ArmsAdvancedEnabled') is not None:
            self.arms_advanced_enabled = m.get('ArmsAdvancedEnabled')

        if m.get('ArmsApmInfo') is not None:
            self.arms_apm_info = m.get('ArmsApmInfo')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')

        if m.get('EnableAgent') is not None:
            self.enable_agent = m.get('EnableAgent')

        if m.get('FileSizeLimit') is not None:
            self.file_size_limit = m.get('FileSizeLimit')

        if m.get('LastChangeOrderId') is not None:
            self.last_change_order_id = m.get('LastChangeOrderId')

        if m.get('LastChangeOrderRunning') is not None:
            self.last_change_order_running = m.get('LastChangeOrderRunning')

        if m.get('LastChangeOrderStatus') is not None:
            self.last_change_order_status = m.get('LastChangeOrderStatus')

        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')

        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')

        return self

