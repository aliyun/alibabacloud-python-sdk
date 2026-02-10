# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSuspiciousOverallConfigRequest(DaraModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
    ):
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of the feature. Valid values:
        # 
        # *   **auto_breaking**: Anti-Virus
        # *   **ransomware_breaking**: Anti-ransomware (Bait Capture)
        # *   **webshell_cloud_breaking**: Webshell Protection
        # *   **alinet**: Behavior prevention
        # *   **k8s_log_analysis**: K8s Threat Detection
        # *   **alisecguard**: Defense mode for Client Protection
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

