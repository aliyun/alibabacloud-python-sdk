# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IgnoreHcCheckWarningsRequest(DaraModel):
    def __init__(
        self,
        check_ids: str = None,
        check_warning_ids: str = None,
        reason: str = None,
        risk_id: str = None,
        source: str = None,
        source_ip: str = None,
        type: int = None,
    ):
        # The ID of the check item.
        # 
        # >  You can call the [DescribeCheckWarnings](https://help.aliyun.com/document_detail/116182.html) operation to query the IDs of check items.
        self.check_ids = check_ids
        # The ID of the alert that is triggered by the check item. Separate multiple IDs with commas (,).
        # 
        # >  You can call the [DescribeCheckWarnings](https://help.aliyun.com/document_detail/116182.html) operation to query the IDs of alerts that are triggered by check items.
        self.check_warning_ids = check_warning_ids
        # The reason for the current operation.
        self.reason = reason
        # The ID of the risk item that you want to ignore or cancel ignoring.
        # 
        # >  You can call the [DescribeCheckWarningSummary](https://help.aliyun.com/document_detail/116179.html) operation to query the IDs of risk items.
        self.risk_id = risk_id
        # The data source. If this parameter is left empty, the server baseline results are queried by default. Valid values:
        # * **default**: server
        # * **agentless**
        self.source = source
        # The source IP address of the request.
        self.source_ip = source_ip
        # The type of the operation that you want to perform. Valid values:
        # 
        # *   **1**: ignores a risk item
        # *   **2**: cancels ignoring a risk item
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
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.check_warning_ids is not None:
            result['CheckWarningIds'] = self.check_warning_ids

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('CheckWarningIds') is not None:
            self.check_warning_ids = m.get('CheckWarningIds')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

