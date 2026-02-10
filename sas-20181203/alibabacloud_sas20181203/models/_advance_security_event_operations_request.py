# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AdvanceSecurityEventOperationsRequest(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        event_type: str = None,
        resource_owner_id: int = None,
        rule_id: int = None,
    ):
        # The alert name.
        self.event_name = event_name
        # The alert event type. Valid values:
        # 
        # *   Suspicious process
        # *   Webshell
        # *   Unusual logon
        # *   Exception
        # *   Sensitive file tampering
        # *   Malicious process (cloud threat detection)
        # *   Unusual network connection
        # *   Abnormal account
        # *   Application intrusion event
        # *   Cloud threat detection
        # *   Precision defense
        # *   Application whitelist
        # *   Persistent webshell
        # *   Web application threat detection
        # *   Malicious script
        # *   Threat intelligence
        # *   Malicious network activity
        # *   Cluster exception
        # *   Webshell (on-premises threat detection)
        # *   Vulnerability exploitation
        # *   Malicious process (on-premises threat detection)
        # *   Trusted exception
        # *   Others
        # 
        # For more information about alert types, see [Alerts](https://help.aliyun.com/document_detail/68388.html).
        self.event_type = event_type
        self.resource_owner_id = resource_owner_id
        # The rule ID.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

