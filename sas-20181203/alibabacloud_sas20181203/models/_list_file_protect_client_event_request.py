# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListFileProtectClientEventRequest(DaraModel):
    def __init__(
        self,
        alert_levels: List[int] = None,
        current_page: int = None,
        end_time: int = None,
        file_path: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        operation: str = None,
        page_size: int = None,
        proc_path: str = None,
        rule_name: str = None,
        start_time: int = None,
        status: str = None,
        uuid: str = None,
    ):
        # The list of alert notification levels.
        self.alert_levels = alert_levels
        # The page number of the current page when paging is used in a paged query.
        self.current_page = current_page
        # The end timestamp.
        self.end_time = end_time
        # The file path.
        self.file_path = file_path
        # The ID of the asset instance.
        self.instance_id = instance_id
        # The name of the asset instance.
        self.instance_name = instance_name
        # The public IP address.
        self.internet_ip = internet_ip
        # The private IP address.
        self.intranet_ip = intranet_ip
        # The type of operation performed on the file. Valid values:
        # 
        # - **DELETE**: deletes the file.
        # - **WRITE**: writes to the file.
        # - **READ**: reads the file.
        # - **RENAME**: renames the file.
        # - **CHOWN**: changes the file owner and associated group.
        self.operation = operation
        # The maximum number of entries per page when paging is used in a paged query.
        self.page_size = page_size
        # The process path.
        self.proc_path = proc_path
        # The name of the configuration rule.
        self.rule_name = rule_name
        # The start time.
        self.start_time = start_time
        # The event status. Valid values:
        # - **0**: Unhandled.
        # - **1**: Handled.
        # - **2**: Whitelisted.
        self.status = status
        # The UUID of the server to query.
        # > Call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain this parameter.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_levels is not None:
            result['AlertLevels'] = self.alert_levels

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proc_path is not None:
            result['ProcPath'] = self.proc_path

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevels') is not None:
            self.alert_levels = m.get('AlertLevels')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProcPath') is not None:
            self.proc_path = m.get('ProcPath')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

