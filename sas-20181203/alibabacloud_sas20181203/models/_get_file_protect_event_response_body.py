# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetFileProtectEventResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFileProtectEventResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data details.
        self.data = data
        # The request ID. Alibaba Cloud generates a unique identifier for each request. You can use the request ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetFileProtectEventResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFileProtectEventResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_level: int = None,
        cmd_line: str = None,
        file_path: str = None,
        file_permission: str = None,
        first_time: int = None,
        handle_time: int = None,
        id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        latest_time: int = None,
        operation: str = None,
        platform: str = None,
        proc_path: str = None,
        process_id: str = None,
        remark: str = None,
        rule_name: str = None,
        status: int = None,
        user_id: str = None,
        user_name: str = None,
        uuid: str = None,
    ):
        # The alert notification level. Valid values:
        # 
        # - 0: No alert.
        # 
        # - 1: Reminder.
        # 
        # - 2: Suspicious.
        # 
        # - 3: High-risk.
        self.alert_level = alert_level
        # The event command line.
        self.cmd_line = cmd_line
        # The file path.
        self.file_path = file_path
        # The process permissions.
        self.file_permission = file_permission
        # The timestamp when the event first occurred.
        self.first_time = first_time
        # The time when the event was handled. The value is a UNIX timestamp. Unit: milliseconds.
        self.handle_time = handle_time
        # The unique ID.
        self.id = id
        # The instance name.
        self.instance_name = instance_name
        # The public IP address of the associated instance.
        self.internet_ip = internet_ip
        # The private IP address of the associated instance.
        self.intranet_ip = intranet_ip
        # The timestamp when the event most recently occurred. The value is a UNIX timestamp. Unit: milliseconds.
        self.latest_time = latest_time
        # The operation performed by the process on the file.
        self.operation = operation
        # The operating system type. Valid values:
        # 
        # - **windows**: Windows.
        # - **linux**: Linux.
        self.platform = platform
        # The process path.
        self.proc_path = proc_path
        # The process ID of the event.
        self.process_id = process_id
        # The remarks.
        self.remark = remark
        # The rule name.
        self.rule_name = rule_name
        # The event status. Valid values:
        # 
        # - 0: Unhandled. 
        # - 1: Manually handled.
        # - 2: Whitelisted.
        # - 3: Ignored.
        self.status = status
        # The user ID that started the current process.
        self.user_id = user_id
        # The username that started the current process.
        self.user_name = user_name
        # The UUID of the asset instance.
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

        if self.file_permission is not None:
            result['FilePermission'] = self.file_permission

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

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

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

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

        if m.get('FilePermission') is not None:
            self.file_permission = m.get('FilePermission')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

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

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

