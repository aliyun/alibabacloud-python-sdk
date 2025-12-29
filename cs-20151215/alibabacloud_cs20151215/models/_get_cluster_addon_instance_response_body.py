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
        # The custom configurations of the component.
        self.config = config
        # The status of Simple Log Service.
        self.logging = logging
        # The name of the component instance.
        self.name = name
        # The status of the component. Valid values:
        # 
        # *   active: The component is installed.
        # *   updating: The component is being modified.
        # *   upgrading: The component is being updated.
        # *   deleting: The component is being uninstalled.
        self.state = state
        # The version of the component instance.
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
        # Indicates whether Simple Log Service is supported by the component.
        self.capable = capable
        # Indicates whether Simple Log Service is enabled for the component.
        self.enabled = enabled
        # The Simple Log Service project that is used to collect logs for the component.
        self.log_project = log_project
        # The Simple Log Service Logstore that is used to collect logs for the component.
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

