# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelFeaturesShrinkRequest(DaraModel):
    def __init__(
        self,
        model_feature_ids_shrink: str = None,
        name: str = None,
        order: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        sort_by: str = None,
    ):
        # The IDs of the model features.
        self.model_feature_ids_shrink = model_feature_ids_shrink
        # The name of the model feature.
        self.name = name
        # The sort order.
        # 
        # - `ASC`: ascending order.
        # 
        # - `DESC`: descending order.
        self.order = order
        # The Alibaba Cloud account ID of the user who creates the model feature.
        self.owner = owner
        # The page number. The value must be a positive integer. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # The project ID. You can call the `ListProjects` API to obtain the project ID.
        self.project_id = project_id
        # The field by which to sort the results.
        # 
        # - `GmtCreateTime`: the creation time.
        # 
        # - `GmtModifiedTime`: the update time.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_feature_ids_shrink is not None:
            result['ModelFeatureIds'] = self.model_feature_ids_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelFeatureIds') is not None:
            self.model_feature_ids_shrink = m.get('ModelFeatureIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

