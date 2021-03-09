# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class GetDirectorySsoStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: str = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
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


class GetDirectorySsoStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sso_status: bool = None,
    ):
        self.request_id = request_id
        self.sso_status = sso_status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sso_status, 'sso_status')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sso_status is not None:
            result['SsoStatus'] = self.sso_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SsoStatus') is not None:
            self.sso_status = m.get('SsoStatus')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.enable_sso, 'enable_sso')

    def to_map(self):
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


class SetDirectorySsoStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSpMetadataRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: str = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
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


class GetSpMetadataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sp_metadata: str = None,
    ):
        self.request_id = request_id
        self.sp_metadata = sp_metadata

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sp_metadata, 'sp_metadata')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sp_metadata is not None:
            result['SpMetadata'] = self.sp_metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpMetadata') is not None:
            self.sp_metadata = m.get('SpMetadata')
        return self


class SetIdpMetadataRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: str = None,
        idp_metadata: str = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id
        self.idp_metadata = idp_metadata

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.idp_metadata, 'idp_metadata')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.idp_metadata is not None:
            result['IdpMetadata'] = self.idp_metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('IdpMetadata') is not None:
            self.idp_metadata = m.get('IdpMetadata')
        return self


class SetIdpMetadataResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        idp_entity_id: str = None,
    ):
        self.request_id = request_id
        self.idp_entity_id = idp_entity_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.idp_entity_id, 'idp_entity_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.idp_entity_id is not None:
            result['IdpEntityId'] = self.idp_entity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IdpEntityId') is not None:
            self.idp_entity_id = m.get('IdpEntityId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
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


class RebuildDesktopsResponseRebuildResults(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.desktop_id = desktop_id
        self.code = code
        self.message = message

    def validate(self):
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RebuildDesktopsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        rebuild_results: List[RebuildDesktopsResponseRebuildResults] = None,
    ):
        self.request_id = request_id
        self.rebuild_results = rebuild_results

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.rebuild_results, 'rebuild_results')
        if self.rebuild_results:
            for k in self.rebuild_results:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = RebuildDesktopsResponseRebuildResults()
                self.rebuild_results.append(temp_model.from_map(k))
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bundle_id, 'bundle_id')

    def to_map(self):
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


class ModifyBundleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.serial_number, 'serial_number')

    def to_map(self):
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


class UnlockVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVirtualMFADevicesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        directory_id: str = None,
        end_user_id: List[str] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.directory_id = directory_id
        self.end_user_id = end_user_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
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
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class DescribeVirtualMFADevicesResponseVirtualMFADevices(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        end_user_id: str = None,
        gmt_enabled: str = None,
        gmt_unlock: str = None,
        consecutive_fails: int = None,
        serial_number: str = None,
        status: str = None,
    ):
        self.directory_id = directory_id
        self.end_user_id = end_user_id
        self.gmt_enabled = gmt_enabled
        self.gmt_unlock = gmt_unlock
        self.consecutive_fails = consecutive_fails
        self.serial_number = serial_number
        self.status = status

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.end_user_id, 'end_user_id')
        self.validate_required(self.gmt_enabled, 'gmt_enabled')
        self.validate_required(self.gmt_unlock, 'gmt_unlock')
        self.validate_required(self.consecutive_fails, 'consecutive_fails')
        self.validate_required(self.serial_number, 'serial_number')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.gmt_enabled is not None:
            result['GmtEnabled'] = self.gmt_enabled
        if self.gmt_unlock is not None:
            result['GmtUnlock'] = self.gmt_unlock
        if self.consecutive_fails is not None:
            result['ConsecutiveFails'] = self.consecutive_fails
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('GmtEnabled') is not None:
            self.gmt_enabled = m.get('GmtEnabled')
        if m.get('GmtUnlock') is not None:
            self.gmt_unlock = m.get('GmtUnlock')
        if m.get('ConsecutiveFails') is not None:
            self.consecutive_fails = m.get('ConsecutiveFails')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeVirtualMFADevicesResponse(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        virtual_mfadevices: List[DescribeVirtualMFADevicesResponseVirtualMFADevices] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.virtual_mfadevices = virtual_mfadevices

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.virtual_mfadevices, 'virtual_mfadevices')
        if self.virtual_mfadevices:
            for k in self.virtual_mfadevices:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeVirtualMFADevicesResponseVirtualMFADevices()
                self.virtual_mfadevices.append(temp_model.from_map(k))
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.serial_number, 'serial_number')

    def to_map(self):
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


class LockVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.serial_number, 'serial_number')

    def to_map(self):
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


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyADConnectorDirectoryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_id: str = None,
        domain_name: str = None,
        domain_user_name: str = None,
        domain_password: str = None,
        dns_address: List[str] = None,
        directory_name: str = None,
        sub_domain_dns_address: List[str] = None,
        sub_domain_name: str = None,
        mfa_enabled: bool = None,
    ):
        self.region_id = region_id
        self.directory_id = directory_id
        self.domain_name = domain_name
        self.domain_user_name = domain_user_name
        self.domain_password = domain_password
        self.dns_address = dns_address
        self.directory_name = directory_name
        self.sub_domain_dns_address = sub_domain_dns_address
        self.sub_domain_name = sub_domain_name
        self.mfa_enabled = mfa_enabled

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
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
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
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
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        return self


class ModifyADConnectorDirectoryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        tag_resources: List[ListTagResourcesResponseTagResources] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.tag_resources = tag_resources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
        all: bool = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key
        self.all = all

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.new_desktop_name, 'new_desktop_name')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
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


class ModifyDesktopNameResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCommandRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        type: str = None,
        command_content: str = None,
        timeout: int = None,
        desktop_id: List[str] = None,
        content_encoding: str = None,
    ):
        self.region_id = region_id
        self.type = type
        self.command_content = command_content
        self.timeout = timeout
        self.desktop_id = desktop_id
        self.content_encoding = content_encoding

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.command_content, 'command_content')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
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
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        return self


class RunCommandResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        invoke_id: str = None,
    ):
        self.request_id = request_id
        self.invoke_id = invoke_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.invoke_id, 'invoke_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.invoke_id, 'invoke_id')

    def to_map(self):
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


class StopInvocationResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
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


class DescribeInvocationsResponseInvocationsInvokeDesktops(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        repeats: int = None,
        invocation_status: str = None,
        creation_time: str = None,
        start_time: str = None,
        stop_time: str = None,
        finish_time: str = None,
        update_time: str = None,
        output: str = None,
        exit_code: int = None,
        dropped: int = None,
        error_code: str = None,
        error_info: str = None,
    ):
        self.desktop_id = desktop_id
        self.repeats = repeats
        self.invocation_status = invocation_status
        self.creation_time = creation_time
        self.start_time = start_time
        self.stop_time = stop_time
        self.finish_time = finish_time
        self.update_time = update_time
        self.output = output
        self.exit_code = exit_code
        self.dropped = dropped
        self.error_code = error_code
        self.error_info = error_info

    def validate(self):
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.repeats, 'repeats')
        self.validate_required(self.invocation_status, 'invocation_status')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.stop_time, 'stop_time')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.output, 'output')
        self.validate_required(self.exit_code, 'exit_code')
        self.validate_required(self.dropped, 'dropped')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_info, 'error_info')

    def to_map(self):
        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.repeats is not None:
            result['Repeats'] = self.repeats
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.output is not None:
            result['Output'] = self.output
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.dropped is not None:
            result['Dropped'] = self.dropped
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        return self


class DescribeInvocationsResponseInvocations(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        creation_time: str = None,
        command_type: str = None,
        command_content: str = None,
        invocation_status: str = None,
        invoke_desktops: List[DescribeInvocationsResponseInvocationsInvokeDesktops] = None,
    ):
        self.invoke_id = invoke_id
        self.creation_time = creation_time
        self.command_type = command_type
        self.command_content = command_content
        self.invocation_status = invocation_status
        self.invoke_desktops = invoke_desktops

    def validate(self):
        self.validate_required(self.invoke_id, 'invoke_id')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.command_type, 'command_type')
        self.validate_required(self.command_content, 'command_content')
        self.validate_required(self.invocation_status, 'invocation_status')
        self.validate_required(self.invoke_desktops, 'invoke_desktops')
        if self.invoke_desktops:
            for k in self.invoke_desktops:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        result['InvokeDesktops'] = []
        if self.invoke_desktops is not None:
            for k in self.invoke_desktops:
                result['InvokeDesktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        self.invoke_desktops = []
        if m.get('InvokeDesktops') is not None:
            for k in m.get('InvokeDesktops'):
                temp_model = DescribeInvocationsResponseInvocationsInvokeDesktops()
                self.invoke_desktops.append(temp_model.from_map(k))
        return self


class DescribeInvocationsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        invocations: List[DescribeInvocationsResponseInvocations] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.invocations = invocations

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.invocations, 'invocations')
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Invocations'] = []
        if self.invocations is not None:
            for k in self.invocations:
                result['Invocations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.invocations = []
        if m.get('Invocations') is not None:
            for k in m.get('Invocations'):
                temp_model = DescribeInvocationsResponseInvocations()
                self.invocations.append(temp_model.from_map(k))
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZonesResponseZones(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        self.validate_required(self.zone_id, 'zone_id')

    def to_map(self):
        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[DescribeZonesResponseZones] = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.zones, 'zones')
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeZonesResponseZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseRegions(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region_endpoint: str = None,
    ):
        self.region_id = region_id
        self.region_endpoint = region_endpoint

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.region_endpoint, 'region_endpoint')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.regions, 'regions')
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeRegionsResponseRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeClientEventsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        end_user_id: str = None,
        desktop_id: str = None,
        desktop_ip: str = None,
        directory_id: str = None,
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
        self.event_type = event_type
        self.start_time = start_time
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
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


