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
        # The switch status. Valid values:
        # 
        # - **on**: Enable
        # - **off**: Disable
        # 
        # This parameter is required.
        self.config = config
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Specifies whether asset configuration is required. Default value: **false**. Valid values:
        # - **true**: Required
        # - **false**: Not required
        # > This value takes effect only when **config** is set to **on**.
        self.no_target_as_on = no_target_as_on
        # The IP address of the access source.
        self.source_ip = source_ip
        # The switch type. Valid values:
        # 
        # - **auto_breaking**: Anti-virus
        # - **ransomware_breaking**: Anti-ransomware (bait capture)
        # - **webshell_cloud_breaking**: Website backdoor connection defense
        # - **alinet**: Malicious network behavior defense
        # - **k8s_log_analysis**: Container K8s threat detection
        # - **alisecguard**: Client self-protection defense mode
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

