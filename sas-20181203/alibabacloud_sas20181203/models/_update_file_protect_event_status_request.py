# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateFileProtectEventStatusRequest(DaraModel):
    def __init__(
        self,
        alert_levels: List[int] = None,
        end_time: int = None,
        id: List[int] = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        operation: str = None,
        rule_name: str = None,
        select_all_across_pages: bool = None,
        start_time: int = None,
        status: int = None,
        uuid: str = None,
    ):
        # The severities of alerts.
        self.alert_levels = alert_levels
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time
        # The IDs of the events.
        self.id = id
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # Type of operation on a file. eg:
        # 
        # - **DELETE**: delete the file.
        # - **WRITE**: write the file.
        # - **READ**: read the file.
        # - **RENAME**: rename the file.
        # - **CHOWN**: set the file owner and file association group operations.
        self.operation = operation
        # The name of the defense rule.
        self.rule_name = rule_name
        # Whether to choose all fields across industries.
        # 
        # - **true**: yes
        # - **false**: no
        self.select_all_across_pages = select_all_across_pages
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time
        # The handling status of the event. Valid values:
        # 
        # *   **0**: unhandled
        # *   **1**: handled
        # *   **2**: added to the whitelist
        self.status = status
        # The UUID of the server.
        # 
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
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

        if self.id is not None:
            result['Id'] = self.id

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

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.select_all_across_pages is not None:
            result['SelectAllAcrossPages'] = self.select_all_across_pages

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

        if m.get('Id') is not None:
            self.id = m.get('Id')

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

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SelectAllAcrossPages') is not None:
            self.select_all_across_pages = m.get('SelectAllAcrossPages')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

