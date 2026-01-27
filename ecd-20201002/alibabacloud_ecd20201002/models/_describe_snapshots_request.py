# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSnapshotsRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        desktop_id: str = None,
        login_token: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        session_id: str = None,
        snapshot_id: str = None,
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
        # The number of entries per page. Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

