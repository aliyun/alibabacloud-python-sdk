# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddUserToDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
        client_token: str = None,
        end_user_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id
        self.client_token = client_token
        self.end_user_ids = end_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class AddUserToDesktopGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserToDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUserToDesktopGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserToDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToSecurityCenterWhiteListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddUserToSecurityCenterWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddUserToSecurityCenterWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUserToSecurityCenterWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserToSecurityCenterWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachCenRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cen_id: str = None,
        office_site_id: str = None,
    ):
        self.region_id = region_id
        self.cen_id = cen_id
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class AttachCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUserInSecurityCenterWhiteListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckUserInSecurityCenterWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        in_white_list: bool = None,
        request_id: str = None,
    ):
        self.in_white_list = in_white_list
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_white_list is not None:
            result['InWhiteList'] = self.in_white_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InWhiteList') is not None:
            self.in_white_list = m.get('InWhiteList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckUserInSecurityCenterWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckUserInSecurityCenterWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckUserInSecurityCenterWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClonePolicyGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        policy_group_id: str = None,
        name: str = None,
    ):
        self.region_id = region_id
        self.policy_group_id = policy_group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ClonePolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        policy_group_id: str = None,
        request_id: str = None,
    ):
        self.policy_group_id = policy_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ClonePolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClonePolicyGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ClonePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateADConnectorDirectoryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        domain_name: str = None,
        domain_user_name: str = None,
        domain_password: str = None,
        directory_name: str = None,
        enable_admin_access: bool = None,
        desktop_access_type: str = None,
        sub_domain_name: str = None,
        mfa_enabled: bool = None,
        dns_address: List[str] = None,
        v_switch_id: List[str] = None,
        sub_domain_dns_address: List[str] = None,
    ):
        self.region_id = region_id
        self.domain_name = domain_name
        self.domain_user_name = domain_user_name
        self.domain_password = domain_password
        self.directory_name = directory_name
        self.enable_admin_access = enable_admin_access
        self.desktop_access_type = desktop_access_type
        self.sub_domain_name = sub_domain_name
        self.mfa_enabled = mfa_enabled
        self.dns_address = dns_address
        self.v_switch_id = v_switch_id
        self.sub_domain_dns_address = sub_domain_dns_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        return self


class CreateADConnectorDirectoryResponseBodyAdConnectors(TeaModel):
    def __init__(
        self,
        address: str = None,
    ):
        self.address = address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class CreateADConnectorDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        trust_password: str = None,
        request_id: str = None,
        directory_id: str = None,
        ad_connectors: List[CreateADConnectorDirectoryResponseBodyAdConnectors] = None,
    ):
        self.trust_password = trust_password
        self.request_id = request_id
        self.directory_id = directory_id
        self.ad_connectors = ad_connectors

    def validate(self):
        if self.ad_connectors:
            for k in self.ad_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        result['AdConnectors'] = []
        if self.ad_connectors is not None:
            for k in self.ad_connectors:
                result['AdConnectors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        self.ad_connectors = []
        if m.get('AdConnectors') is not None:
            for k in m.get('AdConnectors'):
                temp_model = CreateADConnectorDirectoryResponseBodyAdConnectors()
                self.ad_connectors.append(temp_model.from_map(k))
        return self


class CreateADConnectorDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateADConnectorDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateADConnectorDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateADConnectorOfficeSiteRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cidr_block: str = None,
        cen_id: str = None,
        bandwidth: int = None,
        domain_name: str = None,
        domain_user_name: str = None,
        domain_password: str = None,
        office_site_name: str = None,
        enable_admin_access: bool = None,
        desktop_access_type: str = None,
        enable_internet_access: bool = None,
        sub_domain_name: str = None,
        mfa_enabled: bool = None,
        dns_address: List[str] = None,
        sub_domain_dns_address: List[str] = None,
    ):
        self.region_id = region_id
        self.cidr_block = cidr_block
        self.cen_id = cen_id
        self.bandwidth = bandwidth
        self.domain_name = domain_name
        self.domain_user_name = domain_user_name
        self.domain_password = domain_password
        self.office_site_name = office_site_name
        self.enable_admin_access = enable_admin_access
        self.desktop_access_type = desktop_access_type
        self.enable_internet_access = enable_internet_access
        self.sub_domain_name = sub_domain_name
        self.mfa_enabled = mfa_enabled
        self.dns_address = dns_address
        self.sub_domain_dns_address = sub_domain_dns_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        return self


class CreateADConnectorOfficeSiteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        office_site_id: str = None,
    ):
        self.request_id = request_id
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class CreateADConnectorOfficeSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateADConnectorOfficeSiteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateADConnectorOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBundleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        image_id: str = None,
        desktop_type: str = None,
        root_disk_size_gib: int = None,
        bundle_name: str = None,
        description: str = None,
        user_disk_size_gib: List[int] = None,
    ):
        self.region_id = region_id
        self.image_id = image_id
        self.desktop_type = desktop_type
        self.root_disk_size_gib = root_disk_size_gib
        self.bundle_name = bundle_name
        self.description = description
        self.user_disk_size_gib = user_disk_size_gib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        if self.description is not None:
            result['Description'] = self.description
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        return self


class CreateBundleResponseBody(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        request_id: str = None,
    ):
        self.bundle_id = bundle_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBundleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBundleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        bundle_id: str = None,
        office_site_id: str = None,
        policy_group_id: str = None,
        desktop_group_name: str = None,
        directory_id: str = None,
        scale_strategy_id: str = None,
        vpc_id: str = None,
        default_init_desktop_count: int = None,
        keep_duration: int = None,
        charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        own_type: int = None,
        auto_pay: bool = None,
        comments: str = None,
        min_desktops_count: int = None,
        max_desktops_count: int = None,
        allow_auto_setup: int = None,
        allow_buffer_count: int = None,
        client_token: str = None,
        end_user_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.bundle_id = bundle_id
        self.office_site_id = office_site_id
        self.policy_group_id = policy_group_id
        self.desktop_group_name = desktop_group_name
        self.directory_id = directory_id
        self.scale_strategy_id = scale_strategy_id
        self.vpc_id = vpc_id
        self.default_init_desktop_count = default_init_desktop_count
        self.keep_duration = keep_duration
        self.charge_type = charge_type
        self.period = period
        self.period_unit = period_unit
        self.own_type = own_type
        self.auto_pay = auto_pay
        self.comments = comments
        self.min_desktops_count = min_desktops_count
        self.max_desktops_count = max_desktops_count
        self.allow_auto_setup = allow_auto_setup
        self.allow_buffer_count = allow_buffer_count
        self.client_token = client_token
        self.end_user_ids = end_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.default_init_desktop_count is not None:
            result['DefaultInitDesktopCount'] = self.default_init_desktop_count
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup
        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('DefaultInitDesktopCount') is not None:
            self.default_init_desktop_count = m.get('DefaultInitDesktopCount')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')
        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class CreateDesktopGroupResponseBody(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        request_id: str = None,
        order_ids: List[str] = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.request_id = request_id
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDesktopGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDesktopsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        group_id: str = None,
        bundle_id: str = None,
        desktop_name: str = None,
        user_name: str = None,
        vpc_id: str = None,
        amount: int = None,
        directory_id: str = None,
        office_site_id: str = None,
        policy_group_id: str = None,
        charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        promotion_id: str = None,
        user_assign_mode: str = None,
        end_user_id: List[str] = None,
        tag: List[CreateDesktopsRequestTag] = None,
    ):
        self.region_id = region_id
        self.group_id = group_id
        self.bundle_id = bundle_id
        self.desktop_name = desktop_name
        self.user_name = user_name
        self.vpc_id = vpc_id
        self.amount = amount
        self.directory_id = directory_id
        self.office_site_id = office_site_id
        self.policy_group_id = policy_group_id
        self.charge_type = charge_type
        self.period = period
        self.period_unit = period_unit
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.promotion_id = promotion_id
        self.user_assign_mode = user_assign_mode
        self.end_user_id = end_user_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.user_assign_mode is not None:
            result['UserAssignMode'] = self.user_assign_mode
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('UserAssignMode') is not None:
            self.user_assign_mode = m.get('UserAssignMode')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDesktopsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.order_id = order_id
        self.request_id = request_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class CreateDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDesktopsLiteRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        bundle_id: str = None,
        user_assign_mode: str = None,
        amount: int = None,
        enable_internet_access: bool = None,
        bandwidth: int = None,
        period_unit: str = None,
        period: int = None,
        end_user_id: List[str] = None,
    ):
        self.region_id = region_id
        self.bundle_id = bundle_id
        self.user_assign_mode = user_assign_mode
        self.amount = amount
        self.enable_internet_access = enable_internet_access
        self.bandwidth = bandwidth
        self.period_unit = period_unit
        self.period = period
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.user_assign_mode is not None:
            result['UserAssignMode'] = self.user_assign_mode
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('UserAssignMode') is not None:
            self.user_assign_mode = m.get('UserAssignMode')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class CreateDesktopsLiteResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.order_id = order_id
        self.request_id = request_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class CreateDesktopsLiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDesktopsLiteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDesktopsLiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: str = None,
        image_name: str = None,
        description: str = None,
        snapshot_id: str = None,
        image_resource_type: str = None,
        snapshot_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id
        self.image_name = image_name
        self.description = description
        self.snapshot_id = snapshot_id
        self.image_resource_type = image_resource_type
        self.snapshot_ids = snapshot_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.image_resource_type is not None:
            result['ImageResourceType'] = self.image_resource_type
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('ImageResourceType') is not None:
            self.image_resource_type = m.get('ImageResourceType')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        return self


class CreateImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        self.image_id = image_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNASFileSystemRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: str = None,
        name: str = None,
        description: str = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateNASFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_name: str = None,
        mount_target_domain: str = None,
        request_id: str = None,
        office_site_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.file_system_name = file_system_name
        self.mount_target_domain = mount_target_domain
        self.request_id = request_id
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class CreateNASFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNASFileSystemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNASFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkPackageRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        bandwidth: int = None,
        office_site_id: str = None,
        internet_charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
    ):
        self.region_id = region_id
        self.bandwidth = bandwidth
        self.office_site_id = office_site_id
        self.internet_charge_type = internet_charge_type
        self.period = period
        self.period_unit = period_unit
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        return self


class CreateNetworkPackageResponseBody(TeaModel):
    def __init__(
        self,
        network_package_id: str = None,
        request_id: str = None,
        order_id: str = None,
    ):
        self.network_package_id = network_package_id
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateNetworkPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNetworkPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateNetworkPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyGroupRequestAuthorizeSecurityPolicyRule(TeaModel):
    def __init__(
        self,
        type: str = None,
        policy: str = None,
        port_range: str = None,
        description: str = None,
        ip_protocol: str = None,
        priority: str = None,
        cidr_ip: str = None,
    ):
        self.type = type
        self.policy = policy
        self.port_range = port_range
        self.description = description
        self.ip_protocol = ip_protocol
        self.priority = priority
        self.cidr_ip = cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class CreatePolicyGroupRequestAuthorizeAccessPolicyRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        cidr_ip: str = None,
    ):
        self.description = description
        self.cidr_ip = cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class CreatePolicyGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        clipboard: str = None,
        local_drive: str = None,
        usb_redirect: str = None,
        visual_quality: str = None,
        html_5access: str = None,
        html_5file_transfer: str = None,
        watermark: str = None,
        name: str = None,
        watermark_type: str = None,
        watermark_custom_text: str = None,
        watermark_transparency: str = None,
        preempt_login: str = None,
        domain_list: str = None,
        preempt_login_user: List[str] = None,
        authorize_security_policy_rule: List[CreatePolicyGroupRequestAuthorizeSecurityPolicyRule] = None,
        authorize_access_policy_rule: List[CreatePolicyGroupRequestAuthorizeAccessPolicyRule] = None,
    ):
        self.region_id = region_id
        self.clipboard = clipboard
        self.local_drive = local_drive
        self.usb_redirect = usb_redirect
        self.visual_quality = visual_quality
        self.html_5access = html_5access
        self.html_5file_transfer = html_5file_transfer
        self.watermark = watermark
        self.name = name
        self.watermark_type = watermark_type
        self.watermark_custom_text = watermark_custom_text
        self.watermark_transparency = watermark_transparency
        self.preempt_login = preempt_login
        self.domain_list = domain_list
        self.preempt_login_user = preempt_login_user
        self.authorize_security_policy_rule = authorize_security_policy_rule
        self.authorize_access_policy_rule = authorize_access_policy_rule

    def validate(self):
        if self.authorize_security_policy_rule:
            for k in self.authorize_security_policy_rule:
                if k:
                    k.validate()
        if self.authorize_access_policy_rule:
            for k in self.authorize_access_policy_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality
        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.preempt_login_user is not None:
            result['PreemptLoginUser'] = self.preempt_login_user
        result['AuthorizeSecurityPolicyRule'] = []
        if self.authorize_security_policy_rule is not None:
            for k in self.authorize_security_policy_rule:
                result['AuthorizeSecurityPolicyRule'].append(k.to_map() if k else None)
        result['AuthorizeAccessPolicyRule'] = []
        if self.authorize_access_policy_rule is not None:
            for k in self.authorize_access_policy_rule:
                result['AuthorizeAccessPolicyRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')
        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('PreemptLoginUser') is not None:
            self.preempt_login_user = m.get('PreemptLoginUser')
        self.authorize_security_policy_rule = []
        if m.get('AuthorizeSecurityPolicyRule') is not None:
            for k in m.get('AuthorizeSecurityPolicyRule'):
                temp_model = CreatePolicyGroupRequestAuthorizeSecurityPolicyRule()
                self.authorize_security_policy_rule.append(temp_model.from_map(k))
        self.authorize_access_policy_rule = []
        if m.get('AuthorizeAccessPolicyRule') is not None:
            for k in m.get('AuthorizeAccessPolicyRule'):
                temp_model = CreatePolicyGroupRequestAuthorizeAccessPolicyRule()
                self.authorize_access_policy_rule.append(temp_model.from_map(k))
        return self


class CreatePolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        policy_group_id: str = None,
        request_id: str = None,
    ):
        self.policy_group_id = policy_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePolicyGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRAMDirectoryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_name: str = None,
        enable_internet_access: bool = None,
        enable_admin_access: bool = None,
        desktop_access_type: str = None,
        v_switch_id: List[str] = None,
    ):
        self.region_id = region_id
        self.directory_name = directory_name
        self.enable_internet_access = enable_internet_access
        self.enable_admin_access = enable_admin_access
        self.desktop_access_type = desktop_access_type
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateRAMDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        request_id: str = None,
    ):
        self.directory_id = directory_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRAMDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRAMDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRAMDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScaleStrategyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scale_strategy_name: str = None,
        scale_strategy_type: str = None,
        pay_type: str = None,
        min_desktops_count: int = None,
        max_desktops_count: int = None,
        min_available_desktops_count: int = None,
        max_available_desktops_count: int = None,
        scale_step: int = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.scale_strategy_name = scale_strategy_name
        self.scale_strategy_type = scale_strategy_type
        self.pay_type = pay_type
        self.min_desktops_count = min_desktops_count
        self.max_desktops_count = max_desktops_count
        self.min_available_desktops_count = min_available_desktops_count
        self.max_available_desktops_count = max_available_desktops_count
        self.scale_step = scale_step
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_strategy_name is not None:
            result['ScaleStrategyName'] = self.scale_strategy_name
        if self.scale_strategy_type is not None:
            result['ScaleStrategyType'] = self.scale_strategy_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.min_available_desktops_count is not None:
            result['MinAvailableDesktopsCount'] = self.min_available_desktops_count
        if self.max_available_desktops_count is not None:
            result['MaxAvailableDesktopsCount'] = self.max_available_desktops_count
        if self.scale_step is not None:
            result['ScaleStep'] = self.scale_step
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleStrategyName') is not None:
            self.scale_strategy_name = m.get('ScaleStrategyName')
        if m.get('ScaleStrategyType') is not None:
            self.scale_strategy_type = m.get('ScaleStrategyType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('MinAvailableDesktopsCount') is not None:
            self.min_available_desktops_count = m.get('MinAvailableDesktopsCount')
        if m.get('MaxAvailableDesktopsCount') is not None:
            self.max_available_desktops_count = m.get('MaxAvailableDesktopsCount')
        if m.get('ScaleStep') is not None:
            self.scale_step = m.get('ScaleStep')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateScaleStrategyResponseBody(TeaModel):
    def __init__(
        self,
        scale_strategy_id: str = None,
        request_id: str = None,
    ):
        self.scale_strategy_id = scale_strategy_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateScaleStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateScaleStrategyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateScaleStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceLinkedRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimpleOfficeSiteRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cidr_block: str = None,
        cen_id: str = None,
        bandwidth: int = None,
        office_site_name: str = None,
        enable_internet_access: bool = None,
        enable_admin_access: bool = None,
        desktop_access_type: str = None,
    ):
        self.region_id = region_id
        self.cidr_block = cidr_block
        self.cen_id = cen_id
        self.bandwidth = bandwidth
        self.office_site_name = office_site_name
        self.enable_internet_access = enable_internet_access
        self.enable_admin_access = enable_admin_access
        self.desktop_access_type = desktop_access_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        return self


