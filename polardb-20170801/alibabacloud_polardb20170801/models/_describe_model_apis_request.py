# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeModelApisRequest(DaraModel):
    def __init__(
        self,
        gw_cluster_id: str = None,
        model_api_ids: str = None,
        model_category: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        path_prefix: str = None,
        protocol: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        self.model_api_ids = model_api_ids
        self.model_category = model_category
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.path_prefix = path_prefix
        self.protocol = protocol
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.model_api_ids is not None:
            result['ModelApiIds'] = self.model_api_ids

        if self.model_category is not None:
            result['ModelCategory'] = self.model_category

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path_prefix is not None:
            result['PathPrefix'] = self.path_prefix

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('ModelApiIds') is not None:
            self.model_api_ids = m.get('ModelApiIds')

        if m.get('ModelCategory') is not None:
            self.model_category = m.get('ModelCategory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PathPrefix') is not None:
            self.path_prefix = m.get('PathPrefix')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

