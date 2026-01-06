# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class RunCloudBenchTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.RunCloudBenchTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information, including the error codes and the number of returned entries.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.RunCloudBenchTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RunCloudBenchTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        pre_check_item: List[main_models.RunCloudBenchTaskResponseBodyDataPreCheckItem] = None,
    ):
        self.pre_check_item = pre_check_item

    def validate(self):
        if self.pre_check_item:
            for v1 in self.pre_check_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PreCheckItem'] = []
        if self.pre_check_item is not None:
            for k1 in self.pre_check_item:
                result['PreCheckItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pre_check_item = []
        if m.get('PreCheckItem') is not None:
            for k1 in m.get('PreCheckItem'):
                temp_model = main_models.RunCloudBenchTaskResponseBodyDataPreCheckItem()
                self.pre_check_item.append(temp_model.from_map(k1))

        return self

class RunCloudBenchTaskResponseBodyDataPreCheckItem(DaraModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        name: str = None,
        order: int = None,
        status: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information of the check item.
        self.details = details
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The name of the check item. Valid values:
        # 
        # * **SqlArchiveStatusChecker**: checks whether SQL Explorer is available.
        # * **BenchClientEnvChecker**: checks whether the runtime environment for programs on the stress testing client is available.
        # * **SpecChecker**: checks whether the destination instance type and the instance type of the stress testing client support this API operation.
        # * **SourceInstanceChecker**: checks whether the account of the source instance is available and whether the source instance is connected to the destination instance.
        # * **BenchTargetChecker**: checks whether the account of the destination instance is available and whether the source instance is connected to the destination instance.
        self.name = name
        # The sequence number of the check item. Valid values: **0** to **10**.
        self.order = order
        # The status of the task. Valid values:
        # 
        # *   **SUCCESS**: The task is successful.
        # *   **IGNORED**: The task is ignored.
        # *   **RUNNING**: The task is running.
        # *   **EXCEPTION**: An error occurred.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.details is not None:
            result['Details'] = self.details

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

