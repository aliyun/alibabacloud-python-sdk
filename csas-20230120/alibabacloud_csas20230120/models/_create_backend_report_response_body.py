# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateBackendReportResponseBody(DaraModel):
    def __init__(
        self,
        failed_count: int = None,
        items: List[main_models.CreateBackendReportResponseBodyItems] = None,
        object_count: int = None,
        request_id: str = None,
        success_count: int = None,
        target_count: int = None,
        total_count: int = None,
    ):
        # The number of user-object combinations that failed to be created.
        self.failed_count = failed_count
        # The processing results for each user-object combination. If some combinations fail, the operation still returns results for all combinations.
        self.items = items
        # The number of deduplicated filing objects.
        self.object_count = object_count
        # Id of the request
        self.request_id = request_id
        # The number of user-object combinations that are created.
        self.success_count = success_count
        # The number of deduplicated filing users.
        self.target_count = target_count
        # The total number of expanded user-object combinations.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.object_count is not None:
            result['ObjectCount'] = self.object_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.target_count is not None:
            result['TargetCount'] = self.target_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.CreateBackendReportResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('ObjectCount') is not None:
            self.object_count = m.get('ObjectCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TargetCount') is not None:
            self.target_count = m.get('TargetCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class CreateBackendReportResponseBodyItems(DaraModel):
    def __init__(
        self,
        approval_id: str = None,
        code: str = None,
        effect_status: str = None,
        message: str = None,
        report_object: Any = None,
        report_type: str = None,
        status: str = None,
        success: bool = None,
        target: main_models.CreateBackendReportResponseBodyItemsTarget = None,
    ):
        # The approval instance ID generated after a successful creation. This parameter is not returned if the creation fails.
        self.approval_id = approval_id
        # The error code returned when the current combination fails to be created. This parameter is not returned if the creation succeeds.
        self.code = code
        # The filing effective status. Enabled is returned when the creation succeeds, which indicates that the filing is valid.
        self.effect_status = effect_status
        # The error message returned when the current combination fails to be created. This parameter is not returned if the creation succeeds.
        self.message = message
        # The filing object corresponding to the current combination. The fields vary based on the PolicyType value.
        self.report_object = report_object
        # The filing type. BackendReport is always returned when the creation succeeds, which indicates a backend filing.
        self.report_type = report_type
        # The approval status. Approved is returned when the creation succeeds, which indicates that the filing is approved.
        self.status = status
        # Indicates whether the current combination is created.
        self.success = success
        # The filing user corresponding to the current combination.
        self.target = target

    def validate(self):
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id

        if self.code is not None:
            result['Code'] = self.code

        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status

        if self.message is not None:
            result['Message'] = self.message

        if self.report_object is not None:
            result['ReportObject'] = self.report_object

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.target is not None:
            result['Target'] = self.target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ReportObject') is not None:
            self.report_object = m.get('ReportObject')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Target') is not None:
            temp_model = main_models.CreateBackendReportResponseBodyItemsTarget()
            self.target = temp_model.from_map(m.get('Target'))

        return self

class CreateBackendReportResponseBodyItemsTarget(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The SASE user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

