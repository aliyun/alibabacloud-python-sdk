# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListInstancesRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        list_query: main_models.ListInstancesRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        self.env = env
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
            temp_model = main_models.ListInstancesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListInstancesRequestListQuery(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_unit_id: int = None,
        flow_id: str = None,
        max_biz_date: str = None,
        max_run_date: str = None,
        min_biz_date: str = None,
        min_run_date: str = None,
        node_id: str = None,
        owner_list: List[str] = None,
        page: int = None,
        page_size: int = None,
        priority_list: List[str] = None,
        project_id: int = None,
        run_status_list: List[str] = None,
        schedule_paused: bool = None,
        schedule_period_list: List[str] = None,
        schedule_type: str = None,
        search_text: str = None,
        sub_biz_type_list: List[str] = None,
    ):
        self.biz_type = biz_type
        self.biz_unit_id = biz_unit_id
        self.flow_id = flow_id
        self.max_biz_date = max_biz_date
        self.max_run_date = max_run_date
        self.min_biz_date = min_biz_date
        self.min_run_date = min_run_date
        self.node_id = node_id
        self.owner_list = owner_list
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_size = page_size
        self.priority_list = priority_list
        # This parameter is required.
        self.project_id = project_id
        self.run_status_list = run_status_list
        self.schedule_paused = schedule_paused
        self.schedule_period_list = schedule_period_list
        # This parameter is required.
        self.schedule_type = schedule_type
        self.search_text = search_text
        self.sub_biz_type_list = sub_biz_type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.max_biz_date is not None:
            result['MaxBizDate'] = self.max_biz_date

        if self.max_run_date is not None:
            result['MaxRunDate'] = self.max_run_date

        if self.min_biz_date is not None:
            result['MinBizDate'] = self.min_biz_date

        if self.min_run_date is not None:
            result['MinRunDate'] = self.min_run_date

        if self.node_id is not None:
            result['NodeId'] = self.node_id

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

        if self.run_status_list is not None:
            result['RunStatusList'] = self.run_status_list

        if self.schedule_paused is not None:
            result['SchedulePaused'] = self.schedule_paused

        if self.schedule_period_list is not None:
            result['SchedulePeriodList'] = self.schedule_period_list

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.search_text is not None:
            result['SearchText'] = self.search_text

        if self.sub_biz_type_list is not None:
            result['SubBizTypeList'] = self.sub_biz_type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('MaxBizDate') is not None:
            self.max_biz_date = m.get('MaxBizDate')

        if m.get('MaxRunDate') is not None:
            self.max_run_date = m.get('MaxRunDate')

        if m.get('MinBizDate') is not None:
            self.min_biz_date = m.get('MinBizDate')

        if m.get('MinRunDate') is not None:
            self.min_run_date = m.get('MinRunDate')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

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

        if m.get('RunStatusList') is not None:
            self.run_status_list = m.get('RunStatusList')

        if m.get('SchedulePaused') is not None:
            self.schedule_paused = m.get('SchedulePaused')

        if m.get('SchedulePeriodList') is not None:
            self.schedule_period_list = m.get('SchedulePeriodList')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')

        if m.get('SubBizTypeList') is not None:
            self.sub_biz_type_list = m.get('SubBizTypeList')

        return self

