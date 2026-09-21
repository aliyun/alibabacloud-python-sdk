# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class ModifyForwardSqlLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ModifyForwardSqlLogConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code.
        self.code = code
        # ForwardSqlLogResult
        self.data = data
        # The returned message.
        # 
        # > If the request is successful, **Successful** is returned. If the request fails, an error message that contains information such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # * true: The request is successful.
        # * false: The request fails.
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

        if m.get('Data') is not None:
            temp_model = main_models.ModifyForwardSqlLogConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ModifyForwardSqlLogConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        vpc_endpoint: str = None,
    ):
        # The LogStore name for real-time delivery to Simple Log Service.
        self.logstore = logstore
        # The project.
        self.project = project
        # The VPC endpoint of the component.
        self.vpc_endpoint = vpc_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project is not None:
            result['Project'] = self.project

        if self.vpc_endpoint is not None:
            result['VpcEndpoint'] = self.vpc_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('VpcEndpoint') is not None:
            self.vpc_endpoint = m.get('VpcEndpoint')

        return self

