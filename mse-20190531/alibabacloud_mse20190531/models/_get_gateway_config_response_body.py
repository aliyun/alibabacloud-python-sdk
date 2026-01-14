# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetGatewayConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetGatewayConfigResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetGatewayConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetGatewayConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        access_log_header: str = None,
        downstream_connection_buffer_limits: int = None,
        downstream_http_2max_concurrent_stream: int = None,
        downstream_idle_time: int = None,
        enable_custom_auth_config_push: str = None,
        enable_generate_request_id: bool = None,
        enable_gzip: bool = None,
        enable_gzip_hardware_accelerate: bool = None,
        enable_hardware_accelerate: bool = None,
        enable_http_2: bool = None,
        enable_http_3: bool = None,
        enable_k8s_source_workload_filter: main_models.GetGatewayConfigResponseBodyDataEnableK8sSourceWorkloadFilter = None,
        enable_proxy_protocol: bool = None,
        enable_slash_merge: bool = None,
        enable_waf: bool = None,
        enable_xff_trusted_cidrs: main_models.GetGatewayConfigResponseBodyDataEnableXffTrustedCidrs = None,
        gateway_unique_id: str = None,
        initial_connection_window_size: int = None,
        initial_stream_window_size: int = None,
        keepalive_header_timeout: int = None,
        lite_metrics: bool = None,
        log_filter_config: str = None,
        no_supported_config_list: str = None,
        path_with_escaped_slashes: str = None,
        preserve_external_request_id: bool = None,
        preserve_header_format: bool = None,
        sls_config_details: main_models.GetGatewayConfigResponseBodyDataSlsConfigDetails = None,
        support_waf: bool = None,
        upstream_idle_timeout: int = None,
        websocket_term_grace_period: int = None,
        xff_trusted_num: int = None,
        xtrace_details: main_models.GetGatewayConfigResponseBodyDataXtraceDetails = None,
        zip_algorithm: str = None,
    ):
        self.access_log_header = access_log_header
        self.downstream_connection_buffer_limits = downstream_connection_buffer_limits
        self.downstream_http_2max_concurrent_stream = downstream_http_2max_concurrent_stream
        self.downstream_idle_time = downstream_idle_time
        self.enable_custom_auth_config_push = enable_custom_auth_config_push
        self.enable_generate_request_id = enable_generate_request_id
        self.enable_gzip = enable_gzip
        self.enable_gzip_hardware_accelerate = enable_gzip_hardware_accelerate
        self.enable_hardware_accelerate = enable_hardware_accelerate
        self.enable_http_2 = enable_http_2
        self.enable_http_3 = enable_http_3
        self.enable_k8s_source_workload_filter = enable_k8s_source_workload_filter
        self.enable_proxy_protocol = enable_proxy_protocol
        self.enable_slash_merge = enable_slash_merge
        self.enable_waf = enable_waf
        self.enable_xff_trusted_cidrs = enable_xff_trusted_cidrs
        self.gateway_unique_id = gateway_unique_id
        self.initial_connection_window_size = initial_connection_window_size
        self.initial_stream_window_size = initial_stream_window_size
        self.keepalive_header_timeout = keepalive_header_timeout
        self.lite_metrics = lite_metrics
        self.log_filter_config = log_filter_config
        self.no_supported_config_list = no_supported_config_list
        self.path_with_escaped_slashes = path_with_escaped_slashes
        self.preserve_external_request_id = preserve_external_request_id
        self.preserve_header_format = preserve_header_format
        self.sls_config_details = sls_config_details
        self.support_waf = support_waf
        self.upstream_idle_timeout = upstream_idle_timeout
        self.websocket_term_grace_period = websocket_term_grace_period
        self.xff_trusted_num = xff_trusted_num
        self.xtrace_details = xtrace_details
        self.zip_algorithm = zip_algorithm

    def validate(self):
        if self.enable_k8s_source_workload_filter:
            self.enable_k8s_source_workload_filter.validate()
        if self.enable_xff_trusted_cidrs:
            self.enable_xff_trusted_cidrs.validate()
        if self.sls_config_details:
            self.sls_config_details.validate()
        if self.xtrace_details:
            self.xtrace_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_log_header is not None:
            result['AccessLogHeader'] = self.access_log_header

        if self.downstream_connection_buffer_limits is not None:
            result['DownstreamConnectionBufferLimits'] = self.downstream_connection_buffer_limits

        if self.downstream_http_2max_concurrent_stream is not None:
            result['DownstreamHttp2MaxConcurrentStream'] = self.downstream_http_2max_concurrent_stream

        if self.downstream_idle_time is not None:
            result['DownstreamIdleTime'] = self.downstream_idle_time

        if self.enable_custom_auth_config_push is not None:
            result['EnableCustomAuthConfigPush'] = self.enable_custom_auth_config_push

        if self.enable_generate_request_id is not None:
            result['EnableGenerateRequestId'] = self.enable_generate_request_id

        if self.enable_gzip is not None:
            result['EnableGzip'] = self.enable_gzip

        if self.enable_gzip_hardware_accelerate is not None:
            result['EnableGzipHardwareAccelerate'] = self.enable_gzip_hardware_accelerate

        if self.enable_hardware_accelerate is not None:
            result['EnableHardwareAccelerate'] = self.enable_hardware_accelerate

        if self.enable_http_2 is not None:
            result['EnableHttp2'] = self.enable_http_2

        if self.enable_http_3 is not None:
            result['EnableHttp3'] = self.enable_http_3

        if self.enable_k8s_source_workload_filter is not None:
            result['EnableK8sSourceWorkloadFilter'] = self.enable_k8s_source_workload_filter.to_map()

        if self.enable_proxy_protocol is not None:
            result['EnableProxyProtocol'] = self.enable_proxy_protocol

        if self.enable_slash_merge is not None:
            result['EnableSlashMerge'] = self.enable_slash_merge

        if self.enable_waf is not None:
            result['EnableWaf'] = self.enable_waf

        if self.enable_xff_trusted_cidrs is not None:
            result['EnableXffTrustedCidrs'] = self.enable_xff_trusted_cidrs.to_map()

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.initial_connection_window_size is not None:
            result['InitialConnectionWindowSize'] = self.initial_connection_window_size

        if self.initial_stream_window_size is not None:
            result['InitialStreamWindowSize'] = self.initial_stream_window_size

        if self.keepalive_header_timeout is not None:
            result['KeepaliveHeaderTimeout'] = self.keepalive_header_timeout

        if self.lite_metrics is not None:
            result['LiteMetrics'] = self.lite_metrics

        if self.log_filter_config is not None:
            result['LogFilterConfig'] = self.log_filter_config

        if self.no_supported_config_list is not None:
            result['NoSupportedConfigList'] = self.no_supported_config_list

        if self.path_with_escaped_slashes is not None:
            result['PathWithEscapedSlashes'] = self.path_with_escaped_slashes

        if self.preserve_external_request_id is not None:
            result['PreserveExternalRequestID'] = self.preserve_external_request_id

        if self.preserve_header_format is not None:
            result['PreserveHeaderFormat'] = self.preserve_header_format

        if self.sls_config_details is not None:
            result['SlsConfigDetails'] = self.sls_config_details.to_map()

        if self.support_waf is not None:
            result['SupportWaf'] = self.support_waf

        if self.upstream_idle_timeout is not None:
            result['UpstreamIdleTimeout'] = self.upstream_idle_timeout

        if self.websocket_term_grace_period is not None:
            result['WebsocketTermGracePeriod'] = self.websocket_term_grace_period

        if self.xff_trusted_num is not None:
            result['XffTrustedNum'] = self.xff_trusted_num

        if self.xtrace_details is not None:
            result['XtraceDetails'] = self.xtrace_details.to_map()

        if self.zip_algorithm is not None:
            result['ZipAlgorithm'] = self.zip_algorithm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogHeader') is not None:
            self.access_log_header = m.get('AccessLogHeader')

        if m.get('DownstreamConnectionBufferLimits') is not None:
            self.downstream_connection_buffer_limits = m.get('DownstreamConnectionBufferLimits')

        if m.get('DownstreamHttp2MaxConcurrentStream') is not None:
            self.downstream_http_2max_concurrent_stream = m.get('DownstreamHttp2MaxConcurrentStream')

        if m.get('DownstreamIdleTime') is not None:
            self.downstream_idle_time = m.get('DownstreamIdleTime')

        if m.get('EnableCustomAuthConfigPush') is not None:
            self.enable_custom_auth_config_push = m.get('EnableCustomAuthConfigPush')

        if m.get('EnableGenerateRequestId') is not None:
            self.enable_generate_request_id = m.get('EnableGenerateRequestId')

        if m.get('EnableGzip') is not None:
            self.enable_gzip = m.get('EnableGzip')

        if m.get('EnableGzipHardwareAccelerate') is not None:
            self.enable_gzip_hardware_accelerate = m.get('EnableGzipHardwareAccelerate')

        if m.get('EnableHardwareAccelerate') is not None:
            self.enable_hardware_accelerate = m.get('EnableHardwareAccelerate')

        if m.get('EnableHttp2') is not None:
            self.enable_http_2 = m.get('EnableHttp2')

        if m.get('EnableHttp3') is not None:
            self.enable_http_3 = m.get('EnableHttp3')

        if m.get('EnableK8sSourceWorkloadFilter') is not None:
            temp_model = main_models.GetGatewayConfigResponseBodyDataEnableK8sSourceWorkloadFilter()
            self.enable_k8s_source_workload_filter = temp_model.from_map(m.get('EnableK8sSourceWorkloadFilter'))

        if m.get('EnableProxyProtocol') is not None:
            self.enable_proxy_protocol = m.get('EnableProxyProtocol')

        if m.get('EnableSlashMerge') is not None:
            self.enable_slash_merge = m.get('EnableSlashMerge')

        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

        if m.get('EnableXffTrustedCidrs') is not None:
            temp_model = main_models.GetGatewayConfigResponseBodyDataEnableXffTrustedCidrs()
            self.enable_xff_trusted_cidrs = temp_model.from_map(m.get('EnableXffTrustedCidrs'))

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('InitialConnectionWindowSize') is not None:
            self.initial_connection_window_size = m.get('InitialConnectionWindowSize')

        if m.get('InitialStreamWindowSize') is not None:
            self.initial_stream_window_size = m.get('InitialStreamWindowSize')

        if m.get('KeepaliveHeaderTimeout') is not None:
            self.keepalive_header_timeout = m.get('KeepaliveHeaderTimeout')

        if m.get('LiteMetrics') is not None:
            self.lite_metrics = m.get('LiteMetrics')

        if m.get('LogFilterConfig') is not None:
            self.log_filter_config = m.get('LogFilterConfig')

        if m.get('NoSupportedConfigList') is not None:
            self.no_supported_config_list = m.get('NoSupportedConfigList')

        if m.get('PathWithEscapedSlashes') is not None:
            self.path_with_escaped_slashes = m.get('PathWithEscapedSlashes')

        if m.get('PreserveExternalRequestID') is not None:
            self.preserve_external_request_id = m.get('PreserveExternalRequestID')

        if m.get('PreserveHeaderFormat') is not None:
            self.preserve_header_format = m.get('PreserveHeaderFormat')

        if m.get('SlsConfigDetails') is not None:
            temp_model = main_models.GetGatewayConfigResponseBodyDataSlsConfigDetails()
            self.sls_config_details = temp_model.from_map(m.get('SlsConfigDetails'))

        if m.get('SupportWaf') is not None:
            self.support_waf = m.get('SupportWaf')

        if m.get('UpstreamIdleTimeout') is not None:
            self.upstream_idle_timeout = m.get('UpstreamIdleTimeout')

        if m.get('WebsocketTermGracePeriod') is not None:
            self.websocket_term_grace_period = m.get('WebsocketTermGracePeriod')

        if m.get('XffTrustedNum') is not None:
            self.xff_trusted_num = m.get('XffTrustedNum')

        if m.get('XtraceDetails') is not None:
            temp_model = main_models.GetGatewayConfigResponseBodyDataXtraceDetails()
            self.xtrace_details = temp_model.from_map(m.get('XtraceDetails'))

        if m.get('ZipAlgorithm') is not None:
            self.zip_algorithm = m.get('ZipAlgorithm')

        return self

