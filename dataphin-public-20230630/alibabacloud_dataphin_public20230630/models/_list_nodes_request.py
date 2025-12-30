# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListNodesRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        list_query: main_models.ListNodesRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        self.env = env
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
        if self.env is not None:
            result['Env'] = self.env

        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ListQuery') is not None:
            temp_model = main_models.ListNodesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListNodesRequestListQuery(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        node_biz_type: str = None,
        node_sub_biz_type_list: List[str] = None,
        owner_list: List[str] = None,
        page: int = None,
        page_size: int = None,
        priority_list: List[str] = None,
        project_id: int = None,
        schedule_paused: bool = None,
        schedule_period_list: List[str] = None,
        schedule_type: str = None,
        search_text: str = None,
    ):
        self.dry_run = dry_run
        # This parameter is required.
        self.node_biz_type = node_biz_type
        # This parameter is required.
        self.node_sub_biz_type_list = node_sub_biz_type_list
        self.owner_list = owner_list
        self.page = page
        self.page_size = page_size
        self.priority_list = priority_list
        # This parameter is required.
        self.project_id = project_id
        self.schedule_paused = schedule_paused
        self.schedule_period_list = schedule_period_list
        self.schedule_type = schedule_type
        self.search_text = search_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.node_biz_type is not None:
            result['NodeBizType'] = self.node_biz_type

        if self.node_sub_biz_type_list is not None:
            result['NodeSubBizTypeList'] = self.node_sub_biz_type_list

        if self.owner_list is not None:
            result['OwnerList'] = self.owner_list

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.schedule_paused is not None:
            result['SchedulePaused'] = self.schedule_paused

        if self.schedule_period_list is not None:
            result['SchedulePeriodList'] = self.schedule_period_list

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.search_text is not None:
            result['SearchText'] = self.search_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NodeBizType') is not None:
            self.node_biz_type = m.get('NodeBizType')

        if m.get('NodeSubBizTypeList') is not None:
            self.node_sub_biz_type_list = m.get('NodeSubBizTypeList')

        if m.get('OwnerList') is not None:
            self.owner_list = m.get('OwnerList')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')

        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')

        return self

