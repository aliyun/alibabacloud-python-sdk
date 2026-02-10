# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCheckWarningsResponseBody(DaraModel):
    def __init__(
        self,
        check_warnings: List[main_models.DescribeCheckWarningsResponseBodyCheckWarnings] = None,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the check item.
        self.check_warnings = check_warnings
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.check_warnings:
            for v1 in self.check_warnings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckWarnings'] = []
        if self.check_warnings is not None:
            for k1 in self.check_warnings:
                result['CheckWarnings'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_warnings = []
        if m.get('CheckWarnings') is not None:
            for k1 in m.get('CheckWarnings'):
                temp_model = main_models.DescribeCheckWarningsResponseBodyCheckWarnings()
                self.check_warnings.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCheckWarningsResponseBodyCheckWarnings(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        check_warning_id: int = None,
        container_id: str = None,
        container_name: str = None,
        exec_error_message: str = None,
        fix_status: int = None,
        item: str = None,
        last_handle_time: int = None,
        level: str = None,
        reason: str = None,
        status: int = None,
        type: str = None,
        uuid: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The ID of the alert that is generated for the baseline check result.
        self.check_warning_id = check_warning_id
        # The ID of the container.
        self.container_id = container_id
        # The name of the container.
        self.container_name = container_name
        # The error message in the check result.
        self.exec_error_message = exec_error_message
        # Indicates whether fixing is supported. Valid values:
        # 
        # *   **0**: Fixing is not supported.
        # *   **1**: Fixing is supported.
        self.fix_status = fix_status
        # The name of the check item.
        self.item = item
        # The timestamp of the latest processing of the check item risk of the machine. Unit: milliseconds.
        self.last_handle_time = last_handle_time
        # The risk level of the risk item. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.level = level
        # The description.
        self.reason = reason
        # The status of the check item. Valid values:
        # 
        # *   **1**: failed.
        # *   **2**: verifying.
        # *   **3**: passed.
        # *   **5**: expired.
        # *   **6**: ignored.
        self.status = status
        # The type of the check item.
        self.type = type
        # The ID of the server on which the baseline check is performed.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_warning_id is not None:
            result['CheckWarningId'] = self.check_warning_id

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.exec_error_message is not None:
            result['ExecErrorMessage'] = self.exec_error_message

        if self.fix_status is not None:
            result['FixStatus'] = self.fix_status

        if self.item is not None:
            result['Item'] = self.item

        if self.last_handle_time is not None:
            result['LastHandleTime'] = self.last_handle_time

        if self.level is not None:
            result['Level'] = self.level

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckWarningId') is not None:
            self.check_warning_id = m.get('CheckWarningId')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('ExecErrorMessage') is not None:
            self.exec_error_message = m.get('ExecErrorMessage')

        if m.get('FixStatus') is not None:
            self.fix_status = m.get('FixStatus')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('LastHandleTime') is not None:
            self.last_handle_time = m.get('LastHandleTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

