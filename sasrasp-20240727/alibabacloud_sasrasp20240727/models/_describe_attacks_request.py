# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAttacksRequest(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        application_id: str = None,
        attack_host_id: str = None,
        attack_type: str = None,
        attack_url: str = None,
        end_timestamp: int = None,
        handle_status: int = None,
        handler_type: str = None,
        hostname: str = None,
        ip: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        pid: str = None,
        rasp_type: str = None,
        region: str = None,
        remote: str = None,
        severity: str = None,
        start_timestamp: int = None,
        union_id: str = None,
    ):
        self.agent_type = agent_type
        self.application_id = application_id
        self.attack_host_id = attack_host_id
        self.attack_type = attack_type
        self.attack_url = attack_url
        # This parameter is required.
        self.end_timestamp = end_timestamp
        self.handle_status = handle_status
        self.handler_type = handler_type
        self.hostname = hostname
        self.ip = ip
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.pid = pid
        self.rasp_type = rasp_type
        self.region = region
        self.remote = remote
        self.severity = severity
        # This parameter is required.
        self.start_timestamp = start_timestamp
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.attack_host_id is not None:
            result['AttackHostId'] = self.attack_host_id

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.attack_url is not None:
            result['AttackUrl'] = self.attack_url

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status

        if self.handler_type is not None:
            result['HandlerType'] = self.handler_type

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.rasp_type is not None:
            result['RaspType'] = self.rasp_type

        if self.region is not None:
            result['Region'] = self.region

        if self.remote is not None:
            result['Remote'] = self.remote

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.union_id is not None:
            result['UnionId'] = self.union_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('AttackHostId') is not None:
            self.attack_host_id = m.get('AttackHostId')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('AttackUrl') is not None:
            self.attack_url = m.get('AttackUrl')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')

        if m.get('HandlerType') is not None:
            self.handler_type = m.get('HandlerType')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RaspType') is not None:
            self.rasp_type = m.get('RaspType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Remote') is not None:
            self.remote = m.get('Remote')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')

        return self

