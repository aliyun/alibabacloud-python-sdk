# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchHistoricalSnapshotsShrinkRequest(DaraModel):
    def __init__(
        self,
        edition: str = None,
        limit: int = None,
        next_token: str = None,
        order: str = None,
        query_shrink: str = None,
        sort_by: str = None,
        source_type: str = None,
    ):
        self.edition = edition
        # The maximum number of rows that you want the current query to return. To query only the number of matched rows without the need to return specific data, you can set the Limit parameter to `0`. Then, the operation returns only the number of matched rows.
        self.limit = limit
        # The token that is required to obtain the next page of backup snapshots.
        self.next_token = next_token
        # The ordering mode. Valid values:
        # 
        # *   ASC (default): ascending order
        # *   DESC: descending order
        self.order = order
        # The query conditions. Example:
        # 
        #     [
        #       {
        #         "field": "VaultId",
        #         "value": "v-0003rf9m*****qx5",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "InstanceId",
        #         "value": "i-bp1i20zq2*****e9368m",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "PlanId",
        #         "value": "plan-0005vk*****gkd1iu4f",
        #         "operation": "MATCH_TERM"
        #       },
        #       {
        #         "field": "CompleteTime",
        #         "value": "1626769913",
        #         "operation": "GREATER_THAN_OR_EQUAL"
        #       }
        #     ]
        # 
        # *   The following fields are supported:
        # 
        #     *   VaultId: specifies the ID of the backup vault. This field is required.
        #     *   InstanceId: specifies the ID of the Elastic Compute Service (ECS) instance. If the SourceType parameter is set to ECS_FILE, this field is required.
        #     *   Bucket: specifies the name of the Object Storage Service (OSS) bucket. If the SourceType parameter is set to OSS, this field is required.
        #     *   FileSystemId: specifies the ID of the File Storage NAS (NAS) file system. If the SourceType parameter is set to NAS, this field is required.
        #     *   CreateTime: specifies the time when the NAS file system was created. If the SourceType parameter is set to NAS, this field is required.
        #     *   CompleteTime: specifies the time when the backup snapshot was completed.
        #     *   PlanId: the ID of a backup plan.
        # 
        # *   The following operations are supported:
        # 
        #     *   MATCH_TERM: exact match.
        #     *   GREATER_THAN: greater than.
        #     *   GREATER_THAN_OR_EQUAL: greater than or equal to.
        #     *   LESS_THAN: less than.
        #     *   LESS_THAN_OR_EQUAL: less than or equal to.
        #     *   BETWEEN: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,Maximum value]` format.
        #     *   IN: specifies an array as a collection. The results must fall within the collection.
        #     *   NOT_IN: specifies an array as a collection. The results cannot fall within the collection.
        self.query_shrink = query_shrink
        # The field that is used to sort data.
        self.sort_by = sort_by
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: backup snapshots for Elastic Compute Service (ECS) files
        # *   **OSS**: backup snapshots for Object Storage Service (OSS) buckets
        # *   **NAS**: backup snapshots for Apsara File Storage NAS file systems
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.query_shrink is not None:
            result['Query'] = self.query_shrink

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

