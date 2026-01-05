# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSpecRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        matrix_spec: str = None,
        max_results: int = None,
        next_token: str = None,
        sale_mode: str = None,
        spec_ids: List[str] = None,
        spec_status: str = None,
        spec_type: str = None,
    ):
        self.biz_region_id = biz_region_id
        # The matrix specification.
        # 
        # Valid values:
        # 
        # *   cpm.gn6.gx1
        self.matrix_spec = matrix_spec
        # The maximum number of items to return per page in a paginated query. The value range is 1 to 100, with a default value of 100.
        self.max_results = max_results
        # Indicates the starting position for reading. If left empty, it starts from the beginning.
        self.next_token = next_token
        # The purchase mode of cloud mobile phones.
        # 
        # Valid values:
        # 
        # *   Instance (default): the instance group mode.
        # *   Node: the matrix mode [whitelisted].
        self.sale_mode = sale_mode
        # List of specification IDs.
        self.spec_ids = spec_ids
        # Specification status.
        self.spec_status = spec_status
        # Specification type.
        self.spec_type = spec_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.matrix_spec is not None:
            result['MatrixSpec'] = self.matrix_spec

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        if self.spec_ids is not None:
            result['SpecIds'] = self.spec_ids

        if self.spec_status is not None:
            result['SpecStatus'] = self.spec_status

        if self.spec_type is not None:
            result['SpecType'] = self.spec_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('MatrixSpec') is not None:
            self.matrix_spec = m.get('MatrixSpec')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        if m.get('SpecIds') is not None:
            self.spec_ids = m.get('SpecIds')

        if m.get('SpecStatus') is not None:
            self.spec_status = m.get('SpecStatus')

        if m.get('SpecType') is not None:
            self.spec_type = m.get('SpecType')

        return self

