# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListAnsServiceClustersResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListAnsServiceClustersResponseBodyData = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
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
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListAnsServiceClustersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAnsServiceClustersResponseBodyData(DaraModel):
    def __init__(
        self,
        app_detail: main_models.ListAnsServiceClustersResponseBodyDataAppDetail = None,
        clusters: List[main_models.ListAnsServiceClustersResponseBodyDataClusters] = None,
        ephemeral: bool = None,
        group_name: str = None,
        metadata: Dict[str, Any] = None,
        name: str = None,
        protect_threshold: float = None,
        selector_type: str = None,
        source: str = None,
    ):
        # The information about the associated application for which Microservices Governance is enabled when the Source parameter is set to governance.
        self.app_detail = app_detail
        # The cluster information.
        self.clusters = clusters
        # Indicates whether the service is a temporary service. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.ephemeral = ephemeral
        # The service group to which the service belongs.
        self.group_name = group_name
        # The metadata of the service.
        self.metadata = metadata
        # The name of the service.
        self.name = name
        # The protection threshold.
        self.protect_threshold = protect_threshold
        # The election mode.
        self.selector_type = selector_type
        # The source type of the service. Valid values:
        # 
        # *   console: The service was registered in the console.
        # *   sdk: The service was registered by using the SDK.
        # *   governance: The service was registered on Microservices Governance.
        self.source = source

    def validate(self):
        if self.app_detail:
            self.app_detail.validate()
        if self.clusters:
            for v1 in self.clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_detail is not None:
            result['AppDetail'] = self.app_detail.to_map()

        result['Clusters'] = []
        if self.clusters is not None:
            for k1 in self.clusters:
                result['Clusters'].append(k1.to_map() if k1 else None)

        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.name is not None:
            result['Name'] = self.name

        if self.protect_threshold is not None:
            result['ProtectThreshold'] = self.protect_threshold

        if self.selector_type is not None:
            result['SelectorType'] = self.selector_type

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDetail') is not None:
            temp_model = main_models.ListAnsServiceClustersResponseBodyDataAppDetail()
            self.app_detail = temp_model.from_map(m.get('AppDetail'))

        self.clusters = []
        if m.get('Clusters') is not None:
            for k1 in m.get('Clusters'):
                temp_model = main_models.ListAnsServiceClustersResponseBodyDataClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProtectThreshold') is not None:
            self.protect_threshold = m.get('ProtectThreshold')

        if m.get('SelectorType') is not None:
            self.selector_type = m.get('SelectorType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class ListAnsServiceClustersResponseBodyDataClusters(DaraModel):
    def __init__(
        self,
        default_check_port: int = None,
        default_port: int = None,
        health_checker_type: str = None,
        metadata: Dict[str, Any] = None,
        name: str = None,
        service_name: str = None,
        use_ipport_4check: bool = None,
    ):
        # The default port used for a health check.
        self.default_check_port = default_check_port
        # The default port.
        self.default_port = default_port
        # The type of the health check.
        self.health_checker_type = health_checker_type
        # The metadata of the cluster.
        self.metadata = metadata
        # The cluster name.
        self.name = name
        # The full name of the service.
        self.service_name = service_name
        # Indicates whether an end-to-end health check was initiated by the server. This parameter is valid only if the service is not a temporary service.
        self.use_ipport_4check = use_ipport_4check

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_check_port is not None:
            result['DefaultCheckPort'] = self.default_check_port

        if self.default_port is not None:
            result['DefaultPort'] = self.default_port

        if self.health_checker_type is not None:
            result['HealthCheckerType'] = self.health_checker_type

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.name is not None:
            result['Name'] = self.name

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.use_ipport_4check is not None:
            result['UseIPPort4Check'] = self.use_ipport_4check

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCheckPort') is not None:
            self.default_check_port = m.get('DefaultCheckPort')

        if m.get('DefaultPort') is not None:
            self.default_port = m.get('DefaultPort')

        if m.get('HealthCheckerType') is not None:
            self.health_checker_type = m.get('HealthCheckerType')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('UseIPPort4Check') is not None:
            self.use_ipport_4check = m.get('UseIPPort4Check')

        return self

class ListAnsServiceClustersResponseBodyDataAppDetail(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        check_internal: int = None,
        check_path: str = None,
        check_timeout: int = None,
        check_type: str = None,
        healthy_check_times: int = None,
        port: int = None,
        unhealthy_check_times: int = None,
    ):
        # The ID of the application for which Microservices Governance is enabled.
        self.app_id = app_id
        # The name of the application for which Microservices Governance is enabled.
        self.app_name = app_name
        # The health check interval. Unit: seconds.
        self.check_internal = check_internal
        # The path of the health check. This parameter is required only when the CheckType parameter is set to http.
        self.check_path = check_path
        # The timeout period of the health check response. Unit: seconds.
        self.check_timeout = check_timeout
        # The type of the health check. Valid values:
        # 
        # *   connection: connection status check
        # *   tcp: TCP connection check
        # *   http: HTTP connection check
        self.check_type = check_type
        # The maximum number of health check retries when the instance state changes from unhealthy to healthy.
        self.healthy_check_times = healthy_check_times
        # The port number of the application for which Microservices Governance is enabled.
        self.port = port
        # The maximum number of health check retries when the instance state changes from healthy to unhealthy.
        self.unhealthy_check_times = unhealthy_check_times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.check_internal is not None:
            result['CheckInternal'] = self.check_internal

        if self.check_path is not None:
            result['CheckPath'] = self.check_path

        if self.check_timeout is not None:
            result['CheckTimeout'] = self.check_timeout

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.healthy_check_times is not None:
            result['HealthyCheckTimes'] = self.healthy_check_times

        if self.port is not None:
            result['Port'] = self.port

        if self.unhealthy_check_times is not None:
            result['UnhealthyCheckTimes'] = self.unhealthy_check_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CheckInternal') is not None:
            self.check_internal = m.get('CheckInternal')

        if m.get('CheckPath') is not None:
            self.check_path = m.get('CheckPath')

        if m.get('CheckTimeout') is not None:
            self.check_timeout = m.get('CheckTimeout')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('HealthyCheckTimes') is not None:
            self.healthy_check_times = m.get('HealthyCheckTimes')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('UnhealthyCheckTimes') is not None:
            self.unhealthy_check_times = m.get('UnhealthyCheckTimes')

        return self

