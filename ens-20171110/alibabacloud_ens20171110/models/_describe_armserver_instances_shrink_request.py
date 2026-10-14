# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeARMServerInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        aicspecs_shrink: str = None,
        describe_aicinstances: bool = None,
        ens_region_ids_shrink: str = None,
        max_date: str = None,
        min_date: str = None,
        name: str = None,
        namespace: str = None,
        order_by_params: str = None,
        page_number: int = None,
        page_size: int = None,
        server_ids_shrink: str = None,
        server_specs_shrink: str = None,
        states_shrink: str = None,
        tags_shrink: str = None,
    ):
        # The list of container specifications.
        self.aicspecs_shrink = aicspecs_shrink
        # Specifies whether the query results include container information. Valid values:
        # 
        # - **true**: Included.
        # 
        # - **false**: Not included.
        self.describe_aicinstances = describe_aicinstances
        # The list of ENS edge zone IDs.
        self.ens_region_ids_shrink = ens_region_ids_shrink
        # The end time of the query. Format: "2006-01-02". By default, no time limit is applied.
        self.max_date = max_date
        # The start time of the query. Format: "2006-01-02". By default, no time limit is applied.
        self.min_date = min_date
        # The server name.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The sorting method for query results. You can sort results by one or more of the following fields: ServerIdSort (server ID), ServerNameSort (server name), ExpireTimeSort (expiration time), CreationTimeSort (creation time), and EnsRegionIdSort (edge zone ID).
        # 
        # Valid values: asc (ascending order) and desc (descending order).
        self.order_by_params = order_by_params
        # The page number of the query list. Minimum value: **1**.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page for a paged query. Maximum value: **100**.
        # 
        # Default value: **10**.
        self.page_size = page_size
        # The list of server instance IDs.
        self.server_ids_shrink = server_ids_shrink
        # The list of server specifications.
        self.server_specs_shrink = server_specs_shrink
        # The list of operation states.
        self.states_shrink = states_shrink
        # The list of tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aicspecs_shrink is not None:
            result['AICSpecs'] = self.aicspecs_shrink

        if self.describe_aicinstances is not None:
            result['DescribeAICInstances'] = self.describe_aicinstances

        if self.ens_region_ids_shrink is not None:
            result['EnsRegionIds'] = self.ens_region_ids_shrink

        if self.max_date is not None:
            result['MaxDate'] = self.max_date

        if self.min_date is not None:
            result['MinDate'] = self.min_date

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.server_ids_shrink is not None:
            result['ServerIds'] = self.server_ids_shrink

        if self.server_specs_shrink is not None:
            result['ServerSpecs'] = self.server_specs_shrink

        if self.states_shrink is not None:
            result['States'] = self.states_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AICSpecs') is not None:
            self.aicspecs_shrink = m.get('AICSpecs')

        if m.get('DescribeAICInstances') is not None:
            self.describe_aicinstances = m.get('DescribeAICInstances')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids_shrink = m.get('EnsRegionIds')

        if m.get('MaxDate') is not None:
            self.max_date = m.get('MaxDate')

        if m.get('MinDate') is not None:
            self.min_date = m.get('MinDate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServerIds') is not None:
            self.server_ids_shrink = m.get('ServerIds')

        if m.get('ServerSpecs') is not None:
            self.server_specs_shrink = m.get('ServerSpecs')

        if m.get('States') is not None:
            self.states_shrink = m.get('States')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

