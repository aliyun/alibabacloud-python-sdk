# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCommonOverallConfigRequest(DaraModel):
    def __init__(
        self,
        source_ip: str = None,
        type: str = None,
    ):
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of the feature. Valid values:
        # 
        # *   **kdump_switch**: Active defense experience optimization
        # *   **threat_detect**: Dynamic adaptive threat detection capability
        # *   **suspicious_aggregation**: Alert Association
        # *   **alidetect**: File Test
        # *   **USER-ENABLE-SWITCH-TYPE_3277**: Suspicious process startup
        # *   **USER-ENABLE-SWITCH-TYPE_5507**: malicious drivers
        # *   **USER-ENABLE-SWITCH-TYPE_38857**: Entrance service execution high-risk operation
        # *   **USER-ENABLE-SWITCH-TYPE_50858**: Web service performs high-risk operations
        # *   **USER-ENABLE-SWITCH-TYPE_50859**: Entrance service execution suspicious operation
        # *   **USER-ENABLE-SWITCH-TYPE_50861**: Information detection
        # *   **USER-ENABLE-SWITCH-TYPE_50862**: Cloud Assistant Advanced Protection
        # *   **USER-ENABLE-SWITCH-TYPE_50867**: Create malicious files
        # *   **USER-ENABLE-SWITCH-TYPE_50868**: Create suspicious files
        # *   **USER-ENABLE-SWITCH-TYPE_50869**: Unauthorized execution of high-risk orders
        # *   **USER-ENABLE-SWITCH-TYPE_50870**: Rebound Shell
        # *   **USER-ENABLE-SWITCH-TYPE_50873**: WebShell execute command
        # *   **USER-ENABLE-SWITCH-TYPE_50876**: Against security software
        # *   **USER-ENABLE-SWITCH-TYPE_50877**: Malicious soft communication
        # *   **USER-ENABLE-SWITCH-TYPE_50884**: Suspicious worm script behavior
        # *   **USER-ENABLE-SWITCH-TYPE_50885**: malicious script behavior
        # *   **USER-ENABLE-SWITCH-TYPE_50983**: obfuscated command
        # *   **USER-ENABLE-SWITCH-TYPE_51200**: Command line download and run malicious files
        # *   **USER-ENABLE-SWITCH-TYPE_51201**: ransomware
        # *   **USER-ENABLE-SWITCH-TYPE_51202**: Suspected Extortion
        # *   **USER-ENABLE-SWITCH-TYPE_53168**: process debugging
        # *   **USER-ENABLE-SWITCH-TYPE_53272**: Exploiting Kernel Vulnerabilities to Elevate Privileges
        # *   **USER-ENABLE-SWITCH-TYPE_54034**: Intranet scan
        # *   **USER-ENABLE-SWITCH-TYPE_54265**: Hijacking the PAM Module
        # *   **USER-ENABLE-SWITCH-TYPE_54395**: Unauthorized reading and writing of sensitive files
        # *   **USER-ENABLE-SWITCH-TYPE_54699**: Hijack dynamic link library
        # *   **USER-ENABLE-SWITCH-TYPE_54953**: Hashdump Attack
        # *   **USER-ENABLE-SWITCH-TYPE_57897**: suspected privilege escalation
        # *   **USER-ENABLE-SWITCH-TYPE_62981**: Bypassing security monitoring
        # *   **USER-ENABLE-SWITCH-TYPE_64025**: Ingress service execute command [enhanced mode]
        # *   **USER-ENABLE-SWITCH-TYPE_39659**: Sensitive Registry Key Protection
        # *   **USER-ENABLE-SWITCH-TYPE_51225**: Powershell executes high-risk commands
        # *   **USER-ENABLE-SWITCH-TYPE_51226**: Powershell execute suspicious command
        # *   **USER-ENABLE-SWITCH-TYPE_51228**: High-risk lateral penetration tools
        # *   **USER-ENABLE-SWITCH-TYPE_51229**: Browser service execution a high-risk operation
        # *   **USER-ENABLE-SWITCH-TYPE_51230**: Entrance service execution suspicious operation
        # *   **USER-ENABLE-SWITCH-TYPE_51232**: System processes execution high-risk operations
        # *   **USER-ENABLE-SWITCH-TYPE_51233**: Java service execution high-risk operations
        # *   **USER-ENABLE-SWITCH-TYPE_51234**: Office components execution high-risk operations
        # *   **USER-ENABLE-SWITCH-TYPE_51235**: Web service performs high-risk operations
        # *   **USER-ENABLE-SWITCH-TYPE_51236**: Rebound shells
        # *   **USER-ENABLE-SWITCH-TYPE_52815**: Load high-risk drivers
        # *   **USER-ENABLE-SWITCH-TYPE_52816**: high-risk account manipulation behavior
        # *   **USER-ENABLE-SWITCH-TYPE_52818**: Information detection
        # *   **USER-ENABLE-SWITCH-TYPE_52820**: Create malicious files
        # *   **USER-ENABLE-SWITCH-TYPE_52821**: Suspicious process startup
        # *   **USER-ENABLE-SWITCH-TYPE_52823**: Running high-risk ARK tools
        # *   **USER-ENABLE-SWITCH-TYPE_52825**: Unauthorized execution of high-risk orders
        # *   **USER-ENABLE-SWITCH-TYPE_52826**: Entrance service execution high-risk operation
        # *   **USER-ENABLE-SWITCH-TYPE_52827**: Ransomware
        # *   **USER-ENABLE-SWITCH-TYPE_52828**: Suspected Extortion
        # *   **USER-ENABLE-SWITCH-TYPE_52829**: delete system backup behavior
        # *   **USER-ENABLE-SWITCH-TYPE_54168**: LSA security permission service protection
        # *   **USER-ENABLE-SWITCH-TYPE_54365**: Create service autorun item
        # *   **USER-ENABLE-SWITCH-TYPE_54366**: Create high-risk autorun item
        # *   **USER-ENABLE-SWITCH-TYPE_54367**: Create scheduled task autorun item
        # *   **USER-ENABLE-SWITCH-TYPE_54368**: Create registry autorun item
        # *   **USER-ENABLE-SWITCH-TYPE_54369**: Create WMI autorun item
        # *   **USER-ENABLE-SWITCH-TYPE_54373**: Against security software
        # *   **USER-ENABLE-SWITCH-TYPE_54374**: Intrusion trace cleanup
        # *   **USER-ENABLE-SWITCH-TYPE_54384**: Hashdump Attack
        # *   **USER-ENABLE-SWITCH-TYPE_55251**: Database services execution high-risk operations
        # *   **USER-ENABLE-SWITCH-TYPE_57242**: Malicious command execution
        # *   **USER-ENABLE-SWITCH-TYPE_57340**: Command line download and run malicious files
        # *   **USER-ENABLE-SWITCH-TYPE_62357**: Cloud Assistant service information detection
        # *   **USER-ENABLE-SWITCH-TYPE_63725**: Ingress service implants suspicious script/binary file
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

