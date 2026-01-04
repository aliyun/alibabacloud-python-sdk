# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeARMServerInstancesRequest(DaraModel):
    def __init__(
        self,
        aicspecs: List[str] = None,
        describe_aicinstances: bool = None,
        ens_region_ids: List[str] = None,
        max_date: str = None,
        min_date: str = None,
        name: str = None,
        namespace: str = None,
        order_by_params: str = None,
        page_number: int = None,
        page_size: int = None,
        server_ids: List[str] = None,
        server_specs: List[str] = None,
        states: List[str] = None,
        tags: List[main_models.DescribeARMServerInstancesRequestTags] = None,
    ):
        # The container specifications.
        self.aicspecs = aicspecs
        # Spcifies whether the result contains the container information. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.describe_aicinstances = describe_aicinstances
        # The IDs of the Edge Node Service (ENS) nodes.
        self.ens_region_ids = ens_region_ids
        # The end of the time range to query. Specify the time in the 2006-01-02 format. By default, the time range to query is not restricted.
        self.max_date = max_date
        # The beginning of the time range to query. Specify the time in the 2006-01-02 format. By default, the time range to query is not restricted.
        self.min_date = min_date
        # The name of the server.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The sorting order of the results to return. Valid values: ServerIdSort, ServerNameSort, ExpireTimeSort, CreationTimeSort, and EnsRegionIdSort.
        # 
        # asc: ascending order. desc: descending order.
        self.order_by_params = order_by_params
        # The page number. Pages start from page **1**.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **100**.
        # 
        # Default value: **10**.
        self.page_size = page_size
        # The IDs of the ARM servers.
        self.server_ids = server_ids
        # The server specifications.
        self.server_specs = server_specs
        # The operation statuses.
        self.states = states
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aicspecs is not None:
            result['AICSpecs'] = self.aicspecs

        if self.describe_aicinstances is not None:
            result['DescribeAICInstances'] = self.describe_aicinstances

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

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

        if self.server_ids is not None:
            result['ServerIds'] = self.server_ids

        if self.server_specs is not None:
            result['ServerSpecs'] = self.server_specs

        if self.states is not None:
            result['States'] = self.states

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AICSpecs') is not None:
            self.aicspecs = m.get('AICSpecs')

        if m.get('DescribeAICInstances') is not None:
            self.describe_aicinstances = m.get('DescribeAICInstances')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

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
            self.server_ids = m.get('ServerIds')

        if m.get('ServerSpecs') is not None:
            self.server_specs = m.get('ServerSpecs')

        if m.get('States') is not None:
            self.states = m.get('States')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeARMServerInstancesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeARMServerInstancesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

