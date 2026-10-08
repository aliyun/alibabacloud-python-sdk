# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryTaskInfoHistoryResponseBody(DaraModel):
    def __init__(
        self,
        current_page_cursor: main_models.QueryTaskInfoHistoryResponseBodyCurrentPageCursor = None,
        next_page_cursor: main_models.QueryTaskInfoHistoryResponseBodyNextPageCursor = None,
        objects: List[main_models.QueryTaskInfoHistoryResponseBodyObjects] = None,
        page_size: int = None,
        pre_page_cursor: main_models.QueryTaskInfoHistoryResponseBodyPrePageCursor = None,
        request_id: str = None,
    ):
        # Cursor for the current page.
        self.current_page_cursor = current_page_cursor
        # Cursor for the next page.
        self.next_page_cursor = next_page_cursor
        # Job information.
        self.objects = objects
        # Page size.
        self.page_size = page_size
        # Cursor for the previous page.
        self.pre_page_cursor = pre_page_cursor
        # Unique request access token.
        self.request_id = request_id

    def validate(self):
        if self.current_page_cursor:
            self.current_page_cursor.validate()
        if self.next_page_cursor:
            self.next_page_cursor.validate()
        if self.objects:
            for v1 in self.objects:
                 if v1:
                    v1.validate()
        if self.pre_page_cursor:
            self.pre_page_cursor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_cursor is not None:
            result['CurrentPageCursor'] = self.current_page_cursor.to_map()

        if self.next_page_cursor is not None:
            result['NextPageCursor'] = self.next_page_cursor.to_map()

        result['Objects'] = []
        if self.objects is not None:
            for k1 in self.objects:
                result['Objects'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page_cursor is not None:
            result['PrePageCursor'] = self.pre_page_cursor.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageCursor') is not None:
            temp_model = main_models.QueryTaskInfoHistoryResponseBodyCurrentPageCursor()
            self.current_page_cursor = temp_model.from_map(m.get('CurrentPageCursor'))

        if m.get('NextPageCursor') is not None:
            temp_model = main_models.QueryTaskInfoHistoryResponseBodyNextPageCursor()
            self.next_page_cursor = temp_model.from_map(m.get('NextPageCursor'))

        self.objects = []
        if m.get('Objects') is not None:
            for k1 in m.get('Objects'):
                temp_model = main_models.QueryTaskInfoHistoryResponseBodyObjects()
                self.objects.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePageCursor') is not None:
            temp_model = main_models.QueryTaskInfoHistoryResponseBodyPrePageCursor()
            self.pre_page_cursor = temp_model.from_map(m.get('PrePageCursor'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryTaskInfoHistoryResponseBodyPrePageCursor(DaraModel):
    def __init__(
        self,
        clientip: str = None,
        create_time: str = None,
        create_time_long: int = None,
        task_no: str = None,
        task_num: int = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
    ):
        # User IP address when submitting the job.
        self.clientip = clientip
        # Job creation time.
        self.create_time = create_time
        # Job creation time.
        self.create_time_long = create_time_long
        # Task number.
        self.task_no = task_no
        # Number of domain names included in the job.
        self.task_num = task_num
        # Task Status. Valid values:  
        # - **WAITING_EXECUTE**: Waiting for execution;  
        # - **EXECUTING**: Executing;  
        # - **COMPLETE**: Execution completed.
        self.task_status = task_status
        # Task status code. Valid values:  
        # - **1**: Waiting for execution;  
        # - **2**: Executing;  
        # - **3**: Execution completed.
        self.task_status_code = task_status_code
        # Task Type. Valid values:  
        # - **CHG_HOLDER**: Modify registrant information;  
        # - **CHG_DNS**: Modify DNS;  
        # - **SET_WHOIS_PROTECT**: Enable privacy protection;  
        # - **UPDATE_ADMIN_CONTACT**: Update administrative contact;  
        # - **UPDATE_BILLING_CONTACT**: Update billing contact;  
        # - **UPDATE_TECH_CONTACT**: Update technical contact;  
        # - **SET_UPDATE_PROHIBITED**: Enable domain name edit lock;  
        # - **SET_TRANSFER_PROHIBITED**: Enable domain name transfer lock;  
        # - **ORDER_ACTIVATE**: Create a registration order;  
        # - **ORDER_RENEW**: Create a renewal order;  
        # - **ORDER_REDEEM**: Create a redemption order;  
        # - **CREATE_DNSHOST**: Create a DNS host;  
        # - **UPDATE_DNSHOST**: Update a DNS host;  
        # - **UPDATE_REGISTRANT_CONTACT**: Update registrant contact;  
        # - **DELETE_DOMAIN**: Delete a domain name;  
        # - **SYNC_DNSHOST**: Synchronize DNS host.
        self.task_type = task_type
        # Task type description.
        self.task_type_description = task_type_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clientip is not None:
            result['Clientip'] = self.clientip

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_num is not None:
            result['TaskNum'] = self.task_num

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')

        return self

class QueryTaskInfoHistoryResponseBodyObjects(DaraModel):
    def __init__(
        self,
        clientip: str = None,
        create_time: str = None,
        create_time_long: int = None,
        task_no: str = None,
        task_num: int = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
    ):
        # User IP address when submitting the task.
        self.clientip = clientip
        # Task creation time.
        self.create_time = create_time
        # Task creation time.
        self.create_time_long = create_time_long
        # Job number.
        self.task_no = task_no
        # Number of domain names included in the job.
        self.task_num = task_num
        # Task status. Valid values:
        # - **WAITING_EXECUTE**: Waiting for execution;
        # - **EXECUTING**: Executing;
        # - **COMPLETE**: Execution completed.
        self.task_status = task_status
        # Task status code. Valid values:
        # - **1**: Waiting for execution;
        # - **2**: Executing;
        # - **3**: Execution completed.
        self.task_status_code = task_status_code
        # Task Type. Valid values:
        # - **CHG_HOLDER**: Modify owner information;
        # - **CHG_DNS**: Modify DNS;
        # - **SET_WHOIS_PROTECT**: Enable privacy protection;
        # - **UPDATE_ADMIN_CONTACT**: Modify administrative contact information;
        # - **UPDATE_BILLING_CONTACT**: Modify billing contact information;
        # - **UPDATE_TECH_CONTACT**: Modify technical contact information;
        # - **SET_UPDATE_PROHIBITED**: Enable domain name edit lock;
        # - **SET_TRANSFER_PROHIBITED**: Enable domain name transfer lock;
        # - **ORDER_ACTIVATE**: Create a registration order;
        # - **ORDER_RENEW**: Create a renewal order;
        # - **ORDER_REDEEM**: Create a redemption order;
        # - **CREATE_DNSHOST**: Create a DNS host;
        # - **UPDATE_DNSHOST**: Update a DNS host;
        # - **UPDATE_REGISTRANT_CONTACT**: Modify registrant contact information;
        # - **DELETE_DOMAIN**: Delete a domain name;
        # - **SYNC_DNSHOST**: Synchronize a DNS host.
        self.task_type = task_type
        # Task type description.
        self.task_type_description = task_type_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clientip is not None:
            result['Clientip'] = self.clientip

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_num is not None:
            result['TaskNum'] = self.task_num

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')

        return self

class QueryTaskInfoHistoryResponseBodyNextPageCursor(DaraModel):
    def __init__(
        self,
        clientip: str = None,
        create_time: str = None,
        create_time_long: int = None,
        task_no: str = None,
        task_num: int = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
    ):
        # User IP address when the job was submitted.
        self.clientip = clientip
        # Creation Time of the job.
        self.create_time = create_time
        # Creation Time of the job.
        self.create_time_long = create_time_long
        # Job number.
        self.task_no = task_no
        # Number of domain names included in the job.
        self.task_num = task_num
        # Task Status. Valid values:  
        # - **WAITING_EXECUTE**: Waiting to execute;  
        # - **EXECUTING**: Executing;  
        # - **COMPLETE**: Execution completed.
        self.task_status = task_status
        # Job status code. Valid values:  
        # - **1**: Waiting to execute;  
        # - **2**: Executing;  
        # - **3**: Execution completed.
        self.task_status_code = task_status_code
        # Task Type. Valid values:  
        # - **CHG_HOLDER**: Modify registrant information;  
        # - **CHG_DNS**: Modify DNS;  
        # - **SET_WHOIS_PROTECT**: Enable privacy protection;  
        # - **UPDATE_ADMIN_CONTACT**: Modify administrative contact information;  
        # - **UPDATE_BILLING_CONTACT**: Modify billing contact information;  
        # - **UPDATE_TECH_CONTACT**: Modify technical contact information;  
        # - **SET_UPDATE_PROHIBITED**: Enable domain name Edit Lock;  
        # - **SET_TRANSFER_PROHIBITED**: Enable domain name transfer lock;  
        # - **ORDER_ACTIVATE**: Create a registration order;  
        # - **ORDER_RENEW**: Create a renewal order;  
        # - **ORDER_REDEEM**: Create a redemption order;  
        # - **CREATE_DNSHOST**: Create a DNS host;  
        # - **UPDATE_DNSHOST**: Update a DNS host;  
        # - **UPDATE_REGISTRANT_CONTACT**: Modify registrant contact information;  
        # - **DELETE_DOMAIN**: Delete a domain name;  
        # - **SYNC_DNSHOST**: Synchronize DNS host.
        self.task_type = task_type
        # Task type description.
        self.task_type_description = task_type_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clientip is not None:
            result['Clientip'] = self.clientip

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_num is not None:
            result['TaskNum'] = self.task_num

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')

        return self

class QueryTaskInfoHistoryResponseBodyCurrentPageCursor(DaraModel):
    def __init__(
        self,
        clientip: str = None,
        create_time: str = None,
        create_time_long: int = None,
        task_no: str = None,
        task_num: int = None,
        task_status: str = None,
        task_status_code: int = None,
        task_type: str = None,
        task_type_description: str = None,
    ):
        # User IP address when the job was submitted.
        self.clientip = clientip
        # Job creation time.
        self.create_time = create_time
        # Job creation UNIX timestamp.
        self.create_time_long = create_time_long
        # Job number.
        self.task_no = task_no
        # Number of domain names included in the job.
        self.task_num = task_num
        # Task Status. Valid values:
        # - **WAITING_EXECUTE**: Waiting for execution;
        # - **EXECUTING**: Executing;
        # - **COMPLETE**: Execution completed.
        self.task_status = task_status
        # Job status code. Valid values:  
        # - **1**: Waiting for execution  
        # - **2**: Executing  
        # - **3**: Execution completed
        self.task_status_code = task_status_code
        # Job type. Valid values:  
        # - **CHG_HOLDER**: Modify registrant information  
        # - **CHG_DNS**: Modify DNS  
        # - **SET_WHOIS_PROTECT**: Enable privacy protection  
        # - **UPDATE_ADMIN_CONTACT**: Modify administrator contact information  
        # - **UPDATE_BILLING_CONTACT**: Modify billing contact information  
        # - **UPDATE_TECH_CONTACT**: Modify technical contact information  
        # - **SET_UPDATE_PROHIBITED**: Enable domain name edit lock  
        # - **SET_TRANSFER_PROHIBITED**: Enable domain name transfer lock  
        # - **ORDER_ACTIVATE**: Create registration order  
        # - **ORDER_RENEW**: Create renewal order  
        # - **ORDER_REDEEM**: Create redemption order  
        # - **CREATE_DNSHOST**: Create DNS host  
        # - **UPDATE_DNSHOST**: Update DNS host  
        # - **UPDATE_REGISTRANT_CONTACT**: Modify registrant contact  
        # - **DELETE_DOMAIN**: Delete domain name  
        # - **SYNC_DNSHOST**: Synchronize DNS host
        self.task_type = task_type
        # Task Type description.
        self.task_type_description = task_type_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clientip is not None:
            result['Clientip'] = self.clientip

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_long is not None:
            result['CreateTimeLong'] = self.create_time_long

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_num is not None:
            result['TaskNum'] = self.task_num

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_status_code is not None:
            result['TaskStatusCode'] = self.task_status_code

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.task_type_description is not None:
            result['TaskTypeDescription'] = self.task_type_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clientip') is not None:
            self.clientip = m.get('Clientip')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeLong') is not None:
            self.create_time_long = m.get('CreateTimeLong')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskNum') is not None:
            self.task_num = m.get('TaskNum')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskStatusCode') is not None:
            self.task_status_code = m.get('TaskStatusCode')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TaskTypeDescription') is not None:
            self.task_type_description = m.get('TaskTypeDescription')

        return self

