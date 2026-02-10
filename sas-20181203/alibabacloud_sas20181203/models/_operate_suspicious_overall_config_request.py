# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateSuspiciousOverallConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        lang: str = None,
        no_target_as_on: bool = None,
        source_ip: str = None,
        type: str = None,
    ):
        # Specifies whether to enable the feature. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        # 
        # This parameter is required.
        self.config = config
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # Specifies whether to configure assets for the feature. Default value: **false**. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  This parameter takes effect only when you set **Config** to **on**.
        self.no_target_as_on = no_target_as_on
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
        if self.config is not None:
            result['Config'] = self.config

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.no_target_as_on is not None:
            result['NoTargetAsOn'] = self.no_target_as_on

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NoTargetAsOn') is not None:
            self.no_target_as_on = m.get('NoTargetAsOn')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

