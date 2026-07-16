# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListMetaEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListMetaEntitiesResponseBodyPagingInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded.
        self.success = success

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListMetaEntitiesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMetaEntitiesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        meta_entities: List[main_models.MetaEntity] = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # A list of metadata entities.
        self.meta_entities = meta_entities
        # The token used to retrieve the next page of results. If this parameter is empty, no more results are available.
        self.next_token = next_token
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.meta_entities:
            for v1 in self.meta_entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['MetaEntities'] = []
        if self.meta_entities is not None:
            for k1 in self.meta_entities:
                result['MetaEntities'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.meta_entities = []
        if m.get('MetaEntities') is not None:
            for k1 in m.get('MetaEntities'):
                temp_model = main_models.MetaEntity()
                self.meta_entities.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

