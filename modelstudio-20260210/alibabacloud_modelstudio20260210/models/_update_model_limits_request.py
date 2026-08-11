# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class UpdateModelLimitsRequest(DaraModel):
    def __init__(
        self,
        workspace_id: str = None,
        workspace_limits: List[main_models.UpdateModelLimitsRequestWorkspaceLimits] = None,
    ):
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id
        # The throttling values for the workspace.
        self.workspace_limits = workspace_limits

    def validate(self):
        if self.workspace_limits:
            for v1 in self.workspace_limits:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        result['workspaceLimits'] = []
        if self.workspace_limits is not None:
            for k1 in self.workspace_limits:
                result['workspaceLimits'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        self.workspace_limits = []
        if m.get('workspaceLimits') is not None:
            for k1 in m.get('workspaceLimits'):
                temp_model = main_models.UpdateModelLimitsRequestWorkspaceLimits()
                self.workspace_limits.append(temp_model.from_map(k1))

        return self

class UpdateModelLimitsRequestWorkspaceLimits(DaraModel):
    def __init__(
        self,
        model: str = None,
        operation_type: str = None,
        request_limit: int = None,
        request_limit_period: int = None,
        usage_limit: int = None,
        usage_limit_period: int = None,
    ):
        # The model.
        self.model = model
        # The throttling operation type. Valid values:
        # 
        # - **OVERLAY**: Sets or overwrites the throttling configuration.
        # - **DELETE**: Deletes the throttling configuration (restores to no throttling).
        self.operation_type = operation_type
        # The request throttling value.
        self.request_limit = request_limit
        # The time period for request throttling. Unit: seconds.
        self.request_limit_period = request_limit_period
        # The usage throttling value.
        self.usage_limit = usage_limit
        # The time period for usage throttling. Unit: seconds.
        self.usage_limit_period = usage_limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['model'] = self.model

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.request_limit is not None:
            result['requestLimit'] = self.request_limit

        if self.request_limit_period is not None:
            result['requestLimitPeriod'] = self.request_limit_period

        if self.usage_limit is not None:
            result['usageLimit'] = self.usage_limit

        if self.usage_limit_period is not None:
            result['usageLimitPeriod'] = self.usage_limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('requestLimit') is not None:
            self.request_limit = m.get('requestLimit')

        if m.get('requestLimitPeriod') is not None:
            self.request_limit_period = m.get('requestLimitPeriod')

        if m.get('usageLimit') is not None:
            self.usage_limit = m.get('usageLimit')

        if m.get('usageLimitPeriod') is not None:
            self.usage_limit_period = m.get('usageLimitPeriod')

        return self

