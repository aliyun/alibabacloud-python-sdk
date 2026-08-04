# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetApiEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetApiEndpointsResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of parameters.
        self.items = items
        # The maximum number of records to return in this query.
        self.max_results = max_results
        # The token for the next query during paging. Use this token to start the next query.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetApiEndpointsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class GetApiEndpointsResponseBodyItems(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        region_id: str = None,
        service_type: str = None,
    ):
        # The endpoint.
        self.endpoint = endpoint
        # The region ID.
        self.region_id = region_id
        # The service type. Valid values:
        # 
        # - **memory**
        # - **drama**
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self

