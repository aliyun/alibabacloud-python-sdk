# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAndAnalyzeNetworkPathResponseBody(DaraModel):
    def __init__(
        self,
        network_reachable_analysis_id: str = None,
        protocol: str = None,
        request_id: str = None,
        source_id: str = None,
        source_ip_address: str = None,
        source_port: str = None,
        source_type: str = None,
        target_id: str = None,
        target_ip_address: str = None,
        target_port: str = None,
        target_type: str = None,
    ):
        # The ID of the task for analyzing network reachability that you initiated.
        self.network_reachable_analysis_id = network_reachable_analysis_id
        # The protocol type.
        self.protocol = protocol
        # The request ID.
        self.request_id = request_id
        # The ID of the source resource.
        self.source_id = source_id
        # The source IP address.
        self.source_ip_address = source_ip_address
        # The source port.
        self.source_port = source_port
        # The type of the source resource.
        self.source_type = source_type
        # The ID of the destination resource.
        self.target_id = target_id
        # The destination IP address.
        self.target_ip_address = target_ip_address
        # The destination port.
        self.target_port = target_port
        # The type of the destination resource.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_reachable_analysis_id is not None:
            result['NetworkReachableAnalysisId'] = self.network_reachable_analysis_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_ip_address is not None:
            result['SourceIpAddress'] = self.source_ip_address

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_ip_address is not None:
            result['TargetIpAddress'] = self.target_ip_address

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkReachableAnalysisId') is not None:
            self.network_reachable_analysis_id = m.get('NetworkReachableAnalysisId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceIpAddress') is not None:
            self.source_ip_address = m.get('SourceIpAddress')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetIpAddress') is not None:
            self.target_ip_address = m.get('TargetIpAddress')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

