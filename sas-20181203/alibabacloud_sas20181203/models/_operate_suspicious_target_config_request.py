# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateSuspiciousTargetConfigRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        target_operations: str = None,
        target_type: str = None,
        type: str = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip
        # The configuration of proactive defense for your server. The value includes the following fields:
        # 
        # *   **targetType**: specifies the dimension from which you manage proactive defense. UUIDs are supported. Set the value to **uuid**.
        # *   **target**: specifies the UUID of the server for which you want to configure proactive defense.
        # *   **flag**: specifies whether to enable or disable proactive defense for your server. Valid values are **add** and **del**. The value add indicates that proactive defense will be enabled for your server. The value del indicates that proactive defense will be disabled for your server.
        # 
        # This parameter is required.
        self.target_operations = target_operations
        # The dimension from which you manage proactive defense. Only the server UUID dimension is supported.
        # 
        # Set the value to **uuid**.
        # 
        # This parameter is required.
        self.target_type = target_type
        # The type of proactive defense. Valid Values:
        # 
        # *   **auto_breaking**: automatic blocking
        # *   **webshell_cloud_breaking**: webshell defense
        # *   **alinet**: malicious behavior defense
        # *   **ransomware_breaking**: ransomware capture
        # *   **alisecguard**: client protection
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
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.target_operations is not None:
            result['TargetOperations'] = self.target_operations

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TargetOperations') is not None:
            self.target_operations = m.get('TargetOperations')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

