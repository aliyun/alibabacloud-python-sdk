# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchOperateCommonOverallConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        type_list: List[str] = None,
    ):
        # The status of the feature. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        # 
        # This parameter is required.
        self.config = config
        # The type of the feature in proactive defense. Valid values:
        # 
        # *   **kdump_switch**: Active defense experience optimization
        # *   **threat_detect**: Dynamic adaptive threat detection capability
        # *   **suspicious_aggregation**: Alert Association
        # *   **alidetect**: File Test
        # *   **USER-ENABLE-SWITCH-TYPE_38857**: Entrance service execution high-risk operation (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50858**: Web service performs high-risk operations (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50859**: Entrance service execution suspicious operation (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50862**: Cloud Assistant Advanced Protection (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50867**: Create malicious files (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50868**: Create suspicious files (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_64025**: Ingress service execute command [enhanced mode] (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_51229**: Browser service execution a high-risk operation (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_51230**: Entrance service execution suspicious operation (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_51232**: System processes execution high-risk operations (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_51233**: Java service execution high-risk operations (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_51234**: Office components execution high-risk operations (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_51235**: Web service performs high-risk operations (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_52820**: Create malicious files (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_52826**: Entrance service execution high-risk operation (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_55251**: Database services execution high-risk operations (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_63725**: Ingress service implants suspicious script/binary file (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_3277**: Suspicious process startup (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50983**: obfuscated command (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_51200**: Command line download and run malicious files (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_71131**: Ingress service executes sequence of suspicious behavior (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_51225**: Powershell executes high-risk commands (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_51226**: Powershell execute suspicious command (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_52821**: Suspicious process startup (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_57242**: Malicious command execution (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_57340**: Command line download and run malicious files (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_39659**: Sensitive Registry Key Protection (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_52816**: high-risk account manipulation behavior (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54365**: Create service autorun item (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54366**: Create high-risk autorun item (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54367**: Create scheduled task autorun item (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54368**: Create registry autorun item (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54369**: Create WMI autorun item (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_50869**: Unauthorized execution of high-risk orders (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_53272**: Exploiting Kernel Vulnerabilities to Elevate Privileges (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_54395**: Unauthorized reading and writing of sensitive files (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_57897**: suspected privilege escalation (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_52825**: Unauthorized execution of high-risk orders (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_5507**: malicious drivers (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50876**: Against security software (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_53168**: process debugging (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_54699**: Hijack dynamic link library (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_62981**: Bypassing security monitoring (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_52815**: Load high-risk drivers (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_52823**: Running high-risk ARK tools (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54373**: Against security software (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54374**: Intrusion trace cleanup (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54265**: Hijacking the PAM Module (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_54953**: Hashdump Attack (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_54383**: MimiKatz Credential Stealing (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54384**: Hashdump Attack (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_50861**: Information detection (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_52818**: Information detection (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_54034**: Intranet scan (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_51228**: High-risk lateral penetration tools (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_50870**: Rebound Shell (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50873**: WebShell execute command
        # *   **USER-ENABLE-SWITCH-TYPE_51236**: Rebound Shell (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_50877**: Malicious soft communication (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50884**: Suspicious worm script behavior (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_50885**: malicious script behavior (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_51201**: ransomware (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_51202**: Suspected Extortion (Linux)
        # *   **USER-ENABLE-SWITCH-TYPE_52827**: ransomware (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_52828**: Suspected Extortion (Windows)
        # *   **USER-ENABLE-SWITCH-TYPE_52829**: delete system backup behavior (Windows)
        # 
        # This parameter is required.
        self.type_list = type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.type_list is not None:
            result['TypeList'] = self.type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('TypeList') is not None:
            self.type_list = m.get('TypeList')

        return self