class DescribeClientEventsResponseEvents(TeaModel):
    def __init__(
        self,
        event_id: str = None,
        event_type: str = None,
        event_time: str = None,
        region_id: str = None,
        ali_uid: str = None,
        end_user_id: str = None,
        desktop_id: str = None,
        desktop_ip: str = None,
        directory_id: str = None,
        directory_type: str = None,
        client_os: str = None,
        client_version: str = None,
        client_ip: str = None,
        bytes_send: str = None,
        bytes_received: str = None,
        status: str = None,
    ):
        self.event_id = event_id
        self.event_type = event_type
        self.event_time = event_time
        self.region_id = region_id
        self.ali_uid = ali_uid
        self.end_user_id = end_user_id
        self.desktop_id = desktop_id
        self.desktop_ip = desktop_ip
        self.directory_id = directory_id
        self.directory_type = directory_type
        self.client_os = client_os
        self.client_version = client_version
        self.client_ip = client_ip
        self.bytes_send = bytes_send
        self.bytes_received = bytes_received
        self.status = status

    def validate(self):
        self.validate_required(self.event_id, 'event_id')
        self.validate_required(self.event_type, 'event_type')
        self.validate_required(self.event_time, 'event_time')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ali_uid, 'ali_uid')
        self.validate_required(self.end_user_id, 'end_user_id')
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.desktop_ip, 'desktop_ip')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.directory_type, 'directory_type')
        self.validate_required(self.client_os, 'client_os')
        self.validate_required(self.client_version, 'client_version')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.bytes_send, 'bytes_send')
        self.validate_required(self.bytes_received, 'bytes_received')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_ip is not None:
            result['DesktopIp'] = self.desktop_ip
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.bytes_send is not None:
            result['BytesSend'] = self.bytes_send
        if self.bytes_received is not None:
            result['BytesReceived'] = self.bytes_received
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopIp') is not None:
            self.desktop_ip = m.get('DesktopIp')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('BytesSend') is not None:
            self.bytes_send = m.get('BytesSend')
        if m.get('BytesReceived') is not None:
            self.bytes_received = m.get('BytesReceived')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClientEventsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        events: List[DescribeClientEventsResponseEvents] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.events = events

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeClientEventsResponseEvents()
                self.events.append(temp_model.from_map(k))
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.snapshot_id, 'snapshot_id')

    def to_map(self):
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


class ResetSnapshotResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.snapshot_id, 'snapshot_id')

    def to_map(self):
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


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.snapshot_name, 'snapshot_name')
        self.validate_required(self.source_disk_type, 'source_disk_type')

    def to_map(self):
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


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_id: str = None,
    ):
        self.request_id = request_id
        self.snapshot_id = snapshot_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.snapshot_id, 'snapshot_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
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
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
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


class DescribeSnapshotsResponseSnapshots(TeaModel):
    def __init__(
        self,
        snapshot_id: str = None,
        desktop_id: str = None,
        snapshot_name: str = None,
        description: str = None,
        snapshot_type: str = None,
        source_disk_size: str = None,
        source_disk_type: str = None,
        status: str = None,
        creation_time: str = None,
        progress: str = None,
        remain_time: int = None,
    ):
        self.snapshot_id = snapshot_id
        self.desktop_id = desktop_id
        self.snapshot_name = snapshot_name
        self.description = description
        self.snapshot_type = snapshot_type
        self.source_disk_size = source_disk_size
        self.source_disk_type = source_disk_type
        self.status = status
        self.creation_time = creation_time
        self.progress = progress
        self.remain_time = remain_time

    def validate(self):
        self.validate_required(self.snapshot_id, 'snapshot_id')
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.snapshot_name, 'snapshot_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.snapshot_type, 'snapshot_type')
        self.validate_required(self.source_disk_size, 'source_disk_size')
        self.validate_required(self.source_disk_type, 'source_disk_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.progress, 'progress')
        self.validate_required(self.remain_time, 'remain_time')

    def to_map(self):
        result = dict()
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        return self


class DescribeSnapshotsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        snapshots: List[DescribeSnapshotsResponseSnapshots] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.snapshots = snapshots

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.snapshots, 'snapshots')
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeSnapshotsResponseSnapshots()
                self.snapshots.append(temp_model.from_map(k))
        return self


class RenewDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: List[str] = None,
        period: int = None,
        period_unit: str = None,
        auto_pay: bool = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id
        self.period = period
        self.period_unit = period_unit
        self.auto_pay = auto_pay

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        return self


class RenewDesktopsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class StopDesktopsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
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


class StopDesktopsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
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


class StartDesktopsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        watermark: str = None,
        watermark_type: str = None,
        watermark_custom_text: str = None,
        watermark_transparency: str = None,
    ):
        self.region_id = region_id
        self.policy_group_id = policy_group_id
        self.name = name
        self.clipboard = clipboard
        self.local_drive = local_drive
        self.usb_redirect = usb_redirect
        self.watermark = watermark
        self.watermark_type = watermark_type
        self.watermark_custom_text = watermark_custom_text
        self.watermark_transparency = watermark_transparency

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.policy_group_id, 'policy_group_id')

    def to_map(self):
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
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
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
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        return self


class ModifyPolicyGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDesktopTypesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_type_id: str = None,
        instance_type_family: str = None,
    ):
        self.region_id = region_id
        self.desktop_type_id = desktop_type_id
        self.instance_type_family = instance_type_family

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        return self


class DescribeDesktopTypesResponseDesktopTypesAllowDiskSize(TeaModel):
    def __init__(
        self,
        system_disk_size: int = None,
        data_disk_size: int = None,
    ):
        self.system_disk_size = system_disk_size
        self.data_disk_size = data_disk_size

    def validate(self):
        self.validate_required(self.system_disk_size, 'system_disk_size')
        self.validate_required(self.data_disk_size, 'data_disk_size')

    def to_map(self):
        result = dict()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        return self


