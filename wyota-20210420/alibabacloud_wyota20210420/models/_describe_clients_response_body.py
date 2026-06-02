# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wyota20210420 import models as main_models
from darabonba.model import DaraModel

class DescribeClientsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeClientsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeClientsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeClientsResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        alias: str = None,
        area_site: str = None,
        bind_user_count: int = None,
        bind_user_id: str = None,
        build_id: str = None,
        client_type: int = None,
        client_version: str = None,
        current_connect_desktop: str = None,
        current_login_user: str = None,
        custom_res_invalid_reason: str = None,
        custom_resource_id: str = None,
        custom_resource_name: str = None,
        custom_resource_status: bool = None,
        desktop_id: str = None,
        desktop_region_id: str = None,
        device_os: str = None,
        function_support: main_models.DescribeClientsResponseBodyDataFunctionSupport = None,
        hardware_info: main_models.DescribeClientsResponseBodyDataHardwareInfo = None,
        host_os_info: str = None,
        in_manage: bool = None,
        ip_geo_location: str = None,
        ipv_4: str = None,
        last_login_user: str = None,
        local_device_sn: str = None,
        location_info: str = None,
        login_user: str = None,
        main_biz_type: str = None,
        manage_time: str = None,
        manage_timestamp: int = None,
        model: str = None,
        model_preview_url: str = None,
        online: bool = None,
        online_status: bool = None,
        password_free_login_user: str = None,
        platform: str = None,
        product_name: str = None,
        public_ipv_4: str = None,
        set_password_free_login_user_time: str = None,
        terminal_group_id: str = None,
        upgrade_download_type: str = None,
        user_bind_count: int = None,
        uuid: str = None,
        wos_app_version: str = None,
    ):
        # aliUid
        self.ali_uid = ali_uid
        self.alias = alias
        self.area_site = area_site
        self.bind_user_count = bind_user_count
        self.bind_user_id = bind_user_id
        self.build_id = build_id
        self.client_type = client_type
        self.client_version = client_version
        self.current_connect_desktop = current_connect_desktop
        self.current_login_user = current_login_user
        self.custom_res_invalid_reason = custom_res_invalid_reason
        self.custom_resource_id = custom_resource_id
        self.custom_resource_name = custom_resource_name
        self.custom_resource_status = custom_resource_status
        self.desktop_id = desktop_id
        self.desktop_region_id = desktop_region_id
        self.device_os = device_os
        self.function_support = function_support
        self.hardware_info = hardware_info
        self.host_os_info = host_os_info
        self.in_manage = in_manage
        self.ip_geo_location = ip_geo_location
        # ipv4
        self.ipv_4 = ipv_4
        self.last_login_user = last_login_user
        self.local_device_sn = local_device_sn
        self.location_info = location_info
        self.login_user = login_user
        self.main_biz_type = main_biz_type
        self.manage_time = manage_time
        self.manage_timestamp = manage_timestamp
        self.model = model
        self.model_preview_url = model_preview_url
        self.online = online
        self.online_status = online_status
        self.password_free_login_user = password_free_login_user
        self.platform = platform
        # productName
        self.product_name = product_name
        self.public_ipv_4 = public_ipv_4
        self.set_password_free_login_user_time = set_password_free_login_user_time
        self.terminal_group_id = terminal_group_id
        self.upgrade_download_type = upgrade_download_type
        self.user_bind_count = user_bind_count
        # uuid
        self.uuid = uuid
        # appVersion
        self.wos_app_version = wos_app_version

    def validate(self):
        if self.function_support:
            self.function_support.validate()
        if self.hardware_info:
            self.hardware_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.alias is not None:
            result['Alias'] = self.alias

        if self.area_site is not None:
            result['AreaSite'] = self.area_site

        if self.bind_user_count is not None:
            result['BindUserCount'] = self.bind_user_count

        if self.bind_user_id is not None:
            result['BindUserId'] = self.bind_user_id

        if self.build_id is not None:
            result['BuildId'] = self.build_id

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.current_connect_desktop is not None:
            result['CurrentConnectDesktop'] = self.current_connect_desktop

        if self.current_login_user is not None:
            result['CurrentLoginUser'] = self.current_login_user

        if self.custom_res_invalid_reason is not None:
            result['CustomResInvalidReason'] = self.custom_res_invalid_reason

        if self.custom_resource_id is not None:
            result['CustomResourceId'] = self.custom_resource_id

        if self.custom_resource_name is not None:
            result['CustomResourceName'] = self.custom_resource_name

        if self.custom_resource_status is not None:
            result['CustomResourceStatus'] = self.custom_resource_status

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_region_id is not None:
            result['DesktopRegionId'] = self.desktop_region_id

        if self.device_os is not None:
            result['DeviceOs'] = self.device_os

        if self.function_support is not None:
            result['FunctionSupport'] = self.function_support.to_map()

        if self.hardware_info is not None:
            result['HardwareInfo'] = self.hardware_info.to_map()

        if self.host_os_info is not None:
            result['HostOsInfo'] = self.host_os_info

        if self.in_manage is not None:
            result['InManage'] = self.in_manage

        if self.ip_geo_location is not None:
            result['IpGeoLocation'] = self.ip_geo_location

        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4

        if self.last_login_user is not None:
            result['LastLoginUser'] = self.last_login_user

        if self.local_device_sn is not None:
            result['LocalDeviceSn'] = self.local_device_sn

        if self.location_info is not None:
            result['LocationInfo'] = self.location_info

        if self.login_user is not None:
            result['LoginUser'] = self.login_user

        if self.main_biz_type is not None:
            result['MainBizType'] = self.main_biz_type

        if self.manage_time is not None:
            result['ManageTime'] = self.manage_time

        if self.manage_timestamp is not None:
            result['ManageTimestamp'] = self.manage_timestamp

        if self.model is not None:
            result['Model'] = self.model

        if self.model_preview_url is not None:
            result['ModelPreviewUrl'] = self.model_preview_url

        if self.online is not None:
            result['Online'] = self.online

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.password_free_login_user is not None:
            result['PasswordFreeLoginUser'] = self.password_free_login_user

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.public_ipv_4 is not None:
            result['PublicIpv4'] = self.public_ipv_4

        if self.set_password_free_login_user_time is not None:
            result['SetPasswordFreeLoginUserTime'] = self.set_password_free_login_user_time

        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id

        if self.upgrade_download_type is not None:
            result['UpgradeDownloadType'] = self.upgrade_download_type

        if self.user_bind_count is not None:
            result['UserBindCount'] = self.user_bind_count

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.wos_app_version is not None:
            result['WosAppVersion'] = self.wos_app_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('AreaSite') is not None:
            self.area_site = m.get('AreaSite')

        if m.get('BindUserCount') is not None:
            self.bind_user_count = m.get('BindUserCount')

        if m.get('BindUserId') is not None:
            self.bind_user_id = m.get('BindUserId')

        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('CurrentConnectDesktop') is not None:
            self.current_connect_desktop = m.get('CurrentConnectDesktop')

        if m.get('CurrentLoginUser') is not None:
            self.current_login_user = m.get('CurrentLoginUser')

        if m.get('CustomResInvalidReason') is not None:
            self.custom_res_invalid_reason = m.get('CustomResInvalidReason')

        if m.get('CustomResourceId') is not None:
            self.custom_resource_id = m.get('CustomResourceId')

        if m.get('CustomResourceName') is not None:
            self.custom_resource_name = m.get('CustomResourceName')

        if m.get('CustomResourceStatus') is not None:
            self.custom_resource_status = m.get('CustomResourceStatus')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopRegionId') is not None:
            self.desktop_region_id = m.get('DesktopRegionId')

        if m.get('DeviceOs') is not None:
            self.device_os = m.get('DeviceOs')

        if m.get('FunctionSupport') is not None:
            temp_model = main_models.DescribeClientsResponseBodyDataFunctionSupport()
            self.function_support = temp_model.from_map(m.get('FunctionSupport'))

        if m.get('HardwareInfo') is not None:
            temp_model = main_models.DescribeClientsResponseBodyDataHardwareInfo()
            self.hardware_info = temp_model.from_map(m.get('HardwareInfo'))

        if m.get('HostOsInfo') is not None:
            self.host_os_info = m.get('HostOsInfo')

        if m.get('InManage') is not None:
            self.in_manage = m.get('InManage')

        if m.get('IpGeoLocation') is not None:
            self.ip_geo_location = m.get('IpGeoLocation')

        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')

        if m.get('LastLoginUser') is not None:
            self.last_login_user = m.get('LastLoginUser')

        if m.get('LocalDeviceSn') is not None:
            self.local_device_sn = m.get('LocalDeviceSn')

        if m.get('LocationInfo') is not None:
            self.location_info = m.get('LocationInfo')

        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')

        if m.get('MainBizType') is not None:
            self.main_biz_type = m.get('MainBizType')

        if m.get('ManageTime') is not None:
            self.manage_time = m.get('ManageTime')

        if m.get('ManageTimestamp') is not None:
            self.manage_timestamp = m.get('ManageTimestamp')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelPreviewUrl') is not None:
            self.model_preview_url = m.get('ModelPreviewUrl')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('PasswordFreeLoginUser') is not None:
            self.password_free_login_user = m.get('PasswordFreeLoginUser')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('PublicIpv4') is not None:
            self.public_ipv_4 = m.get('PublicIpv4')

        if m.get('SetPasswordFreeLoginUserTime') is not None:
            self.set_password_free_login_user_time = m.get('SetPasswordFreeLoginUserTime')

        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')

        if m.get('UpgradeDownloadType') is not None:
            self.upgrade_download_type = m.get('UpgradeDownloadType')

        if m.get('UserBindCount') is not None:
            self.user_bind_count = m.get('UserBindCount')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('WosAppVersion') is not None:
            self.wos_app_version = m.get('WosAppVersion')

        return self

