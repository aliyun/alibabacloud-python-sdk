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
        # The parameters for the baseline risk item that you want to fix.
        # 
        # *   **checkId**: the ID of the check item that corresponds to the baseline risk item.
        # 
        # *   **rules**: an array that consists of the rules applied to fixes.
        # 
        #     *   **value**: specifies whether a fix method is selected. Valid values: **0** and **1**. The value 0 indicates that no fix method is selected and the value 1 indicates that a fix method is selected.
        #     *   **ruleId**: the ID of the fix method.
        #     *   **paramList**: an array that consists of the details about the fix method.\\
        #         • **paramName**: the name of the fix method.\\
        #         • **value**: the value of the fix method.
        # 
        # This parameter is required.
        self.check_params = check_params
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The retention period of the snapshot that is created when you fix the baseline risk. Valid values: 1 to 365. Unit: days.
        self.retention_days = retention_days
        # The ID of the risk item.
        # 
        # >  To query the information about the risk items and check items of a server, you must specify the IDs of the risk items. You can call the [DescribeCheckWarningSummary](~~DescribeCheckWarningSummary~~) operation to query the IDs of risk items.
        self.risk_id = risk_id
        # The name of the snapshot that is created when you fix the baseline risk.
        self.snapshot_name = snapshot_name
        # The source IP address of the request.
        self.source_ip = source_ip
        # The UUID of the asset for which you want to fix the baseline risk item. You can call the [DescribeWarningMachines](~~DescribeWarningMachines~~) operation to query the UUIDs of assets.
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

