# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNamespaceSlsConfigsRequest(DaraModel):
    def __init__(
        self,
        name_space_short_id: str = None,
        namespace_id: str = None,
        sls_configs: str = None,
        sls_log_env_tags: str = None,
    ):
        # The short ID of the namespace. You do not need to include the region. This parameter is recommended.
        self.name_space_short_id = name_space_short_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The configuration for collecting logs to SLS.
        # 
        # - To use an SLS resource that is automatically created by SAE: `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # 
        # - To use a custom SLS resource: `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # The parameters are described as follows:
        # 
        # - `projectName`: The name of the SLS project.
        # 
        # - `logDir`: The log path.
        # 
        # - `logType`: The log type. A value of `stdout` specifies container standard output logs. You can specify only one `stdout` configuration. If you do not set this parameter, file logs are collected.
        # 
        # - `logstoreName`: The name of the SLS logstore.
        # 
        # - `logtailName`: The name of the Logtail. If you do not specify this parameter, a new Logtail is created.
        # 
        # If the SLS configuration remains the same across deployments, you can omit this parameter. To disable log collection to SLS, set the value of `SlsConfigs` to an empty string ("").
        # 
        # > SAE automatically deletes a project when you delete the task template used to create it. Therefore, when you select an existing project, do not select a project that was automatically created by SAE.
        self.sls_configs = sls_configs
        # The SLS log tags.
        self.sls_log_env_tags = sls_log_env_tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_space_short_id is not None:
            result['NameSpaceShortId'] = self.name_space_short_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs

        if self.sls_log_env_tags is not None:
            result['SlsLogEnvTags'] = self.sls_log_env_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameSpaceShortId') is not None:
            self.name_space_short_id = m.get('NameSpaceShortId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')

        if m.get('SlsLogEnvTags') is not None:
            self.sls_log_env_tags = m.get('SlsLogEnvTags')

        return self

