# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListSessionClustersResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        session_clusters: List[main_models.ListSessionClustersResponseBodySessionClusters] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The sessions.
        self.session_clusters = session_clusters
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.session_clusters:
            for v1 in self.session_clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['sessionClusters'] = []
        if self.session_clusters is not None:
            for k1 in self.session_clusters:
                result['sessionClusters'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.session_clusters = []
        if m.get('sessionClusters') is not None:
            for k1 in m.get('sessionClusters'):
                temp_model = main_models.ListSessionClustersResponseBodySessionClusters()
                self.session_clusters.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListSessionClustersResponseBodySessionClusters(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.ListSessionClustersResponseBodySessionClustersApplicationConfigs] = None,
        auto_start_configuration: main_models.ListSessionClustersResponseBodySessionClustersAutoStartConfiguration = None,
        auto_stop_configuration: main_models.ListSessionClustersResponseBodySessionClustersAutoStopConfiguration = None,
        connection_token: str = None,
        display_release_version: str = None,
        domain: str = None,
        domain_inner: str = None,
        draft_id: str = None,
        extra: str = None,
        fusion: bool = None,
        gmt_create: int = None,
        kind: str = None,
        name: str = None,
        public_endpoint_enabled: bool = None,
        queue_name: str = None,
        release_version: str = None,
        session_cluster_id: str = None,
        start_time: int = None,
        state: str = None,
        state_change_reason: main_models.ListSessionClustersResponseBodySessionClustersStateChangeReason = None,
        user_id: str = None,
        user_name: str = None,
        web_ui: str = None,
        workspace_id: str = None,
    ):
        # The session configurations, which are equivalent to the configurations of the Spark job.
        self.application_configs = application_configs
        # The automatic startup configurations.
        self.auto_start_configuration = auto_start_configuration
        # The configurations of automatic termination.
        self.auto_stop_configuration = auto_stop_configuration
        self.connection_token = connection_token
        # The version of the Spark engine.
        self.display_release_version = display_release_version
        # The public endpoint of the Thrift server.
        self.domain = domain
        # The internal endpoint of the Thrift server.
        self.domain_inner = domain_inner
        # The ID of the job that is associated with the session.
        self.draft_id = draft_id
        # The additional metadata of the session.
        self.extra = extra
        # Indicates whether the Fusion engine is used for acceleration.
        self.fusion = fusion
        # The creation time.
        self.gmt_create = gmt_create
        # The session type.
        # 
        # Valid values:
        # 
        # *   NOTEBOOK
        # *   THRIFT
        # *   SQL
        self.kind = kind
        # The name of the session.
        self.name = name
        self.public_endpoint_enabled = public_endpoint_enabled
        # The name of the queue that is used to run the session.
        self.queue_name = queue_name
        # The version of EMR Serverless Spark.
        self.release_version = release_version
        # The session ID.
        self.session_cluster_id = session_cluster_id
        # The start time.
        self.start_time = start_time
        # The status of the session.
        # 
        # *   Starting
        # *   Running
        # *   Stopping
        # *   Stopped
        # *   Error
        self.state = state
        # The details of the most recent status change of the session.
        self.state_change_reason = state_change_reason
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name
        # The Spark UI of the session.
        self.web_ui = web_ui
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.application_configs:
            for v1 in self.application_configs:
                 if v1:
                    v1.validate()
        if self.auto_start_configuration:
            self.auto_start_configuration.validate()
        if self.auto_stop_configuration:
            self.auto_stop_configuration.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['applicationConfigs'] = []
        if self.application_configs is not None:
            for k1 in self.application_configs:
                result['applicationConfigs'].append(k1.to_map() if k1 else None)

        if self.auto_start_configuration is not None:
            result['autoStartConfiguration'] = self.auto_start_configuration.to_map()

        if self.auto_stop_configuration is not None:
            result['autoStopConfiguration'] = self.auto_stop_configuration.to_map()

        if self.connection_token is not None:
            result['connectionToken'] = self.connection_token

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.domain is not None:
            result['domain'] = self.domain

        if self.domain_inner is not None:
            result['domainInner'] = self.domain_inner

        if self.draft_id is not None:
            result['draftId'] = self.draft_id

        if self.extra is not None:
            result['extra'] = self.extra

        if self.fusion is not None:
            result['fusion'] = self.fusion

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.kind is not None:
            result['kind'] = self.kind

        if self.name is not None:
            result['name'] = self.name

        if self.public_endpoint_enabled is not None:
            result['publicEndpointEnabled'] = self.public_endpoint_enabled

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.state is not None:
            result['state'] = self.state

        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        if self.web_ui is not None:
            result['webUI'] = self.web_ui

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('applicationConfigs') is not None:
            for k1 in m.get('applicationConfigs'):
                temp_model = main_models.ListSessionClustersResponseBodySessionClustersApplicationConfigs()
                self.application_configs.append(temp_model.from_map(k1))

        if m.get('autoStartConfiguration') is not None:
            temp_model = main_models.ListSessionClustersResponseBodySessionClustersAutoStartConfiguration()
            self.auto_start_configuration = temp_model.from_map(m.get('autoStartConfiguration'))

        if m.get('autoStopConfiguration') is not None:
            temp_model = main_models.ListSessionClustersResponseBodySessionClustersAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m.get('autoStopConfiguration'))

        if m.get('connectionToken') is not None:
            self.connection_token = m.get('connectionToken')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('domainInner') is not None:
            self.domain_inner = m.get('domainInner')

        if m.get('draftId') is not None:
            self.draft_id = m.get('draftId')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('publicEndpointEnabled') is not None:
            self.public_endpoint_enabled = m.get('publicEndpointEnabled')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('stateChangeReason') is not None:
            temp_model = main_models.ListSessionClustersResponseBodySessionClustersStateChangeReason()
            self.state_change_reason = temp_model.from_map(m.get('stateChangeReason'))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListSessionClustersResponseBodySessionClustersStateChangeReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The status change code.
        self.code = code
        # The status change message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class ListSessionClustersResponseBodySessionClustersAutoStopConfiguration(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        # Indicates whether automatic termination is enabled.
        self.enable = enable
        # The idle timeout period. The session is automatically terminated when the idle timeout period is exceeded.
        self.idle_timeout_minutes = idle_timeout_minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.idle_timeout_minutes is not None:
            result['idleTimeoutMinutes'] = self.idle_timeout_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('idleTimeoutMinutes') is not None:
            self.idle_timeout_minutes = m.get('idleTimeoutMinutes')

        return self

class ListSessionClustersResponseBodySessionClustersAutoStartConfiguration(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Indicates whether automatic startup is enabled.
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        return self

class ListSessionClustersResponseBodySessionClustersApplicationConfigs(DaraModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        # The name of the configuration file.
        self.config_file_name = config_file_name
        # The key of the configuration.
        self.config_item_key = config_item_key
        # The configuration value.
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name

        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')

        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')

        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')

        return self

