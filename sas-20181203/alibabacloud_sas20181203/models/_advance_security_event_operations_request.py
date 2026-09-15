# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AdvanceSecurityEventOperationsRequest(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        event_type: str = None,
        resource_directory_account_id: int = None,
        resource_owner_id: int = None,
        rule_id: int = None,
    ):
        # The alert name. The EventName and EventType parameters must be specified together. If only one of them is specified, the API returns a 400 error.
        self.event_name = event_name
        # The type of the alerting event. Valid values:
        # 
        # - Abnormal process behavior
        # - Web shell
        # - Unusual logon
        # - Abnormal event
        # - Sensitive file tampering
        # - Malicious process (cloud scan)
        # - Suspicious network connection
        # - Abnormal account
        # - Application intrusion event
        # - Cloud service threat detection
        # - Precise defense
        # - Application whitelist
        # - Persistent backdoor
        # - Web application threat detection
        # - Malicious script
        # - Threat intelligence
        # - Malicious network behavior
        # - Container cluster exception
        # - Web shell (local scan)
        # - Vulnerability exploits
        # - Malicious process (local scan)
        # - Trusted exception
        # - Other
        # 
        # For more information about alert types, see [Security alert check items](https://help.aliyun.com/document_detail/68388.html).
        # 
        # The EventName and EventType parameters must be specified together. If only one of them is specified, the API returns a 400 error.
        self.event_type = event_type
        # The member account ID in the resource directory (Alibaba Cloud account).
        self.resource_directory_account_id = resource_directory_account_id
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

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

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

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

