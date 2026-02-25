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
        # AccessDeniedDetail
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
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
    ):
        self.console_control_restart = console_control_restart
        self.enable_manage_mv = enable_manage_mv
        self.full_managed_security_group = full_managed_security_group
        self.mount_dlf_meta_token = mount_dlf_meta_token
        self.support_add_config_types = support_add_config_types
        self.support_backup = support_backup
        self.support_create_agent = support_create_agent
        self.support_create_non_standard_node_group = support_create_non_standard_node_group
        self.support_eed = support_eed
        self.support_enable_ai = support_enable_ai
        self.support_enable_ssl = support_enable_ssl
        self.support_fast_mode_modify_config = support_fast_mode_modify_config
        self.support_fast_mode_modify_resource = support_fast_mode_modify_resource
        self.support_fast_restart = support_fast_restart
        self.support_fe_gateway = support_fe_gateway
        self.support_host_alias = support_host_alias
        self.support_modify_timezone = support_modify_timezone
        self.support_multi_az = support_multi_az
        self.use_compute_node = use_compute_node

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

        return self