class DescribeDesktopTypesResponseDesktopTypes(TeaModel):
    def __init__(
        self,
        desktop_type_id: str = None,
        instance_type_family: str = None,
        cpu_count: str = None,
        memory_size: str = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        system_disk_size: str = None,
        data_disk_size: str = None,
        allow_disk_size: List[DescribeDesktopTypesResponseDesktopTypesAllowDiskSize] = None,
    ):
        self.desktop_type_id = desktop_type_id
        self.instance_type_family = instance_type_family
        self.cpu_count = cpu_count
        self.memory_size = memory_size
        self.gpu_count = gpu_count
        self.gpu_spec = gpu_spec
        self.system_disk_size = system_disk_size
        self.data_disk_size = data_disk_size
        self.allow_disk_size = allow_disk_size

    def validate(self):
        self.validate_required(self.desktop_type_id, 'desktop_type_id')
        self.validate_required(self.instance_type_family, 'instance_type_family')
        self.validate_required(self.cpu_count, 'cpu_count')
        self.validate_required(self.memory_size, 'memory_size')
        self.validate_required(self.gpu_count, 'gpu_count')
        self.validate_required(self.gpu_spec, 'gpu_spec')
        self.validate_required(self.system_disk_size, 'system_disk_size')
        self.validate_required(self.data_disk_size, 'data_disk_size')
        self.validate_required(self.allow_disk_size, 'allow_disk_size')
        if self.allow_disk_size:
            for k in self.allow_disk_size:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
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
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        result['AllowDiskSize'] = []
        if self.allow_disk_size is not None:
            for k in self.allow_disk_size:
                result['AllowDiskSize'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        self.allow_disk_size = []
        if m.get('AllowDiskSize') is not None:
            for k in m.get('AllowDiskSize'):
                temp_model = DescribeDesktopTypesResponseDesktopTypesAllowDiskSize()
                self.allow_disk_size.append(temp_model.from_map(k))
        return self


class DescribeDesktopTypesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        desktop_types: List[DescribeDesktopTypesResponseDesktopTypes] = None,
    ):
        self.request_id = request_id
        self.desktop_types = desktop_types

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.desktop_types, 'desktop_types')
        if self.desktop_types:
            for k in self.desktop_types:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDesktopTypesResponseDesktopTypes()
                self.desktop_types.append(temp_model.from_map(k))
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        directory_type: str = None,
        directory_id: List[str] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.region_id = region_id
        self.directory_type = directory_type
        self.directory_id = directory_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDirectoriesResponseDirectoriesADConnectors(TeaModel):
    def __init__(
        self,
        adconnector_address: str = None,
        v_switch_id: str = None,
        connector_status: str = None,
        network_interface_id: str = None,
    ):
        self.adconnector_address = adconnector_address
        self.v_switch_id = v_switch_id
        self.connector_status = connector_status
        self.network_interface_id = network_interface_id

    def validate(self):
        self.validate_required(self.adconnector_address, 'adconnector_address')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.connector_status, 'connector_status')
        self.validate_required(self.network_interface_id, 'network_interface_id')

    def to_map(self):
        result = dict()
        if self.adconnector_address is not None:
            result['ADConnectorAddress'] = self.adconnector_address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ADConnectorAddress') is not None:
            self.adconnector_address = m.get('ADConnectorAddress')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        return self


