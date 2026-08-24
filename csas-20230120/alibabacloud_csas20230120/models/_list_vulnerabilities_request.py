# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVulnerabilitiesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        department: str = None,
        dev_tag: str = None,
        dev_type: str = None,
        hostname: str = None,
        page_size: int = None,
        sase_user_id: str = None,
        scan_task_id: str = None,
        title: str = None,
        update_ids: List[str] = None,
        username: str = None,
        vul_level: str = None,
        vul_type: str = None,
    ):
        # The page number of the current page in a paged query with paging. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The department name. Matches any level of department in the organizational structure to which the user belongs. Specify the department name itself without the full path of the organizational structure.
        self.department = department
        # The unique identifier of the user endpoint device. Exact match. The value can be up to 64 characters in length. Valid values are obtained from:
        # - [ListUserDevices](~~ListUserDevices~~): lists user endpoint devices.
        self.dev_tag = dev_tag
        # The operating system type of the user endpoint device. Valid values:
        # - **windows**: Windows. Currently, vulnerability scanning supports only Windows.
        self.dev_type = dev_type
        # The hostname of the user endpoint device. Fuzzy match is supported. The value can be up to 64 characters in length.
        self.hostname = hostname
        # The number of entries per page. Settings for paged query with paging. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The user ID. Exact match. Valid values are obtained from:
        # - [ListUserDevices](~~ListUserDevices~~): lists user endpoint devices.
        # - [GetUserDevice](~~GetUserDevice~~): queries the details of a user endpoint device.
        self.sase_user_id = sase_user_id
        # The ID of the vulnerability scanning node that detected the vulnerability. Used to filter detection results of a specified node. Valid values are obtained from:
        # - [ListVulScanTasks](~~ListVulScanTasks~~): lists vulnerability scanning nodes.
        # - [CreateVulScanTask](~~CreateVulScanTask~~): creates a vulnerability scanning node.
        self.scan_task_id = scan_task_id
        # The vulnerability title. Fuzzy match is supported. Matches both Chinese and English titles.
        self.title = title
        # The patch IDs used for filtering. A maximum of 100 IDs can be specified. Duplicate values are not allowed.
        self.update_ids = update_ids
        # The username. Fuzzy match is supported. The value can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), asterisks (*), hyphens (-), at signs (@), spaces, middle dots (·), and parentheses.
        self.username = username
        # The vulnerability risk level used for filtering. Valid values:
        # - **High**: high risk.
        # - **Mid**: medium risk.
        # - **Low**: low risk.
        self.vul_level = vul_level
        # The vulnerability type used for filtering. Valid values:
        # - **windows**: Windows system vulnerability.
        # - **ai_agent**: AI Agent vulnerability.
        self.vul_type = vul_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.department is not None:
            result['Department'] = self.department

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id

        if self.title is not None:
            result['Title'] = self.title

        if self.update_ids is not None:
            result['UpdateIds'] = self.update_ids

        if self.username is not None:
            result['Username'] = self.username

        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level

        if self.vul_type is not None:
            result['VulType'] = self.vul_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UpdateIds') is not None:
            self.update_ids = m.get('UpdateIds')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        if m.get('VulType') is not None:
            self.vul_type = m.get('VulType')

        return self

