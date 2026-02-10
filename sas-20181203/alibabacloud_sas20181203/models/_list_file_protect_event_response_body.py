# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListFileProtectEventResponseBody(DaraModel):
    def __init__(
        self,
        event_list: List[main_models.ListFileProtectEventResponseBodyEventList] = None,
        page_info: main_models.ListFileProtectEventResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The events.
        self.event_list = event_list
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.event_list:
            for v1 in self.event_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventList'] = []
        if self.event_list is not None:
            for k1 in self.event_list:
                result['EventList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k1 in m.get('EventList'):
                temp_model = main_models.ListFileProtectEventResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListFileProtectEventResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFileProtectEventResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFileProtectEventResponseBodyEventList(DaraModel):
    def __init__(
        self,
        alert_level: int = None,
        cmd_line: str = None,
        file_path: str = None,
        handle_time: int = None,
        id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        latest_time: int = None,
        operation: str = None,
        platform: str = None,
        proc_path: str = None,
        proc_permission: str = None,
        process_id: str = None,
        remark: str = None,
        rule_name: str = None,
        status: int = None,
        uuid: str = None,
    ):
        # The severity of the alert. Valid values:
        # 
        # *   0: no alerts
        # *   1: reminder
        # *   2: suspicious
        # *   3: high-risk
        self.alert_level = alert_level
        # The command line of the event.
        self.cmd_line = cmd_line
        # The path to the file that is managed by the process.
        self.file_path = file_path
        # The time when the event was handled.
        self.handle_time = handle_time
        # The ID of the event.
        self.id = id
        # The instance name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The time when the event last occurred.
        self.latest_time = latest_time
        # The operation performed by the process on the file.
        self.operation = operation
        # The type of the operating system. Valid values:
        # 
        # *   **windows**: Windows
        # *   **linux**: Linux
        self.platform = platform
        # The path to the process.
        self.proc_path = proc_path
        # The permissions required to start the process.
        self.proc_permission = proc_permission
        # The ID of the process.
        self.process_id = process_id
        # The description.
        self.remark = remark
        # The name of the rule.
        self.rule_name = rule_name
        # The status of the event. Valid values:
        # 
        # *   0: unhandled
        # *   1: handled
        # *   2: added to the whitelist
        # *   3: ignored
        self.status = status
        # The UUID of the server that is associated with the process.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.cmd_line is not None:
            result['CmdLine'] = self.cmd_line

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.handle_time is not None:
            result['HandleTime'] = self.handle_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.latest_time is not None:
            result['LatestTime'] = self.latest_time

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.proc_path is not None:
            result['ProcPath'] = self.proc_path

        if self.proc_permission is not None:
            result['ProcPermission'] = self.proc_permission

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('CmdLine') is not None:
            self.cmd_line = m.get('CmdLine')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('HandleTime') is not None:
            self.handle_time = m.get('HandleTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LatestTime') is not None:
            self.latest_time = m.get('LatestTime')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProcPath') is not None:
            self.proc_path = m.get('ProcPath')

        if m.get('ProcPermission') is not None:
            self.proc_permission = m.get('ProcPermission')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

