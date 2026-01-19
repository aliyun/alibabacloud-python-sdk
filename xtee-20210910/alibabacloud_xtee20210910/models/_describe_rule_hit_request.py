# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRuleHitRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        reg_id: str = None,
        request_time: int = None,
        rule_id: str = None,
        rule_snapshot_id: str = None,
        s_request_id: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Region code
        self.reg_id = reg_id
        # Execution time
        self.request_time = request_time
        # Rule ID
        self.rule_id = rule_id
        # Snapshot ID.
        self.rule_snapshot_id = rule_snapshot_id
        # Request ID.
        self.s_request_id = s_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.request_time is not None:
            result['requestTime'] = self.request_time

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_snapshot_id is not None:
            result['ruleSnapshotId'] = self.rule_snapshot_id

        if self.s_request_id is not None:
            result['sRequestId'] = self.s_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleSnapshotId') is not None:
            self.rule_snapshot_id = m.get('ruleSnapshotId')

        if m.get('sRequestId') is not None:
            self.s_request_id = m.get('sRequestId')

        return self

