# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetSnapshotRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        desktop_id: str = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
        snapshot_id: str = None,
        stop_desktop: bool = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id
        # The snapshot ID.
        # 
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # Specifies whether to stop the cloud computer.
        self.stop_desktop = stop_desktop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.stop_desktop is not None:
            result['StopDesktop'] = self.stop_desktop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('StopDesktop') is not None:
            self.stop_desktop = m.get('StopDesktop')

        return self

