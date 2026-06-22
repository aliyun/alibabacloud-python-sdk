# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application: main_models.GetApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The application.
        self.application = application
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['Application'] = self.application.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = main_models.GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m.get('Application'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationResponseBodyApplication(DaraModel):
    def __init__(
        self,
        actions: List[main_models.GetApplicationResponseBodyApplicationActions] = None,
        application_name: str = None,
        application_state: str = None,
        application_version: str = None,
        community_version: str = None,
    ):
        # The list of actions supported by the application.
        self.actions = actions
        # The application name.
        self.application_name = application_name
        # The status of the application.
        self.application_state = application_state
        # The application version.
        self.application_version = application_version
        # The community version.
        self.community_version = community_version

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_state is not None:
            result['ApplicationState'] = self.application_state

        if self.application_version is not None:
            result['ApplicationVersion'] = self.application_version

        if self.community_version is not None:
            result['CommunityVersion'] = self.community_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.GetApplicationResponseBodyApplicationActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationState') is not None:
            self.application_state = m.get('ApplicationState')

        if m.get('ApplicationVersion') is not None:
            self.application_version = m.get('ApplicationVersion')

        if m.get('CommunityVersion') is not None:
            self.community_version = m.get('CommunityVersion')

        return self

class GetApplicationResponseBodyApplicationActions(DaraModel):
    def __init__(
        self,
        action_name: str = None,
        action_params: List[main_models.GetApplicationResponseBodyApplicationActionsActionParams] = None,
        command: str = None,
        component_name: str = None,
        description: str = None,
        run_action_scope: str = None,
    ):
        # The action name.
        self.action_name = action_name
        # The list of action parameters.
        self.action_params = action_params
        # The action command.
        self.command = command
        # The component name.
        self.component_name = component_name
        # The description of the action.
        self.description = description
        # The execution scope. Valid values:
        # 
        # - APPLICATION: the application scope.
        # 
        # - COMPONENT: the component scope.
        # 
        # - COMPONENT_INSTANCE: the component instance scope.
        self.run_action_scope = run_action_scope

    def validate(self):
        if self.action_params:
            for v1 in self.action_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name is not None:
            result['ActionName'] = self.action_name

        result['ActionParams'] = []
        if self.action_params is not None:
            for k1 in self.action_params:
                result['ActionParams'].append(k1.to_map() if k1 else None)

        if self.command is not None:
            result['Command'] = self.command

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.description is not None:
            result['Description'] = self.description

        if self.run_action_scope is not None:
            result['RunActionScope'] = self.run_action_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')

        self.action_params = []
        if m.get('ActionParams') is not None:
            for k1 in m.get('ActionParams'):
                temp_model = main_models.GetApplicationResponseBodyApplicationActionsActionParams()
                self.action_params.append(temp_model.from_map(k1))

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RunActionScope') is not None:
            self.run_action_scope = m.get('RunActionScope')

        return self

class GetApplicationResponseBodyApplicationActionsActionParams(DaraModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        value_attribute: main_models.GetApplicationResponseBodyApplicationActionsActionParamsValueAttribute = None,
    ):
        # Description
        self.description = description
        # The parameter name.
        self.key = key
        # The parameter value attribute.
        self.value_attribute = value_attribute

    def validate(self):
        if self.value_attribute:
            self.value_attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        if self.value_attribute is not None:
            result['ValueAttribute'] = self.value_attribute.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ValueAttribute') is not None:
            temp_model = main_models.GetApplicationResponseBodyApplicationActionsActionParamsValueAttribute()
            self.value_attribute = temp_model.from_map(m.get('ValueAttribute'))

        return self

class GetApplicationResponseBodyApplicationActionsActionParamsValueAttribute(DaraModel):
    def __init__(
        self,
        description: str = None,
        value_increment_step: str = None,
        value_maximum: str = None,
        value_minimum: str = None,
        value_type: str = None,
        value_unit: str = None,
    ):
        # Value description.
        self.description = description
        # The size of the value increment.
        self.value_increment_step = value_increment_step
        # The maximum range of values.
        self.value_maximum = value_maximum
        # The minimum range of values.
        self.value_minimum = value_minimum
        # The value type of the column.
        self.value_type = value_type
        # The unit of the value.
        self.value_unit = value_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.value_increment_step is not None:
            result['ValueIncrementStep'] = self.value_increment_step

        if self.value_maximum is not None:
            result['ValueMaximum'] = self.value_maximum

        if self.value_minimum is not None:
            result['ValueMinimum'] = self.value_minimum

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        if self.value_unit is not None:
            result['ValueUnit'] = self.value_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ValueIncrementStep') is not None:
            self.value_increment_step = m.get('ValueIncrementStep')

        if m.get('ValueMaximum') is not None:
            self.value_maximum = m.get('ValueMaximum')

        if m.get('ValueMinimum') is not None:
            self.value_minimum = m.get('ValueMinimum')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        if m.get('ValueUnit') is not None:
            self.value_unit = m.get('ValueUnit')

        return self

