# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTaskDetailRequest(DaraModel):
    def __init__(
        self,
        called: str = None,
        id: int = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        status_code: str = None,
        task_id: int = None,
    ):
        # The callee number. You can view the callee number on the **Detail** interface of [**Task Management**](https://aiccs.console.aliyun.com/job/list).
        self.called = called
        # The detail ID. You can view the detail ID on the **Detail** interface of [**Task Management**](https://aiccs.console.aliyun.com/job/list).
        self.id = id
        self.owner_id = owner_id
        # The current page number. The value must be greater than **0**. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page. The value must be greater than **0**. Default value: **20**.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Detail status. Valid values:
        # - **SUCCESS**: The outbound call succeeded.
        # - **FAIL**: The outbound call failed.
        # - **INIT**: The outbound call has not been made.
        self.status = status
        # The call status code. For more information, see [Call Status Codes](https://help.aliyun.com/document_detail/112804.html) in Voice Service.
        self.status_code = status_code
        # The job ID. You can view the job ID on the [Task Management](https://aiccs.console.aliyun.com/job/list) page or obtain it by using the [ListTask](https://help.aliyun.com/document_detail/2718008.html) API.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called is not None:
            result['Called'] = self.called

        if self.id is not None:
            result['Id'] = self.id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.status is not None:
            result['Status'] = self.status

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Called') is not None:
            self.called = m.get('Called')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