class DescribeDirectoriesResponseDirectoriesLogs(TeaModel):
    def __init__(
        self,
        level: str = None,
        time_stamp: str = None,
        step: str = None,
        message: str = None,
    ):
        self.level = level
        self.time_stamp = time_stamp
        self.step = step
        self.message = message

    def validate(self):
        self.validate_required(self.level, 'level')
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.step, 'step')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.step is not None:
            result['Step'] = self.step
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeDirectoriesResponseDirectories(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        status: str = None,
        directory_type: str = None,
        creation_time: str = None,
        name: str = None,
        vpc_id: str = None,
        custom_security_group_id: str = None,
        dns_user_name: str = None,
        enable_internet_access: bool = None,
        enable_admin_access: bool = None,
        desktop_access_type: str = None,
        desktop_vpc_endpoint: str = None,
        trust_password: str = None,
        domain_name: str = None,
        domain_user_name: str = None,
        domain_password: str = None,
        sub_domain_name: str = None,
        mfa_enabled: bool = None,
        sso_enabled: bool = None,
        adconnectors: List[DescribeDirectoriesResponseDirectoriesADConnectors] = None,
        logs: List[DescribeDirectoriesResponseDirectoriesLogs] = None,
        dns_address: List[str] = None,
        sub_dns_address: List[str] = None,
        v_switch_ids: List[str] = None,
    ):
        self.directory_id = directory_id
        self.status = status
        self.directory_type = directory_type
        self.creation_time = creation_time
        self.name = name
        self.vpc_id = vpc_id
        self.custom_security_group_id = custom_security_group_id
        self.dns_user_name = dns_user_name
        self.enable_internet_access = enable_internet_access
        self.enable_admin_access = enable_admin_access
        self.desktop_access_type = desktop_access_type
        self.desktop_vpc_endpoint = desktop_vpc_endpoint
        self.trust_password = trust_password
        self.domain_name = domain_name
        self.domain_user_name = domain_user_name
        self.domain_password = domain_password
        self.sub_domain_name = sub_domain_name
        self.mfa_enabled = mfa_enabled
        self.sso_enabled = sso_enabled
        self.adconnectors = adconnectors
        self.logs = logs
        self.dns_address = dns_address
        self.sub_dns_address = sub_dns_address
        self.v_switch_ids = v_switch_ids

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.directory_type, 'directory_type')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.name, 'name')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.custom_security_group_id, 'custom_security_group_id')
        self.validate_required(self.dns_user_name, 'dns_user_name')
        self.validate_required(self.enable_internet_access, 'enable_internet_access')
        self.validate_required(self.enable_admin_access, 'enable_admin_access')
        self.validate_required(self.desktop_access_type, 'desktop_access_type')
        self.validate_required(self.desktop_vpc_endpoint, 'desktop_vpc_endpoint')
        self.validate_required(self.trust_password, 'trust_password')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_user_name, 'domain_user_name')
        self.validate_required(self.domain_password, 'domain_password')
        self.validate_required(self.sub_domain_name, 'sub_domain_name')
        self.validate_required(self.mfa_enabled, 'mfa_enabled')
        self.validate_required(self.sso_enabled, 'sso_enabled')
        self.validate_required(self.adconnectors, 'adconnectors')
        if self.adconnectors:
            for k in self.adconnectors:
                if k:
                    k.validate()
        self.validate_required(self.logs, 'logs')
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()
        self.validate_required(self.dns_address, 'dns_address')
        self.validate_required(self.sub_dns_address, 'sub_dns_address')
        self.validate_required(self.v_switch_ids, 'v_switch_ids')

    def to_map(self):
        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.status is not None:
            result['Status'] = self.status
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.name is not None:
            result['Name'] = self.name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id
        if self.dns_user_name is not None:
            result['DnsUserName'] = self.dns_user_name
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k in self.adconnectors:
                result['ADConnectors'].append(k.to_map() if k else None)
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.sub_dns_address is not None:
            result['SubDnsAddress'] = self.sub_dns_address
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')
        if m.get('DnsUserName') is not None:
            self.dns_user_name = m.get('DnsUserName')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k in m.get('ADConnectors'):
                temp_model = DescribeDirectoriesResponseDirectoriesADConnectors()
                self.adconnectors.append(temp_model.from_map(k))
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeDirectoriesResponseDirectoriesLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('SubDnsAddress') is not None:
            self.sub_dns_address = m.get('SubDnsAddress')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        directories: List[DescribeDirectoriesResponseDirectories] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.directories = directories

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.directories, 'directories')
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeDirectoriesResponseDirectories()
                self.directories.append(temp_model.from_map(k))
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
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


class DeleteDirectoriesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
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


class ListDirectoryUsersResponseUsers(TeaModel):
    def __init__(
        self,
        end_user: str = None,
    ):
        self.end_user = end_user

    def validate(self):
        self.validate_required(self.end_user, 'end_user')

    def to_map(self):
        result = dict()
        if self.end_user is not None:
            result['EndUser'] = self.end_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUser') is not None:
            self.end_user = m.get('EndUser')
        return self


class ListDirectoryUsersResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        users: List[ListDirectoryUsersResponseUsers] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.users = users

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.users, 'users')
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListDirectoryUsersResponseUsers()
                self.users.append(temp_model.from_map(k))
        return self


class CreateImageRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        desktop_id: str = None,
        image_name: str = None,
        description: str = None,
    ):
        self.region_id = region_id
        self.desktop_id = desktop_id
        self.image_name = image_name
        self.description = description

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.description is not None:
            result['Description'] = self.description
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
        return self


class CreateImageResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        image_id: str = None,
    ):
        self.request_id = request_id
        self.image_id = image_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
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


class CreateRAMDirectoryResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        directory_id: str = None,
    ):
        self.request_id = request_id
        self.directory_id = directory_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.policy_group_id, 'policy_group_id')

    def to_map(self):
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


class DeletePolicyGroupsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
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


class DescribePolicyGroupsResponseDescribePolicyGroups(TeaModel):
    def __init__(
        self,
        policy_group_id: str = None,
        policy_group_type: str = None,
        clipboard: str = None,
        local_drive: str = None,
        usb_redirect: str = None,
        watermark: str = None,
        name: str = None,
        watermark_type: str = None,
        watermark_custom_text: str = None,
        watermark_transparency: str = None,
        policy_status: str = None,
        eds_count: int = None,
    ):
        self.policy_group_id = policy_group_id
        self.policy_group_type = policy_group_type
        self.clipboard = clipboard
        self.local_drive = local_drive
        self.usb_redirect = usb_redirect
        self.watermark = watermark
        self.name = name
        self.watermark_type = watermark_type
        self.watermark_custom_text = watermark_custom_text
        self.watermark_transparency = watermark_transparency
        self.policy_status = policy_status
        self.eds_count = eds_count

    def validate(self):
        self.validate_required(self.policy_group_id, 'policy_group_id')
        self.validate_required(self.policy_group_type, 'policy_group_type')
        self.validate_required(self.clipboard, 'clipboard')
        self.validate_required(self.local_drive, 'local_drive')
        self.validate_required(self.usb_redirect, 'usb_redirect')
        self.validate_required(self.watermark, 'watermark')
        self.validate_required(self.name, 'name')
        self.validate_required(self.watermark_type, 'watermark_type')
        self.validate_required(self.watermark_custom_text, 'watermark_custom_text')
        self.validate_required(self.watermark_transparency, 'watermark_transparency')
        self.validate_required(self.policy_status, 'policy_status')
        self.validate_required(self.eds_count, 'eds_count')

    def to_map(self):
        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_type is not None:
            result['PolicyGroupType'] = self.policy_group_type
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
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
        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status
        if self.eds_count is not None:
            result['EdsCount'] = self.eds_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupType') is not None:
            self.policy_group_type = m.get('PolicyGroupType')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
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
        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')
        if m.get('EdsCount') is not None:
            self.eds_count = m.get('EdsCount')
        return self


