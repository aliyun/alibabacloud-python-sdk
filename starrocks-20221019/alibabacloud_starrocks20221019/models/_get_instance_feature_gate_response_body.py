# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class GetInstanceFeatureGateResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: main_models.GetInstanceFeatureGateResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of instances.
        self.total = total

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Data') is not None:
            temp_model = main_models.GetInstanceFeatureGateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetInstanceFeatureGateResponseBodyData(DaraModel):
    def __init__(
        self,
        console_control_restart: bool = None,
        enable_manage_mv: bool = None,
        full_managed_security_group: bool = None,
        mount_dlf_meta_token: bool = None,
        support_add_config_types: List[str] = None,
        support_backup: bool = None,
        support_create_agent: bool = None,
        support_create_non_standard_node_group: bool = None,
        support_eed: bool = None,
        support_enable_ai: bool = None,
        support_enable_ssl: bool = None,
        support_fast_mode_modify_config: bool = None,
        support_fast_mode_modify_resource: bool = None,
        support_fast_restart: bool = None,
        support_fe_gateway: bool = None,
        support_host_alias: bool = None,
        support_modify_timezone: bool = None,
        support_multi_az: bool = None,
        use_compute_node: bool = None,
        support_compaction_service: bool = None,
        support_compaction_service_white_list: bool = None,
    ):
        # Whether the restart process can be controlled from the console.
        self.console_control_restart = console_control_restart
        # Whether materialized views can be managed.
        self.enable_manage_mv = enable_manage_mv
        # Whether managed security groups are supported.
        self.full_managed_security_group = full_managed_security_group
        # Whether DLF meta tokens can be mounted.
        self.mount_dlf_meta_token = mount_dlf_meta_token
        # A list of new configuration types.
        self.support_add_config_types = support_add_config_types
        # Whether data backup is supported.
        # 
        # - **1**: Supports data backup.
        # 
        # - **2**: Does not support data backup.
        self.support_backup = support_backup
        # Whether agents can be created.
        self.support_create_agent = support_create_agent
        # Whether compute groups with specifications other than `standard` can be created.
        self.support_create_non_standard_node_group = support_create_non_standard_node_group
        # Whether elastic ephemeral disks are supported.
        self.support_eed = support_eed
        # Whether the AI function is supported.
        self.support_enable_ai = support_enable_ai
        # Whether SSL can be enabled.
        self.support_enable_ssl = support_enable_ssl
        # Whether fast restart is supported for configuration changes.
        self.support_fast_mode_modify_config = support_fast_mode_modify_config
        # Whether resources can be modified by using fast restart.
        self.support_fast_mode_modify_resource = support_fast_mode_modify_resource
        # Whether fast restart is supported.
        self.support_fast_restart = support_fast_restart
        # Whether the FE gateway is supported.
        self.support_fe_gateway = support_fe_gateway
        # Whether custom domain names are supported.
        self.support_host_alias = support_host_alias
        # Whether the time zone can be modified.
        self.support_modify_timezone = support_modify_timezone
        # Whether observers can be deployed across multiple availability zones (AZs).
        self.support_multi_az = support_multi_az
        # Whether the instance uses compute nodes (CNs).
        self.use_compute_node = use_compute_node
        self.support_compaction_service = support_compaction_service
        # Whether the Compaction Service allowlist feature is supported.
        self.support_compaction_service_white_list = support_compaction_service_white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_control_restart is not None:
            result['ConsoleControlRestart'] = self.console_control_restart

        if self.enable_manage_mv is not None:
            result['EnableManageMv'] = self.enable_manage_mv

        if self.full_managed_security_group is not None:
            result['FullManagedSecurityGroup'] = self.full_managed_security_group

        if self.mount_dlf_meta_token is not None:
            result['MountDlfMetaToken'] = self.mount_dlf_meta_token

        if self.support_add_config_types is not None:
            result['SupportAddConfigTypes'] = self.support_add_config_types

        if self.support_backup is not None:
            result['SupportBackup'] = self.support_backup

        if self.support_create_agent is not None:
            result['SupportCreateAgent'] = self.support_create_agent

        if self.support_create_non_standard_node_group is not None:
            result['SupportCreateNonStandardNodeGroup'] = self.support_create_non_standard_node_group

        if self.support_eed is not None:
            result['SupportEed'] = self.support_eed

        if self.support_enable_ai is not None:
            result['SupportEnableAi'] = self.support_enable_ai

        if self.support_enable_ssl is not None:
            result['SupportEnableSSL'] = self.support_enable_ssl

        if self.support_fast_mode_modify_config is not None:
            result['SupportFastModeModifyConfig'] = self.support_fast_mode_modify_config

        if self.support_fast_mode_modify_resource is not None:
            result['SupportFastModeModifyResource'] = self.support_fast_mode_modify_resource

        if self.support_fast_restart is not None:
            result['SupportFastRestart'] = self.support_fast_restart

        if self.support_fe_gateway is not None:
            result['SupportFeGateway'] = self.support_fe_gateway

        if self.support_host_alias is not None:
            result['SupportHostAlias'] = self.support_host_alias

        if self.support_modify_timezone is not None:
            result['SupportModifyTimezone'] = self.support_modify_timezone

        if self.support_multi_az is not None:
            result['SupportMultiAZ'] = self.support_multi_az

        if self.use_compute_node is not None:
            result['UseComputeNode'] = self.use_compute_node

        if self.support_compaction_service is not None:
            result['supportCompactionService'] = self.support_compaction_service

        if self.support_compaction_service_white_list is not None:
            result['supportCompactionServiceWhiteList'] = self.support_compaction_service_white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleControlRestart') is not None:
            self.console_control_restart = m.get('ConsoleControlRestart')

        if m.get('EnableManageMv') is not None:
            self.enable_manage_mv = m.get('EnableManageMv')

        if m.get('FullManagedSecurityGroup') is not None:
            self.full_managed_security_group = m.get('FullManagedSecurityGroup')

        if m.get('MountDlfMetaToken') is not None:
            self.mount_dlf_meta_token = m.get('MountDlfMetaToken')

        if m.get('SupportAddConfigTypes') is not None:
            self.support_add_config_types = m.get('SupportAddConfigTypes')

        if m.get('SupportBackup') is not None:
            self.support_backup = m.get('SupportBackup')

        if m.get('SupportCreateAgent') is not None:
            self.support_create_agent = m.get('SupportCreateAgent')

        if m.get('SupportCreateNonStandardNodeGroup') is not None:
            self.support_create_non_standard_node_group = m.get('SupportCreateNonStandardNodeGroup')

        if m.get('SupportEed') is not None:
            self.support_eed = m.get('SupportEed')

        if m.get('SupportEnableAi') is not None:
            self.support_enable_ai = m.get('SupportEnableAi')

        if m.get('SupportEnableSSL') is not None:
            self.support_enable_ssl = m.get('SupportEnableSSL')

        if m.get('SupportFastModeModifyConfig') is not None:
            self.support_fast_mode_modify_config = m.get('SupportFastModeModifyConfig')

        if m.get('SupportFastModeModifyResource') is not None:
            self.support_fast_mode_modify_resource = m.get('SupportFastModeModifyResource')

        if m.get('SupportFastRestart') is not None:
            self.support_fast_restart = m.get('SupportFastRestart')

        if m.get('SupportFeGateway') is not None:
            self.support_fe_gateway = m.get('SupportFeGateway')

        if m.get('SupportHostAlias') is not None:
            self.support_host_alias = m.get('SupportHostAlias')

        if m.get('SupportModifyTimezone') is not None:
            self.support_modify_timezone = m.get('SupportModifyTimezone')

        if m.get('SupportMultiAZ') is not None:
            self.support_multi_az = m.get('SupportMultiAZ')

        if m.get('UseComputeNode') is not None:
            self.use_compute_node = m.get('UseComputeNode')

        if m.get('supportCompactionService') is not None:
            self.support_compaction_service = m.get('supportCompactionService')

        if m.get('supportCompactionServiceWhiteList') is not None:
            self.support_compaction_service_white_list = m.get('supportCompactionServiceWhiteList')

        return self

