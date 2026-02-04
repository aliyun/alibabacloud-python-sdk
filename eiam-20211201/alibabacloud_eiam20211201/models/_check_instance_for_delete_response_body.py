# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CheckInstanceForDeleteResponseBody(DaraModel):
    def __init__(
        self,
        check_instance_result: main_models.CheckInstanceForDeleteResponseBodyCheckInstanceResult = None,
        request_id: str = None,
    ):
        self.check_instance_result = check_instance_result
        self.request_id = request_id

    def validate(self):
        if self.check_instance_result:
            self.check_instance_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_instance_result is not None:
            result['CheckInstanceResult'] = self.check_instance_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckInstanceResult') is not None:
            temp_model = main_models.CheckInstanceForDeleteResponseBodyCheckInstanceResult()
            self.check_instance_result = temp_model.from_map(m.get('CheckInstanceResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckInstanceForDeleteResponseBodyCheckInstanceResult(DaraModel):
    def __init__(
        self,
        deletable: bool = None,
        restrict_scenarios: List[main_models.CheckInstanceForDeleteResponseBodyCheckInstanceResultRestrictScenarios] = None,
    ):
        # true表示实例可以被删除；false表示实例不可被删除，具体查看RestrictScenarios属性。
        self.deletable = deletable
        # true表示实例可以被删除；false表示实例不可被删除，具体查看RestrictScenarios属性。
        self.restrict_scenarios = restrict_scenarios

    def validate(self):
        if self.restrict_scenarios:
            for v1 in self.restrict_scenarios:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletable is not None:
            result['Deletable'] = self.deletable

        result['RestrictScenarios'] = []
        if self.restrict_scenarios is not None:
            for k1 in self.restrict_scenarios:
                result['RestrictScenarios'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')

        self.restrict_scenarios = []
        if m.get('RestrictScenarios') is not None:
            for k1 in m.get('RestrictScenarios'):
                temp_model = main_models.CheckInstanceForDeleteResponseBodyCheckInstanceResultRestrictScenarios()
                self.restrict_scenarios.append(temp_model.from_map(k1))

        return self

class CheckInstanceForDeleteResponseBodyCheckInstanceResultRestrictScenarios(DaraModel):
    def __init__(
        self,
        helpful_console_url: str = None,
        resource_id: str = None,
        restrict_reason: str = None,
    ):
        # 有帮助的控制台地址，可以管理对应的资源，从而解除实例删除限制。可能返回为空，不一定所有的资源ID都有管理地址返回。
        self.helpful_console_url = helpful_console_url
        # 导致实例删除受限的资源ID。
        self.resource_id = resource_id
        # 针对实例删除受限的原因文字描述。
        self.restrict_reason = restrict_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.helpful_console_url is not None:
            result['HelpfulConsoleUrl'] = self.helpful_console_url

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.restrict_reason is not None:
            result['RestrictReason'] = self.restrict_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HelpfulConsoleUrl') is not None:
            self.helpful_console_url = m.get('HelpfulConsoleUrl')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('RestrictReason') is not None:
            self.restrict_reason = m.get('RestrictReason')

        return self

