# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyAntiBruteForceRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        default_rule: bool = None,
        fail_count: int = None,
        forbidden_time: int = None,
        id: int = None,
        name: str = None,
        protocol_type_shrink: str = None,
        resource_owner_id: int = None,
        source_ip: str = None,
        span: int = None,
        uuid_list: List[str] = None,
    ):
        # Specifies whether the defense rule against brute-force attacks is set as the default policy in Settings. Valid values:
        # 
        # - **true**: The rule is set as the default policy.
        # 
        # - **false**: The rule is not set as the default policy.
        self.default_rule = default_rule
        # The threshold for the number of logon failures. Valid values:
        # 
        # - **2**: 2 times
        # - **3**: 3 times
        # - **4**: 4 times
        # - **5**: 5 times
        # - **10**: 10 times
        # - **50**: 50 times
        # - **80**: 80 times
        # - **100**: 100 times.
        self.fail_count = fail_count
        # The duration for which logon is prohibited, in minutes. Valid values:
        # 
        # - **5**: 5 minutes
        # - **15**: 15 minutes
        # - **30**: 30 minutes
        # - **60**: 1 hour
        # - **120**: 2 hours
        # - **360**: 6 hours
        # - **720**: 12 hours
        # - **1440**: 24 hours
        # - **10080**: 7 days
        # - **52560000**: permanent (100 years).
        self.forbidden_time = forbidden_time
        # The ID of the defense rule against brute-force attacks.
        # 
        # This parameter is required.
        self.id = id
        # The name of the defense rule against brute-force attacks.
        self.name = name
        # The protocol types that the defense rule against brute-force attacks supports for interception.
        self.protocol_type_shrink = protocol_type_shrink
        self.resource_owner_id = resource_owner_id
        # The IP address of the access source.
        self.source_ip = source_ip
        # The threshold for the period of time during which logon failures are counted, in minutes. Valid values:
        # 
        # - **1**: 1 minute
        # - **2**: 2 minutes
        # - **5**: 5 minutes
        # - **10**: 10 minutes
        # - **15**: 15 minutes.
        self.span = span
        # The list of servers to which the defense rule against brute-force attacks applies.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.forbidden_time is not None:
            result['ForbiddenTime'] = self.forbidden_time

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol_type_shrink is not None:
            result['ProtocolType'] = self.protocol_type_shrink

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.span is not None:
            result['Span'] = self.span

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('ForbiddenTime') is not None:
            self.forbidden_time = m.get('ForbiddenTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProtocolType') is not None:
            self.protocol_type_shrink = m.get('ProtocolType')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Span') is not None:
            self.span = m.get('Span')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

