# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateResourcesRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        associated_mode: str = None,
        associated_resource_id: str = None,
        associated_resource_region_id: str = None,
        associated_resource_type: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.accelerator_id = accelerator_id
        self.associated_mode = associated_mode
        self.associated_resource_id = associated_resource_id
        # This parameter is required.
        self.associated_resource_region_id = associated_resource_region_id
        # This parameter is required.
        self.associated_resource_type = associated_resource_type
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.associated_mode is not None:
            result['AssociatedMode'] = self.associated_mode

        if self.associated_resource_id is not None:
            result['AssociatedResourceId'] = self.associated_resource_id

        if self.associated_resource_region_id is not None:
            result['AssociatedResourceRegionId'] = self.associated_resource_region_id

        if self.associated_resource_type is not None:
            result['AssociatedResourceType'] = self.associated_resource_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AssociatedMode') is not None:
            self.associated_mode = m.get('AssociatedMode')

        if m.get('AssociatedResourceId') is not None:
            self.associated_resource_id = m.get('AssociatedResourceId')

        if m.get('AssociatedResourceRegionId') is not None:
            self.associated_resource_region_id = m.get('AssociatedResourceRegionId')

        if m.get('AssociatedResourceType') is not None:
            self.associated_resource_type = m.get('AssociatedResourceType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