class DescribePolicyGroupsResponse(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        describe_policy_groups: List[DescribePolicyGroupsResponseDescribePolicyGroups] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.describe_policy_groups = describe_policy_groups

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.describe_policy_groups, 'describe_policy_groups')
        if self.describe_policy_groups:
            for k in self.describe_policy_groups:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribePolicyGroupsResponseDescribePolicyGroups()
                self.describe_policy_groups.append(temp_model.from_map(k))
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
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


class DeleteDesktopsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
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


class ModifyImageAttributeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.end_user_id, 'end_user_id')

    def to_map(self):
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


class ModifyEntitlementResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bundle_id, 'bundle_id')

    def to_map(self):
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


class DeleteBundlesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        policy_group_id: str = None,
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
        self.policy_group_id = policy_group_id
        self.desktop_id = desktop_id
        self.end_user_id = end_user_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
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
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
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
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        return self


class DescribeDesktopsResponseDesktopsDisks(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        disk_size: int = None,
        disk_type: str = None,
    ):
        self.disk_id = disk_id
        self.disk_size = disk_size
        self.disk_type = disk_type

    def validate(self):
        self.validate_required(self.disk_id, 'disk_id')
        self.validate_required(self.disk_size, 'disk_size')
        self.validate_required(self.disk_type, 'disk_type')

    def to_map(self):
        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeDesktopsResponseDesktopsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
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


class DescribeDesktopsResponseDesktopsSessions(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        establishment_time: str = None,
    ):
        self.end_user_id = end_user_id
        self.establishment_time = establishment_time

    def validate(self):
        self.validate_required(self.end_user_id, 'end_user_id')
        self.validate_required(self.establishment_time, 'establishment_time')

    def to_map(self):
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


class DescribeDesktopsResponseDesktops(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        directory_type: str = None,
        creation_time: str = None,
        desktop_id: str = None,
        bundle_id: str = None,
        desktop_status: str = None,
        desktop_name: str = None,
        image_id: str = None,
        desktop_type: str = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        data_disk_category: str = None,
        data_disk_size: str = None,
        policy_group_id: str = None,
        cpu: int = None,
        memory: int = None,
        network_interface_id: str = None,
        expired_time: str = None,
        charge_type: str = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        start_time: str = None,
        connection_status: str = None,
        os_type: str = None,
        disks: List[DescribeDesktopsResponseDesktopsDisks] = None,
        tags: List[DescribeDesktopsResponseDesktopsTags] = None,
        sessions: List[DescribeDesktopsResponseDesktopsSessions] = None,
        end_user_ids: List[str] = None,
    ):
        self.directory_id = directory_id
        self.directory_type = directory_type
        self.creation_time = creation_time
        self.desktop_id = desktop_id
        self.bundle_id = bundle_id
        self.desktop_status = desktop_status
        self.desktop_name = desktop_name
        self.image_id = image_id
        self.desktop_type = desktop_type
        self.system_disk_category = system_disk_category
        self.system_disk_size = system_disk_size
        self.data_disk_category = data_disk_category
        self.data_disk_size = data_disk_size
        self.policy_group_id = policy_group_id
        self.cpu = cpu
        self.memory = memory
        self.network_interface_id = network_interface_id
        self.expired_time = expired_time
        self.charge_type = charge_type
        self.gpu_count = gpu_count
        self.gpu_spec = gpu_spec
        self.start_time = start_time
        self.connection_status = connection_status
        self.os_type = os_type
        self.disks = disks
        self.tags = tags
        self.sessions = sessions
        self.end_user_ids = end_user_ids

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.directory_type, 'directory_type')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.bundle_id, 'bundle_id')
        self.validate_required(self.desktop_status, 'desktop_status')
        self.validate_required(self.desktop_name, 'desktop_name')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.desktop_type, 'desktop_type')
        self.validate_required(self.system_disk_category, 'system_disk_category')
        self.validate_required(self.system_disk_size, 'system_disk_size')
        self.validate_required(self.data_disk_category, 'data_disk_category')
        self.validate_required(self.data_disk_size, 'data_disk_size')
        self.validate_required(self.policy_group_id, 'policy_group_id')
        self.validate_required(self.cpu, 'cpu')
        self.validate_required(self.memory, 'memory')
        self.validate_required(self.network_interface_id, 'network_interface_id')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.gpu_count, 'gpu_count')
        self.validate_required(self.gpu_spec, 'gpu_spec')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.connection_status, 'connection_status')
        self.validate_required(self.os_type, 'os_type')
        self.validate_required(self.disks, 'disks')
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        self.validate_required(self.tags, 'tags')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        self.validate_required(self.sessions, 'sessions')
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()
        self.validate_required(self.end_user_ids, 'end_user_ids')

    def to_map(self):
        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.os_type is not None:
            result['OsType'] = self.os_type
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
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDesktopsResponseDesktopsDisks()
                self.disks.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDesktopsResponseDesktopsTags()
                self.tags.append(temp_model.from_map(k))
        self.sessions = []
        if m.get('Sessions') is not None:
            for k in m.get('Sessions'):
                temp_model = DescribeDesktopsResponseDesktopsSessions()
                self.sessions.append(temp_model.from_map(k))
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        return self


class DescribeDesktopsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        desktops: List[DescribeDesktopsResponseDesktops] = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.desktops = desktops

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.desktops, 'desktops')
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Desktops'] = []
        if self.desktops is not None:
            for k in self.desktops:
                result['Desktops'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.desktops = []
        if m.get('Desktops') is not None:
            for k in m.get('Desktops'):
                temp_model = DescribeDesktopsResponseDesktops()
                self.desktops.append(temp_model.from_map(k))
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
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


class RebootDesktopsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.desktop_type, 'desktop_type')
        self.validate_required(self.root_disk_size_gib, 'root_disk_size_gib')
        self.validate_required(self.user_disk_size_gib, 'user_disk_size_gib')

    def to_map(self):
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


class CreateBundleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bundle_id: str = None,
    ):
        self.request_id = request_id
        self.bundle_id = bundle_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.bundle_id, 'bundle_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
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


class ModifyDesktopsPolicyGroupResponseModifyResults(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.desktop_id = desktop_id
        self.code = code
        self.message = message

    def validate(self):
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ModifyDesktopsPolicyGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        modify_results: List[ModifyDesktopsPolicyGroupResponseModifyResults] = None,
    ):
        self.request_id = request_id
        self.modify_results = modify_results

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.modify_results, 'modify_results')
        if self.modify_results:
            for k in self.modify_results:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ModifyDesktopsPolicyGroupResponseModifyResults()
                self.modify_results.append(temp_model.from_map(k))
        return self


class CreatePolicyGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        clipboard: str = None,
        local_drive: str = None,
        usb_redirect: str = None,
        watermark: str = None,
        name: str = None,
        watermark_type: str = None,
        watermark_custom_text: str = None,
        watermark_transparency: str = None,
    ):
        self.region_id = region_id
        self.clipboard = clipboard
        self.local_drive = local_drive
        self.usb_redirect = usb_redirect
        self.watermark = watermark
        self.name = name
        self.watermark_type = watermark_type
        self.watermark_custom_text = watermark_custom_text
        self.watermark_transparency = watermark_transparency

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
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
        if self.name is not None:
            result['Name'] = self.name
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
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
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        return self


class CreatePolicyGroupResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        policy_group_id: str = None,
    ):
        self.request_id = request_id
        self.policy_group_id = policy_group_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy_group_id, 'policy_group_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        return self


class CreateADConnectorDirectoryRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        domain_name: str = None,
        domain_user_name: str = None,
        domain_password: str = None,
        dns_address: List[str] = None,
        v_switch_id: List[str] = None,
        directory_name: str = None,
        enable_admin_access: bool = None,
        desktop_access_type: str = None,
        sub_domain_dns_address: List[str] = None,
        sub_domain_name: str = None,
        mfa_enabled: bool = None,
    ):
        self.region_id = region_id
        self.domain_name = domain_name
        self.domain_user_name = domain_user_name
        self.domain_password = domain_password
        self.dns_address = dns_address
        self.v_switch_id = v_switch_id
        self.directory_name = directory_name
        self.enable_admin_access = enable_admin_access
        self.desktop_access_type = desktop_access_type
        self.sub_domain_dns_address = sub_domain_dns_address
        self.sub_domain_name = sub_domain_name
        self.mfa_enabled = mfa_enabled

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_user_name, 'domain_user_name')
        self.validate_required(self.domain_password, 'domain_password')
        self.validate_required(self.dns_address, 'dns_address')
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
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
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        return self


