# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListAlertEventsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListAlertEventsRequestListQuery = None,
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
            temp_model = main_models.ListAlertEventsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListAlertEventsRequestListQuery(DaraModel):
    def __init__(
        self,
        alert_end_time: str = None,
        alert_object_type_list: List[str] = None,
        alert_reason_list: List[str] = None,
        alert_start_time: str = None,
        biz_name_list: List[str] = None,
        keyword: str = None,
        monitored_item_id_list: List[str] = None,
        page: int = None,
        page_size: int = None,
        project_name_list: List[str] = None,
        source_system: str = None,
        status_list: List[str] = None,
        user_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.alert_end_time = alert_end_time
        self.alert_object_type_list = alert_object_type_list
        self.alert_reason_list = alert_reason_list
        # This parameter is required.
        self.alert_start_time = alert_start_time
        self.biz_name_list = biz_name_list
        self.keyword = keyword
        self.monitored_item_id_list = monitored_item_id_list
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_size = page_size
        self.project_name_list = project_name_list
        # This parameter is required.
        self.source_system = source_system
        self.status_list = status_list
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_end_time is not None:
            result['AlertEndTime'] = self.alert_end_time

        if self.alert_object_type_list is not None:
            result['AlertObjectTypeList'] = self.alert_object_type_list

        if self.alert_reason_list is not None:
            result['AlertReasonList'] = self.alert_reason_list

        if self.alert_start_time is not None:
            result['AlertStartTime'] = self.alert_start_time

        if self.biz_name_list is not None:
            result['BizNameList'] = self.biz_name_list

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.monitored_item_id_list is not None:
            result['MonitoredItemIdList'] = self.monitored_item_id_list

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_name_list is not None:
            result['ProjectNameList'] = self.project_name_list

        if self.source_system is not None:
            result['SourceSystem'] = self.source_system

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertEndTime') is not None:
            self.alert_end_time = m.get('AlertEndTime')

        if m.get('AlertObjectTypeList') is not None:
            self.alert_object_type_list = m.get('AlertObjectTypeList')

        if m.get('AlertReasonList') is not None:
            self.alert_reason_list = m.get('AlertReasonList')

        if m.get('AlertStartTime') is not None:
            self.alert_start_time = m.get('AlertStartTime')

        if m.get('BizNameList') is not None:
            self.biz_name_list = m.get('BizNameList')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MonitoredItemIdList') is not None:
            self.monitored_item_id_list = m.get('MonitoredItemIdList')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectNameList') is not None:
            self.project_name_list = m.get('ProjectNameList')

        if m.get('SourceSystem') is not None:
            self.source_system = m.get('SourceSystem')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')

        return self

