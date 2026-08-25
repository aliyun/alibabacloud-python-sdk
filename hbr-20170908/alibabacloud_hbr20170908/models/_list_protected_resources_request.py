# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProtectedResourcesRequest(DaraModel):
    def __init__(
        self,
        created_by_product: str = None,
        has_snapshot: bool = None,
        max_results: int = None,
        next_token: str = None,
        resource_id: str = None,
        skip: int = None,
        source_type: str = None,
    ):
        # The product capability to which the resource belongs. Valid values:
        # - **HBR**: Cloud Backup standard capability.
        # - **BASIC**: ECS File Backup Essential Edition.
        self.created_by_product = created_by_product
        # Specifies whether the resource has backup points.
        self.has_snapshot = has_snapshot
        # The number of results per query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token for the next page. If this parameter is empty, no more pages are available.
        self.next_token = next_token
        # The resource ID.
        # - **SourceType=ECS_FILE**: the ECS instance ID.
        # - **SourceType=COMMON_FILE_SYSTEM**: the CPFS data source ID.
        # - **SourceType=COMMON_NAS**: the on-premises NAS data source ID.
        # - **SourceType=File**: the local service client ID.
        # - **SourceType=NAS**: the Alibaba Cloud NAS file system ID.
        # - **SourceType=OSS**: the OSS bucket.
        self.resource_id = resource_id
        # The number of entries to skip for paging.
        # If the number of skipped entries exceeds the total number of conditional entries, an empty list is returned. The number of skipped entries must be a multiple of MaxResults.
        self.skip = skip
        # The backup feature type. Valid values:
        # - **ECS_FILE**: ECS file backup.
        # - **COMMON_FILE_SYSTEM**: Cloud Parallel File Storage (CPFS) backup.
        # - **COMMON_NAS**: on-premises NAS backup.
        # - **File**: on-premises file backup.
        # - **NAS**: Alibaba Cloud NAS backup.
        # - **OSS**: OSS backup.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_by_product is not None:
            result['CreatedByProduct'] = self.created_by_product

        if self.has_snapshot is not None:
            result['HasSnapshot'] = self.has_snapshot

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedByProduct') is not None:
            self.created_by_product = m.get('CreatedByProduct')

        if m.get('HasSnapshot') is not None:
            self.has_snapshot = m.get('HasSnapshot')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

