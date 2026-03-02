# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeploymentsByIpRequest(DaraModel):
    def __init__(
        self,
        dst_ip: str = None,
        dst_port: str = None,
        ignore_job_summary: bool = None,
        ignore_resource_setting: bool = None,
        src_ip: str = None,
        src_port: str = None,
    ):
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.ignore_job_summary = ignore_job_summary
        self.ignore_resource_setting = ignore_resource_setting
        self.src_ip = src_ip
        self.src_port = src_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_ip is not None:
            result['dstIp'] = self.dst_ip

        if self.dst_port is not None:
            result['dstPort'] = self.dst_port

        if self.ignore_job_summary is not None:
            result['ignoreJobSummary'] = self.ignore_job_summary

        if self.ignore_resource_setting is not None:
            result['ignoreResourceSetting'] = self.ignore_resource_setting

        if self.src_ip is not None:
            result['srcIp'] = self.src_ip

        if self.src_port is not None:
            result['srcPort'] = self.src_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dstIp') is not None:
            self.dst_ip = m.get('dstIp')

        if m.get('dstPort') is not None:
            self.dst_port = m.get('dstPort')

        if m.get('ignoreJobSummary') is not None:
            self.ignore_job_summary = m.get('ignoreJobSummary')

        if m.get('ignoreResourceSetting') is not None:
            self.ignore_resource_setting = m.get('ignoreResourceSetting')

        if m.get('srcIp') is not None:
            self.src_ip = m.get('srcIp')

        if m.get('srcPort') is not None:
            self.src_port = m.get('srcPort')

        return self

