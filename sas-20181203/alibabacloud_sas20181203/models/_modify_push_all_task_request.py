# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPushAllTaskRequest(DaraModel):
    def __init__(
        self,
        source_ip: str = None,
        tasks: str = None,
        uuids: str = None,
    ):
        # The IP address of the access source.
        self.source_ip = source_ip
        # The check items to include in the security check. Separate multiple check items with commas (,). Valid values:
        # - **OVAL_ENTITY**: CVE vulnerabilities
        # - **CMS**: Web-CMS vulnerabilities
        # - **SYSVUL**: system vulnerabilities
        # - **SCA**: application vulnerabilities
        # - **HEALTH_CHECK**: baselines
        # - **WEBSHELL**: web shells
        # - **PROC_SNAPSHOT**: processes
        # - **PORT_SNAPSHOT**: ports
        # - **ACCOUNT_SNAPSHOT**: accounts
        # - **SOFTWARE_SNAPSHOT**: software
        # - **SCA_SNAPSHOT**: middleware, databases, and web services
        # - **CROND_SNAPSHOT**: scheduled tasks
        # - **AUTORUN_SNAPSHOT**: startup items
        # - **LKM_SNAPSHOT**: kernel modules
        # - **SCA_PROXY_SNAPSHOT**: websites.
        # 
        # This parameter is required.
        self.tasks = tasks
        # The UUIDs of the servers on which you want to perform security checks. Separate multiple UUIDs with commas (,).
        # 
        # This parameter is required.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.tasks is not None:
            result['Tasks'] = self.tasks

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

