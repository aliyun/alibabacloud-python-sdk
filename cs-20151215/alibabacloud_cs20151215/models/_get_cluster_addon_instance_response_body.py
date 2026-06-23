# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class GetClusterAddonInstanceResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        logging: main_models.GetClusterAddonInstanceResponseBodyLogging = None,
        name: str = None,
        state: str = None,
        version: str = None,
    ):
        # The custom parameter settings of the component.
        self.config = config
        # The logging feature status of the component.
        self.logging = logging
        # The component instance name.
        self.name = name
        # The component status. Valid values:
        # - active: installed.
        # - updating: being modified.
        # - upgrading: being upgraded.
        # - deleting: being uninstalled.
        self.state = state
        # The component instance version.
        self.version = version

    def validate(self):
        if self.logging:
            self.logging.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.logging is not None:
            result['logging'] = self.logging.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.state is not None:
            result['state'] = self.state

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('logging') is not None:
            temp_model = main_models.GetClusterAddonInstanceResponseBodyLogging()
            self.logging = temp_model.from_map(m.get('logging'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetClusterAddonInstanceResponseBodyLogging(DaraModel):
    def __init__(
        self,
        capable: bool = None,
        enabled: bool = None,
        log_project: str = None,
        logstore: str = None,
    ):
        # Indicates whether the component supports the logging feature.
        # 
        # - true: Supported.
        # 
        # - false: Not supported.
        self.capable = capable
        # Indicates whether the logging feature is enabled for the component.
        # 
        # - true: Enabled.
        # 
        # - false: Not enabled.
        self.enabled = enabled
        # The Log Service project used by the logging feature of the component.
        self.log_project = log_project
        # The Log Service Logstore used by the logging feature of the component.
        self.logstore = logstore

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capable is not None:
            result['capable'] = self.capable

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.log_project is not None:
            result['log_project'] = self.log_project

        if self.logstore is not None:
            result['logstore'] = self.logstore

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capable') is not None:
            self.capable = m.get('capable')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('log_project') is not None:
            self.log_project = m.get('log_project')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        return self

