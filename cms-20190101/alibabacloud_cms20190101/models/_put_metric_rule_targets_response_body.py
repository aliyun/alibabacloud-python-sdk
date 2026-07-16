# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutMetricRuleTargetsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        fail_data: main_models.PutMetricRuleTargetsResponseBodyFailData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # > The value 200 indicates success.
        self.code = code
        # The list of failures.
        self.fail_data = fail_data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values:
        # 
        # - true: successful.
        # 
        # - false: failed.
        self.success = success

    def validate(self):
        if self.fail_data:
            self.fail_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.fail_data is not None:
            result['FailData'] = self.fail_data.to_map()

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

        if m.get('FailData') is not None:
            temp_model = main_models.PutMetricRuleTargetsResponseBodyFailData()
            self.fail_data = temp_model.from_map(m.get('FailData'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PutMetricRuleTargetsResponseBodyFailData(DaraModel):
    def __init__(
        self,
        targets: main_models.PutMetricRuleTargetsResponseBodyFailDataTargets = None,
    ):
        self.targets = targets

    def validate(self):
        if self.targets:
            self.targets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.targets is not None:
            result['Targets'] = self.targets.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Targets') is not None:
            temp_model = main_models.PutMetricRuleTargetsResponseBodyFailDataTargets()
            self.targets = temp_model.from_map(m.get('Targets'))

        return self

class PutMetricRuleTargetsResponseBodyFailDataTargets(DaraModel):
    def __init__(
        self,
        target: List[main_models.PutMetricRuleTargetsResponseBodyFailDataTargetsTarget] = None,
    ):
        self.target = target

    def validate(self):
        if self.target:
            for v1 in self.target:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Target'] = []
        if self.target is not None:
            for k1 in self.target:
                result['Target'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target = []
        if m.get('Target') is not None:
            for k1 in m.get('Target'):
                temp_model = main_models.PutMetricRuleTargetsResponseBodyFailDataTargetsTarget()
                self.target.append(temp_model.from_map(k1))

        return self

class PutMetricRuleTargetsResponseBodyFailDataTargetsTarget(DaraModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        level: str = None,
    ):
        self.arn = arn
        self.id = id
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.id is not None:
            result['Id'] = self.id

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

