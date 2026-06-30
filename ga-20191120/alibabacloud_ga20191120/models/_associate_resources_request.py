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
        # Alibaba Cloud Global Accelerator (GA) instance ID.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # Association pattern:  
        # - **Managed**: Managed mode. GA restricts user operations based on management policies. Currently, no resources use this type.  
        # - **Associated** (default): Loose coupling association. GA does not restrict user operations. WAF uses loose coupling.
        self.associated_mode = associated_mode
        # Resource ID of the linked instance.
        self.associated_resource_id = associated_resource_id
        # Region of the linked instance.
        # 
        # This parameter is required.
        self.associated_resource_region_id = associated_resource_region_id
        # Resource type of the linked instance.
        # 
        # This parameter is required.
        self.associated_resource_type = associated_resource_type
        # Indicates whether to perform a dry run of the request. Valid values:  
        # - **true**: Sends a dry run request without associating resources. Checks include required parameters, request format, and business restrictions. If the check fails, an error is returned. If the check passes, an HTTP 2xx status code is returned.  
        # - **false** (Default Value): Sends a normal request. If the check passes, an HTTP 2xx status code is returned and the endpoint group is created immediately.
        self.dry_run = dry_run
        # Region ID of the basic Alibaba Cloud Global Accelerator (GA) instance. Valid value: **cn-hangzhou** only.
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

