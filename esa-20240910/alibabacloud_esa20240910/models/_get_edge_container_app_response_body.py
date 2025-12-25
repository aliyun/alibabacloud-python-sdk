# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetEdgeContainerAppResponseBody(DaraModel):
    def __init__(
        self,
        app: main_models.GetEdgeContainerAppResponseBodyApp = None,
        request_id: str = None,
    ):
        # The basic information about the application.
        self.app = app
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = main_models.GetEdgeContainerAppResponseBodyApp()
            self.app = temp_model.from_map(m.get('App'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEdgeContainerAppResponseBodyApp(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: str = None,
        domain_name: str = None,
        gateway_type: str = None,
        health_check: main_models.GetEdgeContainerAppResponseBodyAppHealthCheck = None,
        name: str = None,
        quic_cid: str = None,
        remarks: str = None,
        service_port: int = None,
        status: str = None,
        target_port: int = None,
        update_time: str = None,
        version_count: int = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The time when the application was created.
        self.create_time = create_time
        # The domain name that is associated with the application. If no domain name is associated with the application, the value is an empty string.
        self.domain_name = domain_name
        # The type of the gateway. Valid values:
        # 
        # *   l7: Layer 7 gateway.
        # *   l4: Layer 4 gateway.
        self.gateway_type = gateway_type
        # The information about health checks.
        self.health_check = health_check
        # The application name.
        self.name = name
        # Indicates whether QUIC is enabled.
        self.quic_cid = quic_cid
        # The remarks about the application.
        self.remarks = remarks
        # The server port. Valid values: 1 to 65535.
        self.service_port = service_port
        # The status of the application. Valid values:
        # 
        # *   creating: The application is being created.
        # *   failed: The application failed to be created.
        # *   created: The application is created.
        self.status = status
        # The backend port, which is also the service port of the application. Valid values: 1 to 65535.
        self.target_port = target_port
        # The time when the application was last modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.update_time = update_time
        # The number of versions of the application.
        self.version_count = version_count

    def validate(self):
        if self.health_check:
            self.health_check.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.quic_cid is not None:
            result['QuicCid'] = self.quic_cid

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.status is not None:
            result['Status'] = self.status

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version_count is not None:
            result['VersionCount'] = self.version_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('HealthCheck') is not None:
            temp_model = main_models.GetEdgeContainerAppResponseBodyAppHealthCheck()
            self.health_check = temp_model.from_map(m.get('HealthCheck'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QuicCid') is not None:
            self.quic_cid = m.get('QuicCid')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VersionCount') is not None:
            self.version_count = m.get('VersionCount')

        return self

class GetEdgeContainerAppResponseBodyAppHealthCheck(DaraModel):
    def __init__(
        self,
        fail_times: int = None,
        host: str = None,
        http_code: str = None,
        interval: int = None,
        method: str = None,
        port: int = None,
        succ_times: int = None,
        timeout: int = None,
        type: str = None,
        uri: str = None,
    ):
        # The number of consecutive failed health checks required for an application to be considered as unhealthy.
        self.fail_times = fail_times
        # The domain name that is used for health checks.
        self.host = host
        # The range of health check status codes that indicate successful health checks.
        self.http_code = http_code
        # The interval between health checks. Unit: seconds.
        self.interval = interval
        # The HTTP method that the health check request uses.
        self.method = method
        # The health check port.
        self.port = port
        # The number of consecutive successful health checks required for an application to be considered as healthy.
        self.succ_times = succ_times
        # The timeout period of the health check. Unit: seconds.
        self.timeout = timeout
        # The health check type. Valid values:
        # 
        # *   l7
        # *   l4
        self.type = type
        # The health check URL.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times

        if self.host is not None:
            result['Host'] = self.host

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.method is not None:
            result['Method'] = self.method

        if self.port is not None:
            result['Port'] = self.port

        if self.succ_times is not None:
            result['SuccTimes'] = self.succ_times

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SuccTimes') is not None:
            self.succ_times = m.get('SuccTimes')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

