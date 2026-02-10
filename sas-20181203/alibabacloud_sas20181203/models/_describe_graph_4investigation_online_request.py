# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGraph4InvestigationOnlineRequest(DaraModel):
    def __init__(
        self,
        anomaly_id: str = None,
        anomaly_uuid: str = None,
        lang: str = None,
        namespace: str = None,
        vertex_id: str = None,
    ):
        # The ID of the alert event. You can call [DescribeSuspEvents](~~DescribeSuspEvents~~) to obtain the alert event ID, with the value path being: data.SuspEvents[index].UniqueInfo.
        self.anomaly_id = anomaly_id
        # The UUID of the alert event asset. You can call [DescribeSuspEvents](~~DescribeSuspEvents~~) to obtain the asset UUID, with the value path being: data.SuspEvents[index].Uuid.
        self.anomaly_uuid = anomaly_uuid
        # Sets the language type for the request and response messages. The default is **zh**. Values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The namespace of the graph, which is fixed as: hundun_dc_online.
        # 
        # This parameter is required.
        self.namespace = namespace
        # Vertex ID. This does not need to be proactively provided.
        self.vertex_id = vertex_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anomaly_id is not None:
            result['AnomalyId'] = self.anomaly_id

        if self.anomaly_uuid is not None:
            result['AnomalyUuid'] = self.anomaly_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.vertex_id is not None:
            result['VertexId'] = self.vertex_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnomalyId') is not None:
            self.anomaly_id = m.get('AnomalyId')

        if m.get('AnomalyUuid') is not None:
            self.anomaly_uuid = m.get('AnomalyUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('VertexId') is not None:
            self.vertex_id = m.get('VertexId')

        return self

