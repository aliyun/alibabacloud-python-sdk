# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListJobsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        data: main_models.ListJobsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The page number of the returned page.
        self.current_page = current_page
        # The job templates.
        self.data = data
        # The error code returned. Take note of the following rules:
        # 
        # *   If the call is successful, **ErrorCode** is not returned.
        # *   If the call fails, **ErrorCode** is returned. For more information, see the "**Error codes**" section in this topic.
        self.error_code = error_code
        # The returned message.
        self.message = message
        # The number of entries returned on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the applications were obtained. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of job templates.
        self.total_size = total_size

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

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Data') is not None:
            temp_model = main_models.ListJobsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListJobsResponseBodyDataApplications] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The job templates.
        self.applications = applications
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned on each page.
        self.page_size = page_size
        # The total number of job templates.
        self.total_size = total_size

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListJobsResponseBodyDataApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListJobsResponseBodyDataApplications(DaraModel):
    def __init__(
        self,
        active: int = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        completion_time: int = None,
        cpu: int = None,
        failed: int = None,
        image_url: str = None,
        last_changeorder_state: str = None,
        last_job_state: str = None,
        last_start_time: int = None,
        mem: int = None,
        message: str = None,
        namespace_id: str = None,
        region_id: str = None,
        succeeded: int = None,
        suspend: bool = None,
        tags: List[main_models.ListJobsResponseBodyDataApplicationsTags] = None,
        trigger_config: str = None,
    ):
        # The number of running instances.
        self.active = active
        # The description of the job template.
        self.app_description = app_description
        # The ID of the job template.
        self.app_id = app_id
        # The name of the job template.
        self.app_name = app_name
        # The time when the job was last completed.
        self.completion_time = completion_time
        # The CPU specifications that are required for each instance. Unit: millicores. This parameter cannot be set to 0. Valid values:
        # 
        # *   **500**
        # *   **1000**
        # *   **2000**
        # *   **4000**
        # *   **8000**
        # *   **16000**
        # *   **32000**
        self.cpu = cpu
        # The number of instances that failed to run.
        self.failed = failed
        self.image_url = image_url
        # Indicates whether the latest change order was executed. Valid values:
        # 
        # *   **0**: The latest change order failed to be executed.
        # *   **1**: The latest change order was executed.
        self.last_changeorder_state = last_changeorder_state
        # The status of the latest job. Valid values:
        # 
        # *   **0**: The job is not executed.
        # *   **1**: The job was executed.
        # *   **2**: The job failed to be executed.
        # *   **3**: The job is being executed.
        self.last_job_state = last_job_state
        # The time when the job was last started.
        self.last_start_time = last_start_time
        # The size of memory that is required by each instance. Unit: MB. This parameter cannot be set to 0. The values of this parameter correspond to the values of the Cpu parameter:
        # 
        # *   This parameter is set to **1024** if the Cpu parameter is set to 500 or 1000.
        # *   This parameter is set to **2048** if the Cpu parameter is set to 500, 1000, or 2000.
        # *   This parameter is set to **4096** if the Cpu parameter is set to 1000, 2000, or 4000.
        # *   This parameter is set to **8192** if the Cpu parameter is set to 2000, 4000, or 8000.
        # *   This parameter is set to **12288** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **16384** if the Cpu parameter is set to 4000, 8000, or 16000.
        # *   This parameter is set to **24576** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **32768** if the Cpu parameter is set to 16000.
        # *   This parameter is set to **65536** if the Cpu parameter is set to 8000, 16000, or 32000.
        # *   This parameter is set to **131072** if the Cpu parameter is set to 32000.
        self.mem = mem
        # The returned message.
        self.message = message
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The region ID.
        self.region_id = region_id
        # The number of instances that were successfully run.
        self.succeeded = succeeded
        # Indicates whether the job template is suspended.
        self.suspend = suspend
        # The tags of the job template.
        self.tags = tags
        self.trigger_config = trigger_config

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.app_description is not None:
            result['AppDescription'] = self.app_description

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.failed is not None:
            result['Failed'] = self.failed

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.last_changeorder_state is not None:
            result['LastChangeorderState'] = self.last_changeorder_state

        if self.last_job_state is not None:
            result['LastJobState'] = self.last_job_state

        if self.last_start_time is not None:
            result['LastStartTime'] = self.last_start_time

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.message is not None:
            result['Message'] = self.message

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded

        if self.suspend is not None:
            result['Suspend'] = self.suspend

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('LastChangeorderState') is not None:
            self.last_changeorder_state = m.get('LastChangeorderState')

        if m.get('LastJobState') is not None:
            self.last_job_state = m.get('LastJobState')

        if m.get('LastStartTime') is not None:
            self.last_start_time = m.get('LastStartTime')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')

        if m.get('Suspend') is not None:
            self.suspend = m.get('Suspend')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListJobsResponseBodyDataApplicationsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TriggerConfig') is not None:
            self.trigger_config = m.get('TriggerConfig')

        return self

class ListJobsResponseBodyDataApplicationsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

