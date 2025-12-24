# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        ad_hostname: str = None,
        directories: List[main_models.DescribeDirectoriesResponseBodyDirectories] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The hostname of the domain controller. The hostname must comply with the hostname naming convention of Windows. This parameter is returned only when the directory type is AD office network.
        self.ad_hostname = ad_hostname
        # The directories.
        self.directories = directories
        # The token that is used for the next query. If this parameter is empty, all results are returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.directories:
            for v1 in self.directories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname

        result['Directories'] = []
        if self.directories is not None:
            for k1 in self.directories:
                result['Directories'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')

        self.directories = []
        if m.get('Directories') is not None:
            for k1 in m.get('Directories'):
                temp_model = main_models.DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDirectoriesResponseBodyDirectories(DaraModel):
    def __init__(
        self,
        adconnectors: List[main_models.DescribeDirectoriesResponseBodyDirectoriesADConnectors] = None,
        ad_hostname: str = None,
        backup_dchostname: str = None,
        backup_dns: str = None,
        creation_time: str = None,
        custom_security_group_id: str = None,
        desktop_access_type: str = None,
        desktop_vpc_endpoint: str = None,
        directory_id: str = None,
        directory_type: str = None,
        dns_address: List[str] = None,
        dns_user_name: str = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        enable_admin_access: bool = None,
        enable_cross_desktop_access: bool = None,
        enable_internet_access: bool = None,
        file_system_ids: List[str] = None,
        logs: List[main_models.DescribeDirectoriesResponseBodyDirectoriesLogs] = None,
        mfa_enabled: bool = None,
        name: str = None,
        need_verify_login_risk: bool = None,
        ou_name: str = None,
        sso_enabled: bool = None,
        status: str = None,
        sub_dns_address: List[str] = None,
        sub_domain_name: str = None,
        trust_password: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # Details of the AD connector.
        self.adconnectors = adconnectors
        # The hostname of the domain controller.
        self.ad_hostname = ad_hostname
        # The hostname of the backup domain controller.
        self.backup_dchostname = backup_dchostname
        # The DNS address of the backup domain controller.
        self.backup_dns = backup_dns
        # The time when the directory was created.
        self.creation_time = creation_time
        # The security group ID. This parameter is returned only when the directory type is AD office network.
        self.custom_security_group_id = custom_security_group_id
        # The method in which the cloud computer is connected.
        # 
        # Valid values:
        # 
        # *   VPC
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Internet
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Any
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.desktop_access_type = desktop_access_type
        # The endpoint that is used to connect to cloud computers in the directory over a VPC.
        self.desktop_vpc_endpoint = desktop_vpc_endpoint
        # The directory ID.
        self.directory_id = directory_id
        # The directory type.
        # 
        # Valid values:
        # 
        # *   AD_CONNECTOR: AD directory
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   RAM: RAM directory
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.directory_type = directory_type
        # The DNS address of the directory.
        self.dns_address = dns_address
        # The username of a DNS user.
        self.dns_user_name = dns_user_name
        # The domain name.
        self.domain_name = domain_name
        # The password of the domain administrator. This parameter is returned only when the directory type is AD office network.
        self.domain_password = domain_password
        # The username of the domain administrator.
        self.domain_user_name = domain_user_name
        # Indicates whether the local administrator permissions are granted to users that use cloud computers in the office network.
        self.enable_admin_access = enable_admin_access
        # Indicates whether cloud computers can communicate with each other in the directory.
        self.enable_cross_desktop_access = enable_cross_desktop_access
        # Indicates whether access over the Internet is enabled.
        # 
        # >  This parameter is unavailable.
        self.enable_internet_access = enable_internet_access
        # The IDs of File Storage NAS (NAS) file systems.
        self.file_system_ids = file_system_ids
        # The registration logs. This parameter is returned only when the directory type is AD office network.
        self.logs = logs
        # Indicates whether MFA is enabled.
        self.mfa_enabled = mfa_enabled
        # The directory name.
        self.name = name
        # Indicates whether two-step verification for logons is enabled. This parameter is returned only for directories of convenience account type.\\
        # If two-factor verification is enabled, the system checks whether security risks exist within the logon account when a convenience user logs on to an Alibaba Cloud Workspace client. If risks are detected, the system sends a verification code to the email address that is associated with the account. Then, the convenience user can log on to the client only after the user enters the correct verification code.
        self.need_verify_login_risk = need_verify_login_risk
        # The organization unit that you selected when you added the cloud computer to the domain.
        self.ou_name = ou_name
        # Indicates whether single sign-on (SSO) is enabled.
        self.sso_enabled = sso_enabled
        # The status of the AD directory.
        # 
        # Valid values:
        # 
        # *   REGISTERING
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   REGISTERED
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The DNS address of the enterprise AD subdomain.
        self.sub_dns_address = sub_dns_address
        # The fully qualified domain name (FQDN) of the existing AD subdomain. The value contains both the host name and the domain name.
        self.sub_domain_name = sub_domain_name
        # The AD trust password. This parameter is returned only when the directory type is AD office network.
        self.trust_password = trust_password
        # The IDs of the vSwitches specified when the directory was created.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC to which the vSwitch belongs. This parameter is returned only when the directory type is AD office network.
        self.vpc_id = vpc_id

    def validate(self):
        if self.adconnectors:
            for v1 in self.adconnectors:
                 if v1:
                    v1.validate()
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k1 in self.adconnectors:
                result['ADConnectors'].append(k1.to_map() if k1 else None)

        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname

        if self.backup_dchostname is not None:
            result['BackupDCHostname'] = self.backup_dchostname

        if self.backup_dns is not None:
            result['BackupDns'] = self.backup_dns

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id

        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type

        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type

        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address

        if self.dns_user_name is not None:
            result['DnsUserName'] = self.dns_user_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password

        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name

        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access

        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access

        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access

        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled

        if self.name is not None:
            result['Name'] = self.name

        if self.need_verify_login_risk is not None:
            result['NeedVerifyLoginRisk'] = self.need_verify_login_risk

        if self.ou_name is not None:
            result['OuName'] = self.ou_name

        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_dns_address is not None:
            result['SubDnsAddress'] = self.sub_dns_address

        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name

        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k1 in m.get('ADConnectors'):
                temp_model = main_models.DescribeDirectoriesResponseBodyDirectoriesADConnectors()
                self.adconnectors.append(temp_model.from_map(k1))

        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')

        if m.get('BackupDCHostname') is not None:
            self.backup_dchostname = m.get('BackupDCHostname')

        if m.get('BackupDns') is not None:
            self.backup_dns = m.get('BackupDns')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')

        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')

        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')

        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')

        if m.get('DnsUserName') is not None:
            self.dns_user_name = m.get('DnsUserName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')

        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')

        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')

        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')

        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')

        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribeDirectoriesResponseBodyDirectoriesLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedVerifyLoginRisk') is not None:
            self.need_verify_login_risk = m.get('NeedVerifyLoginRisk')

        if m.get('OuName') is not None:
            self.ou_name = m.get('OuName')

        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubDnsAddress') is not None:
            self.sub_dns_address = m.get('SubDnsAddress')

        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')

        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeDirectoriesResponseBodyDirectoriesLogs(DaraModel):
    def __init__(
        self,
        level: str = None,
        message: str = None,
        step: str = None,
        time_stamp: str = None,
    ):
        # The level of the log entry.
        # 
        # Valid values:
        # 
        # *   ERROR
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   INFO
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   WARN
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.level = level
        # Details of the log entry.
        self.message = message
        # The step that corresponds to the log entry.
        self.step = step
        # The time when the log entry was printed.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.message is not None:
            result['Message'] = self.message

        if self.step is not None:
            result['Step'] = self.step

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

class DescribeDirectoriesResponseBodyDirectoriesADConnectors(DaraModel):
    def __init__(
        self,
        adconnector_address: str = None,
        connector_status: str = None,
        network_interface_id: str = None,
        specification: str = None,
        trust_key: str = None,
        v_switch_id: str = None,
    ):
        # The connection address.
        self.adconnector_address = adconnector_address
        # Valid values:
        # 
        # *   CONNECT_ERROR
        # *   RUNNING
        # *   CONNECTING: You must configure domain trust for your AD system.
        # *   EXPIRED
        # *   CREATING
        self.connector_status = connector_status
        # The ID of the NIC to which the AD connector is mounted.
        self.network_interface_id = network_interface_id
        # The AD connector type.
        # 
        # Valid values:
        # 
        # *   1: General
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   2: Advanced
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.specification = specification
        # The trust password of the AD domain controller.
        self.trust_key = trust_key
        # The ID of the vSwitch with which the AD connector is associated.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adconnector_address is not None:
            result['ADConnectorAddress'] = self.adconnector_address

        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.trust_key is not None:
            result['TrustKey'] = self.trust_key

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ADConnectorAddress') is not None:
            self.adconnector_address = m.get('ADConnectorAddress')

        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('TrustKey') is not None:
            self.trust_key = m.get('TrustKey')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

