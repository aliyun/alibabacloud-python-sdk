# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCommonOverallConfigListResponseBody(DaraModel):
    def __init__(
        self,
        overall_list: List[main_models.DescribeCommonOverallConfigListResponseBodyOverallList] = None,
        request_id: str = None,
    ):
        # The information about the configuration items.
        self.overall_list = overall_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.overall_list:
            for v1 in self.overall_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OverallList'] = []
        if self.overall_list is not None:
            for k1 in self.overall_list:
                result['OverallList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.overall_list = []
        if m.get('OverallList') is not None:
            for k1 in m.get('OverallList'):
                temp_model = main_models.DescribeCommonOverallConfigListResponseBodyOverallList()
                self.overall_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCommonOverallConfigListResponseBodyOverallList(DaraModel):
    def __init__(
        self,
        auth_version_list: List[str] = None,
        config: str = None,
        total_count: int = None,
        type: str = None,
    ):
        # The editions of Security Center.
        self.auth_version_list = auth_version_list
        # Indicates the status of the switch. Valid values:
        # 
        # *   **off**
        # *   **on**
        self.config = config
        # The total number of entries that are returned.
        self.total_count = total_count
        # The type of the configuration. Valid values:
        # 
        # *   **kdump_switch**: Active defense experience optimization.
        # *   **threat_detect**: Adaptive threat detection.
        # *   **suspicious_aggregation**: Alert association.
        # *   **alidetect**: File detection.
        # *   **USER-ENABLE-SWITCH-TYPE_38857**: Entrance service performs high-risk operations (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50858**: Web service performs high-risk operations (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50859**: Entrance service performs suspicious operations (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50862**: Cloud Assistant advanced protection (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50867**: Injects malicious files (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50868**: Injects suspicious files (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_64025**: Entrance service executes commands in an enhanced mode (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_51229**: Browser service performs high-risk operations (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_51230**: Entrance service performs suspicious operations (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_51232**: System processes perform high-risk operations (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_51233**: Java service performs high-risk operations (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_51234**: Office components perform high-risk operations (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_51235**: Web service performs high-risk operations (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_52820**: Injects malicious files (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_52826**: Entrance service performs high-risk operations (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_55251**: Database services perform high-risk operations (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_63725**: Entrance service injects suspicious scripts or binary files (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_3277**: Suspicious process startup (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50983**: Obfuscated commands (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_51200**: Uses command line to download and run malicious files (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_71131**: Entrance service executes sequence of suspicious behavior (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_51225**: Powershell executes high-risk commands (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_51226**: Powershell executes suspicious commands (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_52821**: Suspicious process startup (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_57242**: Malicious command execution (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_57340**: Uses command line to download and run malicious files (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_39659**: Sensitive registry key protection (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_52816**: High-risk account manipulation behavior (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54365**: Creates service auto-startup items (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54366**: Creates high-risk auto-startup items (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54367**: Creates scheduled task auto-startup items (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54368**: Creates registry auto-startup items (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54369**: Creates WMI auto-startup items (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_50869**: Unauthorized execution of high-risk commands (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_53272**: Exploits kernel vulnerabilities to elevate privileges (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_54395**: Unauthorized reading and writing of sensitive files (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_57897**: Suspected privilege escalation (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_52825**: Unauthorized execution of high-risk commands (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_5507**: Malicious drivers (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50876**: Uninstalls security software (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_53168**: Process debugging (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_54699**: Hijacks dynamic link library (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_62981**: Bypasses security monitoring (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_52815**: Loads high-risk drivers (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_52823**: Runs high-risk anti-rootkit (ARK) tools (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54373**: Uninstalls security software (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54374**: Intrusion trace cleanup (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54265**: Hijacks the pluggable authentication module (PAM) (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_54953**: Hashdump attack (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_54383**: MimiKatz credential stealing (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54384**: Hashdump attack (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_50861**: Information detection (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_52818**: Information detection (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_54034**: Intranet scan (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_51228**: High-risk lateral penetration tools (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_50870**: Rebound shell (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50873**: WebShell executes commands.
        # *   **USER-ENABLE-SWITCH-TYPE_51236**: Rebound shell (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_50877**: Malicious program communication (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50884**: Suspicious worm script behavior (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_50885**: Malicious script behavior (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_51201**: Ransomware (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_51202**: Suspected extortion (Linux).
        # *   **USER-ENABLE-SWITCH-TYPE_52827**: Ransomware (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_52828**: Suspected extortion (Windows).
        # *   **USER-ENABLE-SWITCH-TYPE_52829**: Deletes system backup behavior (Windows).
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_version_list is not None:
            result['AuthVersionList'] = self.auth_version_list

        if self.config is not None:
            result['Config'] = self.config

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthVersionList') is not None:
            self.auth_version_list = m.get('AuthVersionList')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

