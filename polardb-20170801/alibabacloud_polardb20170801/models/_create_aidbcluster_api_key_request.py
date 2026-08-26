# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAIDBClusterApiKeyRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        model_space_name: str = None,
        region_id: str = None,
    ):
        # The description.
        self.description = description
        # The model space ID.
        self.model_space_name = model_space_name
        # The region ID.
        # > * You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the region information of all clusters under the specified account.
        # > * If this parameter is left empty, scheduled tasks in all regions under the current account are queried by default.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.model_space_name is not None:
            result['ModelSpaceName'] = self.model_space_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModelSpaceName') is not None:
            self.model_space_name = m.get('ModelSpaceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

