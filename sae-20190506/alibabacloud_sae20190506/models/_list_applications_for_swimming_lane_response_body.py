# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsForSwimmingLaneResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListApplicationsForSwimmingLaneResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # - **2xx**: Success.
        # 
        # - **3xx**: Redirection.
        # 
        # - **4xx**: Client error.
        # 
        # - **5xx**: Server error.
        self.code = code
        # The application list.
        self.data = data
        # The error code.
        # 
        # - The parameter is an empty string if the request is successful.
        # 
        # - This parameter is returned if the request fails. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The response message. Valid values:
        # 
        # - **success** is returned if the request is successful.
        # 
        # - A specific error code is returned if the request fails.
        self.message = message
        # The trace ID used to query the details of a request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListApplicationsForSwimmingLaneResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListApplicationsForSwimmingLaneResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        base_app_id: str = None,
        base_app_name: str = None,
        mse_app_id: str = None,
        mse_app_name: str = None,
        mse_namespace_id: str = None,
        service_tags: Dict[str, str] = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The ID of the baseline application.
        self.base_app_id = base_app_id
        # The name of the baseline application.
        self.base_app_name = base_app_name
        # The ID of the MSE instance.
        self.mse_app_id = mse_app_id
        # The name of the MSE instance.
        self.mse_app_name = mse_app_name
        # The ID of the namespace in which the MSE instance resides.
        self.mse_namespace_id = mse_namespace_id
        # The canary tags configured for the application.
        self.service_tags = service_tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.base_app_id is not None:
            result['BaseAppId'] = self.base_app_id

        if self.base_app_name is not None:
            result['BaseAppName'] = self.base_app_name

        if self.mse_app_id is not None:
            result['MseAppId'] = self.mse_app_id

        if self.mse_app_name is not None:
            result['MseAppName'] = self.mse_app_name

        if self.mse_namespace_id is not None:
            result['MseNamespaceId'] = self.mse_namespace_id

        if self.service_tags is not None:
            result['ServiceTags'] = self.service_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BaseAppId') is not None:
            self.base_app_id = m.get('BaseAppId')

        if m.get('BaseAppName') is not None:
            self.base_app_name = m.get('BaseAppName')

        if m.get('MseAppId') is not None:
            self.mse_app_id = m.get('MseAppId')

        if m.get('MseAppName') is not None:
            self.mse_app_name = m.get('MseAppName')

        if m.get('MseNamespaceId') is not None:
            self.mse_namespace_id = m.get('MseNamespaceId')

        if m.get('ServiceTags') is not None:
            self.service_tags = m.get('ServiceTags')

        return self

