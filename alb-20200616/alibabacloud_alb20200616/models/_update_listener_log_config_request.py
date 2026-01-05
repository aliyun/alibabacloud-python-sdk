# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class UpdateListenerLogConfigRequest(DaraModel):
    def __init__(
        self,
        access_log_record_customized_headers_enabled: bool = None,
        access_log_tracing_config: main_models.UpdateListenerLogConfigRequestAccessLogTracingConfig = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
    ):
        # Specifies whether to record custom headers in the access log. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # > You can set this parameter to **true** only if the access log feature is enabled by specifying **AccessLogEnabled**.
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        # The configuration information about the Xtrace feature.
        self.access_log_tracing_config = access_log_tracing_config
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: (default): performs a dry run and performs the actual request. If the request passes the dry run, a **2xx HTTP** status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the Application Load Balancer (ALB) listener.
        # 
        # This parameter is required.
        self.listener_id = listener_id

    def validate(self):
        if self.access_log_tracing_config:
            self.access_log_tracing_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_log_record_customized_headers_enabled is not None:
            result['AccessLogRecordCustomizedHeadersEnabled'] = self.access_log_record_customized_headers_enabled

        if self.access_log_tracing_config is not None:
            result['AccessLogTracingConfig'] = self.access_log_tracing_config.to_map()

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogRecordCustomizedHeadersEnabled') is not None:
            self.access_log_record_customized_headers_enabled = m.get('AccessLogRecordCustomizedHeadersEnabled')

        if m.get('AccessLogTracingConfig') is not None:
            temp_model = main_models.UpdateListenerLogConfigRequestAccessLogTracingConfig()
            self.access_log_tracing_config = temp_model.from_map(m.get('AccessLogTracingConfig'))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        return self

class UpdateListenerLogConfigRequestAccessLogTracingConfig(DaraModel):
    def __init__(
        self,
        tracing_enabled: bool = None,
        tracing_sample: int = None,
        tracing_type: str = None,
    ):
        # Specifies whether to enable the Xtrace feature. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # > You can set this parameter to **true** only if the access log feature is enabled by specifying **AccessLogEnabled**.
        # 
        # This parameter is required.
        self.tracing_enabled = tracing_enabled
        # The sampling rate of the Xtrace feature.
        # 
        # Valid values: **1 to 10000**.
        # 
        # > This parameter takes effect only if you set **TracingEnabled** to **true**.
        self.tracing_sample = tracing_sample
        # The type of Xtrace. Set the value to **Zipkin**.
        # 
        # > This parameter takes effect only if you set **TracingEnabled** to **true**.
        self.tracing_type = tracing_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tracing_enabled is not None:
            result['TracingEnabled'] = self.tracing_enabled

        if self.tracing_sample is not None:
            result['TracingSample'] = self.tracing_sample

        if self.tracing_type is not None:
            result['TracingType'] = self.tracing_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TracingEnabled') is not None:
            self.tracing_enabled = m.get('TracingEnabled')

        if m.get('TracingSample') is not None:
            self.tracing_sample = m.get('TracingSample')

        if m.get('TracingType') is not None:
            self.tracing_type = m.get('TracingType')

        return self

