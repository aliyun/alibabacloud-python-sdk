# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class PageQueryAgentListNewResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.PageQueryAgentListNewResponseBodyData = None,
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
            temp_model = main_models.PageQueryAgentListNewResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PageQueryAgentListNewResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.PageQueryAgentListNewResponseBodyDataList] = None,
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
                temp_model = main_models.PageQueryAgentListNewResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class PageQueryAgentListNewResponseBodyDataList(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_mode: int = None,
        agent_name: str = None,
        application_code: str = None,
        create_time: str = None,
        deploy_branch_id: int = None,
        deploy_branch_name: str = None,
        description: str = None,
        effective_version_id: int = None,
        effective_version_name: str = None,
        is_available: bool = None,
        latest_publish_time: str = None,
        modify_time: str = None,
        scene: str = None,
    ):
        self.agent_id = agent_id
        self.agent_mode = agent_mode
        self.agent_name = agent_name
        self.application_code = application_code
        self.create_time = create_time
        self.deploy_branch_id = deploy_branch_id
        self.deploy_branch_name = deploy_branch_name
        self.description = description
        self.effective_version_id = effective_version_id
        self.effective_version_name = effective_version_name
        self.is_available = is_available
        self.latest_publish_time = latest_publish_time
        self.modify_time = modify_time
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_mode is not None:
            result['AgentMode'] = self.agent_mode

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deploy_branch_id is not None:
            result['DeployBranchId'] = self.deploy_branch_id

        if self.deploy_branch_name is not None:
            result['DeployBranchName'] = self.deploy_branch_name

        if self.description is not None:
            result['Description'] = self.description

        if self.effective_version_id is not None:
            result['EffectiveVersionId'] = self.effective_version_id

        if self.effective_version_name is not None:
            result['EffectiveVersionName'] = self.effective_version_name

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.latest_publish_time is not None:
            result['LatestPublishTime'] = self.latest_publish_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.scene is not None:
            result['Scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentMode') is not None:
            self.agent_mode = m.get('AgentMode')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeployBranchId') is not None:
            self.deploy_branch_id = m.get('DeployBranchId')

        if m.get('DeployBranchName') is not None:
            self.deploy_branch_name = m.get('DeployBranchName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectiveVersionId') is not None:
            self.effective_version_id = m.get('EffectiveVersionId')

        if m.get('EffectiveVersionName') is not None:
            self.effective_version_name = m.get('EffectiveVersionName')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('LatestPublishTime') is not None:
            self.latest_publish_time = m.get('LatestPublishTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        return self

