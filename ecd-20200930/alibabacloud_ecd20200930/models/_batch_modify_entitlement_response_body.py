# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class BatchModifyEntitlementResponseBody(DaraModel):
    def __init__(
        self,
        entitlements: main_models.BatchModifyEntitlementResponseBodyEntitlements = None,
        request_id: str = None,
    ):
        self.entitlements = entitlements
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entitlements:
            self.entitlements.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entitlements is not None:
            result['Entitlements'] = self.entitlements.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entitlements') is not None:
            temp_model = main_models.BatchModifyEntitlementResponseBodyEntitlements()
            self.entitlements = temp_model.from_map(m.get('Entitlements'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchModifyEntitlementResponseBodyEntitlements(DaraModel):
    def __init__(
        self,
        assign_models: List[main_models.BatchModifyEntitlementResponseBodyEntitlementsAssignModels] = None,
        status: str = None,
        task_id: str = None,
    ):
        self.assign_models = assign_models
        # The result.
        # 
        # Valid values:
        # 
        # *   FAILED
        # *   NOT_STARTED
        # *   STARTED
        # *   PROCESSING
        # *   FINISHED
        self.status = status
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.assign_models:
            for v1 in self.assign_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssignModels'] = []
        if self.assign_models is not None:
            for k1 in self.assign_models:
                result['AssignModels'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assign_models = []
        if m.get('AssignModels') is not None:
            for k1 in m.get('AssignModels'):
                temp_model = main_models.BatchModifyEntitlementResponseBodyEntitlementsAssignModels()
                self.assign_models.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class BatchModifyEntitlementResponseBodyEntitlementsAssignModels(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        end_user_ids: List[str] = None,
        inner_status: str = None,
    ):
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The authorized user IDs for the cloud computer.
        self.end_user_ids = end_user_ids
        # The assign result for each cloud computer.
        # 
        # Valid values:
        # 
        # *   FAILED
        # *   NOT_STARTED
        # *   STARTED
        # *   PROCESSING
        # *   FINISHED
        self.inner_status = inner_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.inner_status is not None:
            result['InnerStatus'] = self.inner_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('InnerStatus') is not None:
            self.inner_status = m.get('InnerStatus')

        return self

