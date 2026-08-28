# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class GetPatrolConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetPatrolConfigResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The inspection configuration response data.
        self.data = data
        # The error code. This field is not empty when success is false. This field is empty when success is true.
        self.error_code = error_code
        # The error message. This field is not empty when success is false. This field is empty when success is true.
        self.error_message = error_message
        # The HTTP status code. The value is always 200. Use the success field to determine whether the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetPatrolConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetPatrolConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        config_created_at: int = None,
        config_updated_at: int = None,
        cron: str = None,
        enabled: bool = None,
        namespace: str = None,
        next_patrol_at: int = None,
        scope_config: main_models.GetPatrolConfigResponseBodyDataScopeConfig = None,
        scope_type: str = None,
        timezone: str = None,
        workspace: str = None,
    ):
        # The configuration creation time, in milliseconds (UNIX timestamp).
        self.config_created_at = config_created_at
        # The configuration update time, in milliseconds (UNIX timestamp).
        self.config_updated_at = config_updated_at
        # The cron expression that defines the inspection scheduling time.
        self.cron = cron
        # Indicates whether inspection is enabled.
        self.enabled = enabled
        # The namespace.
        self.namespace = namespace
        # The next inspection time, in milliseconds (UNIX timestamp).
        self.next_patrol_at = next_patrol_at
        # The inspection scope configuration.
        self.scope_config = scope_config
        # The inspection scope type. Valid values:
        # - ALL: inspects all deployments.
        # - TAGS: filters deployments by tag.
        # - DEPLOYMENTS: inspects specified deployments.
        self.scope_type = scope_type
        # The time zone.
        self.timezone = timezone
        # The workspace ID.
        self.workspace = workspace

    def validate(self):
        if self.scope_config:
            self.scope_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_created_at is not None:
            result['configCreatedAt'] = self.config_created_at

        if self.config_updated_at is not None:
            result['configUpdatedAt'] = self.config_updated_at

        if self.cron is not None:
            result['cron'] = self.cron

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.next_patrol_at is not None:
            result['nextPatrolAt'] = self.next_patrol_at

        if self.scope_config is not None:
            result['scopeConfig'] = self.scope_config.to_map()

        if self.scope_type is not None:
            result['scopeType'] = self.scope_type

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configCreatedAt') is not None:
            self.config_created_at = m.get('configCreatedAt')

        if m.get('configUpdatedAt') is not None:
            self.config_updated_at = m.get('configUpdatedAt')

        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('nextPatrolAt') is not None:
            self.next_patrol_at = m.get('nextPatrolAt')

        if m.get('scopeConfig') is not None:
            temp_model = main_models.GetPatrolConfigResponseBodyDataScopeConfig()
            self.scope_config = temp_model.from_map(m.get('scopeConfig'))

        if m.get('scopeType') is not None:
            self.scope_type = m.get('scopeType')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetPatrolConfigResponseBodyDataScopeConfig(DaraModel):
    def __init__(
        self,
        deployment_ids: List[str] = None,
        tags: Dict[str, List[str]] = None,
    ):
        # The list of deployment IDs. This field is valid only when scopeType is set to DEPLOYMENTS.
        self.deployment_ids = deployment_ids
        # The tag mapping. This field is valid only when scopeType is set to TAGS. The key is the tag name, and the value is the list of tag values.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_ids is not None:
            result['deploymentIds'] = self.deployment_ids

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentIds') is not None:
            self.deployment_ids = m.get('deploymentIds')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

