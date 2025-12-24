# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCdsFileShareLinksRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        creators: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        share_id: str = None,
        share_name: str = None,
        status: str = None,
    ):
        # The ID of the cloud disk.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The users that create the file sharing links.
        self.creators = creators
        # The maximum number of resources to return. Valid values: 1 to 100. Default value: 100. The number of returned resources must be less than or equal to the specified number.
        self.max_results = max_results
        # Specifies the marker after which the returned list begins. If this parameter is not specified, all results are returned. Default value: null.
        self.next_token = next_token
        # The ID of the file sharing link.
        self.share_id = share_id
        # The sharing name for fuzzy search.
        self.share_name = share_name
        # The file sharing status. Valid values: ● disabled: canceled ● enabled: valid
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.creators is not None:
            result['Creators'] = self.creators

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.share_id is not None:
            result['ShareId'] = self.share_id

        if self.share_name is not None:
            result['ShareName'] = self.share_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('Creators') is not None:
            self.creators = m.get('Creators')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ShareId') is not None:
            self.share_id = m.get('ShareId')

        if m.get('ShareName') is not None:
            self.share_name = m.get('ShareName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

