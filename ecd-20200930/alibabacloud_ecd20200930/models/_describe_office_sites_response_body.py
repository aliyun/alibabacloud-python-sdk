# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeOfficeSitesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        office_sites: List[main_models.DescribeOfficeSitesResponseBodyOfficeSites] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The token that determines the start point of the next query. If this parameter is empty, all results are returned.
        self.next_token = next_token
        # The office networks.
        self.office_sites = office_sites
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.office_sites:
            for v1 in self.office_sites:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['OfficeSites'] = []
        if self.office_sites is not None:
            for k1 in self.office_sites:
                result['OfficeSites'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.office_sites = []
        if m.get('OfficeSites') is not None:
            for k1 in m.get('OfficeSites'):
                temp_model = main_models.DescribeOfficeSitesResponseBodyOfficeSites()
                self.office_sites.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOfficeSitesResponseBodyOfficeSites(DaraModel):
    def __init__(
        self,
        adconnectors: List[main_models.DescribeOfficeSitesResponseBodyOfficeSitesADConnectors] = None,
        accelerator_id: str = None,
        account_type: str = None,
        ad_hostname: str = None,
        authority_host: str = None,
        backup_dchostname: str = None,
        backup_dns: str = None,
        bandwidth: int = None,
        cen_attach_status: str = None,
        cen_id: str = None,
        cidr_block: str = None,
        client_id: str = None,
        client_secret: str = None,
        cloud_box_office_site: bool = None,
        creation_time: str = None,
        custom_access_point: str = None,
        custom_dns_address: List[str] = None,
        custom_security_group_id: str = None,
        desktop_access_type: str = None,
        desktop_count: int = None,
        desktop_vpc_endpoint: str = None,
        dns_address: List[str] = None,
        dns_user_name: str = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        enable_admin_access: bool = None,
        enable_cross_desktop_access: bool = None,
        enable_internet_access: bool = None,
        enable_service_route: bool = None,
        file_system_ids: List[str] = None,
        is_ldap: bool = None,
        ldap_url: str = None,
        logs: List[main_models.DescribeOfficeSitesResponseBodyOfficeSitesLogs] = None,
        mfa_enabled: bool = None,
        name: str = None,
        need_verify_login_risk: bool = None,
        need_verify_zero_device: bool = None,
        network_package_id: str = None,
        nm_version: str = None,
        office_site_id: str = None,
        office_site_type: str = None,
        ou_name: str = None,
        protocol_type: str = None,
        rds_license_address: str = None,
        rds_license_domain_name: str = None,
        rds_license_status: str = None,
        resource_amounts: List[main_models.DescribeOfficeSitesResponseBodyOfficeSitesResourceAmounts] = None,
        security_protection: str = None,
        sso_enabled: bool = None,
        sso_type: str = None,
        status: str = None,
        sub_dns_address: List[str] = None,
        sub_domain_name: str = None,
        subnet_mode: str = None,
        tenant_id: str = None,
        total_eds_count: int = None,
        total_eds_count_for_group: int = None,
        total_resource_amount: int = None,
        trust_password: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        vpc_type: str = None,
    ):
        # Details of AD connectors.
        self.adconnectors = adconnectors
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        self.account_type = account_type
        # The hostname of the domain controller. The hostname must comply with the hostname naming convention of Windows.
        self.ad_hostname = ad_hostname
        self.authority_host = authority_host
        # The hostname of the secondary domain controller.
        self.backup_dchostname = backup_dchostname
        # The DNS address of the secondary domain controller.
        self.backup_dns = backup_dns
        # The maximum public bandwidth value. Valid values: 0 to 1000.\\
        # If you leave this parameter empty or set this parameter to 0, Internet access is not enabled.
        self.bandwidth = bandwidth
        # The CEN instance status.
        self.cen_attach_status = cen_attach_status
        # The CEN instance ID.
        self.cen_id = cen_id
        # The IPv4 CIDR block of the VPC that the office network uses.
        self.cidr_block = cidr_block
        self.client_id = client_id
        self.client_secret = client_secret
        # Indicates whether the CloudBox-based office network is created.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.cloud_box_office_site = cloud_box_office_site
        # The time when the office network was created.
        self.creation_time = creation_time
        # The custom endpoint of the access gateway.
        self.custom_access_point = custom_access_point
        # The custom DNS addresses.
        self.custom_dns_address = custom_dns_address
        # The ID of the security group.
        self.custom_security_group_id = custom_security_group_id
        # The method that is used to connect cloud computers that reside in the office network from Alibaba Cloud Workspace clients.
        # 
        # >  The VPC connection depends on Alibaba Cloud PrivateLink. You can use Alibaba Cloud PrivateLink for free. When you set this parameter to `VPC` or `Any`, PrivateLink is automatically activated.
        # 
        # Valid values:
        # 
        # *   INTERNET (default): Cloud computers are connected from Alibaba Cloud Workspace clients over the Internet.
        # *   VPC: Cloud computers are connected from Alibaba Cloud Workspace clients over the VPC.
        # *   ANY: Cloud computers are connected from Alibaba Cloud Workspace clients over the Internet or the VPC. When end users connect to cloud computers from Alibaba Cloud Workspace clients, you can choose a connection method based on your business requirements.
        self.desktop_access_type = desktop_access_type
        # The number of cloud computers that are created.
        self.desktop_count = desktop_count
        # The endpoint that is used to connect to cloud computers in the directory over a VPC.
        self.desktop_vpc_endpoint = desktop_vpc_endpoint
        # The DNS addresses for the AD domains.
        self.dns_address = dns_address
        # The username of a Domain Name System (DNS) user.
        self.dns_user_name = dns_user_name
        # The domain name of the enterprise AD.
        self.domain_name = domain_name
        # The password of the domain administrator.
        self.domain_password = domain_password
        # The username of the domain administrator.
        self.domain_user_name = domain_user_name
        # Indicates whether the local administrator permissions are granted to users that are authorized to use cloud computers in the office network.
        # 
        # Valid values:
        # 
        # *   true (default)
        # *   false
        self.enable_admin_access = enable_admin_access
        # Indicates whether the connection between cloud computers in the office network is enabled. After you enable the connection between cloud computers in the office network, cloud computers in the office network can access each other.
        self.enable_cross_desktop_access = enable_cross_desktop_access
        # Indicates whether Internet access is enabled.
        self.enable_internet_access = enable_internet_access
        # Indicates whether route access control is enabled for cloud services.
        self.enable_service_route = enable_service_route
        # An array of File Storage NAS (NAS) file system IDs.
        self.file_system_ids = file_system_ids
        self.is_ldap = is_ldap
        self.ldap_url = ldap_url
        # Details about registration logs.
        self.logs = logs
        # Indicates whether multi-factor authentication (MFA) is enabled.
        self.mfa_enabled = mfa_enabled
        # The name of the office network. The name is unique in a region.
        self.name = name
        # Indicates whether two-factor verification is enabled when an end user logs on to an Alibaba Cloud Workspace client. This parameter is required only for convenience office networks. If two-factor verification is enabled, the system checks whether security risks exist within the logon account when a convenience user logs on to the client. If risks are detected, the system sends a verification code to the email address that is associated with the account. Then, the convenience user can log on to the client only after the user enters the correct verification code.
        self.need_verify_login_risk = need_verify_login_risk
        # Indicates whether the trusted device verification is enabled.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.need_verify_zero_device = need_verify_zero_device
        # The premium bandwidth plan ID.
        self.network_package_id = network_package_id
        # The network version. The new version supports App Streaming.
        # 
        # Valid values:
        # 
        # *   DEFAULT: the old version.
        # *   NM: the new version.
        self.nm_version = nm_version
        # The IDs of the office networks.
        self.office_site_id = office_site_id
        # The account type of the office network.
        # 
        # Valid values:
        # 
        # *   SIMPLE: the convenience account
        # *   AD_CONNECTOR: the enterprise AD account
        self.office_site_type = office_site_type
        # The organizational unit (OU) in the AD domain to which the office network is connected.
        self.ou_name = ou_name
        # The protocol type.
        # 
        # Valid values:
        # 
        # *   HDX
        # *   ASP
        self.protocol_type = protocol_type
        # The IP address of the RDS license.
        self.rds_license_address = rds_license_address
        # The domain name of the RDS license.
        self.rds_license_domain_name = rds_license_domain_name
        # The remote desktop service (RDS) license status.
        self.rds_license_status = rds_license_status
        # The number of resources.
        self.resource_amounts = resource_amounts
        # The security protection setting of the office network.
        # 
        # Valid values:
        # 
        # *   SASE: SASE is configured.
        # *   OFF: No security protection setting is configured.
        self.security_protection = security_protection
        # Indicates whether single sign-on (SSO) is enabled.
        self.sso_enabled = sso_enabled
        # The SSO type.
        # 
        # Valid values:
        # 
        # *   SAML.
        self.sso_type = sso_type
        # The office network status.
        # 
        # Valid values:
        # 
        # *   REGISTERING: The office network is being registered.
        # *   DEREGISTERING: The office network is being deregistered.
        # *   REGISTERED: The office network is registered.
        # *   NEEDCONFIGTRUST: A trust relationship is required for the office network.
        # *   CONFIGTRUSTFAILED: A trust relationship fails to be configured for the office network.
        # *   DEREGISTERED: The office network is deregistered.
        # *   ERROR: One or more configurations of the office network are invalid.
        # *   CONFIGTRUSTING: A trust relationship is being configured for the office network.
        # *   NEEDCONFIGUSER: Users are required for the office network.
        self.status = status
        # The DNS addresses for the AD subdomains.
        self.sub_dns_address = sub_dns_address
        # The username of enterprise AD subdomain.
        self.sub_domain_name = sub_domain_name
        # The subnet mode of the office network.
        # 
        # Valid values:
        # 
        # *   0: disabled.
        # *   1: enabled.
        self.subnet_mode = subnet_mode
        self.tenant_id = tenant_id
        # The total number of cloud computers.
        self.total_eds_count = total_eds_count
        # The number of cloud computers in the cloud computer share.
        self.total_eds_count_for_group = total_eds_count_for_group
        # The number of network interface controllers (NICs).
        self.total_resource_amount = total_resource_amount
        # >  This parameter is unavailable.
        self.trust_password = trust_password
        # An array of VSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
        self.vpc_id = vpc_id
        # The VPC type.
        # 
        # Valid values:
        # 
        # *   Basic
        # *   Customized
        # *   Standard
        self.vpc_type = vpc_type

    def validate(self):
        if self.adconnectors:
            for v1 in self.adconnectors:
                 if v1:
                    v1.validate()
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()
        if self.resource_amounts:
            for v1 in self.resource_amounts:
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

        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname

        if self.authority_host is not None:
            result['AuthorityHost'] = self.authority_host

        if self.backup_dchostname is not None:
            result['BackupDCHostname'] = self.backup_dchostname

        if self.backup_dns is not None:
            result['BackupDns'] = self.backup_dns

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.cen_attach_status is not None:
            result['CenAttachStatus'] = self.cen_attach_status

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.cloud_box_office_site is not None:
            result['CloudBoxOfficeSite'] = self.cloud_box_office_site

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.custom_access_point is not None:
            result['CustomAccessPoint'] = self.custom_access_point

        if self.custom_dns_address is not None:
            result['CustomDnsAddress'] = self.custom_dns_address

        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id

        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type

        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count

        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint

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

        if self.enable_service_route is not None:
            result['EnableServiceRoute'] = self.enable_service_route

        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids

        if self.is_ldap is not None:
            result['IsLdap'] = self.is_ldap

        if self.ldap_url is not None:
            result['LdapUrl'] = self.ldap_url

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

        if self.need_verify_zero_device is not None:
            result['NeedVerifyZeroDevice'] = self.need_verify_zero_device

        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id

        if self.nm_version is not None:
            result['NmVersion'] = self.nm_version

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.ou_name is not None:
            result['OuName'] = self.ou_name

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.rds_license_address is not None:
            result['RdsLicenseAddress'] = self.rds_license_address

        if self.rds_license_domain_name is not None:
            result['RdsLicenseDomainName'] = self.rds_license_domain_name

        if self.rds_license_status is not None:
            result['RdsLicenseStatus'] = self.rds_license_status

        result['ResourceAmounts'] = []
        if self.resource_amounts is not None:
            for k1 in self.resource_amounts:
                result['ResourceAmounts'].append(k1.to_map() if k1 else None)

        if self.security_protection is not None:
            result['SecurityProtection'] = self.security_protection

        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled

        if self.sso_type is not None:
            result['SsoType'] = self.sso_type

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_dns_address is not None:
            result['SubDnsAddress'] = self.sub_dns_address

        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name

        if self.subnet_mode is not None:
            result['SubnetMode'] = self.subnet_mode

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.total_eds_count is not None:
            result['TotalEdsCount'] = self.total_eds_count

        if self.total_eds_count_for_group is not None:
            result['TotalEdsCountForGroup'] = self.total_eds_count_for_group

        if self.total_resource_amount is not None:
            result['TotalResourceAmount'] = self.total_resource_amount

        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k1 in m.get('ADConnectors'):
                temp_model = main_models.DescribeOfficeSitesResponseBodyOfficeSitesADConnectors()
                self.adconnectors.append(temp_model.from_map(k1))

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')

        if m.get('AuthorityHost') is not None:
            self.authority_host = m.get('AuthorityHost')

        if m.get('BackupDCHostname') is not None:
            self.backup_dchostname = m.get('BackupDCHostname')

        if m.get('BackupDns') is not None:
            self.backup_dns = m.get('BackupDns')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CenAttachStatus') is not None:
            self.cen_attach_status = m.get('CenAttachStatus')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('CloudBoxOfficeSite') is not None:
            self.cloud_box_office_site = m.get('CloudBoxOfficeSite')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CustomAccessPoint') is not None:
            self.custom_access_point = m.get('CustomAccessPoint')

        if m.get('CustomDnsAddress') is not None:
            self.custom_dns_address = m.get('CustomDnsAddress')

        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')

        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')

        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')

        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')

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

        if m.get('EnableServiceRoute') is not None:
            self.enable_service_route = m.get('EnableServiceRoute')

        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')

        if m.get('IsLdap') is not None:
            self.is_ldap = m.get('IsLdap')

        if m.get('LdapUrl') is not None:
            self.ldap_url = m.get('LdapUrl')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.DescribeOfficeSitesResponseBodyOfficeSitesLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedVerifyLoginRisk') is not None:
            self.need_verify_login_risk = m.get('NeedVerifyLoginRisk')

        if m.get('NeedVerifyZeroDevice') is not None:
            self.need_verify_zero_device = m.get('NeedVerifyZeroDevice')

        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')

        if m.get('NmVersion') is not None:
            self.nm_version = m.get('NmVersion')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('OuName') is not None:
            self.ou_name = m.get('OuName')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RdsLicenseAddress') is not None:
            self.rds_license_address = m.get('RdsLicenseAddress')

        if m.get('RdsLicenseDomainName') is not None:
            self.rds_license_domain_name = m.get('RdsLicenseDomainName')

        if m.get('RdsLicenseStatus') is not None:
            self.rds_license_status = m.get('RdsLicenseStatus')

        self.resource_amounts = []
        if m.get('ResourceAmounts') is not None:
            for k1 in m.get('ResourceAmounts'):
                temp_model = main_models.DescribeOfficeSitesResponseBodyOfficeSitesResourceAmounts()
                self.resource_amounts.append(temp_model.from_map(k1))

        if m.get('SecurityProtection') is not None:
            self.security_protection = m.get('SecurityProtection')

        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')

        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubDnsAddress') is not None:
            self.sub_dns_address = m.get('SubDnsAddress')

        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')

        if m.get('SubnetMode') is not None:
            self.subnet_mode = m.get('SubnetMode')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TotalEdsCount') is not None:
            self.total_eds_count = m.get('TotalEdsCount')

        if m.get('TotalEdsCountForGroup') is not None:
            self.total_eds_count_for_group = m.get('TotalEdsCountForGroup')

        if m.get('TotalResourceAmount') is not None:
            self.total_resource_amount = m.get('TotalResourceAmount')

        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

class DescribeOfficeSitesResponseBodyOfficeSitesResourceAmounts(DaraModel):
    def __init__(
        self,
        amount: int = None,
        resource_type: str = None,
    ):
        # The number of resources.
        self.amount = amount
        # The resource type.
        # 
        # Valid values:
        # 
        # *   desktop: the cloud computer.
        # *   DesktopGroup: the cloud computer share.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class DescribeOfficeSitesResponseBodyOfficeSitesLogs(DaraModel):
    def __init__(
        self,
        level: str = None,
        message: str = None,
        step: str = None,
        time_stamp: str = None,
    ):
        # The log severity.
        # 
        # Valid values:
        # 
        # *   ERROR
        # *   INFO
        # *   WARN
        self.level = level
        # Details of the log entry.
        self.message = message
        # The step in the log entry.
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

class DescribeOfficeSitesResponseBodyOfficeSitesADConnectors(DaraModel):
    def __init__(
        self,
        adconnector_address: str = None,
        connector_status: str = None,
        network_interface_id: str = None,
        specification: str = None,
        trust_key: str = None,
        v_switch_id: str = None,
    ):
        # The connection address of the AD connector.
        self.adconnector_address = adconnector_address
        # The status of the AD connector.
        # 
        # Valid values:
        # 
        # *   CONNECT_ERROR
        # *   RUNNING
        # *   CONNECTING (You must configure the AD domain in which the AD connector is used.)
        # *   EXPIRED
        # *   CREATING
        self.connector_status = connector_status
        # The ID of an elastic network interface (ENI) to which the AD connector is mounted.
        self.network_interface_id = network_interface_id
        # The AD connector type.
        # 
        # Valid values:
        # 
        # *   1: General
        # *   2: Advanced
        self.specification = specification
        # The trust password that is specified when you configure the AD trust relationship.
        self.trust_key = trust_key
        # The ID of the vSwitch that resides in the network of the AD connector.
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

