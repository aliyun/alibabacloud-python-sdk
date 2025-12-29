# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataInstancesValueListenersValue(DaraModel):
    def __init__(
        self,
        protocol: str = None,
        port: int = None,
        status: str = None,
        target_port: int = None,
        cert_ids: str = None,
    ):
        # The listener protocol.
        self.protocol = protocol
        # The listener port of the NLB instance.
        self.port = port
        # The status of the NLB listener.
        # 
        # *   **Creating**: The listener is being created.
        # *   **Configuring**: The listener is being configured.
        # *   **Bounded**: The listener runs as expected.
        # *   **Unbinding**: The listener is being deleted.
        # *   **Failed**: The listener is unavailable.
        self.status = status
        # The open ports of the NLB instance.
        self.target_port = target_port
        # The server certificates.
        self.cert_ids = cert_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.port is not None:
            result['Port'] = self.port

        if self.status is not None:
            result['Status'] = self.status

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')

        return self

