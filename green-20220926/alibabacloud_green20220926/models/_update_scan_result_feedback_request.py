# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateScanResultFeedbackRequest(DaraModel):
    def __init__(
        self,
        feedback: str = None,
        labels: str = None,
        query_request_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        risk_level: str = None,
    ):
        # Feedback
        self.feedback = feedback
        # Labels.
        self.labels = labels
        # Request ID
        self.query_request_id = query_request_id
        # Region ID.
        self.region_id = region_id
        # Resource Type
        self.resource_type = resource_type
        # Risk Level
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.query_request_id is not None:
            result['QueryRequestId'] = self.query_request_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('QueryRequestId') is not None:
            self.query_request_id = m.get('QueryRequestId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