class DescribeClientsResponseBodyDataHardwareInfo(DaraModel):
    def __init__(
        self,
        bluetooth: str = None,
        chip_id: str = None,
        cpu: str = None,
        mac: str = None,
        memory: str = None,
        storage: str = None,
        wlan: str = None,
    ):
        self.bluetooth = bluetooth
        # chipId
        self.chip_id = chip_id
        self.cpu = cpu
        self.mac = mac
        self.memory = memory
        self.storage = storage
        # wifi mac
        self.wlan = wlan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bluetooth is not None:
            result['Bluetooth'] = self.bluetooth

        if self.chip_id is not None:
            result['ChipId'] = self.chip_id

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.wlan is not None:
            result['Wlan'] = self.wlan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bluetooth') is not None:
            self.bluetooth = m.get('Bluetooth')

        if m.get('ChipId') is not None:
            self.chip_id = m.get('ChipId')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('Wlan') is not None:
            self.wlan = m.get('Wlan')

        return self

class DescribeClientsResponseBodyDataFunctionSupport(DaraModel):
    def __init__(
        self,
        enable_policy: bool = None,
        password_free_login_forbidden_reason: str = None,
        support_assist_login: bool = None,
        support_diagnose: bool = None,
        support_limit_login_user: bool = None,
        support_local_device_sn: bool = None,
        support_manage: bool = None,
        support_modify_policy: bool = None,
        support_password_free_login: bool = None,
        support_reboot: bool = None,
        support_reset: bool = None,
        support_reset_pin: bool = None,
        support_stop: bool = None,
        support_upgrade: bool = None,
        unsupport_assist_login_reason: str = None,
        unsupport_manage_reason: str = None,
        unsupported_local_device_sn_reason: str = None,
        version_supported: bool = None,
        version_too_low: bool = None,
    ):
        self.enable_policy = enable_policy
        self.password_free_login_forbidden_reason = password_free_login_forbidden_reason
        self.support_assist_login = support_assist_login
        self.support_diagnose = support_diagnose
        self.support_limit_login_user = support_limit_login_user
        self.support_local_device_sn = support_local_device_sn
        self.support_manage = support_manage
        self.support_modify_policy = support_modify_policy
        self.support_password_free_login = support_password_free_login
        self.support_reboot = support_reboot
        self.support_reset = support_reset
        self.support_reset_pin = support_reset_pin
        self.support_stop = support_stop
        self.support_upgrade = support_upgrade
        self.unsupport_assist_login_reason = unsupport_assist_login_reason
        self.unsupport_manage_reason = unsupport_manage_reason
        self.unsupported_local_device_sn_reason = unsupported_local_device_sn_reason
        self.version_supported = version_supported
        self.version_too_low = version_too_low

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_policy is not None:
            result['EnablePolicy'] = self.enable_policy

        if self.password_free_login_forbidden_reason is not None:
            result['PasswordFreeLoginForbiddenReason'] = self.password_free_login_forbidden_reason

        if self.support_assist_login is not None:
            result['SupportAssistLogin'] = self.support_assist_login

        if self.support_diagnose is not None:
            result['SupportDiagnose'] = self.support_diagnose

        if self.support_limit_login_user is not None:
            result['SupportLimitLoginUser'] = self.support_limit_login_user

        if self.support_local_device_sn is not None:
            result['SupportLocalDeviceSn'] = self.support_local_device_sn

        if self.support_manage is not None:
            result['SupportManage'] = self.support_manage

        if self.support_modify_policy is not None:
            result['SupportModifyPolicy'] = self.support_modify_policy

        if self.support_password_free_login is not None:
            result['SupportPasswordFreeLogin'] = self.support_password_free_login

        if self.support_reboot is not None:
            result['SupportReboot'] = self.support_reboot

        if self.support_reset is not None:
            result['SupportReset'] = self.support_reset

        if self.support_reset_pin is not None:
            result['SupportResetPin'] = self.support_reset_pin

        if self.support_stop is not None:
            result['SupportStop'] = self.support_stop

        if self.support_upgrade is not None:
            result['SupportUpgrade'] = self.support_upgrade

        if self.unsupport_assist_login_reason is not None:
            result['UnsupportAssistLoginReason'] = self.unsupport_assist_login_reason

        if self.unsupport_manage_reason is not None:
            result['UnsupportManageReason'] = self.unsupport_manage_reason

        if self.unsupported_local_device_sn_reason is not None:
            result['UnsupportedLocalDeviceSnReason'] = self.unsupported_local_device_sn_reason

        if self.version_supported is not None:
            result['VersionSupported'] = self.version_supported

        if self.version_too_low is not None:
            result['VersionTooLow'] = self.version_too_low

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePolicy') is not None:
            self.enable_policy = m.get('EnablePolicy')

        if m.get('PasswordFreeLoginForbiddenReason') is not None:
            self.password_free_login_forbidden_reason = m.get('PasswordFreeLoginForbiddenReason')

        if m.get('SupportAssistLogin') is not None:
            self.support_assist_login = m.get('SupportAssistLogin')

        if m.get('SupportDiagnose') is not None:
            self.support_diagnose = m.get('SupportDiagnose')

        if m.get('SupportLimitLoginUser') is not None:
            self.support_limit_login_user = m.get('SupportLimitLoginUser')

        if m.get('SupportLocalDeviceSn') is not None:
            self.support_local_device_sn = m.get('SupportLocalDeviceSn')

        if m.get('SupportManage') is not None:
            self.support_manage = m.get('SupportManage')

        if m.get('SupportModifyPolicy') is not None:
            self.support_modify_policy = m.get('SupportModifyPolicy')

        if m.get('SupportPasswordFreeLogin') is not None:
            self.support_password_free_login = m.get('SupportPasswordFreeLogin')

        if m.get('SupportReboot') is not None:
            self.support_reboot = m.get('SupportReboot')

        if m.get('SupportReset') is not None:
            self.support_reset = m.get('SupportReset')

        if m.get('SupportResetPin') is not None:
            self.support_reset_pin = m.get('SupportResetPin')

        if m.get('SupportStop') is not None:
            self.support_stop = m.get('SupportStop')

        if m.get('SupportUpgrade') is not None:
            self.support_upgrade = m.get('SupportUpgrade')

        if m.get('UnsupportAssistLoginReason') is not None:
            self.unsupport_assist_login_reason = m.get('UnsupportAssistLoginReason')

        if m.get('UnsupportManageReason') is not None:
            self.unsupport_manage_reason = m.get('UnsupportManageReason')

        if m.get('UnsupportedLocalDeviceSnReason') is not None:
            self.unsupported_local_device_sn_reason = m.get('UnsupportedLocalDeviceSnReason')

        if m.get('VersionSupported') is not None:
            self.version_supported = m.get('VersionSupported')

        if m.get('VersionTooLow') is not None:
            self.version_too_low = m.get('VersionTooLow')

        return self