class CreateADConnectorDirectoryResponseAdConnectors(TeaModel):
    def __init__(
        self,
        address: str = None,
    ):
        self.address = address

    def validate(self):
        self.validate_required(self.address, 'address')

    def to_map(self):
        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class CreateADConnectorDirectoryResponse(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        request_id: str = None,
        trust_password: str = None,
        ad_connectors: List[CreateADConnectorDirectoryResponseAdConnectors] = None,
    ):
        self.directory_id = directory_id
        self.request_id = request_id
        self.trust_password = trust_password
        self.ad_connectors = ad_connectors

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.trust_password, 'trust_password')
        self.validate_required(self.ad_connectors, 'ad_connectors')
        if self.ad_connectors:
            for k in self.ad_connectors:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        result['AdConnectors'] = []
        if self.ad_connectors is not None:
            for k in self.ad_connectors:
                result['AdConnectors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        self.ad_connectors = []
        if m.get('AdConnectors') is not None:
            for k in m.get('AdConnectors'):
                temp_model = CreateADConnectorDirectoryResponseAdConnectors()
                self.ad_connectors.append(temp_model.from_map(k))
        return self


class DescribeBundlesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        bundle_id: List[str] = None,
        bundle_type: str = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.bundle_id = bundle_id
        self.bundle_type = bundle_type

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        return self


class DescribeBundlesResponseBundlesDisks(TeaModel):
    def __init__(
        self,
        disk_size: int = None,
        disk_type: str = None,
    ):
        self.disk_size = disk_size
        self.disk_type = disk_type

    def validate(self):
        self.validate_required(self.disk_size, 'disk_size')
        self.validate_required(self.disk_type, 'disk_type')

    def to_map(self):
        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeBundlesResponseBundlesDesktopTypeAttribute(TeaModel):
    def __init__(
        self,
        cpu_count: int = None,
        memory_size: int = None,
        gpu_count: float = None,
        gpu_spec: str = None,
    ):
        self.cpu_count = cpu_count
        self.memory_size = memory_size
        self.gpu_count = gpu_count
        self.gpu_spec = gpu_spec

    def validate(self):
        self.validate_required(self.cpu_count, 'cpu_count')
        self.validate_required(self.memory_size, 'memory_size')
        self.validate_required(self.gpu_count, 'gpu_count')
        self.validate_required(self.gpu_spec, 'gpu_spec')

    def to_map(self):
        result = dict()
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        return self


class DescribeBundlesResponseBundles(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        bundle_id: str = None,
        bundle_type: str = None,
        bundle_name: str = None,
        description: str = None,
        desktop_type: str = None,
        disks: List[DescribeBundlesResponseBundlesDisks] = None,
        desktop_type_attribute: DescribeBundlesResponseBundlesDesktopTypeAttribute = None,
    ):
        self.image_id = image_id
        self.bundle_id = bundle_id
        self.bundle_type = bundle_type
        self.bundle_name = bundle_name
        self.description = description
        self.desktop_type = desktop_type
        self.disks = disks
        self.desktop_type_attribute = desktop_type_attribute

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.bundle_id, 'bundle_id')
        self.validate_required(self.bundle_type, 'bundle_type')
        self.validate_required(self.bundle_name, 'bundle_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.desktop_type, 'desktop_type')
        self.validate_required(self.disks, 'disks')
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        self.validate_required(self.desktop_type_attribute, 'desktop_type_attribute')
        if self.desktop_type_attribute:
            self.desktop_type_attribute.validate()

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.desktop_type_attribute is not None:
            result['DesktopTypeAttribute'] = self.desktop_type_attribute.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeBundlesResponseBundlesDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('DesktopTypeAttribute') is not None:
            temp_model = DescribeBundlesResponseBundlesDesktopTypeAttribute()
            self.desktop_type_attribute = temp_model.from_map(m['DesktopTypeAttribute'])
        return self


class DescribeBundlesResponse(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        bundles: List[DescribeBundlesResponseBundles] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.bundles = bundles

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.bundles, 'bundles')
        if self.bundles:
            for k in self.bundles:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeBundlesResponseBundles()
                self.bundles.append(temp_model.from_map(k))
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
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
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


class DeleteImagesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        end_user_id: List[str] = None,
        policy_group_id: str = None,
        charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        auto_pay: bool = None,
        tag: List[CreateDesktopsRequestTag] = None,
        auto_renew: bool = None,
    ):
        self.region_id = region_id
        self.group_id = group_id
        self.bundle_id = bundle_id
        self.desktop_name = desktop_name
        self.user_name = user_name
        self.vpc_id = vpc_id
        self.amount = amount
        self.directory_id = directory_id
        self.end_user_id = end_user_id
        self.policy_group_id = policy_group_id
        self.charge_type = charge_type
        self.period = period
        self.period_unit = period_unit
        self.auto_pay = auto_pay
        self.tag = tag
        self.auto_renew = auto_renew

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bundle_id, 'bundle_id')
        self.validate_required(self.end_user_id, 'end_user_id')
        self.validate_required(self.policy_group_id, 'policy_group_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
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
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
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
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
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
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDesktopsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        return self


class CreateDesktopsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
        desktop_id: List[str] = None,
    ):
        self.request_id = request_id
        self.order_id = order_id
        self.desktop_id = desktop_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        image_type: str = None,
        image_status: str = None,
        image_id: List[str] = None,
        gpu_category: bool = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.image_type = image_type
        self.image_status = image_status
        self.image_id = image_id
        self.gpu_category = gpu_category

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
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
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
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
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        return self


class DescribeImagesResponseImages(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        image_id: str = None,
        image_type: str = None,
        name: str = None,
        progress: str = None,
        size: int = None,
        data_disk_size: int = None,
        gpu_category: bool = None,
        status: str = None,
        description: str = None,
        os_type: str = None,
    ):
        self.creation_time = creation_time
        self.image_id = image_id
        self.image_type = image_type
        self.name = name
        self.progress = progress
        self.size = size
        self.data_disk_size = data_disk_size
        self.gpu_category = gpu_category
        self.status = status
        self.description = description
        self.os_type = os_type

    def validate(self):
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.image_type, 'image_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.progress, 'progress')
        self.validate_required(self.size, 'size')
        self.validate_required(self.data_disk_size, 'data_disk_size')
        self.validate_required(self.gpu_category, 'gpu_category')
        self.validate_required(self.status, 'status')
        self.validate_required(self.description, 'description')
        self.validate_required(self.os_type, 'os_type')

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.size is not None:
            result['Size'] = self.size
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        if self.os_type is not None:
            result['OsType'] = self.os_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        images: List[DescribeImagesResponseImages] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.images = images

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.images, 'images')
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeImagesResponseImages()
                self.images.append(temp_model.from_map(k))
        return self


