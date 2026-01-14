# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ExportZookeeperDataResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ExportZookeeperDataResponseBodyData = None,
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
        # 
        # *   If the request is successful, a success message is returned.
        # *   If the request fails, an error message is returned.
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
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

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
        if m.get('Data') is not None:
            temp_model = main_models.ExportZookeeperDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

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

class ExportZookeeperDataResponseBodyData(DaraModel):
    def __init__(
        self,
        content_map: Dict[str, Any] = None,
        create_time: int = None,
        export_type: str = None,
        extend: str = None,
        id: int = None,
        instance_id: str = None,
        kubeone_task_ids: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # The content of a task.
        self.content_map = content_map
        # The creation time.
        self.create_time = create_time
        # The type of the object that is exported. Valid values:
        # 
        # *   transactionLog: transaction logs
        # *   snapshot: snapshots
        self.export_type = export_type
        # The extended information.
        self.extend = extend
        # The ID of the task.
        self.id = id
        # The ID of the instance
        self.instance_id = instance_id
        # The ID of the associated task at the underlying layer. This parameter is used only to troubleshoot failures.
        self.kubeone_task_ids = kubeone_task_ids
        # The status of the task. Valid values:
        # 
        # *   CREATE: The object is being created.
        # *   RUNNING: The task is running.
        # *   FINISH: The task is completed.
        # *   FAILED: The task fails.
        # *   EXPIRE: The task has expired.
        self.status = status
        # The last update time.
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

