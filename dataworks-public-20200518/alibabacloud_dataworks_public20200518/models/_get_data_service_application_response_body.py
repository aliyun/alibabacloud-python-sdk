# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetDataServiceApplicationResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataServiceApplicationResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the application.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDataServiceApplicationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataServiceApplicationResponseBodyData(DaraModel):
    def __init__(
        self,
        application_code: str = None,
        application_id: int = None,
        application_key: str = None,
        application_name: str = None,
        application_secret: str = None,
        project_id: int = None,
    ):
        # The AppCode for simple authentication. You can select simple authentication or signature authentication when you call an API operation.
        self.application_code = application_code
        # The application ID.
        self.application_id = application_id
        # The AppKey for signature authentication. You can select simple authentication or signature authentication when you call an API operation.
        self.application_key = application_key
        # The name of the application.
        self.application_name = application_name
        # The AppSecret for signature authentication. You can select simple authentication or signature authentication when you call an API operation.
        self.application_secret = application_secret
        # The workspace ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_key is not None:
            result['ApplicationKey'] = self.application_key

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_secret is not None:
            result['ApplicationSecret'] = self.application_secret

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationKey') is not None:
            self.application_key = m.get('ApplicationKey')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationSecret') is not None:
            self.application_secret = m.get('ApplicationSecret')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

