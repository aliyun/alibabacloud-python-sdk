# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FixCheckWarningsRequest(DaraModel):
    def __init__(
        self,
        check_params: str = None,
        lang: str = None,
        retention_days: int = None,
        risk_id: int = None,
        snapshot_name: str = None,
        source_ip: str = None,
        uuids: str = None,
    ):
        # The parameters of the baseline check items to be fixed. Parameter description:
        # - **checkId**: The ID of the check item.
        # - **rules**: The fix rules. This parameter is an array.
        #     - **value**: Specifies whether the fix method is selected. Valid values: **0** (not selected) and **1** (selected).
        #     - **ruleId**: The ID of the fix method.
        #     - **paramList**: The list of fix methods. This parameter is an array.  
        #                 • **paramName**: The name of the fix method.  
        #                 • **value**: The specific value of the fix method.
        # 
        # This parameter is required.
        self.check_params = check_params
        # The language of the request and response. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The retention period of the snapshot created when the baseline fix operation is performed. Valid values: 1 to 365. Unit: days.
        self.retention_days = retention_days
        # The ID of the risk item.
        # 
        # > To query the check item information for a specified risk item and server, you must provide the risk item ID. You can call the [DescribeCheckWarningSummary](~~DescribeCheckWarningSummary~~) operation to obtain the ID.
        self.risk_id = risk_id
        # The name of the snapshot created when the baseline fix operation is performed.
        self.snapshot_name = snapshot_name
        # The source IP address.
        self.source_ip = source_ip
        # The UUIDs of the asset instances to be fixed. You can call the [DescribeWarningMachines](~~DescribeWarningMachines~~) operation to obtain the UUIDs.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_params is not None:
            result['CheckParams'] = self.check_params

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckParams') is not None:
            self.check_params = m.get('CheckParams')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

