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
        # The edition type. Valid values: BASIC and STANDARD. Default value: STANDARD.
        self.edition = edition
        # The maximum number of results to return for this query.
        # If you only want to obtain the row count without actual data, set `limit=0` to return no rows.
        self.limit = limit
        # The token required to retrieve the next page of snapshots.
        self.next_token = next_token
        # The sort order. Default value: ASC.
        # - ASC: ascending order.
        # - DESC: descending order.
        self.order = order
        # The query conditions. Example of Query:
        # 
        # ```
        # [
        #   {
        #     "field": "VaultId",
        #     "value": "v-0003rf9m*****qx5",
        #     "operation": "MATCH_TERM"
        #   },
        #   {
        #     "field": "InstanceId",
        #     "value": "i-bp1i20zq2*****e9368m",
        #     "operation": "MATCH_TERM"
        #   },
        #   {
        #     "field": "PlanId",
        #     "value": "plan-0005vk*****gkd1iu4f",
        #     "operation": "MATCH_TERM"
        #   },
        #   {
        #     "field": "CompleteTime",
        #     "value": "1626769913",
        #     "operation": "GREATER_THAN_OR_EQUAL"
        #   }
        # ]
        # ```
        # 
        # - Supported fields:
        # 
        #     - VaultId: required. The vault ID.
        #     - InstanceId: required only when SourceType=ECS_FILE. The ECS instance ID.
        #     - Bucket: required only when SourceType=OSS. The OSS bucket name.
        #     - FileSystemId: required only when SourceType=NAS. The NAS file system ID.
        #     - CreateTime: required only when SourceType=NAS. The creation time of the NAS file system.
        #     - CompleteTime: the time when the snapshot is completed.
        #     - PlanId: the backup plan ID.
        # 
        # - Supported operations:
        # 
        #     - MATCH_TERM: exact match.
        #     - GREATER_THAN: greater than.
        #     - GREATER_THAN_OR_EQUAL: greater than or equal to.
        #     - LESS_THAN: less than.
        #     - LESS_THAN_OR_EQUAL: less than or equal to.
        #     - BETWEEN: range. The value is a JSON array `[lower bound, upper bound]`.
        #     - IN: in the set. The value is an array.
        #     - NOT_IN: not in the set. The value is an array.
        self.query_shrink = query_shrink
        # The field used for sorting.
        self.sort_by = sort_by
        # The type of the data source. Valid values:
        # * **ECS_FILE**: backup snapshots of ECS files.
        # * **OSS**: backup snapshots of Alibaba Cloud OSS.
        # * **NAS**: backup snapshots of Alibaba Cloud NAS.
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

