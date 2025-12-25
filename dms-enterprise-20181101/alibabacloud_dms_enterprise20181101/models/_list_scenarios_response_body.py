# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListScenariosResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        scenario_list: List[main_models.ListScenariosResponseBodyScenarioList] = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The details of the returned business scenarios.
        self.scenario_list = scenario_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.scenario_list:
            for v1 in self.scenario_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScenarioList'] = []
        if self.scenario_list is not None:
            for k1 in self.scenario_list:
                result['ScenarioList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scenario_list = []
        if m.get('ScenarioList') is not None:
            for k1 in m.get('ScenarioList'):
                temp_model = main_models.ListScenariosResponseBodyScenarioList()
                self.scenario_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListScenariosResponseBodyScenarioList(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        description: str = None,
        id: int = None,
        scenario_name: str = None,
    ):
        # The ID of the user who created the business scenario.
        self.creator_id = creator_id
        # The description of the business scenario.
        self.description = description
        # The ID of the business scenario.
        self.id = id
        # The name of the business scenario.
        self.scenario_name = scenario_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.scenario_name is not None:
            result['ScenarioName'] = self.scenario_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ScenarioName') is not None:
            self.scenario_name = m.get('ScenarioName')

        return self

