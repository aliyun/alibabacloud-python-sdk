# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GatewayOption(DaraModel):
    def __init__(
        self,
        disable_http_2alpn: bool = None,
        enable_hardware_acceleration: bool = None,
        enable_waf: bool = None,
        log_config_details: main_models.GatewayOptionLogConfigDetails = None,
        trace_details: main_models.GatewayOptionTraceDetails = None,
    ):
        self.disable_http_2alpn = disable_http_2alpn
        self.enable_hardware_acceleration = enable_hardware_acceleration
        self.enable_waf = enable_waf
        self.log_config_details = log_config_details
        self.trace_details = trace_details

    def validate(self):
        if self.log_config_details:
            self.log_config_details.validate()
        if self.trace_details:
            self.trace_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_http_2alpn is not None:
            result['DisableHttp2Alpn'] = self.disable_http_2alpn

        if self.enable_hardware_acceleration is not None:
            result['EnableHardwareAcceleration'] = self.enable_hardware_acceleration

        if self.enable_waf is not None:
            result['EnableWaf'] = self.enable_waf

        if self.log_config_details is not None:
            result['LogConfigDetails'] = self.log_config_details.to_map()

        if self.trace_details is not None:
            result['TraceDetails'] = self.trace_details.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableHttp2Alpn') is not None:
            self.disable_http_2alpn = m.get('DisableHttp2Alpn')

        if m.get('EnableHardwareAcceleration') is not None:
            self.enable_hardware_acceleration = m.get('EnableHardwareAcceleration')

        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

        if m.get('LogConfigDetails') is not None:
            temp_model = main_models.GatewayOptionLogConfigDetails()
            self.log_config_details = temp_model.from_map(m.get('LogConfigDetails'))

        if m.get('TraceDetails') is not None:
            temp_model = main_models.GatewayOptionTraceDetails()
            self.trace_details = temp_model.from_map(m.get('TraceDetails'))

        return self

class GatewayOptionTraceDetails(DaraModel):
    def __init__(
        self,
        sample: int = None,
        service_id: int = None,
        service_port: str = None,
        trace_enabled: bool = None,
        trace_type: str = None,
    ):
        self.sample = sample
        self.service_id = service_id
        self.service_port = service_port
        # This parameter is required.
        self.trace_enabled = trace_enabled
        self.trace_type = trace_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sample is not None:
            result['Sample'] = self.sample

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.trace_enabled is not None:
            result['TraceEnabled'] = self.trace_enabled

        if self.trace_type is not None:
            result['TraceType'] = self.trace_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('TraceEnabled') is not None:
            self.trace_enabled = m.get('TraceEnabled')

        if m.get('TraceType') is not None:
            self.trace_type = m.get('TraceType')

        return self



class GatewayOptionLogConfigDetails(DaraModel):
    def __init__(
        self,
        log_enabled: bool = None,
        log_store_name: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.log_enabled = log_enabled
        self.log_store_name = log_store_name
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

