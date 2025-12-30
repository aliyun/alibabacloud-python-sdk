# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListSyslogsResponseBody(DaraModel):
    def __init__(
        self,
        logs: List[main_models.ListSyslogsResponseBodyLogs] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.logs = logs
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.ListSyslogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSyslogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        domain: str = None,
        facility: str = None,
        hostname: str = None,
        ip: str = None,
        msg: str = None,
        node_id: str = None,
        severity: str = None,
        sn: str = None,
        source: str = None,
        syslogtag: str = None,
        tag_hostname: str = None,
        tag_pack_id: str = None,
        tag_path: str = None,
        tag_receive_time: str = None,
        tag_user_defined_id: str = None,
        time: str = None,
        topic: str = None,
    ):
        self.cluster_id = cluster_id
        self.domain = domain
        self.facility = facility
        self.hostname = hostname
        self.ip = ip
        self.msg = msg
        self.node_id = node_id
        self.severity = severity
        self.sn = sn
        self.source = source
        self.syslogtag = syslogtag
        self.tag_hostname = tag_hostname
        self.tag_pack_id = tag_pack_id
        self.tag_path = tag_path
        self.tag_receive_time = tag_receive_time
        self.tag_user_defined_id = tag_user_defined_id
        self.time = time
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.facility is not None:
            result['Facility'] = self.facility

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.source is not None:
            result['Source'] = self.source

        if self.syslogtag is not None:
            result['Syslogtag'] = self.syslogtag

        if self.tag_hostname is not None:
            result['TagHostname'] = self.tag_hostname

        if self.tag_pack_id is not None:
            result['TagPackId'] = self.tag_pack_id

        if self.tag_path is not None:
            result['TagPath'] = self.tag_path

        if self.tag_receive_time is not None:
            result['TagReceiveTime'] = self.tag_receive_time

        if self.tag_user_defined_id is not None:
            result['TagUserDefinedId'] = self.tag_user_defined_id

        if self.time is not None:
            result['Time'] = self.time

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Facility') is not None:
            self.facility = m.get('Facility')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Syslogtag') is not None:
            self.syslogtag = m.get('Syslogtag')

        if m.get('TagHostname') is not None:
            self.tag_hostname = m.get('TagHostname')

        if m.get('TagPackId') is not None:
            self.tag_pack_id = m.get('TagPackId')

        if m.get('TagPath') is not None:
            self.tag_path = m.get('TagPath')

        if m.get('TagReceiveTime') is not None:
            self.tag_receive_time = m.get('TagReceiveTime')

        if m.get('TagUserDefinedId') is not None:
            self.tag_user_defined_id = m.get('TagUserDefinedId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