class CreateSimpleOfficeSiteResponseBody(TeaModel):
    def __init__(
        self,
        office_site_id: str = None,
        request_id: str = None,
    ):
        self.office_site_id = office_site_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSimpleOfficeSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSimpleOfficeSiteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSimpleOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: str = None,
        snapshot_name: str = None,
        description: str = None,
        source_disk_type: str = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id
        self.snapshot_name = snapshot_name
        self.description = description
        self.source_disk_type = source_disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        snapshot_id: str = None,
        request_id: str = None,
    ):
        self.snapshot_id = snapshot_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBundlesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        bundle_id: List[str] = None,
    ):
        self.region_id = region_id
        self.bundle_id = bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        return self


class DeleteBundlesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBundlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBundlesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteBundlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        return self


class DeleteDesktopGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDesktopGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DeleteDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectoriesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: List[str] = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class DeleteDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDirectoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImagesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        image_id: List[str] = None,
    ):
        self.region_id = region_id
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DeleteImagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteImagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNASFileSystemsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        file_system_id: List[str] = None,
    ):
        self.region_id = region_id
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DeleteNASFileSystemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNASFileSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNASFileSystemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNASFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkPackagesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        network_package_id: List[str] = None,
    ):
        self.region_id = region_id
        self.network_package_id = network_package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        return self


class DeleteNetworkPackagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNetworkPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNetworkPackagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteNetworkPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOfficeSitesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: List[str] = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class DeleteOfficeSitesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteOfficeSitesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteOfficeSitesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteOfficeSitesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyGroupsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        policy_group_id: List[str] = None,
    ):
        self.region_id = region_id
        self.policy_group_id = policy_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        return self


class DeletePolicyGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePolicyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePolicyGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScaleStrategyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scale_strategy_id: str = None,
    ):
        self.region_id = region_id
        self.scale_strategy_id = scale_strategy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        return self


class DeleteScaleStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteScaleStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteScaleStrategyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteScaleStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        snapshot_id: List[str] = None,
    ):
        self.region_id = region_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        serial_number: str = None,
    ):
        self.region_id = region_id
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class DeleteVirtualMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVirtualMFADeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmEventStackInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: str = None,
        event_name: str = None,
        unique_info: str = None,
        lang: str = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id
        self.event_name = event_name
        self.unique_info = unique_info
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class DescribeAlarmEventStackInfoResponseBody(TeaModel):
    def __init__(
        self,
        stack_info: str = None,
        request_id: str = None,
    ):
        self.stack_info = stack_info
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stack_info is not None:
            result['StackInfo'] = self.stack_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StackInfo') is not None:
            self.stack_info = m.get('StackInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAlarmEventStackInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAlarmEventStackInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAlarmEventStackInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBundlesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        bundle_type: str = None,
        desktop_type_family: str = None,
        cpu_count: int = None,
        memory_size: int = None,
        gpu_count: float = None,
        check_stock: bool = None,
        from_desktop_group: bool = None,
        protocol_type: str = None,
        bundle_id: List[str] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.bundle_type = bundle_type
        self.desktop_type_family = desktop_type_family
        self.cpu_count = cpu_count
        self.memory_size = memory_size
        self.gpu_count = gpu_count
        self.check_stock = check_stock
        self.from_desktop_group = from_desktop_group
        self.protocol_type = protocol_type
        self.bundle_id = bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
        if self.desktop_type_family is not None:
            result['DesktopTypeFamily'] = self.desktop_type_family
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.check_stock is not None:
            result['CheckStock'] = self.check_stock
        if self.from_desktop_group is not None:
            result['FromDesktopGroup'] = self.from_desktop_group
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        if m.get('DesktopTypeFamily') is not None:
            self.desktop_type_family = m.get('DesktopTypeFamily')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('CheckStock') is not None:
            self.check_stock = m.get('CheckStock')
        if m.get('FromDesktopGroup') is not None:
            self.from_desktop_group = m.get('FromDesktopGroup')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        return self


class DescribeBundlesResponseBodyBundlesDisks(TeaModel):
    def __init__(
        self,
        disk_type: str = None,
        disk_size: int = None,
    ):
        self.disk_type = disk_type
        self.disk_size = disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        return self


class DescribeBundlesResponseBodyBundlesDesktopTypeAttribute(TeaModel):
    def __init__(
        self,
        cpu_count: int = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        memory_size: int = None,
    ):
        self.cpu_count = cpu_count
        self.gpu_count = gpu_count
        self.gpu_spec = gpu_spec
        self.memory_size = memory_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        return self


class DescribeBundlesResponseBodyBundles(TeaModel):
    def __init__(
        self,
        description: str = None,
        bundle_type: str = None,
        os_type: str = None,
        stock_state: str = None,
        desktop_type: str = None,
        protocol_type: str = None,
        bundle_id: str = None,
        image_id: str = None,
        bundle_name: str = None,
        disks: List[DescribeBundlesResponseBodyBundlesDisks] = None,
        desktop_type_attribute: DescribeBundlesResponseBodyBundlesDesktopTypeAttribute = None,
    ):
        self.description = description
        self.bundle_type = bundle_type
        self.os_type = os_type
        self.stock_state = stock_state
        self.desktop_type = desktop_type
        self.protocol_type = protocol_type
        self.bundle_id = bundle_id
        self.image_id = image_id
        self.bundle_name = bundle_name
        self.disks = disks
        self.desktop_type_attribute = desktop_type_attribute

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        if self.desktop_type_attribute:
            self.desktop_type_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.stock_state is not None:
            result['StockState'] = self.stock_state
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.desktop_type_attribute is not None:
            result['DesktopTypeAttribute'] = self.desktop_type_attribute.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('StockState') is not None:
            self.stock_state = m.get('StockState')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeBundlesResponseBodyBundlesDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('DesktopTypeAttribute') is not None:
            temp_model = DescribeBundlesResponseBodyBundlesDesktopTypeAttribute()
            self.desktop_type_attribute = temp_model.from_map(m['DesktopTypeAttribute'])
        return self


class DescribeBundlesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        bundles: List[DescribeBundlesResponseBodyBundles] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.bundles = bundles

    def validate(self):
        if self.bundles:
            for k in self.bundles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Bundles'] = []
        if self.bundles is not None:
            for k in self.bundles:
                result['Bundles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bundles = []
        if m.get('Bundles') is not None:
            for k in m.get('Bundles'):
                temp_model = DescribeBundlesResponseBodyBundles()
                self.bundles.append(temp_model.from_map(k))
        return self


class DescribeBundlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBundlesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBundlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCensRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.region_id = region_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeCensResponseBodyCensTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeCensResponseBodyCensPackageIds(TeaModel):
    def __init__(
        self,
        package_id: str = None,
    ):
        self.package_id = package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
        return self


class DescribeCensResponseBodyCens(TeaModel):
    def __init__(
        self,
        status: str = None,
        creation_time: str = None,
        ipv_6level: str = None,
        description: str = None,
        cen_id: str = None,
        protection_level: str = None,
        name: str = None,
        tags: List[DescribeCensResponseBodyCensTags] = None,
        package_ids: List[DescribeCensResponseBodyCensPackageIds] = None,
    ):
        self.status = status
        self.creation_time = creation_time
        self.ipv_6level = ipv_6level
        self.description = description
        self.cen_id = cen_id
        self.protection_level = protection_level
        self.name = name
        self.tags = tags
        self.package_ids = package_ids

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.package_ids:
            for k in self.package_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.ipv_6level is not None:
            result['Ipv6Level'] = self.ipv_6level
        if self.description is not None:
            result['Description'] = self.description
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.name is not None:
            result['Name'] = self.name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['PackageIds'] = []
        if self.package_ids is not None:
            for k in self.package_ids:
                result['PackageIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Ipv6Level') is not None:
            self.ipv_6level = m.get('Ipv6Level')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeCensResponseBodyCensTags()
                self.tags.append(temp_model.from_map(k))
        self.package_ids = []
        if m.get('PackageIds') is not None:
            for k in m.get('PackageIds'):
                temp_model = DescribeCensResponseBodyCensPackageIds()
                self.package_ids.append(temp_model.from_map(k))
        return self


class DescribeCensResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        cens: List[DescribeCensResponseBodyCens] = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.cens = cens

    def validate(self):
        if self.cens:
            for k in self.cens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Cens'] = []
        if self.cens is not None:
            for k in self.cens:
                result['Cens'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.cens = []
        if m.get('Cens') is not None:
            for k in m.get('Cens'):
                temp_model = DescribeCensResponseBodyCens()
                self.cens.append(temp_model.from_map(k))
        return self


class DescribeCensResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCensResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientEventsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        end_user_id: str = None,
        desktop_id: str = None,
        desktop_ip: str = None,
        directory_id: str = None,
        office_site_id: str = None,
        event_type: str = None,
        start_time: str = None,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.end_user_id = end_user_id
        self.desktop_id = desktop_id
        self.desktop_ip = desktop_ip
        self.directory_id = directory_id
        self.office_site_id = office_site_id
        self.event_type = event_type
        self.start_time = start_time
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_ip is not None:
            result['DesktopIp'] = self.desktop_ip
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopIp') is not None:
            self.desktop_ip = m.get('DesktopIp')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeClientEventsResponseBodyEvents(TeaModel):
    def __init__(
        self,
        status: str = None,
        bytes_received: str = None,
        desktop_ip: str = None,
        event_time: str = None,
        bytes_send: str = None,
        office_site_id: str = None,
        ali_uid: str = None,
        desktop_id: str = None,
        region_id: str = None,
        event_id: str = None,
        directory_type: str = None,
        event_type: str = None,
        end_user_id: str = None,
        client_ip: str = None,
        client_os: str = None,
        office_site_type: str = None,
        directory_id: str = None,
        client_version: str = None,
    ):
        self.status = status
        self.bytes_received = bytes_received
        self.desktop_ip = desktop_ip
        self.event_time = event_time
        self.bytes_send = bytes_send
        self.office_site_id = office_site_id
        self.ali_uid = ali_uid
        self.desktop_id = desktop_id
        self.region_id = region_id
        self.event_id = event_id
        self.directory_type = directory_type
        self.event_type = event_type
        self.end_user_id = end_user_id
        self.client_ip = client_ip
        self.client_os = client_os
        self.office_site_type = office_site_type
        self.directory_id = directory_id
        self.client_version = client_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.bytes_received is not None:
            result['BytesReceived'] = self.bytes_received
        if self.desktop_ip is not None:
            result['DesktopIp'] = self.desktop_ip
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.bytes_send is not None:
            result['BytesSend'] = self.bytes_send
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BytesReceived') is not None:
            self.bytes_received = m.get('BytesReceived')
        if m.get('DesktopIp') is not None:
            self.desktop_ip = m.get('DesktopIp')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('BytesSend') is not None:
            self.bytes_send = m.get('BytesSend')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        return self


class DescribeClientEventsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        events: List[DescribeClientEventsResponseBodyEvents] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.events = events

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeClientEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        return self


class DescribeClientEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClientEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeClientEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopIdsByVulNamesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
        office_site_id: str = None,
        necessity: str = None,
        vul_name: List[str] = None,
    ):
        self.region_id = region_id
        self.type = type
        self.office_site_id = office_site_id
        self.necessity = necessity
        self.vul_name = vul_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.vul_name is not None:
            result['VulName'] = self.vul_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('VulName') is not None:
            self.vul_name = m.get('VulName')
        return self


class DescribeDesktopIdsByVulNamesResponseBodyDesktopItems(TeaModel):
    def __init__(
        self,
        desktop_name: str = None,
        desktop_id: str = None,
    ):
        self.desktop_name = desktop_name
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DescribeDesktopIdsByVulNamesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        desktop_items: List[DescribeDesktopIdsByVulNamesResponseBodyDesktopItems] = None,
    ):
        self.request_id = request_id
        self.desktop_items = desktop_items

    def validate(self):
        if self.desktop_items:
            for k in self.desktop_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DesktopItems'] = []
        if self.desktop_items is not None:
            for k in self.desktop_items:
                result['DesktopItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.desktop_items = []
        if m.get('DesktopItems') is not None:
            for k in m.get('DesktopItems'):
                temp_model = DescribeDesktopIdsByVulNamesResponseBodyDesktopItems()
                self.desktop_items.append(temp_model.from_map(k))
        return self


class DescribeDesktopIdsByVulNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDesktopIdsByVulNamesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopIdsByVulNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopPolicysRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        next_token: str = None,
        max_results: int = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.next_token = next_token
        self.max_results = max_results
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DescribeDesktopPolicysResponseBodyDescribeDesktopPolicys(TeaModel):
    def __init__(
        self,
        usb_redirect: str = None,
        desktop_id: str = None,
        watermark: str = None,
        clipboard: str = None,
        local_drive: str = None,
    ):
        self.usb_redirect = usb_redirect
        self.desktop_id = desktop_id
        self.watermark = watermark
        self.clipboard = clipboard
        self.local_drive = local_drive

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        return self


class DescribeDesktopPolicysResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        describe_desktop_policys: List[DescribeDesktopPolicysResponseBodyDescribeDesktopPolicys] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.describe_desktop_policys = describe_desktop_policys

    def validate(self):
        if self.describe_desktop_policys:
            for k in self.describe_desktop_policys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DescribeDesktopPolicys'] = []
        if self.describe_desktop_policys is not None:
            for k in self.describe_desktop_policys:
                result['DescribeDesktopPolicys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.describe_desktop_policys = []
        if m.get('DescribeDesktopPolicys') is not None:
            for k in m.get('DescribeDesktopPolicys'):
                temp_model = DescribeDesktopPolicysResponseBodyDescribeDesktopPolicys()
                self.describe_desktop_policys.append(temp_model.from_map(k))
        return self


class DescribeDesktopPolicysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDesktopPolicysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopPolicysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        group_id: str = None,
        desktop_status: str = None,
        max_results: int = None,
        next_token: str = None,
        user_name: str = None,
        desktop_name: str = None,
        directory_id: str = None,
        office_site_id: str = None,
        policy_group_id: str = None,
        charge_type: str = None,
        expired_time: str = None,
        desktop_id: List[str] = None,
        end_user_id: List[str] = None,
    ):
        self.region_id = region_id
        self.group_id = group_id
        self.desktop_status = desktop_status
        self.max_results = max_results
        self.next_token = next_token
        self.user_name = user_name
        self.desktop_name = desktop_name
        self.directory_id = directory_id
        self.office_site_id = office_site_id
        self.policy_group_id = policy_group_id
        self.charge_type = charge_type
        self.expired_time = expired_time
        self.desktop_id = desktop_id
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class DescribeDesktopsResponseBodyDesktopsDisks(TeaModel):
    def __init__(
        self,
        disk_type: str = None,
        disk_id: str = None,
        disk_size: int = None,
    ):
        self.disk_type = disk_type
        self.disk_id = disk_id
        self.disk_size = disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        return self


class DescribeDesktopsResponseBodyDesktopsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDesktopsResponseBodyDesktopsSessions(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        establishment_time: str = None,
    ):
        self.end_user_id = end_user_id
        self.establishment_time = establishment_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.establishment_time is not None:
            result['EstablishmentTime'] = self.establishment_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EstablishmentTime') is not None:
            self.establishment_time = m.get('EstablishmentTime')
        return self


class DescribeDesktopsResponseBodyDesktops(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        charge_type: str = None,
        desktop_name: str = None,
        policy_group_name: str = None,
        system_disk_size: int = None,
        policy_group_id: str = None,
        desktop_status: str = None,
        desktop_type: str = None,
        gpu_count: float = None,
        memory: int = None,
        gpu_spec: str = None,
        directory_id: str = None,
        image_id: str = None,
        management_flag: str = None,
        data_disk_category: str = None,
        system_disk_category: str = None,
        office_site_id: str = None,
        network_interface_id: str = None,
        data_disk_size: str = None,
        desktop_id: str = None,
        office_site_name: str = None,
        start_time: str = None,
        directory_type: str = None,
        cpu: int = None,
        network_interface_ip: str = None,
        expired_time: str = None,
        os_type: str = None,
        connection_status: str = None,
        bundle_id: str = None,
        office_site_type: str = None,
        disks: List[DescribeDesktopsResponseBodyDesktopsDisks] = None,
        tags: List[DescribeDesktopsResponseBodyDesktopsTags] = None,
        sessions: List[DescribeDesktopsResponseBodyDesktopsSessions] = None,
        end_user_ids: List[str] = None,
    ):
        self.creation_time = creation_time
        self.charge_type = charge_type
        self.desktop_name = desktop_name
        self.policy_group_name = policy_group_name
        self.system_disk_size = system_disk_size
        self.policy_group_id = policy_group_id
        self.desktop_status = desktop_status
        self.desktop_type = desktop_type
        self.gpu_count = gpu_count
        self.memory = memory
        self.gpu_spec = gpu_spec
        self.directory_id = directory_id
        self.image_id = image_id
        self.management_flag = management_flag
        self.data_disk_category = data_disk_category
        self.system_disk_category = system_disk_category
        self.office_site_id = office_site_id
        self.network_interface_id = network_interface_id
        self.data_disk_size = data_disk_size
        self.desktop_id = desktop_id
        self.office_site_name = office_site_name
        self.start_time = start_time
        self.directory_type = directory_type
        self.cpu = cpu
        self.network_interface_ip = network_interface_ip
        self.expired_time = expired_time
        self.os_type = os_type
        self.connection_status = connection_status
        self.bundle_id = bundle_id
        self.office_site_type = office_site_type
        self.disks = disks
        self.tags = tags
        self.sessions = sessions
        self.end_user_ids = end_user_ids

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['Sessions'] = []
        if self.sessions is not None:
            for k in self.sessions:
                result['Sessions'].append(k.to_map() if k else None)
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDesktopsResponseBodyDesktopsDisks()
                self.disks.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDesktopsResponseBodyDesktopsTags()
                self.tags.append(temp_model.from_map(k))
        self.sessions = []
        if m.get('Sessions') is not None:
            for k in m.get('Sessions'):
                temp_model = DescribeDesktopsResponseBodyDesktopsSessions()
                self.sessions.append(temp_model.from_map(k))
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class DescribeDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        desktops: List[DescribeDesktopsResponseBodyDesktops] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.desktops = desktops

    def validate(self):
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Desktops'] = []
        if self.desktops is not None:
            for k in self.desktops:
                result['Desktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.desktops = []
        if m.get('Desktops') is not None:
            for k in m.get('Desktops'):
                temp_model = DescribeDesktopsResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k))
        return self


class DescribeDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopsInGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
        pay_type: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id
        self.pay_type = pay_type
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDesktopsInGroupResponseBodyPaidDesktops(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        desktop_status: str = None,
        desktop_name: str = None,
        connection_status: str = None,
        desktop_id: str = None,
        end_user_name: str = None,
    ):
        self.end_user_id = end_user_id
        self.desktop_status = desktop_status
        self.desktop_name = desktop_name
        self.connection_status = connection_status
        self.desktop_id = desktop_id
        self.end_user_name = end_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')
        return self


class DescribeDesktopsInGroupResponseBodyPostPaidDesktops(TeaModel):
    def __init__(
        self,
        create_duration: str = None,
        end_user_id: str = None,
        desktop_status: str = None,
        create_time: str = None,
        release_time: str = None,
        desktop_name: str = None,
        connection_status: str = None,
        desktop_id: str = None,
        end_user_name: str = None,
    ):
        self.create_duration = create_duration
        self.end_user_id = end_user_id
        self.desktop_status = desktop_status
        self.create_time = create_time
        self.release_time = release_time
        self.desktop_name = desktop_name
        self.connection_status = connection_status
        self.desktop_id = desktop_id
        self.end_user_name = end_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_duration is not None:
            result['CreateDuration'] = self.create_duration
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDuration') is not None:
            self.create_duration = m.get('CreateDuration')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')
        return self


class DescribeDesktopsInGroupResponseBody(TeaModel):
    def __init__(
        self,
        post_paid_desktops_count: int = None,
        next_token: str = None,
        paid_desktops_count: int = None,
        request_id: str = None,
        post_paid_desktops_total_amount: int = None,
        paid_desktops: List[DescribeDesktopsInGroupResponseBodyPaidDesktops] = None,
        post_paid_desktops: List[DescribeDesktopsInGroupResponseBodyPostPaidDesktops] = None,
    ):
        self.post_paid_desktops_count = post_paid_desktops_count
        self.next_token = next_token
        self.paid_desktops_count = paid_desktops_count
        self.request_id = request_id
        self.post_paid_desktops_total_amount = post_paid_desktops_total_amount
        self.paid_desktops = paid_desktops
        self.post_paid_desktops = post_paid_desktops

    def validate(self):
        if self.paid_desktops:
            for k in self.paid_desktops:
                if k:
                    k.validate()
        if self.post_paid_desktops:
            for k in self.post_paid_desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.post_paid_desktops_count is not None:
            result['PostPaidDesktopsCount'] = self.post_paid_desktops_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.paid_desktops_count is not None:
            result['PaidDesktopsCount'] = self.paid_desktops_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.post_paid_desktops_total_amount is not None:
            result['PostPaidDesktopsTotalAmount'] = self.post_paid_desktops_total_amount
        result['PaidDesktops'] = []
        if self.paid_desktops is not None:
            for k in self.paid_desktops:
                result['PaidDesktops'].append(k.to_map() if k else None)
        result['PostPaidDesktops'] = []
        if self.post_paid_desktops is not None:
            for k in self.post_paid_desktops:
                result['PostPaidDesktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostPaidDesktopsCount') is not None:
            self.post_paid_desktops_count = m.get('PostPaidDesktopsCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PaidDesktopsCount') is not None:
            self.paid_desktops_count = m.get('PaidDesktopsCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PostPaidDesktopsTotalAmount') is not None:
            self.post_paid_desktops_total_amount = m.get('PostPaidDesktopsTotalAmount')
        self.paid_desktops = []
        if m.get('PaidDesktops') is not None:
            for k in m.get('PaidDesktops'):
                temp_model = DescribeDesktopsInGroupResponseBodyPaidDesktops()
                self.paid_desktops.append(temp_model.from_map(k))
        self.post_paid_desktops = []
        if m.get('PostPaidDesktops') is not None:
            for k in m.get('PostPaidDesktops'):
                temp_model = DescribeDesktopsInGroupResponseBodyPostPaidDesktops()
                self.post_paid_desktops.append(temp_model.from_map(k))
        return self


class DescribeDesktopsInGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDesktopsInGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopsInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopTypesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_type_id: str = None,
        instance_type_family: str = None,
        cpu_count: int = None,
        memory_size: int = None,
        gpu_count: float = None,
    ):
        self.region_id = region_id
        self.desktop_type_id = desktop_type_id
        self.instance_type_family = instance_type_family
        self.cpu_count = cpu_count
        self.memory_size = memory_size
        self.gpu_count = gpu_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        return self


