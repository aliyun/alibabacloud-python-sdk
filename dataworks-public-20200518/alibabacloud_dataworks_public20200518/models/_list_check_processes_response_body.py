# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListCheckProcessesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListCheckProcessesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListCheckProcessesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCheckProcessesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        check_processes: List[main_models.ListCheckProcessesResponseBodyPagingInfoCheckProcesses] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The check details of the extension.
        self.check_processes = check_processes
        # The page number.
        self.page_number = page_number
        # The number of entries displayed on each page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.check_processes:
            for v1 in self.check_processes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckProcesses'] = []
        if self.check_processes is not None:
            for k1 in self.check_processes:
                result['CheckProcesses'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_processes = []
        if m.get('CheckProcesses') is not None:
            for k1 in m.get('CheckProcesses'):
                temp_model = main_models.ListCheckProcessesResponseBodyPagingInfoCheckProcesses()
                self.check_processes.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCheckProcessesResponseBodyPagingInfoCheckProcesses(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_name: str = None,
        event_name_en: str = None,
        message_id: str = None,
        operator: str = None,
        process_id: str = None,
        process_name: str = None,
        project_id: int = None,
        status: str = None,
    ):
        # Extension point event encoding.
        self.event_code = event_code
        # The name of the extension point event.
        self.event_name = event_name
        # The English name of the event.
        self.event_name_en = event_name_en
        # DataWorks the message ID of the open message. After an extended point event is triggered, you can obtain the message ID from the received event message.
        self.message_id = message_id
        # The operator ID.
        self.operator = operator
        # The ID of the process instance.
        self.process_id = process_id
        # The name of the check object, such as the file name or node name.
        self.process_name = process_name
        # The ID of the DataWorks workspace.
        self.project_id = project_id
        # The status of the extender check.
        # - CHECKING CHECKING
        # - PASSED the pass check
        # - BLOCKED check failed
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_name_en is not None:
            result['EventNameEn'] = self.event_name_en

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventNameEn') is not None:
            self.event_name_en = m.get('EventNameEn')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

