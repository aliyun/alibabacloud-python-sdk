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
        # The source IP address.
        self.source_ip = source_ip
        # The configuration type. Valid values:
        # 
        # - **kdump_switch**: proactive defense optimization
        # - **threat_detect**: adaptive threat detection
        # - **suspicious_aggregation**: associate alerting
        # - **alidetect**: file detection
        # - **USER-ENABLE-SWITCH-TYPE_3277**: suspicious process startup
        # - **USER-ENABLE-SWITCH-TYPE_5507**: malicious driver
        # - **USER-ENABLE-SWITCH-TYPE_38857**: high-risk operations executed by entry services
        # - **USER-ENABLE-SWITCH-TYPE_50858**: high-risk operations executed by web services
        # - **USER-ENABLE-SWITCH-TYPE_50859**: suspicious operations executed by entry services
        # - **USER-ENABLE-SWITCH-TYPE_50861**: information probing
        # - **USER-ENABLE-SWITCH-TYPE_50862**: Cloud Assistant advanced protection
        # - **USER-ENABLE-SWITCH-TYPE_50867**: malicious file implantation
        # - **USER-ENABLE-SWITCH-TYPE_50868**: suspicious file implantation
        # - **USER-ENABLE-SWITCH-TYPE_50869**: unauthorized execution of high-risk commands
        # - **USER-ENABLE-SWITCH-TYPE_50870**: reverse shell
        # - **USER-ENABLE-SWITCH-TYPE_50873**: webshell command execution
        # - **USER-ENABLE-SWITCH-TYPE_50876**: security software evasion
        # - **USER-ENABLE-SWITCH-TYPE_50877**: malicious program communication
        # - **USER-ENABLE-SWITCH-TYPE_50884**: suspicious worm script behavior
        # - **USER-ENABLE-SWITCH-TYPE_50885**: malicious script behavior
        # - **USER-ENABLE-SWITCH-TYPE_50983**: obfuscation commands
        # - **USER-ENABLE-SWITCH-TYPE_51200**: downloading and running malicious files via command line
        # - **USER-ENABLE-SWITCH-TYPE_51201**: ransomware virus
        # - **USER-ENABLE-SWITCH-TYPE_51202**: suspicious ransomware behavior
        # - **USER-ENABLE-SWITCH-TYPE_53168**: process debugging
        # - **USER-ENABLE-SWITCH-TYPE_53272**: privilege escalation by exploiting kernel vulnerabilities
        # - **USER-ENABLE-SWITCH-TYPE_54034**: internal network scanning
        # - **USER-ENABLE-SWITCH-TYPE_54265**: PAM module hijacking
        # - **USER-ENABLE-SWITCH-TYPE_54395**: unauthorized reading and writing of sensitive files
        # - **USER-ENABLE-SWITCH-TYPE_54699**: dynamic-link library hijacking
        # - **USER-ENABLE-SWITCH-TYPE_54953**: HashDump attack
        # - **USER-ENABLE-SWITCH-TYPE_57897**: suspected privilege escalation
        # - **USER-ENABLE-SWITCH-TYPE_62981**: bypassing security monitoring
        # - **USER-ENABLE-SWITCH-TYPE_64025**: command execution by entry services [Enhanced pattern]
        # - **USER-ENABLE-SWITCH-TYPE_39659**: sensitive registry key protection
        # - **USER-ENABLE-SWITCH-TYPE_51225**: high-risk command execution by PowerShell
        # - **USER-ENABLE-SWITCH-TYPE_51226**: suspicious command execution by PowerShell
        # - **USER-ENABLE-SWITCH-TYPE_51228**: high-risk lateral movement tools
        # - **USER-ENABLE-SWITCH-TYPE_51229**: high-risk operations executed by browser services
        # - **USER-ENABLE-SWITCH-TYPE_51230**: suspicious operations executed by entry services
        # - **USER-ENABLE-SWITCH-TYPE_51232**: high-risk operations executed by system processes
        # - **USER-ENABLE-SWITCH-TYPE_51233**: high-risk operations executed by Java services
        # - **USER-ENABLE-SWITCH-TYPE_51234**: high-risk operations executed by Office components
        # - **USER-ENABLE-SWITCH-TYPE_51235**: high-risk operations executed by web services
        # - **USER-ENABLE-SWITCH-TYPE_51236**: reverse shell
        # - **USER-ENABLE-SWITCH-TYPE_52815**: loading high-risk drivers
        # - **USER-ENABLE-SWITCH-TYPE_52816**: high-risk account manipulation
        # - **USER-ENABLE-SWITCH-TYPE_52818**: information probing
        # - **USER-ENABLE-SWITCH-TYPE_52820**: malicious file implantation
        # - **USER-ENABLE-SWITCH-TYPE_52821**: suspicious process startup
        # - **USER-ENABLE-SWITCH-TYPE_52823**: running high-risk ARK tools
        # - **USER-ENABLE-SWITCH-TYPE_52825**: unauthorized execution of high-risk commands
        # - **USER-ENABLE-SWITCH-TYPE_52826**: high-risk operations executed by entry services
        # - **USER-ENABLE-SWITCH-TYPE_52827**: ransomware virus
        # - **USER-ENABLE-SWITCH-TYPE_52828**: suspicious ransomware behavior
        # - **USER-ENABLE-SWITCH-TYPE_52829**: delete system backup behavior
        # - **USER-ENABLE-SWITCH-TYPE_54168**: LSA security authority service protection
        # - **USER-ENABLE-SWITCH-TYPE_54365**: creating service auto-start items
        # - **USER-ENABLE-SWITCH-TYPE_54366**: creating high-risk auto-start items
        # - **USER-ENABLE-SWITCH-TYPE_54367**: creating scheduled node auto-start items
        # - **USER-ENABLE-SWITCH-TYPE_54368**: creating registry auto-start items
        # - **USER-ENABLE-SWITCH-TYPE_54369**: creating WMI auto-start items
        # - **USER-ENABLE-SWITCH-TYPE_54373**: security software evasion
        # - **USER-ENABLE-SWITCH-TYPE_54374**: intrusion trace cleanup
        # - **USER-ENABLE-SWITCH-TYPE_54384**: HashDump attack
        # - **USER-ENABLE-SWITCH-TYPE_55251**: high-risk operations executed by database services
        # - **USER-ENABLE-SWITCH-TYPE_57242**: malicious command execution
        # - **USER-ENABLE-SWITCH-TYPE_57340**: downloading and running malicious files via command line
        # - **USER-ENABLE-SWITCH-TYPE_62357**: Cloud Assistant service information probing
        # - **USER-ENABLE-SWITCH-TYPE_63725**: implantation of suspicious scripts or binary files by entry services
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

