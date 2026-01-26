# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEnvironmentFeaturesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListEnvironmentFeaturesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status Code. Description 200 indicates success.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the alert rule was deleted. Valid values:
        # 
        # *   `true`: The alert rule was deleted.
        # *   `false`: The alert rule failed to be deleted.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListEnvironmentFeaturesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEnvironmentFeaturesResponseBodyData(DaraModel):
    def __init__(
        self,
        alias: str = None,
        config: Dict[str, str] = None,
        description: str = None,
        environment_id: str = None,
        icon: str = None,
        language: str = None,
        latest_version: str = None,
        managed: bool = None,
        name: str = None,
        status: str = None,
        version: str = None,
    ):
        # The alias of the feature.
        self.alias = alias
        # The feature configuration.
        self.config = config
        # The description of the feature.
        self.description = description
        # The ID of the environment instance.
        self.environment_id = environment_id
        # The URL of the icon.
        self.icon = icon
        # The language. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.language = language
        # The latest version number.
        self.latest_version = latest_version
        # Indicates whether the component is fully managed.
        self.managed = managed
        # The name of the feature.
        self.name = name
        # The status of the feature. Valid values:
        # 
        # *   Installing: The agent is being installed.
        # *   Success: The agent is installed.
        # *   Failed: The agent failed to be installed.
        # *   UnInstall: The agent is uninstalled.
        # *   Uninstalling: The agent is being uninstalled.
        # *   UnInstallFailed: The agent failed to be uninstalled.
        self.status = status
        # The version of the feature.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.language is not None:
            result['Language'] = self.language

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.managed is not None:
            result['Managed'] = self.managed

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('Managed') is not None:
            self.managed = m.get('Managed')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

