# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListScenarioResponseBody(DaraModel):
    def __init__(
        self,
        arms_scenarios: List[main_models.ListScenarioResponseBodyArmsScenarios] = None,
        request_id: str = None,
    ):
        # The detailed information of the business monitoring job.
        self.arms_scenarios = arms_scenarios
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.arms_scenarios:
            for v1 in self.arms_scenarios:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ArmsScenarios'] = []
        if self.arms_scenarios is not None:
            for k1 in self.arms_scenarios:
                result['ArmsScenarios'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.arms_scenarios = []
        if m.get('ArmsScenarios') is not None:
            for k1 in m.get('ArmsScenarios'):
                temp_model = main_models.ListScenarioResponseBodyArmsScenarios()
                self.arms_scenarios.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListScenarioResponseBodyArmsScenarios(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: str = None,
        extensions: str = None,
        id: int = None,
        name: str = None,
        region_id: str = None,
        sign: str = None,
        update_time: str = None,
        user_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The time when the business monitoring job was created.
        self.create_time = create_time
        # The extended information. The value is a JSON string.
        self.extensions = extensions
        # The ID of the business monitoring job.
        self.id = id
        # The name of the business monitoring job.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The code of the business monitoring job.
        self.sign = sign
        # The time when the business monitoring job was updated.
        self.update_time = update_time
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.extensions is not None:
            result['Extensions'] = self.extensions

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sign is not None:
            result['Sign'] = self.sign

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sign') is not None:
            self.sign = m.get('Sign')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

