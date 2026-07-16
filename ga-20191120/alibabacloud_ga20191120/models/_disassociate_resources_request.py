# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisassociateResourcesRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        associated_resource_id: str = None,
        associated_resource_region_id: str = None,
        associated_resource_type: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        # Alibaba Cloud Global Accelerator (GA) instance ID.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # Linked instance ID.
        # 
        # This parameter is required.
        self.associated_resource_id = associated_resource_id
        # Region ID of the linked instance.
        self.associated_resource_region_id = associated_resource_region_id
        # Resource type of the linked peripheral resource.
        # 
        # This parameter is required.
        self.associated_resource_type = associated_resource_type
        # Specifies whether to perform a dry run of the request. Valid values:  
        # - **true**: Sends a dry run request without detaching the resource. The system checks whether required parameters are specified, whether the request format is valid, and whether business limits are met. If the check fails, an error is returned. If the check passes, an HTTP 2xx status code is returned.  
        # - **false** (default): Sends a normal request. If the check passes, an HTTP 2xx status code is returned and the endpoint group is created immediately.
        self.dry_run = dry_run
        # Region ID of the Alibaba Cloud Global Accelerator (GA) instance. Valid value: **cn-hangzhou** only.
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

