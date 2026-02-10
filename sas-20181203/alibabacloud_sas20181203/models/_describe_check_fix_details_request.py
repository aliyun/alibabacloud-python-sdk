# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCheckFixDetailsRequest(DaraModel):
    def __init__(
        self,
        check_ids: str = None,
        lang: str = None,
        risk_id: int = None,
    ):
        # The ID of the risk item.
        # 
        # >  You can call the [DescribeRiskType](~~DescribeRiskType~~) operation to query the IDs of risk items.
        self.check_ids = check_ids
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the baseline.
        # 
        # >  You can call the [DescribeCheckWarningSummary](https://help.aliyun.com/document_detail/116179.html) operation to query the IDs of baselines.
        self.risk_id = risk_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        return self

