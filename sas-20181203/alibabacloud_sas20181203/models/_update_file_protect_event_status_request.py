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
        # The list of alert notification levels.
        self.alert_levels = alert_levels
        # The end timestamp of the query.
        self.end_time = end_time
        # The list of event IDs.
        self.id = id
        # The ID of the asset instance.
        self.instance_id = instance_id
        # The name of the asset instance.
        self.instance_name = instance_name
        # The public IP address.
        self.internet_ip = internet_ip
        # The internal IP address.
        self.intranet_ip = intranet_ip
        # The type of operation performed on the file. Valid values:
        # 
        # - **DELETE**: Deletes a file.
        # - **WRITE**: Writes to a file.
        # - **READ**: Reads a file.
        # - **RENAME**: Renames a file.
        # - **CHOWN**: Changes the file owner and associated file group.
        self.operation = operation
        # The rule name.
        self.rule_name = rule_name
        # Specifies whether to select all items across pages. Valid values:
        # - **true**: Selected.
        # - **false**: Not selected.
        self.select_all_across_pages = select_all_across_pages
        # The start timestamp of the query.
        self.start_time = start_time
        # The event handling status.
        # - **0**: Unhandled
        # - **1**: Manually handled
        # - **2**: Added to whitelist
        # - **3**: Ignored
        self.status = status
        # The UUID of the server.
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

