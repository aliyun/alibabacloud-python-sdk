# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListQueryViewsResponseBody(DaraModel):
    def __init__(
        self,
        log_project_name: str = None,
        log_region_id: str = None,
        log_store_name: str = None,
        max_results: int = None,
        next_token: str = None,
        query_views: List[main_models.ListQueryViewsResponseBodyQueryViews] = None,
        request_id: str = None,
    ):
        self.log_project_name = log_project_name
        self.log_region_id = log_region_id
        self.log_store_name = log_store_name
        # The maximum number of results to return when you use the NextToken-based pagination method. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request or if no more results exist. If more results exist, set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The list of query views.
        self.query_views = query_views
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.query_views:
            for v1 in self.query_views:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_project_name is not None:
            result['LogProjectName'] = self.log_project_name

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['QueryViews'] = []
        if self.query_views is not None:
            for k1 in self.query_views:
                result['QueryViews'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogProjectName') is not None:
            self.log_project_name = m.get('LogProjectName')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.query_views = []
        if m.get('QueryViews') is not None:
            for k1 in m.get('QueryViews'):
                temp_model = main_models.ListQueryViewsResponseBodyQueryViews()
                self.query_views.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListQueryViewsResponseBodyQueryViews(DaraModel):
    def __init__(
        self,
        query_view_condition: str = None,
        query_view_criteria: str = None,
        query_view_fields: str = None,
        query_view_id: str = None,
        query_view_name: str = None,
        query_view_order: str = None,
        query_view_scene: str = None,
        query_view_status: str = None,
        query_view_type: str = None,
    ):
        # The custom query condition of the view.
        self.query_view_condition = query_view_condition
        # The alert filter statement of the view.
        self.query_view_criteria = query_view_criteria
        # The list of displayed fields.
        self.query_view_fields = query_view_fields
        # The unique identifier of the query view.
        self.query_view_id = query_view_id
        # The view name.
        self.query_view_name = query_view_name
        # The display order.
        self.query_view_order = query_view_order
        # The scene to which the view belongs.
        self.query_view_scene = query_view_scene
        # The view status.
        self.query_view_status = query_view_status
        # The view type.
        self.query_view_type = query_view_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_view_condition is not None:
            result['QueryViewCondition'] = self.query_view_condition

        if self.query_view_criteria is not None:
            result['QueryViewCriteria'] = self.query_view_criteria

        if self.query_view_fields is not None:
            result['QueryViewFields'] = self.query_view_fields

        if self.query_view_id is not None:
            result['QueryViewId'] = self.query_view_id

        if self.query_view_name is not None:
            result['QueryViewName'] = self.query_view_name

        if self.query_view_order is not None:
            result['QueryViewOrder'] = self.query_view_order

        if self.query_view_scene is not None:
            result['QueryViewScene'] = self.query_view_scene

        if self.query_view_status is not None:
            result['QueryViewStatus'] = self.query_view_status

        if self.query_view_type is not None:
            result['QueryViewType'] = self.query_view_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryViewCondition') is not None:
            self.query_view_condition = m.get('QueryViewCondition')

        if m.get('QueryViewCriteria') is not None:
            self.query_view_criteria = m.get('QueryViewCriteria')

        if m.get('QueryViewFields') is not None:
            self.query_view_fields = m.get('QueryViewFields')

        if m.get('QueryViewId') is not None:
            self.query_view_id = m.get('QueryViewId')

        if m.get('QueryViewName') is not None:
            self.query_view_name = m.get('QueryViewName')

        if m.get('QueryViewOrder') is not None:
            self.query_view_order = m.get('QueryViewOrder')

        if m.get('QueryViewScene') is not None:
            self.query_view_scene = m.get('QueryViewScene')

        if m.get('QueryViewStatus') is not None:
            self.query_view_status = m.get('QueryViewStatus')

        if m.get('QueryViewType') is not None:
            self.query_view_type = m.get('QueryViewType')

        return self

