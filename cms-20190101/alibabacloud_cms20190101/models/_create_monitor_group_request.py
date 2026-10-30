# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMonitorGroupRequest(DaraModel):
    def __init__(
        self,
        contact_groups: str = None,
        dry_run: bool = None,
        group_name: str = None,
        region_id: str = None,
    ):
        # The alert contact group. Alert notifications for the application group are sent to the alert contacts in this alert contact group.
        # 
        # > An alert contact group contains one or more alert contacts. For more information about how to create alert contacts and alert contact groups, see [PutContact](~~PutContact~~) and [PutContactGroup](~~PutContactGroup~~).
        self.contact_groups = contact_groups
        # Specifies whether to perform a dry run on the request. A dry run checks items such as permissions and instance status. Valid values:
        # 
        # - **false** (default): Sends a normal request. If the request passes the check, the name and description of the route table are modified.
        # - **true**: Sends a dry run request. Only the check is performed, and the name and description of the route table are not modified. The check items include whether required parameters are specified and whether the request format is valid. If the request fails the check, an error is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        # The name of the application group.
        # 
        # This parameter is required.
        self.group_name = group_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

