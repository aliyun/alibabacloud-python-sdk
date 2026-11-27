# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class TokenUsageDetailDTO(DaraModel):
    def __init__(
        self,
        biz_objects: List[main_models.TokenUsageDetailDTOBizObjects] = None,
        namespace: str = None,
        occurred_at: int = None,
        scope_config: main_models.TokenUsageDetailDTOScopeConfig = None,
        scope_type: str = None,
        session_id: str = None,
        status: str = None,
        total_jobs: int = None,
        total_tokens: int = None,
        trigger_source: str = None,
        usage_type: str = None,
        workspace: str = None,
    ):
        # The associated items of the intelligent assistant, such as jobs and deployments.
        self.biz_objects = biz_objects
        # namespace
        self.namespace = namespace
        # The time when the request is initiated, in epoch milliseconds.
        self.occurred_at = occurred_at
        # The inspection configuration.
        self.scope_config = scope_config
        # The inspection type.
        self.scope_type = scope_type
        # The session ID shared across multiple requests in the same session.
        self.session_id = session_id
        # The request status.
        self.status = status
        # The number of jobs covered by the inspection.
        self.total_jobs = total_jobs
        # The number of tokens consumed by this request.
        self.total_tokens = total_tokens
        # The request trigger type, such as cron or manual.
        self.trigger_source = trigger_source
        # The token consumption scenario.
        self.usage_type = usage_type
        # workspace
        self.workspace = workspace

    def validate(self):
        if self.biz_objects:
            for v1 in self.biz_objects:
                 if v1:
                    v1.validate()
        if self.scope_config:
            self.scope_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BizObjects'] = []
        if self.biz_objects is not None:
            for k1 in self.biz_objects:
                result['BizObjects'].append(k1.to_map() if k1 else None)

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.occurred_at is not None:
            result['OccurredAt'] = self.occurred_at

        if self.scope_config is not None:
            result['ScopeConfig'] = self.scope_config.to_map()

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_jobs is not None:
            result['TotalJobs'] = self.total_jobs

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_objects = []
        if m.get('BizObjects') is not None:
            for k1 in m.get('BizObjects'):
                temp_model = main_models.TokenUsageDetailDTOBizObjects()
                self.biz_objects.append(temp_model.from_map(k1))

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('OccurredAt') is not None:
            self.occurred_at = m.get('OccurredAt')

        if m.get('ScopeConfig') is not None:
            temp_model = main_models.TokenUsageDetailDTOScopeConfig()
            self.scope_config = temp_model.from_map(m.get('ScopeConfig'))

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalJobs') is not None:
            self.total_jobs = m.get('TotalJobs')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

class TokenUsageDetailDTOScopeConfig(DaraModel):
    def __init__(
        self,
        deployment_ids: List[str] = None,
        tags: Dict[str, List[str]] = None,
    ):
        # The list of deployments selected for inspection.
        self.deployment_ids = deployment_ids
        # The tag configuration selected for inspection.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_ids is not None:
            result['DeploymentIds'] = self.deployment_ids

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentIds') is not None:
            self.deployment_ids = m.get('DeploymentIds')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self



class TokenUsageDetailDTOBizObjects(DaraModel):
    def __init__(
        self,
        id: str = None,
        kind: str = None,
        name: str = None,
    ):
        # The ID of the associated item.
        self.id = id
        # The type of the associated item.
        self.kind = kind
        # The name of the associated item.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

