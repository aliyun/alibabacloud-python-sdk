# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAclEntriesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        region_id: str = None,
        source_id: str = None,
        source_type: str = None,
    ):
        # The number of entries per page.
        # 
        # *   Maximum value: 1600.
        # *   Default value: 1600.
        self.max_results = max_results
        # The token that is used for the next query. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The office network ID.
        self.office_site_id = office_site_id
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the instance to which the ACL applies. You can specify an office network ID or a cloud computer ID.
        self.source_id = source_id
        # The granularity of the ACL.
        # 
        # Valid values:
        # 
        # *   desktop: cloud computer
        # *   vpc: office network
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