class DescribeDesktopTypesResponseBodyDesktopTypesAllowDiskSize(TeaModel):
    def __init__(
        self,
        data_disk_size: int = None,
        system_disk_size: int = None,
    ):
        self.data_disk_size = data_disk_size
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeDesktopTypesResponseBodyDesktopTypes(TeaModel):
    def __init__(
        self,
        system_disk_size: str = None,
        desktop_type_id: str = None,
        data_disk_size: str = None,
        cpu_count: str = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        instance_type_family: str = None,
        memory_size: str = None,
        allow_disk_size: List[DescribeDesktopTypesResponseBodyDesktopTypesAllowDiskSize] = None,
    ):
        self.system_disk_size = system_disk_size
        self.desktop_type_id = desktop_type_id
        self.data_disk_size = data_disk_size
        self.cpu_count = cpu_count
        self.gpu_count = gpu_count
        self.gpu_spec = gpu_spec
        self.instance_type_family = instance_type_family
        self.memory_size = memory_size
        self.allow_disk_size = allow_disk_size

    def validate(self):
        if self.allow_disk_size:
            for k in self.allow_disk_size:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        result['AllowDiskSize'] = []
        if self.allow_disk_size is not None:
            for k in self.allow_disk_size:
                result['AllowDiskSize'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        self.allow_disk_size = []
        if m.get('AllowDiskSize') is not None:
            for k in m.get('AllowDiskSize'):
                temp_model = DescribeDesktopTypesResponseBodyDesktopTypesAllowDiskSize()
                self.allow_disk_size.append(temp_model.from_map(k))
        return self


class DescribeDesktopTypesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        desktop_types: List[DescribeDesktopTypesResponseBodyDesktopTypes] = None,
    ):
        self.request_id = request_id
        self.desktop_types = desktop_types

    def validate(self):
        if self.desktop_types:
            for k in self.desktop_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DesktopTypes'] = []
        if self.desktop_types is not None:
            for k in self.desktop_types:
                result['DesktopTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.desktop_types = []
        if m.get('DesktopTypes') is not None:
            for k in m.get('DesktopTypes'):
                temp_model = DescribeDesktopTypesResponseBodyDesktopTypes()
                self.desktop_types.append(temp_model.from_map(k))
        return self


class DescribeDesktopTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDesktopTypesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDesktopTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_type: str = None,
        directory_status: str = None,
        max_results: int = None,
        next_token: str = None,
        directory_id: List[str] = None,
    ):
        self.region_id = region_id
        self.directory_type = directory_type
        self.directory_status = directory_status
        self.max_results = max_results
        self.next_token = next_token
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.directory_status is not None:
            result['DirectoryStatus'] = self.directory_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('DirectoryStatus') is not None:
            self.directory_status = m.get('DirectoryStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class DescribeDirectoriesResponseBodyDirectoriesADConnectors(TeaModel):
    def __init__(
        self,
        connector_status: str = None,
        v_switch_id: str = None,
        adconnector_address: str = None,
        network_interface_id: str = None,
    ):
        self.connector_status = connector_status
        self.v_switch_id = v_switch_id
        self.adconnector_address = adconnector_address
        self.network_interface_id = network_interface_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.adconnector_address is not None:
            result['ADConnectorAddress'] = self.adconnector_address
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ADConnectorAddress') is not None:
            self.adconnector_address = m.get('ADConnectorAddress')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class DescribeDirectoriesResponseBodyDirectoriesLogs(TeaModel):
    def __init__(
        self,
        step: str = None,
        message: str = None,
        time_stamp: str = None,
        level: str = None,
    ):
        self.step = step
        self.message = message
        self.time_stamp = time_stamp
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.message is not None:
            result['Message'] = self.message
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(
        self,
        enable_internet_access: bool = None,
        vpc_id: str = None,
        creation_time: str = None,
        status: str = None,
        domain_password: str = None,
        enable_admin_access: bool = None,
        sub_domain_name: str = None,
        domain_user_name: str = None,
        enable_cross_desktop_access: bool = None,
        custom_security_group_id: str = None,
        desktop_vpc_endpoint: str = None,
        sso_enabled: bool = None,
        domain_name: str = None,
        desktop_access_type: str = None,
        mfa_enabled: bool = None,
        directory_type: str = None,
        dns_user_name: str = None,
        trust_password: str = None,
        name: str = None,
        directory_id: str = None,
        adconnectors: List[DescribeDirectoriesResponseBodyDirectoriesADConnectors] = None,
        logs: List[DescribeDirectoriesResponseBodyDirectoriesLogs] = None,
        v_switch_ids: List[str] = None,
        file_system_ids: List[str] = None,
        sub_dns_address: List[str] = None,
        dns_address: List[str] = None,
    ):
        self.enable_internet_access = enable_internet_access
        self.vpc_id = vpc_id
        self.creation_time = creation_time
        self.status = status
        self.domain_password = domain_password
        self.enable_admin_access = enable_admin_access
        self.sub_domain_name = sub_domain_name
        self.domain_user_name = domain_user_name
        self.enable_cross_desktop_access = enable_cross_desktop_access
        self.custom_security_group_id = custom_security_group_id
        self.desktop_vpc_endpoint = desktop_vpc_endpoint
        self.sso_enabled = sso_enabled
        self.domain_name = domain_name
        self.desktop_access_type = desktop_access_type
        self.mfa_enabled = mfa_enabled
        self.directory_type = directory_type
        self.dns_user_name = dns_user_name
        self.trust_password = trust_password
        self.name = name
        self.directory_id = directory_id
        self.adconnectors = adconnectors
        self.logs = logs
        self.v_switch_ids = v_switch_ids
        self.file_system_ids = file_system_ids
        self.sub_dns_address = sub_dns_address
        self.dns_address = dns_address

    def validate(self):
        if self.adconnectors:
            for k in self.adconnectors:
                if k:
                    k.validate()
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access
        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.dns_user_name is not None:
            result['DnsUserName'] = self.dns_user_name
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.name is not None:
            result['Name'] = self.name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k in self.adconnectors:
                result['ADConnectors'].append(k.to_map() if k else None)
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        if self.sub_dns_address is not None:
            result['SubDnsAddress'] = self.sub_dns_address
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')
        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('DnsUserName') is not None:
            self.dns_user_name = m.get('DnsUserName')
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k in m.get('ADConnectors'):
                temp_model = DescribeDirectoriesResponseBodyDirectoriesADConnectors()
                self.adconnectors.append(temp_model.from_map(k))
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeDirectoriesResponseBodyDirectoriesLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        if m.get('SubDnsAddress') is not None:
            self.sub_dns_address = m.get('SubDnsAddress')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        return self


class DescribeDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        directories: List[DescribeDirectoriesResponseBodyDirectories] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.directories = directories

    def validate(self):
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDirectoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFrontVulPatchListRequestVulInfo(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        tag: str = None,
        name: str = None,
    ):
        self.desktop_id = desktop_id
        self.tag = tag
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeFrontVulPatchListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        operate_type: str = None,
        type: str = None,
        vul_info: List[DescribeFrontVulPatchListRequestVulInfo] = None,
    ):
        self.region_id = region_id
        self.operate_type = operate_type
        self.type = type
        self.vul_info = vul_info

    def validate(self):
        if self.vul_info:
            for k in self.vul_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.type is not None:
            result['Type'] = self.type
        result['VulInfo'] = []
        if self.vul_info is not None:
            for k in self.vul_info:
                result['VulInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.vul_info = []
        if m.get('VulInfo') is not None:
            for k in m.get('VulInfo'):
                temp_model = DescribeFrontVulPatchListRequestVulInfo()
                self.vul_info.append(temp_model.from_map(k))
        return self


class DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList(TeaModel):
    def __init__(
        self,
        name: str = None,
        alias_name: str = None,
    ):
        self.name = name
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class DescribeFrontVulPatchListResponseBodyFrontPatchList(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        patch_list: List[DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList] = None,
    ):
        self.desktop_id = desktop_id
        self.patch_list = patch_list

    def validate(self):
        if self.patch_list:
            for k in self.patch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        result['PatchList'] = []
        if self.patch_list is not None:
            for k in self.patch_list:
                result['PatchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        self.patch_list = []
        if m.get('PatchList') is not None:
            for k in m.get('PatchList'):
                temp_model = DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList()
                self.patch_list.append(temp_model.from_map(k))
        return self


class DescribeFrontVulPatchListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        front_patch_list: List[DescribeFrontVulPatchListResponseBodyFrontPatchList] = None,
    ):
        self.request_id = request_id
        self.front_patch_list = front_patch_list

    def validate(self):
        if self.front_patch_list:
            for k in self.front_patch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FrontPatchList'] = []
        if self.front_patch_list is not None:
            for k in self.front_patch_list:
                result['FrontPatchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.front_patch_list = []
        if m.get('FrontPatchList') is not None:
            for k in m.get('FrontPatchList'):
                temp_model = DescribeFrontVulPatchListResponseBodyFrontPatchList()
                self.front_patch_list.append(temp_model.from_map(k))
        return self


class DescribeFrontVulPatchListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFrontVulPatchListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFrontVulPatchListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupedVulRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        lang: str = None,
        type: str = None,
        office_site_id: str = None,
        necessity: str = None,
        dealed: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.lang = lang
        self.type = type
        self.office_site_id = office_site_id
        self.necessity = necessity
        self.dealed = dealed
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeGroupedVulResponseBodyGroupedVulItems(TeaModel):
    def __init__(
        self,
        type: str = None,
        nntf_count: int = None,
        handled_count: int = None,
        gmt_last: str = None,
        tags: str = None,
        later_count: int = None,
        alias_name: str = None,
        name: str = None,
        asap_count: int = None,
    ):
        self.type = type
        self.nntf_count = nntf_count
        self.handled_count = handled_count
        self.gmt_last = gmt_last
        self.tags = tags
        self.later_count = later_count
        self.alias_name = alias_name
        self.name = name
        self.asap_count = asap_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.handled_count is not None:
            result['HandledCount'] = self.handled_count
        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('HandledCount') is not None:
            self.handled_count = m.get('HandledCount')
        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        return self


class DescribeGroupedVulResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        grouped_vul_items: List[DescribeGroupedVulResponseBodyGroupedVulItems] = None,
    ):
        self.current_page = current_page
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.grouped_vul_items = grouped_vul_items

    def validate(self):
        if self.grouped_vul_items:
            for k in self.grouped_vul_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['GroupedVulItems'] = []
        if self.grouped_vul_items is not None:
            for k in self.grouped_vul_items:
                result['GroupedVulItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.grouped_vul_items = []
        if m.get('GroupedVulItems') is not None:
            for k in m.get('GroupedVulItems'):
                temp_model = DescribeGroupedVulResponseBodyGroupedVulItems()
                self.grouped_vul_items.append(temp_model.from_map(k))
        return self


class DescribeGroupedVulResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGroupedVulResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGroupedVulResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        image_type: str = None,
        image_status: str = None,
        gpu_category: bool = None,
        protocol_type: str = None,
        image_id: List[str] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.image_type = image_type
        self.image_status = image_status
        self.gpu_category = gpu_category
        self.protocol_type = protocol_type
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_status is not None:
            result['ImageStatus'] = self.image_status
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageStatus') is not None:
            self.image_status = m.get('ImageStatus')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DescribeImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        status: str = None,
        progress: str = None,
        data_disk_size: int = None,
        image_type: str = None,
        description: str = None,
        size: int = None,
        os_type: str = None,
        protocol_type: str = None,
        name: str = None,
        image_id: str = None,
        gpu_category: bool = None,
    ):
        self.creation_time = creation_time
        self.status = status
        self.progress = progress
        self.data_disk_size = data_disk_size
        self.image_type = image_type
        self.description = description
        self.size = size
        self.os_type = os_type
        self.protocol_type = protocol_type
        self.name = name
        self.image_id = image_id
        self.gpu_category = gpu_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.description is not None:
            result['Description'] = self.description
        if self.size is not None:
            result['Size'] = self.size
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.name is not None:
            result['Name'] = self.name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        return self


class DescribeImagesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        images: List[DescribeImagesResponseBodyImages] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.images = images

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = DescribeImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        invoke_id: str = None,
        command_type: str = None,
        invoke_status: str = None,
        desktop_id: str = None,
        include_output: bool = None,
        content_encoding: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.invoke_id = invoke_id
        self.command_type = command_type
        self.invoke_status = invoke_status
        self.desktop_id = desktop_id
        self.include_output = include_output
        self.content_encoding = content_encoding
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.include_output is not None:
            result['IncludeOutput'] = self.include_output
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('IncludeOutput') is not None:
            self.include_output = m.get('IncludeOutput')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeInvocationsResponseBodyInvocationsInvokeDesktops(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        invocation_status: str = None,
        finish_time: str = None,
        update_time: str = None,
        repeats: int = None,
        desktop_id: str = None,
        output: str = None,
        dropped: int = None,
        stop_time: str = None,
        exit_code: int = None,
        start_time: str = None,
        error_info: str = None,
        error_code: str = None,
    ):
        self.creation_time = creation_time
        self.invocation_status = invocation_status
        self.finish_time = finish_time
        self.update_time = update_time
        self.repeats = repeats
        self.desktop_id = desktop_id
        self.output = output
        self.dropped = dropped
        self.stop_time = stop_time
        self.exit_code = exit_code
        self.start_time = start_time
        self.error_info = error_info
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.repeats is not None:
            result['Repeats'] = self.repeats
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.output is not None:
            result['Output'] = self.output
        if self.dropped is not None:
            result['Dropped'] = self.dropped
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DescribeInvocationsResponseBodyInvocations(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        command_type: str = None,
        command_content: str = None,
        invoke_desktops: List[DescribeInvocationsResponseBodyInvocationsInvokeDesktops] = None,
    ):
        self.creation_time = creation_time
        self.invocation_status = invocation_status
        self.invoke_id = invoke_id
        self.command_type = command_type
        self.command_content = command_content
        self.invoke_desktops = invoke_desktops

    def validate(self):
        if self.invoke_desktops:
            for k in self.invoke_desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        result['InvokeDesktops'] = []
        if self.invoke_desktops is not None:
            for k in self.invoke_desktops:
                result['InvokeDesktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        self.invoke_desktops = []
        if m.get('InvokeDesktops') is not None:
            for k in m.get('InvokeDesktops'):
                temp_model = DescribeInvocationsResponseBodyInvocationsInvokeDesktops()
                self.invoke_desktops.append(temp_model.from_map(k))
        return self


class DescribeInvocationsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        invocations: List[DescribeInvocationsResponseBodyInvocations] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.invocations = invocations

    def validate(self):
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Invocations'] = []
        if self.invocations is not None:
            for k in self.invocations:
                result['Invocations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.invocations = []
        if m.get('Invocations') is not None:
            for k in m.get('Invocations'):
                temp_model = DescribeInvocationsResponseBodyInvocations()
                self.invocations.append(temp_model.from_map(k))
        return self


class DescribeInvocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInvocationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeModificationPriceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        root_disk_size_gib: int = None,
        user_disk_size_gib: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.root_disk_size_gib = root_disk_size_gib
        self.user_disk_size_gib = user_disk_size_gib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        return self


class DescribeModificationPriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeModificationPriceResponseBodyPriceInfoPricePromotions(TeaModel):
    def __init__(
        self,
        promotion_desc: str = None,
        option_code: str = None,
        selected: bool = None,
        promotion_id: str = None,
        promotion_name: str = None,
    ):
        self.promotion_desc = promotion_desc
        self.option_code = option_code
        self.selected = selected
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        return self


class DescribeModificationPriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(
        self,
        original_price: float = None,
        discount_price: float = None,
        currency: str = None,
        trade_price: float = None,
        promotions: List[DescribeModificationPriceResponseBodyPriceInfoPricePromotions] = None,
    ):
        self.original_price = original_price
        self.discount_price = discount_price
        self.currency = currency
        self.trade_price = trade_price
        self.promotions = promotions

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = DescribeModificationPriceResponseBodyPriceInfoPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        return self


class DescribeModificationPriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        rules: List[DescribeModificationPriceResponseBodyPriceInfoRules] = None,
        price: DescribeModificationPriceResponseBodyPriceInfoPrice = None,
    ):
        self.rules = rules
        self.price = price

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeModificationPriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('Price') is not None:
            temp_model = DescribeModificationPriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class DescribeModificationPriceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        price_info: DescribeModificationPriceResponseBodyPriceInfo = None,
    ):
        self.request_id = request_id
        self.price_info = price_info

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PriceInfo') is not None:
            temp_model = DescribeModificationPriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        return self


class DescribeModificationPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeModificationPriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeModificationPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNASFileSystemsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: str = None,
        max_results: int = None,
        next_token: str = None,
        file_system_id: List[str] = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id
        self.max_results = max_results
        self.next_token = next_token
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class DescribeNASFileSystemsResponseBodyFileSystems(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        mount_target_status: str = None,
        create_time: str = None,
        office_site_id: str = None,
        support_acl: bool = None,
        storage_type: str = None,
        office_site_name: str = None,
        region_id: str = None,
        file_system_id: str = None,
        file_system_type: str = None,
        file_system_name: str = None,
        metered_size: int = None,
        mount_target_domain: str = None,
        description: str = None,
        zone_id: str = None,
        file_system_status: str = None,
    ):
        self.capacity = capacity
        self.mount_target_status = mount_target_status
        self.create_time = create_time
        self.office_site_id = office_site_id
        self.support_acl = support_acl
        self.storage_type = storage_type
        self.office_site_name = office_site_name
        self.region_id = region_id
        self.file_system_id = file_system_id
        self.file_system_type = file_system_type
        self.file_system_name = file_system_name
        self.metered_size = metered_size
        self.mount_target_domain = mount_target_domain
        self.description = description
        self.zone_id = zone_id
        self.file_system_status = file_system_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.mount_target_status is not None:
            result['MountTargetStatus'] = self.mount_target_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.support_acl is not None:
            result['SupportAcl'] = self.support_acl
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.description is not None:
            result['Description'] = self.description
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.file_system_status is not None:
            result['FileSystemStatus'] = self.file_system_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('MountTargetStatus') is not None:
            self.mount_target_status = m.get('MountTargetStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('SupportAcl') is not None:
            self.support_acl = m.get('SupportAcl')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('FileSystemStatus') is not None:
            self.file_system_status = m.get('FileSystemStatus')
        return self


class DescribeNASFileSystemsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        file_systems: List[DescribeNASFileSystemsResponseBodyFileSystems] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.file_systems = file_systems

    def validate(self):
        if self.file_systems:
            for k in self.file_systems:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k in self.file_systems:
                result['FileSystems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k in m.get('FileSystems'):
                temp_model = DescribeNASFileSystemsResponseBodyFileSystems()
                self.file_systems.append(temp_model.from_map(k))
        return self


class DescribeNASFileSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNASFileSystemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNASFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkPackagesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        network_package_id: List[str] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.network_package_id = network_package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        return self


class DescribeNetworkPackagesResponseBodyNetworkPackages(TeaModel):
    def __init__(
        self,
        network_package_id: str = None,
        bandwidth: int = None,
        expired_time: str = None,
        create_time: str = None,
        office_site_id: str = None,
        internet_charge_type: str = None,
        network_package_status: str = None,
        office_site_name: str = None,
        eip_addresses: List[str] = None,
    ):
        self.network_package_id = network_package_id
        self.bandwidth = bandwidth
        self.expired_time = expired_time
        self.create_time = create_time
        self.office_site_id = office_site_id
        self.internet_charge_type = internet_charge_type
        self.network_package_status = network_package_status
        self.office_site_name = office_site_name
        self.eip_addresses = eip_addresses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.network_package_status is not None:
            result['NetworkPackageStatus'] = self.network_package_status
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('NetworkPackageStatus') is not None:
            self.network_package_status = m.get('NetworkPackageStatus')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('EipAddresses') is not None:
            self.eip_addresses = m.get('EipAddresses')
        return self


class DescribeNetworkPackagesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        network_packages: List[DescribeNetworkPackagesResponseBodyNetworkPackages] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.network_packages = network_packages

    def validate(self):
        if self.network_packages:
            for k in self.network_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['NetworkPackages'] = []
        if self.network_packages is not None:
            for k in self.network_packages:
                result['NetworkPackages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.network_packages = []
        if m.get('NetworkPackages') is not None:
            for k in m.get('NetworkPackages'):
                temp_model = DescribeNetworkPackagesResponseBodyNetworkPackages()
                self.network_packages.append(temp_model.from_map(k))
        return self


class DescribeNetworkPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNetworkPackagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNetworkPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOfficeSitesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_type: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: List[str] = None,
    ):
        self.region_id = region_id
        self.office_site_type = office_site_type
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class DescribeOfficeSitesResponseBodyOfficeSitesADConnectors(TeaModel):
    def __init__(
        self,
        connector_status: str = None,
        v_switch_id: str = None,
        adconnector_address: str = None,
        network_interface_id: str = None,
    ):
        self.connector_status = connector_status
        self.v_switch_id = v_switch_id
        self.adconnector_address = adconnector_address
        self.network_interface_id = network_interface_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.adconnector_address is not None:
            result['ADConnectorAddress'] = self.adconnector_address
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ADConnectorAddress') is not None:
            self.adconnector_address = m.get('ADConnectorAddress')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class DescribeOfficeSitesResponseBodyOfficeSitesLogs(TeaModel):
    def __init__(
        self,
        step: str = None,
        message: str = None,
        time_stamp: str = None,
        level: str = None,
    ):
        self.step = step
        self.message = message
        self.time_stamp = time_stamp
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.step is not None:
            result['Step'] = self.step
        if self.message is not None:
            result['Message'] = self.message
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class DescribeOfficeSitesResponseBodyOfficeSites(TeaModel):
    def __init__(
        self,
        status: str = None,
        creation_time: str = None,
        vpc_id: str = None,
        enable_admin_access: bool = None,
        enable_cross_desktop_access: bool = None,
        desktop_vpc_endpoint: str = None,
        desktop_access_type: str = None,
        domain_name: str = None,
        sso_enabled: bool = None,
        cidr_block: str = None,
        bandwidth: int = None,
        trust_password: str = None,
        name: str = None,
        enable_internet_access: bool = None,
        domain_password: str = None,
        custom_security_group_id: str = None,
        domain_user_name: str = None,
        sub_domain_name: str = None,
        office_site_id: str = None,
        cen_id: str = None,
        mfa_enabled: bool = None,
        network_package_id: str = None,
        dns_user_name: str = None,
        office_site_type: str = None,
        adconnectors: List[DescribeOfficeSitesResponseBodyOfficeSitesADConnectors] = None,
        logs: List[DescribeOfficeSitesResponseBodyOfficeSitesLogs] = None,
        v_switch_ids: List[str] = None,
        file_system_ids: List[str] = None,
        sub_dns_address: List[str] = None,
        dns_address: List[str] = None,
    ):
        self.status = status
        self.creation_time = creation_time
        self.vpc_id = vpc_id
        self.enable_admin_access = enable_admin_access
        self.enable_cross_desktop_access = enable_cross_desktop_access
        self.desktop_vpc_endpoint = desktop_vpc_endpoint
        self.desktop_access_type = desktop_access_type
        self.domain_name = domain_name
        self.sso_enabled = sso_enabled
        self.cidr_block = cidr_block
        self.bandwidth = bandwidth
        self.trust_password = trust_password
        self.name = name
        self.enable_internet_access = enable_internet_access
        self.domain_password = domain_password
        self.custom_security_group_id = custom_security_group_id
        self.domain_user_name = domain_user_name
        self.sub_domain_name = sub_domain_name
        self.office_site_id = office_site_id
        self.cen_id = cen_id
        self.mfa_enabled = mfa_enabled
        self.network_package_id = network_package_id
        self.dns_user_name = dns_user_name
        self.office_site_type = office_site_type
        self.adconnectors = adconnectors
        self.logs = logs
        self.v_switch_ids = v_switch_ids
        self.file_system_ids = file_system_ids
        self.sub_dns_address = sub_dns_address
        self.dns_address = dns_address

    def validate(self):
        if self.adconnectors:
            for k in self.adconnectors:
                if k:
                    k.validate()
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.name is not None:
            result['Name'] = self.name
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.dns_user_name is not None:
            result['DnsUserName'] = self.dns_user_name
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k in self.adconnectors:
                result['ADConnectors'].append(k.to_map() if k else None)
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        if self.sub_dns_address is not None:
            result['SubDnsAddress'] = self.sub_dns_address
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('DnsUserName') is not None:
            self.dns_user_name = m.get('DnsUserName')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k in m.get('ADConnectors'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSitesADConnectors()
                self.adconnectors.append(temp_model.from_map(k))
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSitesLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        if m.get('SubDnsAddress') is not None:
            self.sub_dns_address = m.get('SubDnsAddress')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        return self


class DescribeOfficeSitesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        office_sites: List[DescribeOfficeSitesResponseBodyOfficeSites] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.office_sites = office_sites

    def validate(self):
        if self.office_sites:
            for k in self.office_sites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OfficeSites'] = []
        if self.office_sites is not None:
            for k in self.office_sites:
                result['OfficeSites'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.office_sites = []
        if m.get('OfficeSites') is not None:
            for k in m.get('OfficeSites'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSites()
                self.office_sites.append(temp_model.from_map(k))
        return self


class DescribeOfficeSitesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOfficeSitesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeOfficeSitesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyGroupsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        policy_group_id: List[str] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.policy_group_id = policy_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules(TeaModel):
    def __init__(
        self,
        type: str = None,
        policy: str = None,
        description: str = None,
        port_range: str = None,
        ip_protocol: str = None,
        priority: str = None,
        cidr_ip: str = None,
    ):
        self.type = type
        self.policy = policy
        self.description = description
        self.port_range = port_range
        self.ip_protocol = ip_protocol
        self.priority = priority
        self.cidr_ip = cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.description is not None:
            result['Description'] = self.description
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        cidr_ip: str = None,
    ):
        self.description = description
        self.cidr_ip = cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroups(TeaModel):
    def __init__(
        self,
        policy_status: str = None,
        html_5access: str = None,
        watermark_type: str = None,
        preempt_login: str = None,
        watermark_custom_text: str = None,
        clipboard: str = None,
        domain_list: str = None,
        policy_group_id: str = None,
        watermark_transparency: str = None,
        html_5file_transfer: str = None,
        usb_redirect: str = None,
        policy_group_type: str = None,
        watermark: str = None,
        visual_quality: str = None,
        eds_count: int = None,
        name: str = None,
        local_drive: str = None,
        authorize_security_policy_rules: List[DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules] = None,
        authorize_access_policy_rules: List[DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules] = None,
        preempt_login_users: List[str] = None,
    ):
        self.policy_status = policy_status
        self.html_5access = html_5access
        self.watermark_type = watermark_type
        self.preempt_login = preempt_login
        self.watermark_custom_text = watermark_custom_text
        self.clipboard = clipboard
        self.domain_list = domain_list
        self.policy_group_id = policy_group_id
        self.watermark_transparency = watermark_transparency
        self.html_5file_transfer = html_5file_transfer
        self.usb_redirect = usb_redirect
        self.policy_group_type = policy_group_type
        self.watermark = watermark
        self.visual_quality = visual_quality
        self.eds_count = eds_count
        self.name = name
        self.local_drive = local_drive
        self.authorize_security_policy_rules = authorize_security_policy_rules
        self.authorize_access_policy_rules = authorize_access_policy_rules
        self.preempt_login_users = preempt_login_users

    def validate(self):
        if self.authorize_security_policy_rules:
            for k in self.authorize_security_policy_rules:
                if k:
                    k.validate()
        if self.authorize_access_policy_rules:
            for k in self.authorize_access_policy_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status
        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.policy_group_type is not None:
            result['PolicyGroupType'] = self.policy_group_type
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality
        if self.eds_count is not None:
            result['EdsCount'] = self.eds_count
        if self.name is not None:
            result['Name'] = self.name
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        result['AuthorizeSecurityPolicyRules'] = []
        if self.authorize_security_policy_rules is not None:
            for k in self.authorize_security_policy_rules:
                result['AuthorizeSecurityPolicyRules'].append(k.to_map() if k else None)
        result['AuthorizeAccessPolicyRules'] = []
        if self.authorize_access_policy_rules is not None:
            for k in self.authorize_access_policy_rules:
                result['AuthorizeAccessPolicyRules'].append(k.to_map() if k else None)
        if self.preempt_login_users is not None:
            result['PreemptLoginUsers'] = self.preempt_login_users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')
        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('PolicyGroupType') is not None:
            self.policy_group_type = m.get('PolicyGroupType')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')
        if m.get('EdsCount') is not None:
            self.eds_count = m.get('EdsCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        self.authorize_security_policy_rules = []
        if m.get('AuthorizeSecurityPolicyRules') is not None:
            for k in m.get('AuthorizeSecurityPolicyRules'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules()
                self.authorize_security_policy_rules.append(temp_model.from_map(k))
        self.authorize_access_policy_rules = []
        if m.get('AuthorizeAccessPolicyRules') is not None:
            for k in m.get('AuthorizeAccessPolicyRules'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules()
                self.authorize_access_policy_rules.append(temp_model.from_map(k))
        if m.get('PreemptLoginUsers') is not None:
            self.preempt_login_users = m.get('PreemptLoginUsers')
        return self


class DescribePolicyGroupsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        describe_policy_groups: List[DescribePolicyGroupsResponseBodyDescribePolicyGroups] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.describe_policy_groups = describe_policy_groups

    def validate(self):
        if self.describe_policy_groups:
            for k in self.describe_policy_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DescribePolicyGroups'] = []
        if self.describe_policy_groups is not None:
            for k in self.describe_policy_groups:
                result['DescribePolicyGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.describe_policy_groups = []
        if m.get('DescribePolicyGroups') is not None:
            for k in m.get('DescribePolicyGroups'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroups()
                self.describe_policy_groups.append(temp_model.from_map(k))
        return self


class DescribePolicyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePolicyGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePostPaidDesktopBillsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
        bill_start_time: str = None,
        bill_end_time: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id
        self.bill_start_time = bill_start_time
        self.bill_end_time = bill_end_time
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.bill_start_time is not None:
            result['BillStartTime'] = self.bill_start_time
        if self.bill_end_time is not None:
            result['BillEndTime'] = self.bill_end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('BillStartTime') is not None:
            self.bill_start_time = m.get('BillStartTime')
        if m.get('BillEndTime') is not None:
            self.bill_end_time = m.get('BillEndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribePostPaidDesktopBillsResponseBodyBills(TeaModel):
    def __init__(
        self,
        bill_id: str = None,
        discount_price: str = None,
        product: str = None,
        price_unit: str = None,
        cash_payment: str = None,
        payment: str = None,
        original_price: str = None,
        instance_id: str = None,
        product_detail: str = None,
        usage: str = None,
        gold_note: str = None,
        usage_unit: str = None,
        price: str = None,
        bill_start_time: str = None,
        bill_type: str = None,
        resource_group_id: str = None,
        charge_item: str = None,
        resource_group_name: str = None,
        consume_time: str = None,
        consume_type: str = None,
        bill_end_time: str = None,
    ):
        self.bill_id = bill_id
        self.discount_price = discount_price
        self.product = product
        self.price_unit = price_unit
        self.cash_payment = cash_payment
        self.payment = payment
        self.original_price = original_price
        self.instance_id = instance_id
        self.product_detail = product_detail
        self.usage = usage
        self.gold_note = gold_note
        self.usage_unit = usage_unit
        self.price = price
        self.bill_start_time = bill_start_time
        self.bill_type = bill_type
        self.resource_group_id = resource_group_id
        self.charge_item = charge_item
        self.resource_group_name = resource_group_name
        self.consume_time = consume_time
        self.consume_type = consume_type
        self.bill_end_time = bill_end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.product is not None:
            result['Product'] = self.product
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.cash_payment is not None:
            result['CashPayment'] = self.cash_payment
        if self.payment is not None:
            result['Payment'] = self.payment
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.gold_note is not None:
            result['GoldNote'] = self.gold_note
        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit
        if self.price is not None:
            result['Price'] = self.price
        if self.bill_start_time is not None:
            result['BillStartTime'] = self.bill_start_time
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.charge_item is not None:
            result['ChargeItem'] = self.charge_item
        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name
        if self.consume_time is not None:
            result['ConsumeTime'] = self.consume_time
        if self.consume_type is not None:
            result['ConsumeType'] = self.consume_type
        if self.bill_end_time is not None:
            result['BillEndTime'] = self.bill_end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('CashPayment') is not None:
            self.cash_payment = m.get('CashPayment')
        if m.get('Payment') is not None:
            self.payment = m.get('Payment')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('GoldNote') is not None:
            self.gold_note = m.get('GoldNote')
        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('BillStartTime') is not None:
            self.bill_start_time = m.get('BillStartTime')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ChargeItem') is not None:
            self.charge_item = m.get('ChargeItem')
        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')
        if m.get('ConsumeTime') is not None:
            self.consume_time = m.get('ConsumeTime')
        if m.get('ConsumeType') is not None:
            self.consume_type = m.get('ConsumeType')
        if m.get('BillEndTime') is not None:
            self.bill_end_time = m.get('BillEndTime')
        return self


class DescribePostPaidDesktopBillsResponseBody(TeaModel):
    def __init__(
        self,
        post_paid_desktops_bills_url: str = None,
        post_paid_desktops_count: int = None,
        next_token: str = None,
        request_id: str = None,
        post_paid_desktops_total_amount: float = None,
        bills: List[DescribePostPaidDesktopBillsResponseBodyBills] = None,
    ):
        self.post_paid_desktops_bills_url = post_paid_desktops_bills_url
        self.post_paid_desktops_count = post_paid_desktops_count
        self.next_token = next_token
        self.request_id = request_id
        self.post_paid_desktops_total_amount = post_paid_desktops_total_amount
        self.bills = bills

    def validate(self):
        if self.bills:
            for k in self.bills:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.post_paid_desktops_bills_url is not None:
            result['PostPaidDesktopsBillsUrl'] = self.post_paid_desktops_bills_url
        if self.post_paid_desktops_count is not None:
            result['PostPaidDesktopsCount'] = self.post_paid_desktops_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.post_paid_desktops_total_amount is not None:
            result['PostPaidDesktopsTotalAmount'] = self.post_paid_desktops_total_amount
        result['Bills'] = []
        if self.bills is not None:
            for k in self.bills:
                result['Bills'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostPaidDesktopsBillsUrl') is not None:
            self.post_paid_desktops_bills_url = m.get('PostPaidDesktopsBillsUrl')
        if m.get('PostPaidDesktopsCount') is not None:
            self.post_paid_desktops_count = m.get('PostPaidDesktopsCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PostPaidDesktopsTotalAmount') is not None:
            self.post_paid_desktops_total_amount = m.get('PostPaidDesktopsTotalAmount')
        self.bills = []
        if m.get('Bills') is not None:
            for k in m.get('Bills'):
                temp_model = DescribePostPaidDesktopBillsResponseBodyBills()
                self.bills.append(temp_model.from_map(k))
        return self


class DescribePostPaidDesktopBillsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePostPaidDesktopBillsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePostPaidDesktopBillsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePriceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        instance_type: str = None,
        root_disk_size_gib: int = None,
        user_disk_size_gib: int = None,
        os_type: str = None,
        period_unit: str = None,
        period: int = None,
        amount: int = None,
        promotion_id: str = None,
        internet_charge_type: str = None,
        bandwidth: int = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.instance_type = instance_type
        self.root_disk_size_gib = root_disk_size_gib
        self.user_disk_size_gib = user_disk_size_gib
        self.os_type = os_type
        self.period_unit = period_unit
        self.period = period
        self.amount = amount
        self.promotion_id = promotion_id
        self.internet_charge_type = internet_charge_type
        self.bandwidth = bandwidth

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class DescribePriceResponseBodyPriceInfoRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        rule_id: int = None,
    ):
        self.description = description
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribePriceResponseBodyPriceInfoPricePromotions(TeaModel):
    def __init__(
        self,
        promotion_desc: str = None,
        option_code: str = None,
        selected: bool = None,
        promotion_id: str = None,
        promotion_name: str = None,
    ):
        self.promotion_desc = promotion_desc
        self.option_code = option_code
        self.selected = selected
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        return self


class DescribePriceResponseBodyPriceInfoPrice(TeaModel):
    def __init__(
        self,
        original_price: float = None,
        discount_price: float = None,
        currency: str = None,
        trade_price: float = None,
        promotions: List[DescribePriceResponseBodyPriceInfoPricePromotions] = None,
    ):
        self.original_price = original_price
        self.discount_price = discount_price
        self.currency = currency
        self.trade_price = trade_price
        self.promotions = promotions

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = DescribePriceResponseBodyPriceInfoPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        return self


class DescribePriceResponseBodyPriceInfo(TeaModel):
    def __init__(
        self,
        rules: List[DescribePriceResponseBodyPriceInfoRules] = None,
        price: DescribePriceResponseBodyPriceInfoPrice = None,
    ):
        self.rules = rules
        self.price = price

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribePriceResponseBodyPriceInfoRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('Price') is not None:
            temp_model = DescribePriceResponseBodyPriceInfoPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class DescribePriceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        price_info: DescribePriceResponseBodyPriceInfo = None,
    ):
        self.request_id = request_id
        self.price_info = price_info

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PriceInfo') is not None:
            temp_model = DescribePriceResponseBodyPriceInfo()
            self.price_info = temp_model.from_map(m['PriceInfo'])
        return self


class DescribePriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePriceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScaleStrategysRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scale_strategy_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.scale_strategy_name = scale_strategy_name
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_strategy_name is not None:
            result['ScaleStrategyName'] = self.scale_strategy_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleStrategyName') is not None:
            self.scale_strategy_name = m.get('ScaleStrategyName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeScaleStrategysResponseBodyScaleStrategys(TeaModel):
    def __init__(
        self,
        scale_strategy_id: str = None,
        max_desktops_count: int = None,
        max_available_desktops_count: int = None,
        scale_strategy_name: str = None,
        scale_strategy_type: str = None,
        min_desktops_count: int = None,
        min_available_desktops_count: int = None,
        scale_step: int = None,
    ):
        self.scale_strategy_id = scale_strategy_id
        self.max_desktops_count = max_desktops_count
        self.max_available_desktops_count = max_available_desktops_count
        self.scale_strategy_name = scale_strategy_name
        self.scale_strategy_type = scale_strategy_type
        self.min_desktops_count = min_desktops_count
        self.min_available_desktops_count = min_available_desktops_count
        self.scale_step = scale_step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.max_available_desktops_count is not None:
            result['MaxAvailableDesktopsCount'] = self.max_available_desktops_count
        if self.scale_strategy_name is not None:
            result['ScaleStrategyName'] = self.scale_strategy_name
        if self.scale_strategy_type is not None:
            result['ScaleStrategyType'] = self.scale_strategy_type
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.min_available_desktops_count is not None:
            result['MinAvailableDesktopsCount'] = self.min_available_desktops_count
        if self.scale_step is not None:
            result['ScaleStep'] = self.scale_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('MaxAvailableDesktopsCount') is not None:
            self.max_available_desktops_count = m.get('MaxAvailableDesktopsCount')
        if m.get('ScaleStrategyName') is not None:
            self.scale_strategy_name = m.get('ScaleStrategyName')
        if m.get('ScaleStrategyType') is not None:
            self.scale_strategy_type = m.get('ScaleStrategyType')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MinAvailableDesktopsCount') is not None:
            self.min_available_desktops_count = m.get('MinAvailableDesktopsCount')
        if m.get('ScaleStep') is not None:
            self.scale_step = m.get('ScaleStep')
        return self


class DescribeScaleStrategysResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        scale_strategys: List[DescribeScaleStrategysResponseBodyScaleStrategys] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.scale_strategys = scale_strategys

    def validate(self):
        if self.scale_strategys:
            for k in self.scale_strategys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScaleStrategys'] = []
        if self.scale_strategys is not None:
            for k in self.scale_strategys:
                result['ScaleStrategys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scale_strategys = []
        if m.get('ScaleStrategys') is not None:
            for k in m.get('ScaleStrategys'):
                temp_model = DescribeScaleStrategysResponseBodyScaleStrategys()
                self.scale_strategys.append(temp_model.from_map(k))
        return self


class DescribeScaleStrategysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScaleStrategysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScaleStrategysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScanTaskProgressRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: int = None,
    ):
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeScanTaskProgressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_status: str = None,
        create_time: str = None,
    ):
        self.request_id = request_id
        self.task_status = task_status
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class DescribeScanTaskProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScanTaskProgressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScanTaskProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityEventOperationsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        security_event_id: int = None,
    ):
        self.region_id = region_id
        self.security_event_id = security_event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        return self


class DescribeSecurityEventOperationsResponseBodySecurityEventOperations(TeaModel):
    def __init__(
        self,
        operation_params: str = None,
        operation_code: str = None,
        user_can_operate: bool = None,
    ):
        self.operation_params = operation_params
        self.operation_code = operation_code
        self.user_can_operate = user_can_operate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params
        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code
        if self.user_can_operate is not None:
            result['UserCanOperate'] = self.user_can_operate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')
        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')
        if m.get('UserCanOperate') is not None:
            self.user_can_operate = m.get('UserCanOperate')
        return self


class DescribeSecurityEventOperationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_operations: List[DescribeSecurityEventOperationsResponseBodySecurityEventOperations] = None,
    ):
        self.request_id = request_id
        self.security_event_operations = security_event_operations

    def validate(self):
        if self.security_event_operations:
            for k in self.security_event_operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityEventOperations'] = []
        if self.security_event_operations is not None:
            for k in self.security_event_operations:
                result['SecurityEventOperations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_event_operations = []
        if m.get('SecurityEventOperations') is not None:
            for k in m.get('SecurityEventOperations'):
                temp_model = DescribeSecurityEventOperationsResponseBodySecurityEventOperations()
                self.security_event_operations.append(temp_model.from_map(k))
        return self


class DescribeSecurityEventOperationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityEventOperationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityEventOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityEventOperationStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: int = None,
        security_event_id: List[str] = None,
    ):
        self.region_id = region_id
        self.task_id = task_id
        self.security_event_id = security_event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        return self


class DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses(TeaModel):
    def __init__(
        self,
        status: str = None,
        security_event_id: int = None,
        error_code: str = None,
    ):
        self.status = status
        self.security_event_id = security_event_id
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DescribeSecurityEventOperationStatusResponseBody(TeaModel):
    def __init__(
        self,
        task_status: str = None,
        request_id: str = None,
        security_event_operation_statuses: List[DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses] = None,
    ):
        self.task_status = task_status
        self.request_id = request_id
        self.security_event_operation_statuses = security_event_operation_statuses

    def validate(self):
        if self.security_event_operation_statuses:
            for k in self.security_event_operation_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityEventOperationStatuses'] = []
        if self.security_event_operation_statuses is not None:
            for k in self.security_event_operation_statuses:
                result['SecurityEventOperationStatuses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_event_operation_statuses = []
        if m.get('SecurityEventOperationStatuses') is not None:
            for k in m.get('SecurityEventOperationStatuses'):
                temp_model = DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses()
                self.security_event_operation_statuses.append(temp_model.from_map(k))
        return self


class DescribeSecurityEventOperationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityEventOperationStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSecurityEventOperationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnapshotsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: str = None,
        snapshot_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id
        self.snapshot_id = snapshot_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        status: str = None,
        snapshot_type: str = None,
        snapshot_name: str = None,
        progress: str = None,
        description: str = None,
        snapshot_id: str = None,
        remain_time: int = None,
        source_disk_size: str = None,
        source_disk_type: str = None,
        desktop_id: str = None,
    ):
        self.creation_time = creation_time
        self.status = status
        self.snapshot_type = snapshot_type
        self.snapshot_name = snapshot_name
        self.progress = progress
        self.description = description
        self.snapshot_id = snapshot_id
        self.remain_time = remain_time
        self.source_disk_size = source_disk_size
        self.source_disk_type = source_disk_type
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DescribeSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        snapshots: List[DescribeSnapshotsResponseBodySnapshots] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.snapshots = snapshots

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        return self


class DescribeSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSnapshotsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventOverviewRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSuspEventOverviewResponseBody(TeaModel):
    def __init__(
        self,
        suspicious_count: int = None,
        remind_count: int = None,
        serious_count: int = None,
        request_id: str = None,
    ):
        self.suspicious_count = suspicious_count
        self.remind_count = remind_count
        self.serious_count = serious_count
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.suspicious_count is not None:
            result['SuspiciousCount'] = self.suspicious_count
        if self.remind_count is not None:
            result['RemindCount'] = self.remind_count
        if self.serious_count is not None:
            result['SeriousCount'] = self.serious_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuspiciousCount') is not None:
            self.suspicious_count = m.get('SuspiciousCount')
        if m.get('RemindCount') is not None:
            self.remind_count = m.get('RemindCount')
        if m.get('SeriousCount') is not None:
            self.serious_count = m.get('SeriousCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSuspEventOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSuspEventOverviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSuspEventOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventQuaraFilesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        status: str = None,
        office_site_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.status = status
        self.office_site_id = office_site_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSuspEventQuaraFilesResponseBodyQuaraFiles(TeaModel):
    def __init__(
        self,
        status: str = None,
        event_name: str = None,
        event_type: str = None,
        path: str = None,
        desktop_name: str = None,
        md_5: str = None,
        tag: str = None,
        desktop_id: str = None,
        id: int = None,
        modify_time: str = None,
    ):
        self.status = status
        self.event_name = event_name
        self.event_type = event_type
        self.path = path
        self.desktop_name = desktop_name
        self.md_5 = md_5
        self.tag = tag
        self.desktop_id = desktop_id
        self.id = id
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.path is not None:
            result['Path'] = self.path
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class DescribeSuspEventQuaraFilesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        quara_files: List[DescribeSuspEventQuaraFilesResponseBodyQuaraFiles] = None,
    ):
        self.current_page = current_page
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.quara_files = quara_files

    def validate(self):
        if self.quara_files:
            for k in self.quara_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['QuaraFiles'] = []
        if self.quara_files is not None:
            for k in self.quara_files:
                result['QuaraFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.quara_files = []
        if m.get('QuaraFiles') is not None:
            for k in m.get('QuaraFiles'):
                temp_model = DescribeSuspEventQuaraFilesResponseBodyQuaraFiles()
                self.quara_files.append(temp_model.from_map(k))
        return self


class DescribeSuspEventQuaraFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSuspEventQuaraFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSuspEventQuaraFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        lang: str = None,
        office_site_id: str = None,
        dealed: str = None,
        levels: str = None,
        parent_event_type: str = None,
        alarm_unique_info: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.lang = lang
        self.office_site_id = office_site_id
        self.dealed = dealed
        self.levels = levels
        self.parent_event_type = parent_event_type
        self.alarm_unique_info = alarm_unique_info
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.levels is not None:
            result['Levels'] = self.levels
        if self.parent_event_type is not None:
            result['ParentEventType'] = self.parent_event_type
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        if m.get('ParentEventType') is not None:
            self.parent_event_type = m.get('ParentEventType')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeSuspEventsResponseBodySuspEventsDetails(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        name_display: str = None,
        name: str = None,
        value_display: str = None,
    ):
        self.type = type
        self.value = value
        self.name_display = name_display
        self.name = name
        self.value_display = value_display

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.name_display is not None:
            result['NameDisplay'] = self.name_display
        if self.name is not None:
            result['Name'] = self.name
        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')
        return self


class DescribeSuspEventsResponseBodySuspEvents(TeaModel):
    def __init__(
        self,
        data_source: str = None,
        event_sub_type: str = None,
        desktop_name: str = None,
        desktop_id: str = None,
        occurrence_time: str = None,
        alarm_event_type_display: str = None,
        alarm_unique_info: str = None,
        desc: str = None,
        alarm_event_name_display: str = None,
        can_cancel_fault: bool = None,
        last_time: str = None,
        operate_msg: str = None,
        can_be_deal_on_line: str = None,
        alarm_event_type: str = None,
        event_status: int = None,
        operate_error_code: str = None,
        alarm_event_name: str = None,
        name: str = None,
        unique_info: str = None,
        level: str = None,
        id: int = None,
        details: List[DescribeSuspEventsResponseBodySuspEventsDetails] = None,
    ):
        self.data_source = data_source
        self.event_sub_type = event_sub_type
        self.desktop_name = desktop_name
        self.desktop_id = desktop_id
        self.occurrence_time = occurrence_time
        self.alarm_event_type_display = alarm_event_type_display
        self.alarm_unique_info = alarm_unique_info
        self.desc = desc
        self.alarm_event_name_display = alarm_event_name_display
        self.can_cancel_fault = can_cancel_fault
        self.last_time = last_time
        self.operate_msg = operate_msg
        self.can_be_deal_on_line = can_be_deal_on_line
        self.alarm_event_type = alarm_event_type
        self.event_status = event_status
        self.operate_error_code = operate_error_code
        self.alarm_event_name = alarm_event_name
        self.name = name
        self.unique_info = unique_info
        self.level = level
        self.id = id
        self.details = details

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.event_sub_type is not None:
            result['EventSubType'] = self.event_sub_type
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time
        if self.alarm_event_type_display is not None:
            result['AlarmEventTypeDisplay'] = self.alarm_event_type_display
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.alarm_event_name_display is not None:
            result['AlarmEventNameDisplay'] = self.alarm_event_name_display
        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.operate_msg is not None:
            result['OperateMsg'] = self.operate_msg
        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.operate_error_code is not None:
            result['OperateErrorCode'] = self.operate_error_code
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name
        if self.name is not None:
            result['Name'] = self.name
        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info
        if self.level is not None:
            result['Level'] = self.level
        if self.id is not None:
            result['Id'] = self.id
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('EventSubType') is not None:
            self.event_sub_type = m.get('EventSubType')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')
        if m.get('AlarmEventTypeDisplay') is not None:
            self.alarm_event_type_display = m.get('AlarmEventTypeDisplay')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('AlarmEventNameDisplay') is not None:
            self.alarm_event_name_display = m.get('AlarmEventNameDisplay')
        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('OperateMsg') is not None:
            self.operate_msg = m.get('OperateMsg')
        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('OperateErrorCode') is not None:
            self.operate_error_code = m.get('OperateErrorCode')
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = DescribeSuspEventsResponseBodySuspEventsDetails()
                self.details.append(temp_model.from_map(k))
        return self


class DescribeSuspEventsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        request_id: str = None,
        page_size: str = None,
        total_count: int = None,
        susp_events: List[DescribeSuspEventsResponseBodySuspEvents] = None,
    ):
        self.current_page = current_page
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.susp_events = susp_events

    def validate(self):
        if self.susp_events:
            for k in self.susp_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['SuspEvents'] = []
        if self.susp_events is not None:
            for k in self.susp_events:
                result['SuspEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.susp_events = []
        if m.get('SuspEvents') is not None:
            for k in m.get('SuspEvents'):
                temp_model = DescribeSuspEventsResponseBodySuspEvents()
                self.susp_events.append(temp_model.from_map(k))
        return self


class DescribeSuspEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSuspEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSuspEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserConnectionRecordsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
        end_user_id: str = None,
        end_user_type: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id
        self.end_user_id = end_user_id
        self.end_user_type = end_user_type
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_type is not None:
            result['EndUserType'] = self.end_user_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserType') is not None:
            self.end_user_type = m.get('EndUserType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeUserConnectionRecordsResponseBodyConnectionRecords(TeaModel):
    def __init__(
        self,
        connection_record_id: str = None,
        connect_start_time: str = None,
        desktop_name: str = None,
        connect_duration: str = None,
        connect_end_time: str = None,
        desktop_id: str = None,
    ):
        self.connection_record_id = connection_record_id
        self.connect_start_time = connect_start_time
        self.desktop_name = desktop_name
        self.connect_duration = connect_duration
        self.connect_end_time = connect_end_time
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_record_id is not None:
            result['ConnectionRecordId'] = self.connection_record_id
        if self.connect_start_time is not None:
            result['ConnectStartTime'] = self.connect_start_time
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration
        if self.connect_end_time is not None:
            result['ConnectEndTime'] = self.connect_end_time
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionRecordId') is not None:
            self.connection_record_id = m.get('ConnectionRecordId')
        if m.get('ConnectStartTime') is not None:
            self.connect_start_time = m.get('ConnectStartTime')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')
        if m.get('ConnectEndTime') is not None:
            self.connect_end_time = m.get('ConnectEndTime')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DescribeUserConnectionRecordsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        connection_records: List[DescribeUserConnectionRecordsResponseBodyConnectionRecords] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.connection_records = connection_records

    def validate(self):
        if self.connection_records:
            for k in self.connection_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ConnectionRecords'] = []
        if self.connection_records is not None:
            for k in self.connection_records:
                result['ConnectionRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.connection_records = []
        if m.get('ConnectionRecords') is not None:
            for k in m.get('ConnectionRecords'):
                temp_model = DescribeUserConnectionRecordsResponseBodyConnectionRecords()
                self.connection_records.append(temp_model.from_map(k))
        return self


class DescribeUserConnectionRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserConnectionRecordsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserConnectionRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersInGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeUsersInGroupResponseBodyEndUsers(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        end_user_email: str = None,
        desktop_name: str = None,
        connection_status: str = None,
        desktop_id: str = None,
        end_user_type: str = None,
        end_user_phone: str = None,
        end_user_name: str = None,
    ):
        self.end_user_id = end_user_id
        self.end_user_email = end_user_email
        self.desktop_name = desktop_name
        self.connection_status = connection_status
        self.desktop_id = desktop_id
        self.end_user_type = end_user_type
        self.end_user_phone = end_user_phone
        self.end_user_name = end_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_email is not None:
            result['EndUserEmail'] = self.end_user_email
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_type is not None:
            result['EndUserType'] = self.end_user_type
        if self.end_user_phone is not None:
            result['EndUserPhone'] = self.end_user_phone
        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserEmail') is not None:
            self.end_user_email = m.get('EndUserEmail')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserType') is not None:
            self.end_user_type = m.get('EndUserType')
        if m.get('EndUserPhone') is not None:
            self.end_user_phone = m.get('EndUserPhone')
        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')
        return self


class DescribeUsersInGroupResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users_count: int = None,
        online_users_count: int = None,
        end_users: List[DescribeUsersInGroupResponseBodyEndUsers] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.users_count = users_count
        self.online_users_count = online_users_count
        self.end_users = end_users

    def validate(self):
        if self.end_users:
            for k in self.end_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users_count is not None:
            result['UsersCount'] = self.users_count
        if self.online_users_count is not None:
            result['OnlineUsersCount'] = self.online_users_count
        result['EndUsers'] = []
        if self.end_users is not None:
            for k in self.end_users:
                result['EndUsers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsersCount') is not None:
            self.users_count = m.get('UsersCount')
        if m.get('OnlineUsersCount') is not None:
            self.online_users_count = m.get('OnlineUsersCount')
        self.end_users = []
        if m.get('EndUsers') is not None:
            for k in m.get('EndUsers'):
                temp_model = DescribeUsersInGroupResponseBodyEndUsers()
                self.end_users.append(temp_model.from_map(k))
        return self


class DescribeUsersInGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUsersInGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUsersInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualMFADevicesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        directory_id: str = None,
        office_site_id: str = None,
        end_user_id: List[str] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.directory_id = directory_id
        self.office_site_id = office_site_id
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class DescribeVirtualMFADevicesResponseBodyVirtualMFADevices(TeaModel):
    def __init__(
        self,
        serial_number: str = None,
        gmt_unlock: str = None,
        end_user_id: str = None,
        consecutive_fails: int = None,
        office_site_id: str = None,
        status: str = None,
        directory_id: str = None,
        gmt_enabled: str = None,
    ):
        self.serial_number = serial_number
        self.gmt_unlock = gmt_unlock
        self.end_user_id = end_user_id
        self.consecutive_fails = consecutive_fails
        self.office_site_id = office_site_id
        self.status = status
        self.directory_id = directory_id
        self.gmt_enabled = gmt_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.gmt_unlock is not None:
            result['GmtUnlock'] = self.gmt_unlock
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.consecutive_fails is not None:
            result['ConsecutiveFails'] = self.consecutive_fails
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.status is not None:
            result['status'] = self.status
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.gmt_enabled is not None:
            result['GmtEnabled'] = self.gmt_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('GmtUnlock') is not None:
            self.gmt_unlock = m.get('GmtUnlock')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ConsecutiveFails') is not None:
            self.consecutive_fails = m.get('ConsecutiveFails')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('GmtEnabled') is not None:
            self.gmt_enabled = m.get('GmtEnabled')
        return self


class DescribeVirtualMFADevicesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        virtual_mfadevices: List[DescribeVirtualMFADevicesResponseBodyVirtualMFADevices] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.virtual_mfadevices = virtual_mfadevices

    def validate(self):
        if self.virtual_mfadevices:
            for k in self.virtual_mfadevices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VirtualMFADevices'] = []
        if self.virtual_mfadevices is not None:
            for k in self.virtual_mfadevices:
                result['VirtualMFADevices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.virtual_mfadevices = []
        if m.get('VirtualMFADevices') is not None:
            for k in m.get('VirtualMFADevices'):
                temp_model = DescribeVirtualMFADevicesResponseBodyVirtualMFADevices()
                self.virtual_mfadevices.append(temp_model.from_map(k))
        return self


class DescribeVirtualMFADevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVirtualMFADevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVirtualMFADevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulDetailsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        lang: str = None,
        type: str = None,
        name: str = None,
        alias_name: str = None,
    ):
        self.region_id = region_id
        self.lang = lang
        self.type = type
        self.name = name
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class DescribeVulDetailsResponseBodyCves(TeaModel):
    def __init__(
        self,
        cve_id: str = None,
        summary: str = None,
        title: str = None,
        cvss_score: str = None,
    ):
        self.cve_id = cve_id
        self.summary = summary
        self.title = title
        self.cvss_score = cvss_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        if self.cvss_score is not None:
            result['CvssScore'] = self.cvss_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CvssScore') is not None:
            self.cvss_score = m.get('CvssScore')
        return self


class DescribeVulDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cves: List[DescribeVulDetailsResponseBodyCves] = None,
    ):
        self.request_id = request_id
        self.cves = cves

    def validate(self):
        if self.cves:
            for k in self.cves:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Cves'] = []
        if self.cves is not None:
            for k in self.cves:
                result['Cves'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.cves = []
        if m.get('Cves') is not None:
            for k in m.get('Cves'):
                temp_model = DescribeVulDetailsResponseBodyCves()
                self.cves.append(temp_model.from_map(k))
        return self


class DescribeVulDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVulDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        lang: str = None,
        type: str = None,
        office_site_id: str = None,
        necessity: str = None,
        alias_name: str = None,
        dealed: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.lang = lang
        self.type = type
        self.office_site_id = office_site_id
        self.necessity = necessity
        self.alias_name = alias_name
        self.dealed = dealed
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList(TeaModel):
    def __init__(
        self,
        path: str = None,
        update_cmd: str = None,
        name: str = None,
        full_version: str = None,
        match_detail: str = None,
    ):
        self.path = path
        self.update_cmd = update_cmd
        self.name = name
        self.full_version = full_version
        self.match_detail = match_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.update_cmd is not None:
            result['UpdateCmd'] = self.update_cmd
        if self.name is not None:
            result['Name'] = self.name
        if self.full_version is not None:
            result['FullVersion'] = self.full_version
        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdateCmd') is not None:
            self.update_cmd = m.get('UpdateCmd')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FullVersion') is not None:
            self.full_version = m.get('FullVersion')
        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')
        return self


class DescribeVulListResponseBodyVulRecordsExtendContentJson(TeaModel):
    def __init__(
        self,
        rpm_entity_list: List[DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList] = None,
    ):
        self.rpm_entity_list = rpm_entity_list

    def validate(self):
        if self.rpm_entity_list:
            for k in self.rpm_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RpmEntityList'] = []
        if self.rpm_entity_list is not None:
            for k in self.rpm_entity_list:
                result['RpmEntityList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rpm_entity_list = []
        if m.get('RpmEntityList') is not None:
            for k in m.get('RpmEntityList'):
                temp_model = DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList()
                self.rpm_entity_list.append(temp_model.from_map(k))
        return self


class DescribeVulListResponseBodyVulRecords(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: str = None,
        modify_ts: int = None,
        desktop_name: str = None,
        result_code: str = None,
        tag: str = None,
        desktop_id: str = None,
        related: str = None,
        last_ts: int = None,
        first_ts: int = None,
        necessity: str = None,
        repair_ts: int = None,
        online: bool = None,
        result_message: str = None,
        os_version: str = None,
        alias_name: str = None,
        name: str = None,
        extend_content_json: DescribeVulListResponseBodyVulRecordsExtendContentJson = None,
    ):
        self.status = status
        self.type = type
        self.modify_ts = modify_ts
        self.desktop_name = desktop_name
        self.result_code = result_code
        self.tag = tag
        self.desktop_id = desktop_id
        self.related = related
        self.last_ts = last_ts
        self.first_ts = first_ts
        self.necessity = necessity
        self.repair_ts = repair_ts
        self.online = online
        self.result_message = result_message
        self.os_version = os_version
        self.alias_name = alias_name
        self.name = name
        self.extend_content_json = extend_content_json

    def validate(self):
        if self.extend_content_json:
            self.extend_content_json.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.modify_ts is not None:
            result['ModifyTs'] = self.modify_ts
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.related is not None:
            result['Related'] = self.related
        if self.last_ts is not None:
            result['LastTs'] = self.last_ts
        if self.first_ts is not None:
            result['FirstTs'] = self.first_ts
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.repair_ts is not None:
            result['RepairTs'] = self.repair_ts
        if self.online is not None:
            result['Online'] = self.online
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        if self.extend_content_json is not None:
            result['ExtendContentJson'] = self.extend_content_json.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ModifyTs') is not None:
            self.modify_ts = m.get('ModifyTs')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Related') is not None:
            self.related = m.get('Related')
        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')
        if m.get('FirstTs') is not None:
            self.first_ts = m.get('FirstTs')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('RepairTs') is not None:
            self.repair_ts = m.get('RepairTs')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExtendContentJson') is not None:
            temp_model = DescribeVulListResponseBodyVulRecordsExtendContentJson()
            self.extend_content_json = temp_model.from_map(m['ExtendContentJson'])
        return self


class DescribeVulListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        vul_records: List[DescribeVulListResponseBodyVulRecords] = None,
    ):
        self.current_page = current_page
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.vul_records = vul_records

    def validate(self):
        if self.vul_records:
            for k in self.vul_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VulRecords'] = []
        if self.vul_records is not None:
            for k in self.vul_records:
                result['VulRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vul_records = []
        if m.get('VulRecords') is not None:
            for k in m.get('VulRecords'):
                temp_model = DescribeVulListResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k))
        return self


class DescribeVulListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVulListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulOverviewRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeVulOverviewResponseBody(TeaModel):
    def __init__(
        self,
        nntf_count: int = None,
        later_count: int = None,
        request_id: str = None,
        asap_count: int = None,
    ):
        self.nntf_count = nntf_count
        self.later_count = later_count
        self.request_id = request_id
        self.asap_count = asap_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        return self


class DescribeVulOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVulOverviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVulOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[DescribeZonesResponseBodyZones] = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZonesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachCenRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: str = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class DetachCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoCheckResourceRequest(TeaModel):
    def __init__(
        self,
        invoker: str = None,
        pk: str = None,
        bid: str = None,
        hid: int = None,
        country: str = None,
        task_identifier: str = None,
        task_extra_data: str = None,
        gmt_wakeup: str = None,
        region_id: str = None,
    ):
        self.invoker = invoker
        self.pk = pk
        self.bid = bid
        self.hid = hid
        self.country = country
        self.task_identifier = task_identifier
        self.task_extra_data = task_extra_data
        self.gmt_wakeup = gmt_wakeup
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.country is not None:
            result['Country'] = self.country
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DoCheckResourceResponseBody(TeaModel):
    def __init__(
        self,
        gmt_wakeup: str = None,
        hid: int = None,
        message: str = None,
        task_identifier: str = None,
        request_id: str = None,
        success: bool = None,
        url: str = None,
        interrupt: bool = None,
        invoker: str = None,
        task_extra_data: str = None,
        country: str = None,
        prompt: str = None,
        level: int = None,
        pk: str = None,
        bid: str = None,
    ):
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.message = message
        self.task_identifier = task_identifier
        self.request_id = request_id
        self.success = success
        self.url = url
        self.interrupt = interrupt
        self.invoker = invoker
        self.task_extra_data = task_extra_data
        self.country = country
        self.prompt = prompt
        self.level = level
        self.pk = pk
        self.bid = bid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.message is not None:
            result['Message'] = self.message
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.country is not None:
            result['Country'] = self.country
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.level is not None:
            result['Level'] = self.level
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        return self


class DoCheckResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoCheckResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DoCheckResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoLogicalDeleteResourceRequest(TeaModel):
    def __init__(
        self,
        invoker: str = None,
        pk: str = None,
        bid: str = None,
        hid: int = None,
        country: str = None,
        task_identifier: str = None,
        task_extra_data: str = None,
        gmt_wakeup: str = None,
        region_id: str = None,
    ):
        self.invoker = invoker
        self.pk = pk
        self.bid = bid
        self.hid = hid
        self.country = country
        self.task_identifier = task_identifier
        self.task_extra_data = task_extra_data
        self.gmt_wakeup = gmt_wakeup
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.country is not None:
            result['Country'] = self.country
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DoLogicalDeleteResourceResponseBody(TeaModel):
    def __init__(
        self,
        gmt_wakeup: str = None,
        hid: int = None,
        message: str = None,
        task_identifier: str = None,
        request_id: str = None,
        invoker: str = None,
        task_extra_data: str = None,
        country: str = None,
        pk: str = None,
        bid: str = None,
        success: bool = None,
        interrupt: bool = None,
    ):
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.message = message
        self.task_identifier = task_identifier
        self.request_id = request_id
        self.invoker = invoker
        self.task_extra_data = task_extra_data
        self.country = country
        self.pk = pk
        self.bid = bid
        self.success = success
        self.interrupt = interrupt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.message is not None:
            result['Message'] = self.message
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.country is not None:
            result['Country'] = self.country
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.success is not None:
            result['Success'] = self.success
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        return self


class DoLogicalDeleteResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoLogicalDeleteResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DoLogicalDeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoPhysicalDeleteResourceRequest(TeaModel):
    def __init__(
        self,
        invoker: str = None,
        pk: str = None,
        bid: str = None,
        hid: int = None,
        country: str = None,
        task_identifier: str = None,
        task_extra_data: str = None,
        gmt_wakeup: str = None,
        region_id: str = None,
    ):
        self.invoker = invoker
        self.pk = pk
        self.bid = bid
        self.hid = hid
        self.country = country
        self.task_identifier = task_identifier
        self.task_extra_data = task_extra_data
        self.gmt_wakeup = gmt_wakeup
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.country is not None:
            result['Country'] = self.country
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DoPhysicalDeleteResourceResponseBody(TeaModel):
    def __init__(
        self,
        gmt_wakeup: str = None,
        hid: int = None,
        message: str = None,
        task_identifier: str = None,
        request_id: str = None,
        invoker: str = None,
        task_extra_data: str = None,
        country: str = None,
        pk: str = None,
        bid: str = None,
        success: bool = None,
        interrupt: bool = None,
    ):
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.message = message
        self.task_identifier = task_identifier
        self.request_id = request_id
        self.invoker = invoker
        self.task_extra_data = task_extra_data
        self.country = country
        self.pk = pk
        self.bid = bid
        self.success = success
        self.interrupt = interrupt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.message is not None:
            result['Message'] = self.message
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.country is not None:
            result['Country'] = self.country
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.success is not None:
            result['Success'] = self.success
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        return self


class DoPhysicalDeleteResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoPhysicalDeleteResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DoPhysicalDeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionTicketRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        instance_id: str = None,
        user_name: str = None,
        password: str = None,
        task_id: str = None,
        desktop_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.instance_id = instance_id
        self.user_name = user_name
        self.password = password
        self.task_id = task_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class GetConnectionTicketResponseBody(TeaModel):
    def __init__(
        self,
        ticket: str = None,
        task_id: str = None,
        request_id: str = None,
        task_status: str = None,
    ):
        self.ticket = ticket
        self.task_id = task_id
        self.request_id = request_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConnectionTicketResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDesktopGroupDetailRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        return self


class GetDesktopGroupDetailResponseBodyDesktops(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        pay_type: str = None,
        policy_group_name: str = None,
        creator: str = None,
        max_desktops_count: int = None,
        allow_auto_setup: int = None,
        res_type: int = None,
        system_disk_size: int = None,
        policy_group_id: str = None,
        own_bundle_id: str = None,
        gpu_count: float = None,
        allow_buffer_count: int = None,
        memory: int = None,
        gpu_spec: str = None,
        directory_id: str = None,
        own_bundle_name: str = None,
        data_disk_category: str = None,
        desktop_group_name: str = None,
        system_disk_category: str = None,
        office_site_id: str = None,
        keep_duration: int = None,
        min_desktops_count: int = None,
        data_disk_size: str = None,
        desktop_group_id: str = None,
        office_site_name: str = None,
        directory_type: str = None,
        cpu: int = None,
        expired_time: str = None,
        comments: str = None,
        office_site_type: str = None,
    ):
        self.creation_time = creation_time
        self.pay_type = pay_type
        self.policy_group_name = policy_group_name
        self.creator = creator
        self.max_desktops_count = max_desktops_count
        self.allow_auto_setup = allow_auto_setup
        self.res_type = res_type
        self.system_disk_size = system_disk_size
        self.policy_group_id = policy_group_id
        self.own_bundle_id = own_bundle_id
        self.gpu_count = gpu_count
        self.allow_buffer_count = allow_buffer_count
        self.memory = memory
        self.gpu_spec = gpu_spec
        self.directory_id = directory_id
        self.own_bundle_name = own_bundle_name
        self.data_disk_category = data_disk_category
        self.desktop_group_name = desktop_group_name
        self.system_disk_category = system_disk_category
        self.office_site_id = office_site_id
        self.keep_duration = keep_duration
        self.min_desktops_count = min_desktops_count
        self.data_disk_size = data_disk_size
        self.desktop_group_id = desktop_group_id
        self.office_site_name = office_site_name
        self.directory_type = directory_type
        self.cpu = cpu
        self.expired_time = expired_time
        self.comments = comments
        self.office_site_type = office_site_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.own_bundle_name is not None:
            result['OwnBundleName'] = self.own_bundle_name
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OwnBundleName') is not None:
            self.own_bundle_name = m.get('OwnBundleName')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        return self


class GetDesktopGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        desktops: List[GetDesktopGroupDetailResponseBodyDesktops] = None,
    ):
        self.request_id = request_id
        self.desktops = desktops

    def validate(self):
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Desktops'] = []
        if self.desktops is not None:
            for k in self.desktops:
                result['Desktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.desktops = []
        if m.get('Desktops') is not None:
            for k in m.get('Desktops'):
                temp_model = GetDesktopGroupDetailResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k))
        return self


class GetDesktopGroupDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDesktopGroupDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDesktopGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDesktopUsersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: str = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class GetDesktopUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        end_user_ids: List[str] = None,
    ):
        self.request_id = request_id
        self.end_user_ids = end_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class GetDesktopUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDesktopUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDesktopUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDirectorySsoStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: str = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        return self


class GetDirectorySsoStatusResponseBody(TeaModel):
    def __init__(
        self,
        sso_status: bool = None,
        request_id: str = None,
    ):
        self.sso_status = sso_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sso_status is not None:
            result['SsoStatus'] = self.sso_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SsoStatus') is not None:
            self.sso_status = m.get('SsoStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDirectorySsoStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDirectorySsoStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDirectorySsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficeSiteSsoStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: str = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class GetOfficeSiteSsoStatusResponseBody(TeaModel):
    def __init__(
        self,
        sso_status: bool = None,
        request_id: str = None,
    ):
        self.sso_status = sso_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sso_status is not None:
            result['SsoStatus'] = self.sso_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SsoStatus') is not None:
            self.sso_status = m.get('SsoStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOfficeSiteSsoStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOfficeSiteSsoStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOfficeSiteSsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpMetadataRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: str = None,
        office_site_id: str = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class GetSpMetadataResponseBody(TeaModel):
    def __init__(
        self,
        sp_metadata: str = None,
        request_id: str = None,
    ):
        self.sp_metadata = sp_metadata
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sp_metadata is not None:
            result['SpMetadata'] = self.sp_metadata
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpMetadata') is not None:
            self.sp_metadata = m.get('SpMetadata')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSpMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSpMetadataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSpMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HandleSecurityEventsRequestSecurityEvent(TeaModel):
    def __init__(
        self,
        security_event_id: str = None,
        desktop_id: str = None,
    ):
        self.security_event_id = security_event_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class HandleSecurityEventsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        operation_code: str = None,
        operation_params: str = None,
        security_event: List[HandleSecurityEventsRequestSecurityEvent] = None,
    ):
        self.region_id = region_id
        self.operation_code = operation_code
        self.operation_params = operation_params
        self.security_event = security_event

    def validate(self):
        if self.security_event:
            for k in self.security_event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code
        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params
        result['SecurityEvent'] = []
        if self.security_event is not None:
            for k in self.security_event:
                result['SecurityEvent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')
        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')
        self.security_event = []
        if m.get('SecurityEvent') is not None:
            for k in m.get('SecurityEvent'):
                temp_model = HandleSecurityEventsRequestSecurityEvent()
                self.security_event.append(temp_model.from_map(k))
        return self


class HandleSecurityEventsResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class HandleSecurityEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HandleSecurityEventsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = HandleSecurityEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectoryUsersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        filter: str = None,
        directory_id: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.region_id = region_id
        self.filter = filter
        self.directory_id = directory_id
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDirectoryUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        end_user: str = None,
    ):
        self.end_user = end_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user is not None:
            result['EndUser'] = self.end_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUser') is not None:
            self.end_user = m.get('EndUser')
        return self


class ListDirectoryUsersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users: List[ListDirectoryUsersResponseBodyUsers] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListDirectoryUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListDirectoryUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDirectoryUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDirectoryUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfficeSiteOverviewRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        force_refresh: bool = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: List[str] = None,
    ):
        self.region_id = region_id
        self.force_refresh = force_refresh
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.force_refresh is not None:
            result['ForceRefresh'] = self.force_refresh
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ForceRefresh') is not None:
            self.force_refresh = m.get('ForceRefresh')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults(TeaModel):
    def __init__(
        self,
        office_site_status: str = None,
        total_eds_count: int = None,
        will_expired_eds_count: int = None,
        office_site_id: str = None,
        running_eds_count: int = None,
        office_site_name: str = None,
        has_expired_eds_count: int = None,
        region_id: str = None,
    ):
        self.office_site_status = office_site_status
        self.total_eds_count = total_eds_count
        self.will_expired_eds_count = will_expired_eds_count
        self.office_site_id = office_site_id
        self.running_eds_count = running_eds_count
        self.office_site_name = office_site_name
        self.has_expired_eds_count = has_expired_eds_count
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_status is not None:
            result['OfficeSiteStatus'] = self.office_site_status
        if self.total_eds_count is not None:
            result['TotalEdsCount'] = self.total_eds_count
        if self.will_expired_eds_count is not None:
            result['WillExpiredEdsCount'] = self.will_expired_eds_count
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.running_eds_count is not None:
            result['RunningEdsCount'] = self.running_eds_count
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.has_expired_eds_count is not None:
            result['HasExpiredEdsCount'] = self.has_expired_eds_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteStatus') is not None:
            self.office_site_status = m.get('OfficeSiteStatus')
        if m.get('TotalEdsCount') is not None:
            self.total_eds_count = m.get('TotalEdsCount')
        if m.get('WillExpiredEdsCount') is not None:
            self.will_expired_eds_count = m.get('WillExpiredEdsCount')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RunningEdsCount') is not None:
            self.running_eds_count = m.get('RunningEdsCount')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('HasExpiredEdsCount') is not None:
            self.has_expired_eds_count = m.get('HasExpiredEdsCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOfficeSiteOverviewResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        office_site_overview_results: List[ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.office_site_overview_results = office_site_overview_results

    def validate(self):
        if self.office_site_overview_results:
            for k in self.office_site_overview_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OfficeSiteOverviewResults'] = []
        if self.office_site_overview_results is not None:
            for k in self.office_site_overview_results:
                result['OfficeSiteOverviewResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.office_site_overview_results = []
        if m.get('OfficeSiteOverviewResults') is not None:
            for k in m.get('OfficeSiteOverviewResults'):
                temp_model = ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults()
                self.office_site_overview_results.append(temp_model.from_map(k))
        return self


class ListOfficeSiteOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOfficeSiteOverviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOfficeSiteOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfficeSiteUsersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        filter: str = None,
        office_site_id: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.region_id = region_id
        self.filter = filter
        self.office_site_id = office_site_id
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListOfficeSiteUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        end_user: str = None,
    ):
        self.end_user = end_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user is not None:
            result['EndUser'] = self.end_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUser') is not None:
            self.end_user = m.get('EndUser')
        return self


class ListOfficeSiteUsersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users: List[ListOfficeSiteUsersResponseBodyUsers] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListOfficeSiteUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListOfficeSiteUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOfficeSiteUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOfficeSiteUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.max_results = max_results
        self.next_token = next_token
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        resource_type: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        serial_number: str = None,
    ):
        self.region_id = region_id
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class LockVirtualMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LockVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LockVirtualMFADeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LockVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyADConnectorDirectoryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: str = None,
        domain_name: str = None,
        domain_user_name: str = None,
        domain_password: str = None,
        directory_name: str = None,
        sub_domain_name: str = None,
        mfa_enabled: bool = None,
        dns_address: List[str] = None,
        sub_domain_dns_address: List[str] = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id
        self.domain_name = domain_name
        self.domain_user_name = domain_user_name
        self.domain_password = domain_password
        self.directory_name = directory_name
        self.sub_domain_name = sub_domain_name
        self.mfa_enabled = mfa_enabled
        self.dns_address = dns_address
        self.sub_domain_dns_address = sub_domain_dns_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        return self


class ModifyADConnectorDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyADConnectorDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyADConnectorDirectoryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyADConnectorDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyADConnectorOfficeSiteRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: str = None,
        domain_name: str = None,
        domain_user_name: str = None,
        domain_password: str = None,
        office_site_name: str = None,
        sub_domain_name: str = None,
        mfa_enabled: bool = None,
        dns_address: List[str] = None,
        sub_domain_dns_address: List[str] = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id
        self.domain_name = domain_name
        self.domain_user_name = domain_user_name
        self.domain_password = domain_password
        self.office_site_name = office_site_name
        self.sub_domain_name = sub_domain_name
        self.mfa_enabled = mfa_enabled
        self.dns_address = dns_address
        self.sub_domain_dns_address = sub_domain_dns_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        return self


class ModifyADConnectorOfficeSiteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyADConnectorOfficeSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyADConnectorOfficeSiteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyADConnectorOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBundleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        bundle_id: str = None,
        image_id: str = None,
        bundle_name: str = None,
        description: str = None,
    ):
        self.region_id = region_id
        self.bundle_id = bundle_id
        self.image_id = image_id
        self.bundle_name = bundle_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyBundleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyBundleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBundleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
        own_bundle_id: str = None,
        policy_group_id: str = None,
        desktop_group_name: str = None,
        scale_strategy_id: str = None,
        keep_duration: int = None,
        comments: str = None,
        min_desktops_count: int = None,
        max_desktops_count: int = None,
        allow_auto_setup: int = None,
        allow_buffer_count: int = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id
        self.own_bundle_id = own_bundle_id
        self.policy_group_id = policy_group_id
        self.desktop_group_name = desktop_group_name
        self.scale_strategy_id = scale_strategy_id
        self.keep_duration = keep_duration
        self.comments = comments
        self.min_desktops_count = min_desktops_count
        self.max_desktops_count = max_desktops_count
        self.allow_auto_setup = allow_auto_setup
        self.allow_buffer_count = allow_buffer_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup
        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')
        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')
        return self


class ModifyDesktopGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDesktopGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopNameRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        new_desktop_name: str = None,
        desktop_id: str = None,
    ):
        self.region_id = region_id
        self.new_desktop_name = new_desktop_name
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.new_desktop_name is not None:
            result['NewDesktopName'] = self.new_desktop_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NewDesktopName') is not None:
            self.new_desktop_name = m.get('NewDesktopName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDesktopNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDesktopNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopPolicysRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        clipboard: str = None,
        local_drive: str = None,
        usb_redirect: str = None,
        watermark: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.clipboard = clipboard
        self.local_drive = local_drive
        self.usb_redirect = usb_redirect
        self.watermark = watermark
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopPolicysResponseBodyResults(TeaModel):
    def __init__(
        self,
        success: str = None,
        code: str = None,
        message: str = None,
        desktop_id: str = None,
    ):
        self.success = success
        self.code = code
        self.message = message
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopPolicysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[ModifyDesktopPolicysResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ModifyDesktopPolicysResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class ModifyDesktopPolicysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDesktopPolicysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopPolicysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopSpecRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: str = None,
        desktop_type: str = None,
        root_disk_size_gib: int = None,
        user_disk_size_gib: int = None,
        auto_pay: bool = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id
        self.desktop_type = desktop_type
        self.root_disk_size_gib = root_disk_size_gib
        self.user_disk_size_gib = user_disk_size_gib
        self.auto_pay = auto_pay

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        return self


class ModifyDesktopSpecResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDesktopSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDesktopSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopsPolicyGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        policy_group_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.policy_group_id = policy_group_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopsPolicyGroupResponseBodyModifyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        desktop_id: str = None,
    ):
        self.code = code
        self.message = message
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class ModifyDesktopsPolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        modify_results: List[ModifyDesktopsPolicyGroupResponseBodyModifyResults] = None,
    ):
        self.request_id = request_id
        self.modify_results = modify_results

    def validate(self):
        if self.modify_results:
            for k in self.modify_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ModifyResults'] = []
        if self.modify_results is not None:
            for k in self.modify_results:
                result['ModifyResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.modify_results = []
        if m.get('ModifyResults') is not None:
            for k in m.get('ModifyResults'):
                temp_model = ModifyDesktopsPolicyGroupResponseBodyModifyResults()
                self.modify_results.append(temp_model.from_map(k))
        return self


class ModifyDesktopsPolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDesktopsPolicyGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDesktopsPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEntitlementRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: str = None,
        end_user_id: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id
        self.end_user_id = end_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class ModifyEntitlementResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyEntitlementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyEntitlementResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyEntitlementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        image_id: str = None,
        name: str = None,
        description: str = None,
    ):
        self.region_id = region_id
        self.image_id = image_id
        self.name = name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyImageAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyImageAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyImageAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyImageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNASDefaultMountTargetRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        file_system_id: str = None,
        mount_target_domain: str = None,
    ):
        self.region_id = region_id
        self.file_system_id = file_system_id
        self.mount_target_domain = mount_target_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        return self


class ModifyNASDefaultMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNASDefaultMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyNASDefaultMountTargetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNASDefaultMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkPackageRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        network_package_id: str = None,
        bandwidth: int = None,
    ):
        self.region_id = region_id
        self.network_package_id = network_package_id
        self.bandwidth = bandwidth

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class ModifyNetworkPackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNetworkPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyNetworkPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNetworkPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkPackageEnabledRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        network_package_id: str = None,
        enabled: bool = None,
    ):
        self.region_id = region_id
        self.network_package_id = network_package_id
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ModifyNetworkPackageEnabledResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNetworkPackageEnabledResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyNetworkPackageEnabledResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyNetworkPackageEnabledResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfficeSiteAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: str = None,
        desktop_access_type: str = None,
        office_site_name: str = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id
        self.desktop_access_type = desktop_access_type
        self.office_site_name = office_site_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        return self


class ModifyOfficeSiteAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyOfficeSiteAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyOfficeSiteAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOfficeSiteAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfficeSiteCrossDesktopAccessRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: str = None,
        enable_cross_desktop_access: bool = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id
        self.enable_cross_desktop_access = enable_cross_desktop_access

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')
        return self


class ModifyOfficeSiteCrossDesktopAccessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyOfficeSiteCrossDesktopAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyOfficeSiteCrossDesktopAccessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOfficeSiteCrossDesktopAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfficeSiteMfaEnabledRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: str = None,
        mfa_enabled: bool = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id
        self.mfa_enabled = mfa_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        return self


class ModifyOfficeSiteMfaEnabledResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyOfficeSiteMfaEnabledResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyOfficeSiteMfaEnabledResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOfficeSiteMfaEnabledResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOperateVulRequestVulInfo(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        tag: str = None,
        name: str = None,
    ):
        self.desktop_id = desktop_id
        self.tag = tag
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyOperateVulRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
        operate_type: str = None,
        reason: str = None,
        vul_info: List[ModifyOperateVulRequestVulInfo] = None,
    ):
        self.region_id = region_id
        self.type = type
        self.operate_type = operate_type
        self.reason = reason
        self.vul_info = vul_info

    def validate(self):
        if self.vul_info:
            for k in self.vul_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.reason is not None:
            result['Reason'] = self.reason
        result['VulInfo'] = []
        if self.vul_info is not None:
            for k in self.vul_info:
                result['VulInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        self.vul_info = []
        if m.get('VulInfo') is not None:
            for k in m.get('VulInfo'):
                temp_model = ModifyOperateVulRequestVulInfo()
                self.vul_info.append(temp_model.from_map(k))
        return self


class ModifyOperateVulResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyOperateVulResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyOperateVulResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOperateVulResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule(TeaModel):
    def __init__(
        self,
        type: str = None,
        policy: str = None,
        port_range: str = None,
        description: str = None,
        ip_protocol: str = None,
        priority: str = None,
        cidr_ip: str = None,
    ):
        self.type = type
        self.policy = policy
        self.port_range = port_range
        self.description = description
        self.ip_protocol = ip_protocol
        self.priority = priority
        self.cidr_ip = cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class ModifyPolicyGroupRequestRevokeSecurityPolicyRule(TeaModel):
    def __init__(
        self,
        type: str = None,
        policy: str = None,
        port_range: str = None,
        description: str = None,
        ip_protocol: str = None,
        priority: str = None,
        cidr_ip: str = None,
    ):
        self.type = type
        self.policy = policy
        self.port_range = port_range
        self.description = description
        self.ip_protocol = ip_protocol
        self.priority = priority
        self.cidr_ip = cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class ModifyPolicyGroupRequestAuthorizeAccessPolicyRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        cidr_ip: str = None,
    ):
        self.description = description
        self.cidr_ip = cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class ModifyPolicyGroupRequestRevokeAccessPolicyRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        cidr_ip: str = None,
    ):
        self.description = description
        self.cidr_ip = cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        return self


class ModifyPolicyGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        policy_group_id: str = None,
        name: str = None,
        clipboard: str = None,
        local_drive: str = None,
        usb_redirect: str = None,
        visual_quality: str = None,
        html_5access: str = None,
        html_5file_transfer: str = None,
        watermark: str = None,
        watermark_type: str = None,
        watermark_custom_text: str = None,
        watermark_transparency: str = None,
        preempt_login: str = None,
        domain_list: str = None,
        preempt_login_user: List[str] = None,
        authorize_security_policy_rule: List[ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule] = None,
        revoke_security_policy_rule: List[ModifyPolicyGroupRequestRevokeSecurityPolicyRule] = None,
        authorize_access_policy_rule: List[ModifyPolicyGroupRequestAuthorizeAccessPolicyRule] = None,
        revoke_access_policy_rule: List[ModifyPolicyGroupRequestRevokeAccessPolicyRule] = None,
    ):
        self.region_id = region_id
        self.policy_group_id = policy_group_id
        self.name = name
        self.clipboard = clipboard
        self.local_drive = local_drive
        self.usb_redirect = usb_redirect
        self.visual_quality = visual_quality
        self.html_5access = html_5access
        self.html_5file_transfer = html_5file_transfer
        self.watermark = watermark
        self.watermark_type = watermark_type
        self.watermark_custom_text = watermark_custom_text
        self.watermark_transparency = watermark_transparency
        self.preempt_login = preempt_login
        self.domain_list = domain_list
        self.preempt_login_user = preempt_login_user
        self.authorize_security_policy_rule = authorize_security_policy_rule
        self.revoke_security_policy_rule = revoke_security_policy_rule
        self.authorize_access_policy_rule = authorize_access_policy_rule
        self.revoke_access_policy_rule = revoke_access_policy_rule

    def validate(self):
        if self.authorize_security_policy_rule:
            for k in self.authorize_security_policy_rule:
                if k:
                    k.validate()
        if self.revoke_security_policy_rule:
            for k in self.revoke_security_policy_rule:
                if k:
                    k.validate()
        if self.authorize_access_policy_rule:
            for k in self.authorize_access_policy_rule:
                if k:
                    k.validate()
        if self.revoke_access_policy_rule:
            for k in self.revoke_access_policy_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality
        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.preempt_login_user is not None:
            result['PreemptLoginUser'] = self.preempt_login_user
        result['AuthorizeSecurityPolicyRule'] = []
        if self.authorize_security_policy_rule is not None:
            for k in self.authorize_security_policy_rule:
                result['AuthorizeSecurityPolicyRule'].append(k.to_map() if k else None)
        result['RevokeSecurityPolicyRule'] = []
        if self.revoke_security_policy_rule is not None:
            for k in self.revoke_security_policy_rule:
                result['RevokeSecurityPolicyRule'].append(k.to_map() if k else None)
        result['AuthorizeAccessPolicyRule'] = []
        if self.authorize_access_policy_rule is not None:
            for k in self.authorize_access_policy_rule:
                result['AuthorizeAccessPolicyRule'].append(k.to_map() if k else None)
        result['RevokeAccessPolicyRule'] = []
        if self.revoke_access_policy_rule is not None:
            for k in self.revoke_access_policy_rule:
                result['RevokeAccessPolicyRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')
        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('PreemptLoginUser') is not None:
            self.preempt_login_user = m.get('PreemptLoginUser')
        self.authorize_security_policy_rule = []
        if m.get('AuthorizeSecurityPolicyRule') is not None:
            for k in m.get('AuthorizeSecurityPolicyRule'):
                temp_model = ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule()
                self.authorize_security_policy_rule.append(temp_model.from_map(k))
        self.revoke_security_policy_rule = []
        if m.get('RevokeSecurityPolicyRule') is not None:
            for k in m.get('RevokeSecurityPolicyRule'):
                temp_model = ModifyPolicyGroupRequestRevokeSecurityPolicyRule()
                self.revoke_security_policy_rule.append(temp_model.from_map(k))
        self.authorize_access_policy_rule = []
        if m.get('AuthorizeAccessPolicyRule') is not None:
            for k in m.get('AuthorizeAccessPolicyRule'):
                temp_model = ModifyPolicyGroupRequestAuthorizeAccessPolicyRule()
                self.authorize_access_policy_rule.append(temp_model.from_map(k))
        self.revoke_access_policy_rule = []
        if m.get('RevokeAccessPolicyRule') is not None:
            for k in m.get('RevokeAccessPolicyRule'):
                temp_model = ModifyPolicyGroupRequestRevokeAccessPolicyRule()
                self.revoke_access_policy_rule.append(temp_model.from_map(k))
        return self


class ModifyPolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPolicyGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScaleStrategyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scale_strategy_id: str = None,
        scale_strategy_name: str = None,
        scale_strategy_type: str = None,
        min_desktops_count: int = None,
        max_desktops_count: int = None,
        min_available_desktops_count: int = None,
        max_available_desktops_count: int = None,
        scale_step: int = None,
    ):
        self.region_id = region_id
        self.scale_strategy_id = scale_strategy_id
        self.scale_strategy_name = scale_strategy_name
        self.scale_strategy_type = scale_strategy_type
        self.min_desktops_count = min_desktops_count
        self.max_desktops_count = max_desktops_count
        self.min_available_desktops_count = min_available_desktops_count
        self.max_available_desktops_count = max_available_desktops_count
        self.scale_step = scale_step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.scale_strategy_name is not None:
            result['ScaleStrategyName'] = self.scale_strategy_name
        if self.scale_strategy_type is not None:
            result['ScaleStrategyType'] = self.scale_strategy_type
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.min_available_desktops_count is not None:
            result['MinAvailableDesktopsCount'] = self.min_available_desktops_count
        if self.max_available_desktops_count is not None:
            result['MaxAvailableDesktopsCount'] = self.max_available_desktops_count
        if self.scale_step is not None:
            result['ScaleStep'] = self.scale_step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('ScaleStrategyName') is not None:
            self.scale_strategy_name = m.get('ScaleStrategyName')
        if m.get('ScaleStrategyType') is not None:
            self.scale_strategy_type = m.get('ScaleStrategyType')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('MinAvailableDesktopsCount') is not None:
            self.min_available_desktops_count = m.get('MinAvailableDesktopsCount')
        if m.get('MaxAvailableDesktopsCount') is not None:
            self.max_available_desktops_count = m.get('MaxAvailableDesktopsCount')
        if m.get('ScaleStep') is not None:
            self.scale_step = m.get('ScaleStep')
        return self


class ModifyScaleStrategyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyScaleStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyScaleStrategyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyScaleStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserToDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
        old_end_user_ids: List[str] = None,
        new_end_user_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id
        self.old_end_user_ids = old_end_user_ids
        self.new_end_user_ids = new_end_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.old_end_user_ids is not None:
            result['OldEndUserIds'] = self.old_end_user_ids
        if self.new_end_user_ids is not None:
            result['NewEndUserIds'] = self.new_end_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OldEndUserIds') is not None:
            self.old_end_user_ids = m.get('OldEndUserIds')
        if m.get('NewEndUserIds') is not None:
            self.new_end_user_ids = m.get('NewEndUserIds')
        return self


class ModifyUserToDesktopGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUserToDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUserToDesktopGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserToDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateVulsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
        operate_type: str = None,
        reason: str = None,
        precondition: int = None,
        vul_name: List[str] = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.type = type
        self.operate_type = operate_type
        self.reason = reason
        self.precondition = precondition
        self.vul_name = vul_name
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.precondition is not None:
            result['Precondition'] = self.precondition
        if self.vul_name is not None:
            result['VulName'] = self.vul_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Precondition') is not None:
            self.precondition = m.get('Precondition')
        if m.get('VulName') is not None:
            self.vul_name = m.get('VulName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class OperateVulsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OperateVulsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OperateVulsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OperateVulsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PayOrderCallbackRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class PayOrderCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PayOrderCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PayOrderCallbackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PayOrderCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RebootDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RebootDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebootDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebuildDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RebuildDesktopsResponseBodyRebuildResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        desktop_id: str = None,
    ):
        self.code = code
        self.message = message
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RebuildDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rebuild_results: List[RebuildDesktopsResponseBodyRebuildResults] = None,
    ):
        self.request_id = request_id
        self.rebuild_results = rebuild_results

    def validate(self):
        if self.rebuild_results:
            for k in self.rebuild_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RebuildResults'] = []
        if self.rebuild_results is not None:
            for k in self.rebuild_results:
                result['RebuildResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rebuild_results = []
        if m.get('RebuildResults') is not None:
            for k in m.get('RebuildResults'):
                temp_model = RebuildDesktopsResponseBodyRebuildResults()
                self.rebuild_results.append(temp_model.from_map(k))
        return self


class RebuildDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RebuildDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RebuildDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecreateDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
        own_bundle_id: str = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id
        self.own_bundle_id = own_bundle_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')
        return self


class RecreateDesktopGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecreateDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecreateDesktopGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RecreateDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_group_id: str = None,
        end_user_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_group_id = desktop_group_id
        self.end_user_ids = end_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class RemoveUserFromDesktopGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveUserFromDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveUserFromDesktopGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveUserFromDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        period: int = None,
        period_unit: str = None,
        auto_pay: bool = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.period = period
        self.period_unit = period_unit
        self.auto_pay = auto_pay
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RenewDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetNASDefaultMountTargetRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        file_system_id: str = None,
    ):
        self.region_id = region_id
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        return self


class ResetNASDefaultMountTargetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetNASDefaultMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetNASDefaultMountTargetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetNASDefaultMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSnapshotRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        snapshot_id: str = None,
    ):
        self.region_id = region_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackSuspEventQuaraFileRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        quara_field_id: int = None,
        desktop_id: str = None,
    ):
        self.region_id = region_id
        self.quara_field_id = quara_field_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.quara_field_id is not None:
            result['QuaraFieldId'] = self.quara_field_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('QuaraFieldId') is not None:
            self.quara_field_id = m.get('QuaraFieldId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RollbackSuspEventQuaraFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RollbackSuspEventQuaraFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollbackSuspEventQuaraFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RollbackSuspEventQuaraFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
        command_content: str = None,
        timeout: int = None,
        content_encoding: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.type = type
        self.command_content = command_content
        self.timeout = timeout
        self.content_encoding = content_encoding
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class RunCommandResponseBody(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
    ):
        self.invoke_id = invoke_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunCommandResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDirectorySsoStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: str = None,
        enable_sso: bool = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id
        self.enable_sso = enable_sso

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.enable_sso is not None:
            result['EnableSso'] = self.enable_sso
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EnableSso') is not None:
            self.enable_sso = m.get('EnableSso')
        return self


class SetDirectorySsoStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDirectorySsoStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetDirectorySsoStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetDirectorySsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIdpMetadataRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: str = None,
        office_site_id: str = None,
        idp_metadata: str = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id
        self.office_site_id = office_site_id
        self.idp_metadata = idp_metadata

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.idp_metadata is not None:
            result['IdpMetadata'] = self.idp_metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('IdpMetadata') is not None:
            self.idp_metadata = m.get('IdpMetadata')
        return self


class SetIdpMetadataResponseBody(TeaModel):
    def __init__(
        self,
        idp_entity_id: str = None,
        request_id: str = None,
    ):
        self.idp_entity_id = idp_entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_entity_id is not None:
            result['IdpEntityId'] = self.idp_entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpEntityId') is not None:
            self.idp_entity_id = m.get('IdpEntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetIdpMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetIdpMetadataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetIdpMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetOfficeSiteSsoStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: str = None,
        enable_sso: bool = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id
        self.enable_sso = enable_sso

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.enable_sso is not None:
            result['EnableSso'] = self.enable_sso
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('EnableSso') is not None:
            self.enable_sso = m.get('EnableSso')
        return self


class SetOfficeSiteSsoStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetOfficeSiteSsoStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetOfficeSiteSsoStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetOfficeSiteSsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class StartDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartVirusScanTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        office_site_id: List[str] = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.office_site_id = office_site_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class StartVirusScanTaskResponseBody(TeaModel):
    def __init__(
        self,
        scan_task_id: int = None,
        request_id: str = None,
    ):
        self.scan_task_id = scan_task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartVirusScanTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartVirusScanTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartVirusScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        stopped_mode: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.stopped_mode = stopped_mode
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class StopDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDesktopsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInvocationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        invoke_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.invoke_id = invoke_id
        self.desktop_id = desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class StopInvocationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInvocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInvocationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInvocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        serial_number: str = None,
    ):
        self.region_id = region_id
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnlockVirtualMFADeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnlockVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnlockVirtualMFADeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnlockVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


