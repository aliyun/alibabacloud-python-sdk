# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListExportZookeeperDataResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListExportZookeeperDataResponseBodyData] = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the data.
        self.data = data
        # The dynamic part in the error message. This parameter is used to replace the \\*\\*%s\\*\\* variable in the **ErrMessage** parameter.
        # 
        # > If the return value of the **ErrMessage** parameter is **The Value of Input Parameter %s is not valid** and the return value of the **DynamicMessage** parameter is **DtsJobId**, the specified **DtsJobId** parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListExportZookeeperDataResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListExportZookeeperDataResponseBodyData(DaraModel):
    def __init__(
        self,
        content_map: str = None,
        create_time: int = None,
        export_type: str = None,
        extend: str = None,
        id: int = None,
        instance_id: str = None,
        kubeone_task_ids: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The details of the task.
        self.content_map = content_map
        # The time when the task was created.
        self.create_time = create_time
        # The type of the object that is exported. Valid values:
        # 
        # *   transactionLog: transaction logs
        # *   snapshot: snapshots
        self.export_type = export_type
        # The extension information that is in the JSON format. The extension information facilitates addition of parameters.
        self.extend = extend
        # The ID of the task.
        self.id = id
        # The ID of the instance
        self.instance_id = instance_id
        # The ID of the associated task at the underlying layer. This parameter is used only to troubleshoot failures.
        self.kubeone_task_ids = kubeone_task_ids
        # The status of the task. Valid values:
        # 
        # *   CREATE: The task is being created.
        # *   RUNNING: The task is being executed.
        # *   FINISH: The task is completed.
        # *   FAILED: The task failed.
        # *   EXPIRE: The task has expired.
        self.status = status
        # The time when the task was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_map is not None:
            result['ContentMap'] = self.content_map

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.kubeone_task_ids is not None:
            result['KubeoneTaskIds'] = self.kubeone_task_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentMap') is not None:
            self.content_map = m.get('ContentMap')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KubeoneTaskIds') is not None:
            self.kubeone_task_ids = m.get('KubeoneTaskIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

