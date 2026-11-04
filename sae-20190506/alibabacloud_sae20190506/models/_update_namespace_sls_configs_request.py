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
        # The short ID of the namespace. The region is not required. This parameter is recommended.
        self.name_space_short_id = name_space_short_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The configuration for collecting logs to Simple Log Service (SLS).
        # 
        # - To use SLS resources automatically created by Serverless App Engine (SAE): `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # - To use custom SLS resources: `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # The parameter settings are as follows:
        # 
        # - **projectName**: the name of the SLS project.  
        # - **logDir**: the log path.
        # - **logType**: the log type. **stdout** indicates container standard output logs. Only one stdout log can be set. If it is not set, file logs are collected.
        # - **logstoreName**: the name of the SLS Logstore.
        # - **logtailName**: the name of the SLS Logtail. If this parameter is not specified, a new Logtail is created.
        # 
        # If the SLS collection configuration remains unchanged during multiple deployments, you do not need to set this parameter (that is, the **SlsConfigs** field is not required in the request). If you no longer need the SLS collection feature, you must set the value of this field to an empty string (that is, set the **SlsConfigs** field to "") in the request.
        # 
        # > A project automatically created with a job template is deleted when the job template is deleted. Therefore, when you select an existing project, you cannot select a project automatically created by SAE.
        self.sls_configs = sls_configs
        # sls log tags
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

