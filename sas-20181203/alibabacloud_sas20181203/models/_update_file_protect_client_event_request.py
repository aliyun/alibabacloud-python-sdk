# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateFileProtectClientEventRequest(DaraModel):
    def __init__(
        self,
        alert_levels: List[int] = None,
        end_time: int = None,
        exclude_id_list: List[int] = None,
        file_path: str = None,
        id_list: List[int] = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        new_status: int = None,
        operation: str = None,
        proc_path: str = None,
        remark: List[str] = None,
        rule_name: str = None,
        select_all: bool = None,
        start_time: int = None,
        status: str = None,
        uuid: str = None,
    ):
        # The list of alert notification levels.
        self.alert_levels = alert_levels
        # The timestamp of the end time.
        self.end_time = end_time
        # The list of excluded event IDs.
        self.exclude_id_list = exclude_id_list
        # The file path.
        self.file_path = file_path
        # The list of event IDs.
        self.id_list = id_list
        # The ID of the asset instance.
        self.instance_id = instance_id
        # The name of the asset instance.
        self.instance_name = instance_name
        # The public IP address.
        self.internet_ip = internet_ip
        # The internal IP address.
        self.intranet_ip = intranet_ip
        # The new status. Valid values:
        # 
        # - **0**: Unhandled.
        # - **1**: Handled.
        # - **2**: Whitelisted.
        # 
        # This parameter is required.
        self.new_status = new_status
        # The type of the operation.
        self.operation = operation
        # The process path.
        self.proc_path = proc_path
        # The remarks.
        self.remark = remark
        # The rule name.
        self.rule_name = rule_name
        # Specifies whether to select all.
        # 
        # This parameter is required.
        self.select_all = select_all
        # The start time.
        self.start_time = start_time
        # The event status. Valid values:
        # - **0**: Unhandled.
        # - **1**: Handled.
        # - **2**: Whitelisted.
        self.status = status
        # The UUID of the protected server.
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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.exclude_id_list is not None:
            result['ExcludeIdList'] = self.exclude_id_list

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.id_list is not None:
            result['IdList'] = self.id_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.new_status is not None:
            result['NewStatus'] = self.new_status

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.proc_path is not None:
            result['ProcPath'] = self.proc_path

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.select_all is not None:
            result['SelectAll'] = self.select_all

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

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExcludeIdList') is not None:
            self.exclude_id_list = m.get('ExcludeIdList')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('NewStatus') is not None:
            self.new_status = m.get('NewStatus')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('ProcPath') is not None:
            self.proc_path = m.get('ProcPath')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SelectAll') is not None:
            self.select_all = m.get('SelectAll')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

