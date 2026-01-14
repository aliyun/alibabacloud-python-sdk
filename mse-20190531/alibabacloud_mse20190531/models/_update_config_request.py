# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        auth_enabled: bool = None,
        autopurge_purge_interval: str = None,
        autopurge_snap_retain_count: str = None,
        cluster_id: str = None,
        config_auth_enabled: bool = None,
        config_secret_enabled: bool = None,
        config_type: str = None,
        console_uienabled: bool = None,
        enable_4lw: bool = None,
        eureka_supported: bool = None,
        extended_types_enable: str = None,
        init_limit: str = None,
        instance_id: str = None,
        jute_maxbuffer: str = None,
        mcpenabled: bool = None,
        max_client_cnxns: str = None,
        max_session_timeout: str = None,
        min_session_timeout: str = None,
        naming_auth_enabled: bool = None,
        open_super_acl: str = None,
        pass_word: str = None,
        request_pars: str = None,
        snapshot_count: str = None,
        sync_limit: str = None,
        tlsenabled: bool = None,
        tick_time: str = None,
        user_name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        self.auth_enabled = auth_enabled
        # A reserved parameter.
        self.autopurge_purge_interval = autopurge_purge_interval
        # A reserved parameter.
        self.autopurge_snap_retain_count = autopurge_snap_retain_count
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # Specifies whether to enable Resource Access Management (RAM) authentication for a configuration center. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: enabled.
        # *   `false`: disabled.
        # 
        # > Before you configure this parameter, you must call the QueryConfig operation to obtain the ConfigAuthSupported parameter value to check whether the instance supports the RAM authentication feature.
        self.config_auth_enabled = config_auth_enabled
        # Specifies whether to enable configuration encryption for a configuration center. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: enabled.
        # *   `false`: disabled.
        # 
        # > Before you configure this parameter, you must call the QueryConfig operation to obtain the ConfigSecretSupported parameter value to check whether the instance supports configuration encryption.
        self.config_secret_enabled = config_secret_enabled
        # The format of the configuration. Supported formats include TEXT, JSON, XML, and HTML.
        self.config_type = config_type
        self.console_uienabled = console_uienabled
        self.enable_4lw = enable_4lw
        self.eureka_supported = eureka_supported
        # Specifies whether to enable the time to live (TTL) configuration. This parameter is valid for ZooKeeper instances.
        self.extended_types_enable = extended_types_enable
        # The maximum connection duration of the instance. This parameter is valid for ZooKeeper instances. Unit: seconds.
        self.init_limit = init_limit
        # The ID of the instance.
        self.instance_id = instance_id
        # The maximum amount of data on each node. This parameter is valid for ZooKeeper instances. The default maximum data amount on each node is 1 megabyte. Unit: bytes.
        self.jute_maxbuffer = jute_maxbuffer
        # Specifies whether to enable Mesh Configuration Protocol (MCP). This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: enabled.
        # *   `false`: disabled.
        # 
        # > Before you configure this parameter, you must call the QueryConfig operation to obtain the MCPSupported parameter value to check whether the instance supports MCP.
        self.mcpenabled = mcpenabled
        # The number of connections between a client and a server. This parameter is valid for ZooKeeper instances.\\
        # If this parameter is set to 0, no limits are imposed on the number of connections.
        self.max_client_cnxns = max_client_cnxns
        # The maximum timeout period. This parameter is valid for ZooKeeper instances. Unit: seconds.
        self.max_session_timeout = max_session_timeout
        # The minimum timeout period. This parameter is valid for ZooKeeper instances. Unit: seconds.
        self.min_session_timeout = min_session_timeout
        # Specifies whether to enable RAM authentication for a registry. This parameter is valid for Nacos instances. Valid values:
        # 
        # *   `true`: enabled.
        # *   `false`: disabled.
        # 
        # > Before you configure this parameter, you must call the QueryConfig operation to obtain the NamingAuthSupporte parameter value to check whether the instance supports the RAM authentication feature.
        self.naming_auth_enabled = naming_auth_enabled
        # Specifies whether to enable super permissions. This parameter is valid for ZooKeeper instances. Valid values:
        # 
        # *   `true`: enabled
        # *   `false`: disabled
        self.open_super_acl = open_super_acl
        # The password that corresponds to the username.
        # 
        # > You must specify this parameter if OpenSuperAcl is set to true.
        self.pass_word = pass_word
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars
        # The frequency for generating snapshots. This parameter is valid for ZooKeeper instances.
        self.snapshot_count = snapshot_count
        # The connection timeout period of the instance. This parameter is valid for ZooKeeper instances. Unit: seconds.
        self.sync_limit = sync_limit
        self.tlsenabled = tlsenabled
        # The time unit. This parameter is valid for ZooKeeper instances. Default value: 2000. Unit: milliseconds.
        self.tick_time = tick_time
        # The name of the user.
        # 
        # > You must specify this parameter if OpenSuperAcl is set to true.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.auth_enabled is not None:
            result['AuthEnabled'] = self.auth_enabled

        if self.autopurge_purge_interval is not None:
            result['AutopurgePurgeInterval'] = self.autopurge_purge_interval

        if self.autopurge_snap_retain_count is not None:
            result['AutopurgeSnapRetainCount'] = self.autopurge_snap_retain_count

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.config_auth_enabled is not None:
            result['ConfigAuthEnabled'] = self.config_auth_enabled

        if self.config_secret_enabled is not None:
            result['ConfigSecretEnabled'] = self.config_secret_enabled

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.jute_maxbuffer is not None:
            result['JuteMaxbuffer'] = self.jute_maxbuffer

        if self.mcpenabled is not None:
            result['MCPEnabled'] = self.mcpenabled

        if self.max_client_cnxns is not None:
            result['MaxClientCnxns'] = self.max_client_cnxns

        if self.max_session_timeout is not None:
            result['MaxSessionTimeout'] = self.max_session_timeout

        if self.min_session_timeout is not None:
            result['MinSessionTimeout'] = self.min_session_timeout

        if self.naming_auth_enabled is not None:
            result['NamingAuthEnabled'] = self.naming_auth_enabled

        if self.open_super_acl is not None:
            result['OpenSuperAcl'] = self.open_super_acl

        if self.pass_word is not None:
            result['PassWord'] = self.pass_word

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

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
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AuthEnabled') is not None:
            self.auth_enabled = m.get('AuthEnabled')

        if m.get('AutopurgePurgeInterval') is not None:
            self.autopurge_purge_interval = m.get('AutopurgePurgeInterval')

        if m.get('AutopurgeSnapRetainCount') is not None:
            self.autopurge_snap_retain_count = m.get('AutopurgeSnapRetainCount')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigAuthEnabled') is not None:
            self.config_auth_enabled = m.get('ConfigAuthEnabled')

        if m.get('ConfigSecretEnabled') is not None:
            self.config_secret_enabled = m.get('ConfigSecretEnabled')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JuteMaxbuffer') is not None:
            self.jute_maxbuffer = m.get('JuteMaxbuffer')

        if m.get('MCPEnabled') is not None:
            self.mcpenabled = m.get('MCPEnabled')

        if m.get('MaxClientCnxns') is not None:
            self.max_client_cnxns = m.get('MaxClientCnxns')

        if m.get('MaxSessionTimeout') is not None:
            self.max_session_timeout = m.get('MaxSessionTimeout')

        if m.get('MinSessionTimeout') is not None:
            self.min_session_timeout = m.get('MinSessionTimeout')

        if m.get('NamingAuthEnabled') is not None:
            self.naming_auth_enabled = m.get('NamingAuthEnabled')

        if m.get('OpenSuperAcl') is not None:
            self.open_super_acl = m.get('OpenSuperAcl')

        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

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

