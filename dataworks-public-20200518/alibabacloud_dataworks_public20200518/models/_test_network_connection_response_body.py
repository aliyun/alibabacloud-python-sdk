# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class TestNetworkConnectionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        task_list: main_models.TestNetworkConnectionResponseBodyTaskList = None,
    ):
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The information about the connectivity test.
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            self.task_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_list is not None:
            result['TaskList'] = self.task_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskList') is not None:
            temp_model = main_models.TestNetworkConnectionResponseBodyTaskList()
            self.task_list = temp_model.from_map(m.get('TaskList'))

        return self

class TestNetworkConnectionResponseBodyTaskList(DaraModel):
    def __init__(
        self,
        connect_message: str = None,
        connect_status: bool = None,
    ):
        # The reason why the data source and resource group failed the connectivity test. If data source and the resource group passed the connectivity test, this parameter is left empty.
        self.connect_message = connect_message
        # The result of the connectivity test. Valid values:
        # 
        # *   true: The data source and the resource group passed the connectivity test.
        # *   false: The data source and the resource group failed the connectivity test. You can troubleshoot issues based on the ConnectMessage parameter.
        self.connect_status = connect_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_message is not None:
            result['ConnectMessage'] = self.connect_message

        if self.connect_status is not None:
            result['ConnectStatus'] = self.connect_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectMessage') is not None:
            self.connect_message = m.get('ConnectMessage')

        if m.get('ConnectStatus') is not None:
            self.connect_status = m.get('ConnectStatus')

        return self

