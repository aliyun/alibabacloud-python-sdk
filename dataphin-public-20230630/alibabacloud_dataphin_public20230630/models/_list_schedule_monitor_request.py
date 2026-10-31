# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListScheduleMonitorRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListScheduleMonitorRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The query conditions for scheduling monitoring and alerting.
        # 
        # This parameter is required.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The user ID of the operator.
        self.op_user_id = op_user_id

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

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListScheduleMonitorRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListScheduleMonitorRequestListQuery(DaraModel):
    def __init__(
        self,
        alert_reason_list: List[str] = None,
        key_word: str = None,
        logic_field_id_list: List[int] = None,
        logical_table_id_list: List[int] = None,
        on_call_table_list: List[str] = None,
        owner_list: List[str] = None,
        page_no: int = None,
        page_size: int = None,
        project_ids: List[int] = None,
        received_way_type_list: List[str] = None,
        receiver_list: List[str] = None,
        type_list: List[str] = None,
    ):
        # The list of alert cause types. Valid values: FAILED (the task execution failed), TIME_OUT (the task execution timed out), UNFINISHED (the task did not generate output), SUCCESS (the task execution succeeded), and DATA_DELAY (the data is delayed).
        self.alert_reason_list = alert_reason_list
        # The keyword for search. Supports fuzzy matching for monitored task names. If this parameter is empty or not specified, no filtering is applied.
        self.key_word = key_word
        # The list of logical field IDs.
        self.logic_field_id_list = logic_field_id_list
        # The list of logical table IDs.
        self.logical_table_id_list = logical_table_id_list
        # The list of on-call schedule IDs.
        self.on_call_table_list = on_call_table_list
        # The list of user IDs of the creators of monitored objects.
        self.owner_list = owner_list
        # The current page number. Pages start from 1. Default value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Default value: 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The list of project IDs. If this parameter is empty, all projects that the current user has permissions on are automatically queried.
        self.project_ids = project_ids
        # The list of notification method types. Valid values: PHONE (phone call), MESSAGE (text message), EMAIL (email), DING_TALK (DingTalk), FEISHU (Lark), WECHAT (WeChat), and CUSTOM (custom channel).
        self.received_way_type_list = received_way_type_list
        # The list of user IDs of the recipients.
        self.receiver_list = receiver_list
        # The list of monitored object types. Valid values: LOGICAL_FIELD (logical field), OND_ID_NODE (logical table node), SCHEDULE_PHYSICAL_NODE (periodically scheduled physical task), MANUAL_PHYSICAL_NODE (manually scheduled physical task), ODM_NODE (source path task), LOGICAL_TABLE_NODE (logical table task), and PROJECT (project).
        # 
        # This parameter is required.
        self.type_list = type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_reason_list is not None:
            result['AlertReasonList'] = self.alert_reason_list

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.logic_field_id_list is not None:
            result['LogicFieldIdList'] = self.logic_field_id_list

        if self.logical_table_id_list is not None:
            result['LogicalTableIdList'] = self.logical_table_id_list

        if self.on_call_table_list is not None:
            result['OnCallTableList'] = self.on_call_table_list

        if self.owner_list is not None:
            result['OwnerList'] = self.owner_list

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.received_way_type_list is not None:
            result['ReceivedWayTypeList'] = self.received_way_type_list

        if self.receiver_list is not None:
            result['ReceiverList'] = self.receiver_list

        if self.type_list is not None:
            result['TypeList'] = self.type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertReasonList') is not None:
            self.alert_reason_list = m.get('AlertReasonList')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('LogicFieldIdList') is not None:
            self.logic_field_id_list = m.get('LogicFieldIdList')

        if m.get('LogicalTableIdList') is not None:
            self.logical_table_id_list = m.get('LogicalTableIdList')

        if m.get('OnCallTableList') is not None:
            self.on_call_table_list = m.get('OnCallTableList')

        if m.get('OwnerList') is not None:
            self.owner_list = m.get('OwnerList')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('ReceivedWayTypeList') is not None:
            self.received_way_type_list = m.get('ReceivedWayTypeList')

        if m.get('ReceiverList') is not None:
            self.receiver_list = m.get('ReceiverList')

        if m.get('TypeList') is not None:
            self.type_list = m.get('TypeList')

        return self

