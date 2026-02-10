# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateFileProtectRemarkRequest(DaraModel):
    def __init__(
        self,
        alert_levels: List[int] = None,
        end_time: int = None,
        id: int = None,
        id_list: List[int] = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        operation: str = None,
        remark: List[str] = None,
        rule_name: str = None,
        select_all_across_pages: bool = None,
        start_time: int = None,
        uuid: str = None,
    ):
        # Alert notification level list.
        self.alert_levels = alert_levels
        # End time timestamp.
        self.end_time = end_time
        # The ID of the event.
        self.id = id
        # Event ID list.
        self.id_list = id_list
        # Asset instance ID.
        self.instance_id = instance_id
        # Asset instance name.
        self.instance_name = instance_name
        # Public IP.
        self.internet_ip = internet_ip
        # Private IP.
        self.intranet_ip = intranet_ip
        # File operation type. Values:
        # 
        # - **DELETE**: File deletion operation.
        # - **WRITE**: File write operation.
        # - **READ**: File read operation.
        # - **RENAME**: File rename operation.
        # - **CHOWN**: Set file owner and associated group operation.
        self.operation = operation
        # The remarks.
        self.remark = remark
        # Rule name.
        self.rule_name = rule_name
        # Cross-page select all indicator. Values:
        # - **true**: Yes
        # - **false**: No
        self.select_all_across_pages = select_all_across_pages
        # Start time timestamp.
        self.start_time = start_time
        # Server UUID.
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

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.select_all_across_pages is not None:
            result['SelectAllAcrossPages'] = self.select_all_across_pages

        if self.start_time is not None:
            result['StartTime'] = self.start_time

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

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SelectAllAcrossPages') is not None:
            self.select_all_across_pages = m.get('SelectAllAcrossPages')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

