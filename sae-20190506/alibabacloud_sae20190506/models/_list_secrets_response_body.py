# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListSecretsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListSecretsResponseBodyData = None,
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
        # The data returned.
        self.data = data
        # The error code returned. Take note of the following rules:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the "**Error codes**" section in this topic.
        self.error_code = error_code
        # The returned message. Take note of the following rules:
        # 
        # *   If the call is successful, **success** is returned.
        # *   If the call fails, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.ListSecretsResponseBodyData()
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

class ListSecretsResponseBodyData(DaraModel):
    def __init__(
        self,
        secrets: List[main_models.ListSecretsResponseBodyDataSecrets] = None,
    ):
        # The Secrets.
        self.secrets = secrets

    def validate(self):
        if self.secrets:
            for v1 in self.secrets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Secrets'] = []
        if self.secrets is not None:
            for k1 in self.secrets:
                result['Secrets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.secrets = []
        if m.get('Secrets') is not None:
            for k1 in m.get('Secrets'):
                temp_model = main_models.ListSecretsResponseBodyDataSecrets()
                self.secrets.append(temp_model.from_map(k1))

        return self

class ListSecretsResponseBodyDataSecrets(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        namespace_id: str = None,
        relate_apps: List[main_models.ListSecretsResponseBodyDataSecretsRelateApps] = None,
        secret_id: int = None,
        secret_name: str = None,
        secret_type: str = None,
        update_time: int = None,
    ):
        # The time when the Secret was created.
        self.create_time = create_time
        # The namespace ID.
        self.namespace_id = namespace_id
        # The associated applications.
        self.relate_apps = relate_apps
        # The Secret ID.
        self.secret_id = secret_id
        # The Secret name.
        self.secret_name = secret_name
        # The Secret type.
        # 
        # Set the value to **kubernetes.io/dockerconfigjson**. The value indicates the secret for the username and password of the image repository and is used for authentication when images are pulled during application deployment.
        self.secret_type = secret_type
        # The time when the Secret was updated.
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
                temp_model = main_models.ListSecretsResponseBodyDataSecretsRelateApps()
                self.relate_apps.append(temp_model.from_map(k1))

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListSecretsResponseBodyDataSecretsRelateApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The application name.
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

