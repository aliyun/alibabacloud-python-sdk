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
        # The short ID of the namespace. No need to specify a region ID. We recommend configuring this parameter.
        self.name_space_short_id = name_space_short_id
        # The namespace ID.
        self.namespace_id = namespace_id
        # The logging configurations of Simple Log Service.
        # 
        # *   `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`: Simple Log Service resources automatically created by Serverless App Engine (SAE) are used.
        # *   To use custom Simple Log Service resources, set this parameter to `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # Take note of the following subparameters:
        # 
        # *   **projectName**: the name of the Simple Log Service project.
        # *   **logDir**: the path in which logs are stored.
        # *   **logType**: the log type. **stdout** indicates the standard output (stdout) logs of the container. You can specify only one stdout value for this parameter. If not specified, file logs are collected.
        # *   **logstoreName**: the name of the Logstore in Simple Log Service.
        # *   **logtailName**: the name of the Logtail in Simple Log Service. If not specified, a new Logtail is created.
        # 
        # If logging configuration changes are not needed during job template deployment, specify **SlsConfigs** only in the first request. Omit this parameter in later requests. To stop using Simple Log Service, leave **SlsConfigs** empty.
        # 
        # > Projects automatically created by SAE for job templates are deleted when their corresponding job templates are deleted. Therefore, you should not select an existing SAE-created project for log collection.
        self.sls_configs = sls_configs
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

