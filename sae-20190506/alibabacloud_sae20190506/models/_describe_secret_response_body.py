# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeSecretResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSecretResponseBodyData = None,
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
        # The response.
        self.data = data
        # The error code returned. Valid values:
        # 
        # *   The **ErrorCode** parameter is not returned if the request succeeds.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # The additional information that is returned. Valid values:
        # 
        # *   success: If the call is successful, **success** is returned.
        # *   An error code: If the call fails, an error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the details of the Secret instance are successfully queried. Valid values:
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
            temp_model = main_models.DescribeSecretResponseBodyData()
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

class DescribeSecretResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        namespace_id: str = None,
        relate_apps: List[main_models.DescribeSecretResponseBodyDataRelateApps] = None,
        secret_data: Dict[str, str] = None,
        secret_id: int = None,
        secret_name: str = None,
        secret_type: str = None,
        update_time: int = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The associated application.
        self.relate_apps = relate_apps
        # Secret key-value pair data.
        self.secret_data = secret_data
        # The ID of the Secret instance.
        self.secret_id = secret_id
        # The name of the Secret instance.
        self.secret_name = secret_name
        # The type of the Secret instance.
        self.secret_type = secret_type
        # The time when the task was updated.
        self.update_time = update_time

    def validate(self):
        if self.relate_apps:
            for v1 in self.relate_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k1 in self.relate_apps:
                result['RelateApps'].append(k1.to_map() if k1 else None)

        if self.secret_data is not None:
            result['SecretData'] = self.secret_data

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.secret_type is not None:
            result['SecretType'] = self.secret_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k1 in m.get('RelateApps'):
                temp_model = main_models.DescribeSecretResponseBodyDataRelateApps()
                self.relate_apps.append(temp_model.from_map(k1))

        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeSecretResponseBodyDataRelateApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

