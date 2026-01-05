# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class TestDataSourceConnectivityResponseBody(DaraModel):
    def __init__(
        self,
        connectivity: main_models.TestDataSourceConnectivityResponseBodyConnectivity = None,
        request_id: str = None,
    ):
        # The details of the connectivity test.
        self.connectivity = connectivity
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.connectivity:
            self.connectivity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connectivity is not None:
            result['Connectivity'] = self.connectivity.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connectivity') is not None:
            temp_model = main_models.TestDataSourceConnectivityResponseBodyConnectivity()
            self.connectivity = temp_model.from_map(m.get('Connectivity'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TestDataSourceConnectivityResponseBodyConnectivity(DaraModel):
    def __init__(
        self,
        connect_message: str = None,
        connect_state: str = None,
        detail_logs: List[main_models.TestDataSourceConnectivityResponseBodyConnectivityDetailLogs] = None,
    ):
        # The error message returned if the connectivity test fails. No such a message is returned if the connectivity test is successful.
        self.connect_message = connect_message
        # The result of the connectivity test. Valid values: Connectable: The network can be connected. ConfigError: The network can be connected, but the configurations are incorrect. Unreachable: The network cannot be connected. Unsupport: An error is reported due to other causes. For example, the desired resource group is being initialized.
        self.connect_state = connect_state
        # The detailed logs of each step in the connectivity test.
        self.detail_logs = detail_logs

    def validate(self):
        if self.detail_logs:
            for v1 in self.detail_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_message is not None:
            result['ConnectMessage'] = self.connect_message

        if self.connect_state is not None:
            result['ConnectState'] = self.connect_state

        result['DetailLogs'] = []
        if self.detail_logs is not None:
            for k1 in self.detail_logs:
                result['DetailLogs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectMessage') is not None:
            self.connect_message = m.get('ConnectMessage')

        if m.get('ConnectState') is not None:
            self.connect_state = m.get('ConnectState')

        self.detail_logs = []
        if m.get('DetailLogs') is not None:
            for k1 in m.get('DetailLogs'):
                temp_model = main_models.TestDataSourceConnectivityResponseBodyConnectivityDetailLogs()
                self.detail_logs.append(temp_model.from_map(k1))

        return self

class TestDataSourceConnectivityResponseBodyConnectivityDetailLogs(DaraModel):
    def __init__(
        self,
        code: str = None,
        end_time: int = None,
        message: str = None,
        start_time: int = None,
    ):
        # The code of the test item.
        self.code = code
        # The end time of a step.
        self.end_time = end_time
        # The name of the step.
        self.message = message
        # The start time of a step.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.message is not None:
            result['Message'] = self.message

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