class GetGatewayConfigResponseBodyDataXtraceDetails(DaraModel):
    def __init__(
        self,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        sample: int = None,
        service_id: int = None,
        service_port: str = None,
        trace_on: bool = None,
        trace_type: str = None,
    ):
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.sample = sample
        self.service_id = service_id
        self.service_port = service_port
        self.trace_on = trace_on
        self.trace_type = trace_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.trace_on is not None:
            result['TraceOn'] = self.trace_on

        if self.trace_type is not None:
            result['TraceType'] = self.trace_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('TraceOn') is not None:
            self.trace_on = m.get('TraceOn')

        if m.get('TraceType') is not None:
            self.trace_type = m.get('TraceType')

        return self

class GetGatewayConfigResponseBodyDataSlsConfigDetails(DaraModel):
    def __init__(
        self,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        log_on: bool = None,
        log_store_name: str = None,
        nginx_compatible: bool = None,
        project_name: str = None,
    ):
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.log_on = log_on
        self.log_store_name = log_store_name
        self.nginx_compatible = nginx_compatible
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.log_on is not None:
            result['LogOn'] = self.log_on

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.nginx_compatible is not None:
            result['NginxCompatible'] = self.nginx_compatible

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LogOn') is not None:
            self.log_on = m.get('LogOn')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('NginxCompatible') is not None:
            self.nginx_compatible = m.get('NginxCompatible')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class GetGatewayConfigResponseBodyDataEnableXffTrustedCidrs(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        ip_list_content: str = None,
    ):
        self.enable = enable
        self.ip_list_content = ip_list_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.ip_list_content is not None:
            result['IpListContent'] = self.ip_list_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('IpListContent') is not None:
            self.ip_list_content = m.get('IpListContent')

        return self

class GetGatewayConfigResponseBodyDataEnableK8sSourceWorkloadFilter(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        filter_opt: str = None,
        label_key: str = None,
        label_value: str = None,
    ):
        self.enable = enable
        self.filter_opt = filter_opt
        self.label_key = label_key
        self.label_value = label_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.filter_opt is not None:
            result['FilterOpt'] = self.filter_opt

        if self.label_key is not None:
            result['LabelKey'] = self.label_key

        if self.label_value is not None:
            result['LabelValue'] = self.label_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FilterOpt') is not None:
            self.filter_opt = m.get('FilterOpt')

        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')

        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')

        return self

