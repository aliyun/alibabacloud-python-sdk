# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertySoftwareDetailRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        extend: str = None,
        install_time_end: int = None,
        install_time_start: int = None,
        name: str = None,
        next_token: str = None,
        page_size: int = None,
        path: str = None,
        remark: str = None,
        software_version: str = None,
        use_next_token: bool = None,
        uuid: str = None,
    ):
        # Set which page of the returned results to start displaying the query results. The default value is **1**, indicating that the display starts from the first page.
        self.current_page = current_page
        # Whether the software name supports fuzzy search. To enable fuzzy search, set the value of this parameter to 1; other values or an empty value indicate that fuzzy search is not supported.
        self.extend = extend
        # The timestamp when the software update ended. Unit: milliseconds.
        self.install_time_end = install_time_end
        # The timestamp when the software update started. Unit: milliseconds.
        self.install_time_start = install_time_start
        # The name of the software to be queried.
        self.name = name
        # Used to mark the starting position for reading. Leave it blank to start from the beginning.
        # 
        # > For the first call, you do not need to fill this in; the response will include the NextToken for the second call, and each subsequent call\\"s response will contain the NextToken for the next call.
        self.next_token = next_token
        # Set the number of software asset fingerprint information items displayed per page during pagination. The default value is **10**, indicating that 10 items of software asset fingerprint information are displayed per page.
        self.page_size = page_size
        # The installation path of the software.
        self.path = path
        # The name or IP address of the server to be queried.
        self.remark = remark
        # The version information of the software.
        self.software_version = software_version
        # Whether to use the NextToken method to pull asset list data. If this parameter is used, TotalCount will no longer be returned. Values:
        # 
        # - **true**: Use the NextToken method.
        # - **false**: Do not use the NextToken method.
        self.use_next_token = use_next_token
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.install_time_end is not None:
            result['InstallTimeEnd'] = self.install_time_end

        if self.install_time_start is not None:
            result['InstallTimeStart'] = self.install_time_start

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.software_version is not None:
            result['SoftwareVersion'] = self.software_version

        if self.use_next_token is not None:
            result['UseNextToken'] = self.use_next_token

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('InstallTimeEnd') is not None:
            self.install_time_end = m.get('InstallTimeEnd')

        if m.get('InstallTimeStart') is not None:
            self.install_time_start = m.get('InstallTimeStart')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SoftwareVersion') is not None:
            self.software_version = m.get('SoftwareVersion')

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

