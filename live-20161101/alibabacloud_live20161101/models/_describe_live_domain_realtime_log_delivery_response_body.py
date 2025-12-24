# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainRealtimeLogDeliveryResponseBody(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The name of the Logstore to which log entries are delivered.
        self.logstore = logstore
        # The name of the Log Service project that is used for real-time log delivery.
        self.project = project
        # The ID of the region where the Log Service project is deployed.
        self.region = region
        # The request ID.
        self.request_id = request_id
        # The status of real-time log delivery. Valid values:
        # 
        # *   online: Real-time log delivery is enabled.
        # *   offline: Real-time log delivery is disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project is not None:
            result['Project'] = self.project

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

