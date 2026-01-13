# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetLivyComputeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetLivyComputeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetLivyComputeResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetLivyComputeResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        auto_stop_configuration: main_models.GetLivyComputeResponseBodyDataAutoStopConfiguration = None,
        compute_id: str = None,
        cpu_limit: str = None,
        created_by: str = None,
        display_release_version: str = None,
        enable_public: bool = None,
        endpoint: str = None,
        endpoint_inner: str = None,
        environment_id: str = None,
        fusion: bool = None,
        gmt_create: int = None,
        livy_server_conf: str = None,
        livy_version: str = None,
        memory_limit: str = None,
        name: str = None,
        network_name: str = None,
        queue_name: str = None,
        ram_user_id: str = None,
        release_version: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.auth_type = auth_type
        self.auto_stop_configuration = auto_stop_configuration
        self.compute_id = compute_id
        self.cpu_limit = cpu_limit
        self.created_by = created_by
        self.display_release_version = display_release_version
        self.enable_public = enable_public
        self.endpoint = endpoint
        self.endpoint_inner = endpoint_inner
        self.environment_id = environment_id
        self.fusion = fusion
        self.gmt_create = gmt_create
        self.livy_server_conf = livy_server_conf
        self.livy_version = livy_version
        self.memory_limit = memory_limit
        self.name = name
        self.network_name = network_name
        self.queue_name = queue_name
        self.ram_user_id = ram_user_id
        self.release_version = release_version
        self.start_time = start_time
        self.status = status

    def validate(self):
        if self.auto_stop_configuration:
            self.auto_stop_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['authType'] = self.auth_type

        if self.auto_stop_configuration is not None:
            result['autoStopConfiguration'] = self.auto_stop_configuration.to_map()

        if self.compute_id is not None:
            result['computeId'] = self.compute_id

        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.endpoint_inner is not None:
            result['endpointInner'] = self.endpoint_inner

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.fusion is not None:
            result['fusion'] = self.fusion

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.livy_server_conf is not None:
            result['livyServerConf'] = self.livy_server_conf

        if self.livy_version is not None:
            result['livyVersion'] = self.livy_version

        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit

        if self.name is not None:
            result['name'] = self.name

        if self.network_name is not None:
            result['networkName'] = self.network_name

        if self.queue_name is not None:
            result['queueName'] = self.queue_name

        if self.ram_user_id is not None:
            result['ramUserId'] = self.ram_user_id

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')

        if m.get('autoStopConfiguration') is not None:
            temp_model = main_models.GetLivyComputeResponseBodyDataAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m.get('autoStopConfiguration'))

        if m.get('computeId') is not None:
            self.compute_id = m.get('computeId')

        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('endpointInner') is not None:
            self.endpoint_inner = m.get('endpointInner')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('livyServerConf') is not None:
            self.livy_server_conf = m.get('livyServerConf')

        if m.get('livyVersion') is not None:
            self.livy_version = m.get('livyVersion')

        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkName') is not None:
            self.network_name = m.get('networkName')

        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')

        if m.get('ramUserId') is not None:
            self.ram_user_id = m.get('ramUserId')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetLivyComputeResponseBodyDataAutoStopConfiguration(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        self.enable = enable
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

