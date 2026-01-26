# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateRumAppResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.CreateRumAppResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. 2XX indicates that the request was successful. 3XX indicates that the request was redirected. 4XX indicates that a request error occurred. 5XX indicates that a server error occurred.
        self.code = code
        # The application ID and domain names. This parameter is returned if the application is created. Multiple domain names are separated with commas (,).
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateRumAppResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateRumAppResponseBodyData(DaraModel):
    def __init__(
        self,
        cdn_domain: str = None,
        endpoint: str = None,
        pid: str = None,
    ):
        # The domain name of the SDK.
        self.cdn_domain = cdn_domain
        # The endpoint that is used to report application data.
        self.endpoint = endpoint
        # The process ID (PID) of the application.
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_domain is not None:
            result['CdnDomain'] = self.cdn_domain

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.pid is not None:
            result['Pid'] = self.pid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnDomain') is not None:
            self.cdn_domain = m.get('CdnDomain')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        return self

