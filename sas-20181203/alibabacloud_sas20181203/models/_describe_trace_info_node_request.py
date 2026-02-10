# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTraceInfoNodeRequest(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        from_: str = None,
        incident_time: int = None,
        lang: str = None,
        source_ip: str = None,
        type: str = None,
        uuid: str = None,
        vertex_id: str = None,
    ):
        # The name of the alert event.
        # 
        # > You can call the [DescribeSuspEvents](~~DescribeSuspEvents~~) operation to query the names of alerts events.
        self.event_name = event_name
        # The ID of the request source. Set the value to sas.
        # 
        # This parameter is required.
        self.from_ = from_
        # The time when the alert event was first detected.
        self.incident_time = incident_time
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request. The value of this parameter is specified by the system.
        self.source_ip = source_ip
        # The type of the vertex. You can call the [DescribeTraceInfoDetail](~~DescribeTraceInfoDetail~~) operation to query the types of vertexes.
        # 
        # This parameter is required.
        self.type = type
        # The UUID of the server. You can call the [DescribeSuspEvents](~~DescribeSuspEvents~~) operation to query the UUIDs of servers.
        # 
        # This parameter is required.
        self.uuid = uuid
        # The ID of the vertex.
        # 
        # This parameter is required.
        self.vertex_id = vertex_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.from_ is not None:
            result['From'] = self.from_

        if self.incident_time is not None:
            result['IncidentTime'] = self.incident_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vertex_id is not None:
            result['VertexId'] = self.vertex_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('IncidentTime') is not None:
            self.incident_time = m.get('IncidentTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VertexId') is not None:
            self.vertex_id = m.get('VertexId')

        return self

