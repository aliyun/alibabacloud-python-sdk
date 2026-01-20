# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QueryConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.QueryConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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
            temp_model = main_models.QueryConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_enabled: bool = None,
        autopurge_purge_interval: str = None,
        autopurge_snap_retain_count: str = None,
        cluster_name: str = None,
        config_auth_enabled: bool = None,
        config_auth_supported: bool = None,
        config_content_limit: int = None,
        config_secret_enabled: bool = None,
        config_secret_supported: bool = None,
        console_uienabled: bool = None,
        enable_4lw: bool = None,
        eureka_supported: bool = None,
        extended_types_enable: bool = None,
        init_limit: str = None,
        jute_maxbuffer: str = None,
        jvm_flags_custom: str = None,
        mcpenabled: bool = None,
        mcpsupported: bool = None,
        max_client_cnxns: str = None,
        max_session_timeout: str = None,
        min_session_timeout: str = None,
        nacos_running_env: main_models.QueryConfigResponseBodyDataNacosRunningEnv = None,
        naming_auth_enabled: bool = None,
        naming_auth_supported: bool = None,
        naming_create_service_supported: bool = None,
        open_super_acl: bool = None,
        pass_word: str = None,
        prometheus_sd_protocol_enabled: str = None,
        restart_flag: bool = None,
        snapshot_count: str = None,
        sync_limit: str = None,
        tlsenabled: bool = None,
        tick_time: str = None,
        user_name: str = None,
    ):
        # Indicates whether Simple Authentication and Security Layer (SASL) forced identity authentication is enabled for the ZooKeeper instance.
        self.auth_enabled = auth_enabled
        # A reserved parameter.
        self.autopurge_purge_interval = autopurge_purge_interval
        # A reserved parameter.
        self.autopurge_snap_retain_count = autopurge_snap_retain_count
        # The name of the instance.
        self.cluster_name = cluster_name
        # Indicates whether RAM authentication of a configuration center is enabled. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: enabled.
        # *   `false`: disabled.
        self.config_auth_enabled = config_auth_enabled
        # Indicates whether RAM authentication is supported by a configuration center of the instance. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: supported.
        # *   `false`: not supported.
        self.config_auth_supported = config_auth_supported
        # The maximum size of contents in a configuration. Unit: KB.
        self.config_content_limit = config_content_limit
        # Indicates whether configuration encryption of a configuration center is enabled by the instance. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: enabled.
        # *   `false`: disabled.
        self.config_secret_enabled = config_secret_enabled
        # Indicates whether configuration encryption of a configuration center is supported by the instance. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: supported.
        # *   `false`: not supported.
        self.config_secret_supported = config_secret_supported
        # Indicates whether the Nacos open source console is enabled.
        self.console_uienabled = console_uienabled
        self.enable_4lw = enable_4lw
        # Indicates whether access port 8761 was enabled for Eureka. If this port is disabled, applications cannot use the Eureka protocol for service registration and discovery.
        self.eureka_supported = eureka_supported
        # Indicates whether the time to live (TTL) configuration is enabled. This parameter is valid for ZooKeeper instances.
        self.extended_types_enable = extended_types_enable
        # The maximum connection duration of the instance. Unit: seconds. This parameter is valid for ZooKeeper instances.
        self.init_limit = init_limit
        # The maximum amount of data on each node. This parameter is valid for ZooKeeper instances. Unit: bytes.
        self.jute_maxbuffer = jute_maxbuffer
        # A reserved parameter.
        self.jvm_flags_custom = jvm_flags_custom
        # Indicates whether Mesh Configuration Protocol (MCP) is enabled. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: enabled.
        # *   `false`: disabled.
        self.mcpenabled = mcpenabled
        # Indicates whether MCP is supported. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: supported.
        # *   `false`: not supported.
        self.mcpsupported = mcpsupported
        # The number of connections between a client and a server. This parameter is valid for ZooKeeper instances.\\
        # If this parameter is set to 0, no limits are imposed on the number of connections.
        self.max_client_cnxns = max_client_cnxns
        # The maximum timeout period. This parameter is valid for ZooKeeper instances.
        self.max_session_timeout = max_session_timeout
        # The minimum timeout period. This parameter is valid for ZooKeeper instances.
        self.min_session_timeout = min_session_timeout
        # The runtime configuration of the Nacos instance.
        self.nacos_running_env = nacos_running_env
        # Indicates whether RAM authentication of a registry is enabled. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: enabled.
        # *   `false`: disabled.
        self.naming_auth_enabled = naming_auth_enabled
        # Indicates whether RAM authentication of services is supported by the instance. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: supported.
        # *   `false`: not supported.
        self.naming_auth_supported = naming_auth_supported
        # Indicates whether service creation is supported for the instance. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: supported.
        # *   `false`: not supported.
        self.naming_create_service_supported = naming_create_service_supported
        # Indicates whether super permissions are enabled. This parameter is valid for ZooKeeper instances. Valid values:
        # 
        # *   `true`: enabled.
        # *   `false`: disabled.
        self.open_super_acl = open_super_acl
        # The password that corresponds to the username. This parameter is valid only if OpenSuperAcl is set to true.
        self.pass_word = pass_word
        self.prometheus_sd_protocol_enabled = prometheus_sd_protocol_enabled
        # Indicates whether the instance was restarted and new configurations have taken effect. Valid values:
        # 
        # *   `true`: The restart was successful.
        # *   `false`: The restart failed.
        self.restart_flag = restart_flag
        # The frequency for generating snapshots. This parameter is valid for ZooKeeper instances.
        self.snapshot_count = snapshot_count
        # The connection timeout period of the instance. This parameter is valid for ZooKeeper instances. Unit: seconds.
        self.sync_limit = sync_limit
        # MSE Nacos supports TLS transmission link encryption since version 2.1.2.1. Nacos clients must be upgraded to version 2.2.1 or later. After TLS is enabled, the system performance will decrease by about 10%. You must evaluate the system capacity. For more information about the relevant operations, see Nacos TLS transmission encryption.
        self.tlsenabled = tlsenabled
        # The time unit of the engine. This parameter is valid for ZooKeeper instances. Default value: 2000. Unit: milliseconds.
        self.tick_time = tick_time
        # The username of the user. This parameter is valid only if OpenSuperAcl is set to true.
        self.user_name = user_name

    def validate(self):
        if self.nacos_running_env:
            self.nacos_running_env.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_enabled is not None:
            result['AuthEnabled'] = self.auth_enabled

        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval

        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled

        if self.config_auth_supported is not None:
            result['ConfigAuthSupported'] = self.config_auth_supported

        if self.config_content_limit is not None:
            result['ConfigContentLimit'] = self.config_content_limit

        if self.config_secret_enabled is not None:
            result['ConfigSecretEnabled'] = self.config_secret_enabled

        if self.config_secret_supported is not None:
            result['ConfigSecretSupported'] = self.config_secret_supported

        if self.console_uienabled is not None:
            result['ConsoleUIEnabled'] = self.console_uienabled

        if self.enable_4lw is not None:
            result['Enable4lw'] = self.enable_4lw

        if self.eureka_supported is not None:
            result['EurekaSupported'] = self.eureka_supported

        if self.extended_types_enable is not None:
            result['ExtendedTypesEnable'] = self.extended_types_enable

        if self.init_limit is not None:
            result['InitLimit'] = self.init_limit

        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer

        if self.jvm_flags_custom is not None:
            result['JvmFlagsCustom'] = self.jvm_flags_custom

        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled

        if self.mcpsupported is not None:
            result['MCPSupported'] = self.mcpsupported

        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns

        if self.max_session_timeout is not None:
            result['MaxSessionTimeout'] = self.max_session_timeout

        if self.min_session_timeout is not None:
            result['MinSessionTimeout'] = self.min_session_timeout

        if self.nacos_running_env is not None:
            result['NacosRunningEnv'] = self.nacos_running_env.to_map()

        if self.naming_auth_enabled is not None:
            result['NamingAuthEnabled'] = self.naming_auth_enabled

        if self.naming_auth_supported is not None:
            result['NamingAuthSupported'] = self.naming_auth_supported

        if self.naming_create_service_supported is not None:
            result['NamingCreateServiceSupported'] = self.naming_create_service_supported

        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl

        if self.pass_word is not None:
            result['PassWord'] = self.pass_word

        if self.prometheus_sd_protocol_enabled is not None:
            result['PrometheusSdProtocolEnabled'] = self.prometheus_sd_protocol_enabled

        if self.restart_flag is not None:
            result['RestartFlag'] = self.restart_flag

        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count

        if self.sync_limit is not None:
            result['SyncLimit'] = self.sync_limit

        if self.tlsenabled is not None:
            result['TLSEnabled'] = self.tlsenabled

        if self.tick_time is not None:
            result['TickTime'] = self.tick_time

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthEnabled') is not None:
            self.auth_enabled = m.get('AuthEnabled')

        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')

        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')

        if m.get('ConfigAuthSupported') is not None:
            self.config_auth_supported = m.get('ConfigAuthSupported')

        if m.get('ConfigContentLimit') is not None:
            self.config_content_limit = m.get('ConfigContentLimit')

        if m.get('ConfigSecretEnabled') is not None:
            self.config_secret_enabled = m.get('ConfigSecretEnabled')

        if m.get('ConfigSecretSupported') is not None:
            self.config_secret_supported = m.get('ConfigSecretSupported')

        if m.get('ConsoleUIEnabled') is not None:
            self.console_uienabled = m.get('ConsoleUIEnabled')

        if m.get('Enable4lw') is not None:
            self.enable_4lw = m.get('Enable4lw')

        if m.get('EurekaSupported') is not None:
            self.eureka_supported = m.get('EurekaSupported')

        if m.get('ExtendedTypesEnable') is not None:
            self.extended_types_enable = m.get('ExtendedTypesEnable')

        if m.get('InitLimit') is not None:
            self.init_limit = m.get('InitLimit')

        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')

        if m.get('JvmFlagsCustom') is not None:
            self.jvm_flags_custom = m.get('JvmFlagsCustom')

        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')

        if m.get('MCPSupported') is not None:
            self.mcpsupported = m.get('MCPSupported')

        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')

        if m.get('MaxSessionTimeout') is not None:
            self.max_session_timeout = m.get('MaxSessionTimeout')

        if m.get('MinSessionTimeout') is not None:
            self.min_session_timeout = m.get('MinSessionTimeout')

        if m.get('NacosRunningEnv') is not None:
            temp_model = main_models.QueryConfigResponseBodyDataNacosRunningEnv()
            self.nacos_running_env = temp_model.from_map(m.get('NacosRunningEnv'))

        if m.get('NamingAuthEnabled') is not None:
            self.naming_auth_enabled = m.get('NamingAuthEnabled')

        if m.get('NamingAuthSupported') is not None:
            self.naming_auth_supported = m.get('NamingAuthSupported')

        if m.get('NamingCreateServiceSupported') is not None:
            self.naming_create_service_supported = m.get('NamingCreateServiceSupported')

        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')

        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')

        if m.get('PrometheusSdProtocolEnabled') is not None:
            self.prometheus_sd_protocol_enabled = m.get('PrometheusSdProtocolEnabled')

        if m.get('RestartFlag') is not None:
            self.restart_flag = m.get('RestartFlag')

        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')

        if m.get('SyncLimit') is not None:
            self.sync_limit = m.get('SyncLimit')

        if m.get('TLSEnabled') is not None:
            self.tlsenabled = m.get('TLSEnabled')

        if m.get('TickTime') is not None:
            self.tick_time = m.get('TickTime')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class QueryConfigResponseBodyDataNacosRunningEnv(DaraModel):
    def __init__(
        self,
        empty_protect: bool = None,
        fence_enabled: bool = None,
        fence_policy: main_models.QueryConfigResponseBodyDataNacosRunningEnvFencePolicy = None,
        gray_auth: str = None,
    ):
        # Indicates whether empty list protection is enabled.
        self.empty_protect = empty_protect
        self.fence_enabled = fence_enabled
        self.fence_policy = fence_policy
        self.gray_auth = gray_auth

    def validate(self):
        if self.fence_policy:
            self.fence_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.empty_protect is not None:
            result['emptyProtect'] = self.empty_protect

        if self.fence_enabled is not None:
            result['fenceEnabled'] = self.fence_enabled

        if self.fence_policy is not None:
            result['fencePolicy'] = self.fence_policy.to_map()

        if self.gray_auth is not None:
            result['grayAuth'] = self.gray_auth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('emptyProtect') is not None:
            self.empty_protect = m.get('emptyProtect')

        if m.get('fenceEnabled') is not None:
            self.fence_enabled = m.get('fenceEnabled')

        if m.get('fencePolicy') is not None:
            temp_model = main_models.QueryConfigResponseBodyDataNacosRunningEnvFencePolicy()
            self.fence_policy = temp_model.from_map(m.get('fencePolicy'))

        if m.get('grayAuth') is not None:
            self.gray_auth = m.get('grayAuth')

        return self

class QueryConfigResponseBodyDataNacosRunningEnvFencePolicy(DaraModel):
    def __init__(
        self,
        enabled_modules: List[str] = None,
        intercept_policy: Dict[str, str] = None,
        service_name: str = None,
    ):
        self.enabled_modules = enabled_modules
        self.intercept_policy = intercept_policy
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled_modules is not None:
            result['enabledModules'] = self.enabled_modules

        if self.intercept_policy is not None:
            result['interceptPolicy'] = self.intercept_policy

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabledModules') is not None:
            self.enabled_modules = m.get('enabledModules')

        if m.get('interceptPolicy') is not None:
            self.intercept_policy = m.get('interceptPolicy')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        return self

