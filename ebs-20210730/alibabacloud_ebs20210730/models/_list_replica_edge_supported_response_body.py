# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class ListReplicaEdgeSupportedResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        supported_regions: List[main_models.ListReplicaEdgeSupportedResponseBodySupportedRegions] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.supported_regions = supported_regions

    def validate(self):
        if self.supported_regions:
            for v1 in self.supported_regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SupportedRegions'] = []
        if self.supported_regions is not None:
            for k1 in self.supported_regions:
                result['SupportedRegions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.supported_regions = []
        if m.get('SupportedRegions') is not None:
            for k1 in m.get('SupportedRegions'):
                temp_model = main_models.ListReplicaEdgeSupportedResponseBodySupportedRegions()
                self.supported_regions.append(temp_model.from_map(k1))

        return self

class ListReplicaEdgeSupportedResponseBodySupportedRegions(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        zones: List[main_models.ListReplicaEdgeSupportedResponseBodySupportedRegionsZones] = None,
    ):
        self.region_id = region_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.ListReplicaEdgeSupportedResponseBodySupportedRegionsZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class ListReplicaEdgeSupportedResponseBodySupportedRegionsZones(DaraModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

