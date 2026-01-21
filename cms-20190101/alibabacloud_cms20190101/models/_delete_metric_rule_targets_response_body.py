# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DeleteMetricRuleTargetsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        fail_ids: main_models.DeleteMetricRuleTargetsResponseBodyFailIds = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # **
        # 
        # **Description** The status code 200 indicates that the request was successful.
        self.code = code
        # The IDs of the resources that failed to be deleted.
        self.fail_ids = fail_ids
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.fail_ids:
            self.fail_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.fail_ids is not None:
            result['FailIds'] = self.fail_ids.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('FailIds') is not None:
            temp_model = main_models.DeleteMetricRuleTargetsResponseBodyFailIds()
            self.fail_ids = temp_model.from_map(m.get('FailIds'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DeleteMetricRuleTargetsResponseBodyFailIds(DaraModel):
    def __init__(
        self,
        target_ids: main_models.DeleteMetricRuleTargetsResponseBodyFailIdsTargetIds = None,
    ):
        # The IDs of the resources that failed to be deleted.
        self.target_ids = target_ids

    def validate(self):
        if self.target_ids:
            self.target_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetIds') is not None:
            temp_model = main_models.DeleteMetricRuleTargetsResponseBodyFailIdsTargetIds()
            self.target_ids = temp_model.from_map(m.get('TargetIds'))

        return self

class DeleteMetricRuleTargetsResponseBodyFailIdsTargetIds(DaraModel):
    def __init__(
        self,
        target_id: List[str] = None,
    ):
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_id is not None:
            result['TargetId'] = self.target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        return self

