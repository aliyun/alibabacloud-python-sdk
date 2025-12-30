# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListPublishRecordsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListPublishRecordsRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListPublishRecordsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListPublishRecordsRequestListQuery(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        search_filter: main_models.ListPublishRecordsRequestListQuerySearchFilter = None,
    ):
        self.keyword = keyword
        # This parameter is required.
        self.search_filter = search_filter

    def validate(self):
        if self.search_filter:
            self.search_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.search_filter is not None:
            result['SearchFilter'] = self.search_filter.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('SearchFilter') is not None:
            temp_model = main_models.ListPublishRecordsRequestListQuerySearchFilter()
            self.search_filter = temp_model.from_map(m.get('SearchFilter'))

        return self

class ListPublishRecordsRequestListQuerySearchFilter(DaraModel):
    def __init__(
        self,
        change_type_list: List[int] = None,
        page: int = None,
        page_size: int = None,
        project_id_list: List[int] = None,
        publish_end_time: str = None,
        publish_start_time: str = None,
        publish_status_list: List[int] = None,
        submitter_list: List[str] = None,
    ):
        self.change_type_list = change_type_list
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.project_id_list = project_id_list
        self.publish_end_time = publish_end_time
        self.publish_start_time = publish_start_time
        self.publish_status_list = publish_status_list
        self.submitter_list = submitter_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type_list is not None:
            result['ChangeTypeList'] = self.change_type_list

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id_list is not None:
            result['ProjectIdList'] = self.project_id_list

        if self.publish_end_time is not None:
            result['PublishEndTime'] = self.publish_end_time

        if self.publish_start_time is not None:
            result['PublishStartTime'] = self.publish_start_time

        if self.publish_status_list is not None:
            result['PublishStatusList'] = self.publish_status_list

        if self.submitter_list is not None:
            result['SubmitterList'] = self.submitter_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeTypeList') is not None:
            self.change_type_list = m.get('ChangeTypeList')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectIdList') is not None:
            self.project_id_list = m.get('ProjectIdList')

        if m.get('PublishEndTime') is not None:
            self.publish_end_time = m.get('PublishEndTime')

        if m.get('PublishStartTime') is not None:
            self.publish_start_time = m.get('PublishStartTime')

        if m.get('PublishStatusList') is not None:
            self.publish_status_list = m.get('PublishStatusList')

        if m.get('SubmitterList') is not None:
            self.submitter_list = m.get('SubmitterList')

        return self

