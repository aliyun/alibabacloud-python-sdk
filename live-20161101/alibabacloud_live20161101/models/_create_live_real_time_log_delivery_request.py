# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveRealTimeLogDeliveryRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        logstore: str = None,
        owner_id: int = None,
        project: str = None,
        region: str = None,
        region_id: str = None,
    ):
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The name of the Logstore to which log entries are delivered.
        # 
        # This parameter is required.
        self.logstore = logstore
        self.owner_id = owner_id
        # The name of the Log Service project that is used for real-time log delivery.
        # 
        # This parameter is required.
        self.project = project
        # The ID of the region where the Log Service project is deployed.
        # 
        # This parameter is required.
        self.region = region
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.project is not None:
            result['Project'] = self.project

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

