# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryTaskDetailListResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: main_models.QueryTaskDetailListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        # The page number returned.
        self.current_page_num = current_page_num
        # The tasks.
        self.data = data
        # Indicates whether the current page is followed by a page.
        self.next_page = next_page
        # The number of entries per page.
        self.page_size = page_size
        # Indicates whether the current page is preceded by a page.
        self.pre_page = pre_page
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_item_num = total_item_num
        # The total number of pages.
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        if m.get('Data') is not None:
            temp_model = main_models.QueryTaskDetailListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryTaskDetailListResponseBodyData(DaraModel):
    def __init__(
        self,
        task_detail: List[main_models.QueryTaskDetailListResponseBodyDataTaskDetail] = None,
    ):
        self.task_detail = task_detail

    def validate(self):
        if self.task_detail:
            for v1 in self.task_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskDetail'] = []
        if self.task_detail is not None:
            for k1 in self.task_detail:
                result['TaskDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_detail = []
        if m.get('TaskDetail') is not None:
            for k1 in m.get('TaskDetail'):
                temp_model = main_models.QueryTaskDetailListResponseBodyDataTaskDetail()
                self.task_detail.append(temp_model.from_map(k1))

        return self

class QueryTaskDetailListResponseBodyDataTaskDetail(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        domain_name: str = None,
        error_msg: str = None,
        fail_reason: str = None,
        instance_id: str = None,
        task_detail_no: str = None,
        task_no: str = None,
        task_result: str = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
        try_count: int = None,
        update_time: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The domain name.
        self.domain_name = domain_name
        # The error message returned when the task failed.
        self.error_msg = error_msg
        # The cause of a domain name task failure.
        self.fail_reason = fail_reason
        # The instance ID of the domain name.
        self.instance_id = instance_id
        # The ID of the task details.
        self.task_detail_no = task_detail_no
        # The task ID.
        self.task_no = task_no
        # The result of the task.
        self.task_result = task_result
        # The task status. Valid values:
        # 
        # *   **WAITING_EXECUTE**: To be executed
        # *   **EXECUTING**: being executed
        # *   **EXECUTE_SUCCESS**: successful
        # *   **EXECUTE_FAILURE**: failed
        self.task_status = task_status
        # The status code of the task. Valid values:
        # 
        # *   **0**: waiting for execution
        # *   **1**: being executed
        # *   **2**: successful
        # *   **3**: failed
        self.task_status_code = task_status_code
        # The task type. Valid values:
        # 
        # *   **CHG_HOLDER**: The task is run to modify the domain name registrant.
        # *   **CHG_DNS**: The task is run to change the Domain Name System (DNS) servers.
        # *   **SET_WHOIS_PROTECT**: The task is run to configure privacy protection for the domain name.
        # *   **UPDATE_ADMIN_CONTACT**: The task is run to modify the information about the administrator of the domain name.
        # *   **UPDATE_BILLING_CONTACT**: The task is run to modify the information about the payer for the domain name.
        # *   **UPDATE_TECH_CONTACT**: The task is run to modify the information about the technical support for the domain name.
        # *   **SET_UPDATE_PROHIBITED**: The task is run to configure the security lock for the domain name.
        # *   **SET_TRANSFER_PROHIBITED**: The task is run to configure the transfer lock for the domain name.
        # *   **ORDER_ACTIVATE**: The task is run to create a registration order for the domain name.
        # *   **ORDER_RENEW**: The task is run to create a renewal order for the domain name.
        # *   **ORDER_REDEEM**: The task is run to create a redemption order for the domain name.
        # *   **CREATE_DNSHOST**: The task is run to create a DNS server for the domain name.
        # *   **UPDATE_DNSHOST**: The task is run to update the information about a DNS server for the domain name.
        # *   **SYNC_DNSHOST**: The task is run to synchronize a DNS server for the domain name.
        self.task_type = task_type
        # The description of the task type.
        self.task_type_description = task_type_description
        # The number of times the task was retried.
        self.try_count = try_count
        # The last time when the task was run.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_result is not None:
            result['TaskResult'] = self.task_result

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description

        if self.try_count is not None:
            result['TryCount'] = self.try_count

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')

        if m.get('TryCount') is not None:
            self.try_count = m.get('TryCount')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

