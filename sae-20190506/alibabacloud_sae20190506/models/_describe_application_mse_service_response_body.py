# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationMseServiceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeApplicationMseServiceResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The API status code or POP error code. Valid values: 2xx: success. 3xx: redirection. 4xx: request error. 5xx: server error.
        self.code = code
        # The MSE microservice governance application information.
        self.data = data
        # The error code. Details:
        # 
        # - If the request is successful, the **ErrorCode** parameter is not returned.
        # - If the request fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The additional information. Details:
        # 
        # - If the request is normal, **success** is returned.
        # - If the request is abnormal, a specific error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the application instance group was retrieved successfully. Valid values:
        # 
        # - **true**: The application instance group was retrieved successfully.
        # - **false**: The application instance group failed to be retrieved.
        self.success = success
        # The trace ID, which is used to precisely query trace information.
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
            temp_model = main_models.DescribeApplicationMseServiceResponseBodyData()
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

class DescribeApplicationMseServiceResponseBodyData(DaraModel):
    def __init__(
        self,
        mse_app_id: str = None,
        mse_app_name: str = None,
        mse_app_name_space: str = None,
        status: str = None,
    ):
        # The MSE microservice governance application ID.
        self.mse_app_id = mse_app_id
        # The MSE microservice governance application name.
        self.mse_app_name = mse_app_name
        # The MSE microservice governance namespace.
        self.mse_app_name_space = mse_app_name_space
        # The MSE microservice governance application status. Valid values:
        # - EXPIRED: The feature has expired or is not activated.
        # - REBOOTING: The application is restarting.
        # - WAITING: Waiting for the application to restart.
        # - FAIL: The activation failed.
        # - NULL/SUCCESS: The activation succeeded.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mse_app_id is not None:
            result['MseAppId'] = self.mse_app_id

        if self.mse_app_name is not None:
            result['MseAppName'] = self.mse_app_name

        if self.mse_app_name_space is not None:
            result['MseAppNameSpace'] = self.mse_app_name_space

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MseAppId') is not None:
            self.mse_app_id = m.get('MseAppId')

        if m.get('MseAppName') is not None:
            self.mse_app_name = m.get('MseAppName')

        if m.get('MseAppNameSpace') is not None:
            self.mse_app_name_space = m.get('MseAppNameSpace')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

