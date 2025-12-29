# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListChangeOrdersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListChangeOrdersResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # Indicates whether the list of change orders was obtained. Valid values:
        # 
        # *   **true**: indicates that the list was obtained.
        # *   **false**: indicates that the list could not be obtained.
        self.code = code
        # The information about change orders.
        self.data = data
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: indicates that the request was successful.
        # *   **3xx**: indicates that the request was redirected.
        # *   **4xx**: indicates that the request was invalid.
        # *   **5xx**: indicates that a server error occurred.
        self.error_code = error_code
        # The ID of the trace. It is used to query the details of a request.
        self.message = message
        # The returned message.
        self.request_id = request_id
        self.success = success
        # The information about change orders.
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
            temp_model = main_models.ListChangeOrdersResponseBodyData()
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

class ListChangeOrdersResponseBodyData(DaraModel):
    def __init__(
        self,
        change_order_list: List[main_models.ListChangeOrdersResponseBodyDataChangeOrderList] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The change orders.
        self.change_order_list = change_order_list
        # The total number of change orders.
        self.current_page = current_page
        # The error code.
        # 
        # *   The **ErrorCode** parameter is not returned when the request succeeds.
        # *   The **ErrorCode** parameter is returned when the request fails. For more information, see **Error codes** in this topic.
        self.page_size = page_size
        # The list of change orders.
        self.total_size = total_size

    def validate(self):
        if self.change_order_list:
            for v1 in self.change_order_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChangeOrderList'] = []
        if self.change_order_list is not None:
            for k1 in self.change_order_list:
                result['ChangeOrderList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_order_list = []
        if m.get('ChangeOrderList') is not None:
            for k1 in m.get('ChangeOrderList'):
                temp_model = main_models.ListChangeOrdersResponseBodyDataChangeOrderList()
                self.change_order_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListChangeOrdersResponseBodyDataChangeOrderList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        batch_count: int = None,
        batch_type: str = None,
        change_order_id: str = None,
        co_type: str = None,
        co_type_code: str = None,
        create_time: str = None,
        create_user_id: str = None,
        description: str = None,
        finish_time: str = None,
        group_id: str = None,
        source: str = None,
        status: int = None,
        user_id: str = None,
    ):
        # The number of entries returned on each page.
        self.app_id = app_id
        # The ID of the user who created the change order.
        self.batch_count = batch_count
        # The ID of the group.
        self.batch_type = batch_type
        # The mode in which the release batches are determined. Valid values:
        # 
        # *   **auto**: SAE automatically determines the release batches.
        # *   **manual**: You must manually determine the release batches.
        self.change_order_id = change_order_id
        # The ID of the application.
        self.co_type = co_type
        # The code of the change order. Valid values:
        # 
        # *   **CoBindSlb**: associates the Server Load Balancer (SLB) instance with the application.
        # *   **CoUnbindSlb**: disassociates an SLB instance from the application.
        # *   **CoCreateApp**: creates the application.
        # *   **CoDeleteApp**: deletes the application.
        # *   **CoDeploy**: deploys the application.
        # *   **CoRestartApplication**: restarts the application.
        # *   **CoRollback**: rolls back the application.
        # *   **CoScaleIn**: scales in the application.
        # *   **CoScaleOut**: scales out the application.
        # *   **CoStartApplication**: starts the application.
        # *   **CoStopApplication**: stops the application.
        # *   **CoRescaleApplicationVertically**: modifies the instance type.
        # *   **CoDeployHistroy**: rolls back the application to an earlier version.
        # *   **CoBindNas**: associates a network-attached storage (NAS) file system with the application.
        # *   **CoUnbindNas**: disassociates a NAS file system from the application.
        # *   **CoBatchStartApplication**: starts multiple applications concurrently.
        # *   **CoBatchStopApplication**: stops multiple applications concurrently.
        # *   **CoRestartInstances**: restarts the instance.
        # *   **CoDeleteInstances**: deletes the instance.
        # *   **CoScaleInAppWithInstances**: reduces the specified number of application instances.
        self.co_type_code = co_type_code
        # The ID of the user.
        self.create_time = create_time
        # The code of the change type. Valid values:
        # 
        # *   **CoBindSlb**: associates an SLB instance with the application.
        # *   **CoUnbindSlb**: disassociates the SLB instance from the application.
        # *   **CoCreateApp**: creates the application.
        # *   **CoDeleteApp**: deletes the application.
        # *   **CoDeploy**: deploys the application.
        # *   **CoRestartApplication**: restarts the application.
        # *   **CoRollback**: rolls back the application.
        # *   **CoScaleIn**: scales in the application.
        # *   **CoScaleOut**: scales out the application.
        # *   **CoStart**: starts the application.
        # *   **CoStop**: stops the application.
        # *   **CoRescaleApplicationVertically**: modifies the instance specifications.
        # *   **CoDeployHistroy**: rolls back the application to a historical version.
        # *   **CoBindNas**: associates a NAS file system with the application.
        # *   **CoUnbindNas**: disassociates the NAS file system from the application.
        # *   **CoBatchStartApplication**: starts multiple applications concurrently.
        # *   **CoBatchStopApplication**: stops multiple applications concurrently.
        # *   **CoRestartInstances**: restarts the instances.
        # *   **CoDeleteInstances**: deletes the instances.
        # *   **CoScaleInAppWithInstances**: reduces the number of the specified application instances.
        self.create_user_id = create_user_id
        # The change type, which corresponds to the **CoTypeCode** parameter.
        self.description = description
        # The time when the change order was created.
        self.finish_time = finish_time
        # The description about the application.
        self.group_id = group_id
        # The number of release batches.
        self.source = source
        # The time when the change order was completed.
        self.status = status
        # The source of the change order.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count

        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.co_type is not None:
            result['CoType'] = self.co_type

        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.description is not None:
            result['Description'] = self.description

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')

        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')

        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

