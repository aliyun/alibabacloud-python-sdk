# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMonitorGroupRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        group_id: int = None,
        region_id: str = None,
    ):
        # Specifies whether to perform a dry run on the request. A dry run includes checks on permissions and instance status. Valid values:
        # 
        # - **false** (default): Sends a normal request. If the request passes the check, the name and description of the route table are modified.
        # - **true**: Sends a dry run request. Only the check is performed, and the name and description of the route table are not modified. Check items include whether required parameters are specified and the request format. If the check fails, the corresponding error is returned. If the check passes, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        # The ID of the application group.
        # 
        # This parameter is required.
        self.group_id = group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

