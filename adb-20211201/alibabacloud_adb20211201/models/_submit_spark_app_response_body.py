# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class SubmitSparkAppResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SubmitSparkAppResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SubmitSparkAppResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SubmitSparkAppResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        message: str = None,
        state: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The alert message returned for the operation, such as task execution failure or insufficient resources. If no alert occurs, null is returned.
        self.message = message
        # The execution state of the application. Valid values:
        # 
        # *   **SUBMITTED**
        # *   **STARTING**
        # *   **RUNNING**
        # *   **FAILING**
        # *   **FAILED**
        # *   **KILLING**
        # *   **KILLED**
        # *   **SUCCEEDING**
        # *   **COMPLETED**
        # *   **FATAL**
        # *   **UNKNOWN**
        self.state = state

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

        if self.message is not None:
            result['Message'] = self.message

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

