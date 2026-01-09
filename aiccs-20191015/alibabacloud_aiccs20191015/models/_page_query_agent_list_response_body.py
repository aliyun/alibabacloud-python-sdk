# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class PageQueryAgentListResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.PageQueryAgentListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.PageQueryAgentListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PageQueryAgentListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.PageQueryAgentListResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.PageQueryAgentListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class PageQueryAgentListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        application_code: str = None,
        audit_reason: str = None,
        build_fail_reason: str = None,
        business_type_name: str = None,
        create_time: str = None,
        description: str = None,
        last_online_time: str = None,
        modify_time: str = None,
        status: int = None,
        with_active_prompt: bool = None,
        with_config: bool = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.application_code = application_code
        self.audit_reason = audit_reason
        self.build_fail_reason = build_fail_reason
        self.business_type_name = business_type_name
        self.create_time = create_time
        self.description = description
        self.last_online_time = last_online_time
        self.modify_time = modify_time
        self.status = status
        self.with_active_prompt = with_active_prompt
        self.with_config = with_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason

        if self.build_fail_reason is not None:
            result['BuildFailReason'] = self.build_fail_reason

        if self.business_type_name is not None:
            result['BusinessTypeName'] = self.business_type_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.last_online_time is not None:
            result['LastOnlineTime'] = self.last_online_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.status is not None:
            result['Status'] = self.status

        if self.with_active_prompt is not None:
            result['WithActivePrompt'] = self.with_active_prompt

        if self.with_config is not None:
            result['WithConfig'] = self.with_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')

        if m.get('BuildFailReason') is not None:
            self.build_fail_reason = m.get('BuildFailReason')

        if m.get('BusinessTypeName') is not None:
            self.business_type_name = m.get('BusinessTypeName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LastOnlineTime') is not None:
            self.last_online_time = m.get('LastOnlineTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WithActivePrompt') is not None:
            self.with_active_prompt = m.get('WithActivePrompt')

        if m.get('WithConfig') is not None:
            self.with_config = m.get('WithConfig')

        return self

