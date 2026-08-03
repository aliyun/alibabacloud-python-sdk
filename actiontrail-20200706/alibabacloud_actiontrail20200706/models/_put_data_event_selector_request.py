# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutDataEventSelectorRequest(DaraModel):
    def __init__(
        self,
        event_selectors: str = None,
        is_trail_all_region: bool = None,
        trail_name: str = None,
        trail_region_ids: str = None,
    ):
        # The configuration of the data event selector. This parameter is a JSON array that can contain a maximum of 20 elements.
        # 
        # Each element in the JSON array includes the following fields:
        # 
        # - `ServiceName`: The name of the Alibaba Cloud service that supports data events.
        # 
        # - `ReadWriteType`: The type of data event. Valid values: Read, Write, and All.
        # 
        # - `EventName`: This field contains the `Equals` and `NotEquals` subfields.
        # 
        #   For example, the following configuration specifies that only `GetObject`, `CopyObject`, and `AppendObject`events are delivered:
        # 
        #   `{"EventName":{"Equals":["GetObject","CopyObject","AppendObject"]}}`
        # 
        #   If you specify `NotEquals`, events other than `GetObject`, `CopyObject`, and `AppendObject` are delivered.
        # 
        # - `ResourceArn`: This field also contains the `Equals` and `NotEquals` subfields, similar to `EventName`. For example:
        # 
        #   `{"ResourceArn":{"Equals":[arn1,...,arnx]}}`
        # 
        # This parameter is required.
        self.event_selectors = event_selectors
        # Specifies whether the trail tracks data events in all regions.
        # 
        # Default value: `false`.
        self.is_trail_all_region = is_trail_all_region
        # The name of the trail.
        # 
        # This parameter is required.
        self.trail_name = trail_name
        # The regions where the trail tracks data events. Separate multiple region IDs with a comma (`,`).
        self.trail_region_ids = trail_region_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_selectors is not None:
            result['EventSelectors'] = self.event_selectors

        if self.is_trail_all_region is not None:
            result['IsTrailAllRegion'] = self.is_trail_all_region

        if self.trail_name is not None:
            result['TrailName'] = self.trail_name

        if self.trail_region_ids is not None:
            result['TrailRegionIds'] = self.trail_region_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSelectors') is not None:
            self.event_selectors = m.get('EventSelectors')

        if m.get('IsTrailAllRegion') is not None:
            self.is_trail_all_region = m.get('IsTrailAllRegion')

        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')

        if m.get('TrailRegionIds') is not None:
            self.trail_region_ids = m.get('TrailRegionIds')

        return self

