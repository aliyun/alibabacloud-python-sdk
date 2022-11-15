# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddEntriesToAclRequestAclEntries(TeaModel):
    def __init__(
        self,
        entry: str = None,
        entry_description: str = None,
    ):
        self.entry = entry
        self.entry_description = entry_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')
        return self


class AddEntriesToAclRequest(TeaModel):
    def __init__(
        self,
        acl_entries: List[AddEntriesToAclRequestAclEntries] = None,
        acl_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.acl_entries = acl_entries
        self.acl_id = acl_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = AddEntriesToAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddEntriesToAclResponseBody(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        request_id: str = None,
    ):
        self.acl_id = acl_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddEntriesToAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddEntriesToAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddEntriesToAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAclsWithListenerRequest(TeaModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        acl_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.acl_ids = acl_ids
        self.acl_type = acl_type
        self.client_token = client_token
        self.dry_run = dry_run
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateAclsWithListenerResponseBody(TeaModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        listener_id: str = None,
        request_id: str = None,
    ):
        self.acl_ids = acl_ids
        self.listener_id = listener_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateAclsWithListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateAclsWithListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateAclsWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAdditionalCertificatesWithListenerRequestCertificates(TeaModel):
    def __init__(
        self,
        domain: str = None,
        id: str = None,
    ):
        self.domain = domain
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AssociateAdditionalCertificatesWithListenerRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        certificates: List[AssociateAdditionalCertificatesWithListenerRequestCertificates] = None,
        client_token: str = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.certificates = certificates
        self.client_token = client_token
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = AssociateAdditionalCertificatesWithListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateAdditionalCertificatesWithListenerResponseBody(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        request_id: str = None,
    ):
        self.listener_id = listener_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateAdditionalCertificatesWithListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateAdditionalCertificatesWithListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateAdditionalCertificatesWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachDdosToAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        ddos_id: str = None,
        ddos_region_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.ddos_id = ddos_id
        self.ddos_region_id = ddos_region_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachDdosToAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        ddos_id: str = None,
        ga_id: str = None,
        request_id: str = None,
    ):
        self.ddos_id = ddos_id
        self.ga_id = ga_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.ga_id is not None:
            result['GaId'] = self.ga_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('GaId') is not None:
            self.ga_id = m.get('GaId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachDdosToAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachDdosToAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachDdosToAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachLogStoreToEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        endpoint_group_ids: List[str] = None,
        listener_id: str = None,
        region_id: str = None,
        sls_log_store_name: str = None,
        sls_project_name: str = None,
        sls_region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.endpoint_group_ids = endpoint_group_ids
        self.listener_id = listener_id
        self.region_id = region_id
        self.sls_log_store_name = sls_log_store_name
        self.sls_project_name = sls_project_name
        self.sls_region_id = sls_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name
        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name
        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')
        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')
        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')
        return self


class AttachLogStoreToEndpointGroupResponseBody(TeaModel):
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


class AttachLogStoreToEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachLogStoreToEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachLogStoreToEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandwidthPackageAddAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth_package_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.bandwidth_package_id = bandwidth_package_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BandwidthPackageAddAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        accelerators: List[str] = None,
        bandwidth_package_id: str = None,
        request_id: str = None,
    ):
        self.accelerators = accelerators
        self.bandwidth_package_id = bandwidth_package_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BandwidthPackageAddAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BandwidthPackageAddAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BandwidthPackageAddAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BandwidthPackageRemoveAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth_package_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.bandwidth_package_id = bandwidth_package_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BandwidthPackageRemoveAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        accelerators: List[str] = None,
        bandwidth_package_id: str = None,
        request_id: str = None,
    ):
        self.accelerators = accelerators
        self.bandwidth_package_id = bandwidth_package_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BandwidthPackageRemoveAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BandwidthPackageRemoveAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BandwidthPackageRemoveAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.client_token = client_token
        self.new_resource_group_id = new_resource_group_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
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


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigEndpointProbeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        enable: str = None,
        endpoint: str = None,
        endpoint_group_id: str = None,
        endpoint_type: str = None,
        probe_port: str = None,
        probe_protocol: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.enable = enable
        self.endpoint = endpoint
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_type = endpoint_type
        self.probe_port = probe_port
        self.probe_protocol = probe_protocol
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port
        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')
        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigEndpointProbeResponseBody(TeaModel):
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


class ConfigEndpointProbeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigEndpointProbeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConfigEndpointProbeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAcceleratorRequestIpSetConfig(TeaModel):
    def __init__(
        self,
        access_mode: str = None,
    ):
        self.access_mode = access_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class CreateAcceleratorRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_use_coupon: str = None,
        bandwidth_billing_type: str = None,
        client_token: str = None,
        duration: int = None,
        ip_set_config: CreateAcceleratorRequestIpSetConfig = None,
        name: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_use_coupon = auto_use_coupon
        self.bandwidth_billing_type = bandwidth_billing_type
        self.client_token = client_token
        self.duration = duration
        self.ip_set_config = ip_set_config
        self.name = name
        self.pricing_cycle = pricing_cycle
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.spec = spec

    def validate(self):
        if self.ip_set_config:
            self.ip_set_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.ip_set_config is not None:
            result['IpSetConfig'] = self.ip_set_config.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('IpSetConfig') is not None:
            temp_model = CreateAcceleratorRequestIpSetConfig()
            self.ip_set_config = temp_model.from_map(m['IpSetConfig'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class CreateAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAclRequestAclEntries(TeaModel):
    def __init__(
        self,
        entry: str = None,
        entry_description: str = None,
    ):
        self.entry = entry
        self.entry_description = entry_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')
        return self


class CreateAclRequest(TeaModel):
    def __init__(
        self,
        acl_entries: List[CreateAclRequestAclEntries] = None,
        acl_name: str = None,
        address_ipversion: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.acl_entries = acl_entries
        self.acl_name = acl_name
        self.address_ipversion = address_ipversion
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = CreateAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateAclResponseBody(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        request_id: str = None,
    ):
        self.acl_id = acl_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationMonitorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        address: str = None,
        client_token: str = None,
        detect_enable: bool = None,
        detect_threshold: int = None,
        detect_times: int = None,
        listener_id: str = None,
        options_json: str = None,
        region_id: str = None,
        silence_time: int = None,
        task_name: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.address = address
        self.client_token = client_token
        self.detect_enable = detect_enable
        self.detect_threshold = detect_threshold
        self.detect_times = detect_times
        self.listener_id = listener_id
        self.options_json = options_json
        self.region_id = region_id
        self.silence_time = silence_time
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.detect_enable is not None:
            result['DetectEnable'] = self.detect_enable
        if self.detect_threshold is not None:
            result['DetectThreshold'] = self.detect_threshold
        if self.detect_times is not None:
            result['DetectTimes'] = self.detect_times
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.options_json is not None:
            result['OptionsJson'] = self.options_json
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DetectEnable') is not None:
            self.detect_enable = m.get('DetectEnable')
        if m.get('DetectThreshold') is not None:
            self.detect_threshold = m.get('DetectThreshold')
        if m.get('DetectTimes') is not None:
            self.detect_times = m.get('DetectTimes')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateApplicationMonitorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateApplicationMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApplicationMonitorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBandwidthPackageRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_use_coupon: str = None,
        bandwidth: int = None,
        bandwidth_type: str = None,
        billing_type: str = None,
        cbn_geographic_region_id_a: str = None,
        cbn_geographic_region_id_b: str = None,
        charge_type: str = None,
        client_token: str = None,
        duration: str = None,
        pricing_cycle: str = None,
        ratio: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_use_coupon = auto_use_coupon
        self.bandwidth = bandwidth
        self.bandwidth_type = bandwidth_type
        self.billing_type = billing_type
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b
        self.charge_type = charge_type
        self.client_token = client_token
        self.duration = duration
        self.pricing_cycle = pricing_cycle
        self.ratio = ratio
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateBandwidthPackageResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBandwidthPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBandwidthPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBasicAcceleratorRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_use_coupon: str = None,
        bandwidth_billing_type: str = None,
        client_token: str = None,
        duration: int = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.auto_use_coupon = auto_use_coupon
        self.bandwidth_billing_type = bandwidth_billing_type
        self.client_token = client_token
        self.duration = duration
        self.pricing_cycle = pricing_cycle
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateBasicAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBasicAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBasicAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBasicAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBasicEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        description: str = None,
        endpoint_address: str = None,
        endpoint_group_region: str = None,
        endpoint_sub_address: str = None,
        endpoint_type: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.description = description
        self.endpoint_address = endpoint_address
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_sub_address = endpoint_sub_address
        self.endpoint_type = endpoint_type
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateBasicEndpointGroupResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
        request_id: str = None,
    ):
        self.endpoint_group_id = endpoint_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBasicEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBasicEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBasicEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBasicIpSetRequest(TeaModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        accelerator_id: str = None,
        bandwidth: int = None,
        client_token: str = None,
        isp_type: str = None,
        region_id: str = None,
    ):
        self.accelerate_region_id = accelerate_region_id
        self.accelerator_id = accelerator_id
        self.bandwidth = bandwidth
        self.client_token = client_token
        self.isp_type = isp_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateBasicIpSetResponseBody(TeaModel):
    def __init__(
        self,
        ip_set_id: str = None,
        request_id: str = None,
    ):
        self.ip_set_id = ip_set_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBasicIpSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBasicIpSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBasicIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        protocols: List[str] = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.protocols = protocols
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        destination_configurations: List[CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations] = None,
        dry_run: bool = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.destination_configurations = destination_configurations
        self.dry_run = dry_run
        self.endpoint_group_id = endpoint_group_id
        self.region_id = region_id

    def validate(self):
        if self.destination_configurations:
            for k in self.destination_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k in self.destination_configurations:
                result['DestinationConfigurations'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k in m.get('DestinationConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k))
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
    def __init__(
        self,
        destination_ids: List[str] = None,
        request_id: str = None,
    ):
        self.destination_ids = destination_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_ids is not None:
            result['DestinationIds'] = self.destination_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationIds') is not None:
            self.destination_ids = m.get('DestinationIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomRoutingEndpointGroupDestinationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        protocols: List[str] = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.protocols = protocols
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations(TeaModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges] = None,
    ):
        self.address = address
        self.port_ranges = port_ranges

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        policy_configurations: List[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations] = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        self.endpoint = endpoint
        self.policy_configurations = policy_configurations
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        self.type = type

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations(TeaModel):
    def __init__(
        self,
        description: str = None,
        destination_configurations: List[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations] = None,
        endpoint_configurations: List[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations] = None,
        endpoint_group_region: str = None,
        name: str = None,
    ):
        self.description = description
        self.destination_configurations = destination_configurations
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_region = endpoint_group_region
        self.name = name

    def validate(self):
        if self.destination_configurations:
            for k in self.destination_configurations:
                if k:
                    k.validate()
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k in self.destination_configurations:
                result['DestinationConfigurations'].append(k.to_map() if k else None)
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k in m.get('DestinationConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k))
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateCustomRoutingEndpointGroupsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_group_configurations: List[CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_group_configurations = endpoint_group_configurations
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = CreateCustomRoutingEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCustomRoutingEndpointGroupsResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_group_ids: List[str] = None,
        request_id: str = None,
    ):
        self.endpoint_group_ids = endpoint_group_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomRoutingEndpointGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomRoutingEndpointGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomRoutingEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations(TeaModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges] = None,
    ):
        self.address = address
        self.port_ranges = port_ranges

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class CreateCustomRoutingEndpointTrafficPoliciesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_id: str = None,
        policy_configurations: List[CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations] = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.endpoint_id = endpoint_id
        self.policy_configurations = policy_configurations
        self.region_id = region_id

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = CreateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCustomRoutingEndpointTrafficPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        request_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomRoutingEndpointTrafficPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomRoutingEndpointTrafficPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomRoutingEndpointTrafficPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations(TeaModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges] = None,
    ):
        self.address = address
        self.port_ranges = port_ranges

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class CreateCustomRoutingEndpointsRequestEndpointConfigurations(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        policy_configurations: List[CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations] = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        self.endpoint = endpoint
        self.policy_configurations = policy_configurations
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        self.type = type

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = CreateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCustomRoutingEndpointsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_configurations: List[CreateCustomRoutingEndpointsRequestEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_id = endpoint_group_id
        self.region_id = region_id

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateCustomRoutingEndpointsRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateCustomRoutingEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_ids: List[str] = None,
        request_id: str = None,
    ):
        self.endpoint_ids = endpoint_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomRoutingEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomRoutingEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCustomRoutingEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEndpointGroupRequestEndpointConfigurations(TeaModel):
    def __init__(
        self,
        enable_client_ippreservation: bool = None,
        endpoint: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.enable_client_ippreservation = enable_client_ippreservation
        self.endpoint = endpoint
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateEndpointGroupRequestPortOverrides(TeaModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        self.endpoint_port = endpoint_port
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class CreateEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        description: str = None,
        endpoint_configurations: List[CreateEndpointGroupRequestEndpointConfigurations] = None,
        endpoint_group_region: str = None,
        endpoint_group_type: str = None,
        endpoint_request_protocol: str = None,
        health_check_enabled: bool = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        listener_id: str = None,
        name: str = None,
        port_overrides: List[CreateEndpointGroupRequestPortOverrides] = None,
        region_id: str = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.description = description
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_group_type = endpoint_group_type
        self.endpoint_request_protocol = endpoint_request_protocol
        self.health_check_enabled = health_check_enabled
        self.health_check_interval_seconds = health_check_interval_seconds
        self.health_check_path = health_check_path
        self.health_check_port = health_check_port
        self.health_check_protocol = health_check_protocol
        self.listener_id = listener_id
        self.name = name
        self.port_overrides = port_overrides
        self.region_id = region_id
        self.threshold_count = threshold_count
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateEndpointGroupRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = CreateEndpointGroupRequestPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class CreateEndpointGroupResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
        request_id: str = None,
    ):
        self.endpoint_group_id = endpoint_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.endpoint = endpoint
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides(TeaModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        self.endpoint_port = endpoint_port
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class CreateEndpointGroupsRequestEndpointGroupConfigurations(TeaModel):
    def __init__(
        self,
        enable_client_ippreservation_proxy_protocol: bool = None,
        enable_client_ippreservation_toa: bool = None,
        endpoint_configurations: List[CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations] = None,
        endpoint_group_description: str = None,
        endpoint_group_name: str = None,
        endpoint_group_region: str = None,
        endpoint_group_type: str = None,
        endpoint_request_protocol: str = None,
        health_check_enabled: bool = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        port_overrides: List[CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides] = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        self.enable_client_ippreservation_proxy_protocol = enable_client_ippreservation_proxy_protocol
        self.enable_client_ippreservation_toa = enable_client_ippreservation_toa
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_description = endpoint_group_description
        self.endpoint_group_name = endpoint_group_name
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_group_type = endpoint_group_type
        self.endpoint_request_protocol = endpoint_request_protocol
        self.health_check_enabled = health_check_enabled
        self.health_check_interval_seconds = health_check_interval_seconds
        self.health_check_path = health_check_path
        self.health_check_port = health_check_port
        self.health_check_protocol = health_check_protocol
        self.port_overrides = port_overrides
        self.threshold_count = threshold_count
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation_proxy_protocol is not None:
            result['EnableClientIPPreservationProxyProtocol'] = self.enable_client_ippreservation_proxy_protocol
        if self.enable_client_ippreservation_toa is not None:
            result['EnableClientIPPreservationToa'] = self.enable_client_ippreservation_toa
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description
        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableClientIPPreservationProxyProtocol') is not None:
            self.enable_client_ippreservation_proxy_protocol = m.get('EnableClientIPPreservationProxyProtocol')
        if m.get('EnableClientIPPreservationToa') is not None:
            self.enable_client_ippreservation_toa = m.get('EnableClientIPPreservationToa')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')
        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class CreateEndpointGroupsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_group_configurations: List[CreateEndpointGroupsRequestEndpointGroupConfigurations] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_group_configurations = endpoint_group_configurations
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = CreateEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateEndpointGroupsResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_group_ids: List[str] = None,
        request_id: str = None,
    ):
        self.endpoint_group_ids = endpoint_group_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEndpointGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEndpointGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
    ):
        self.endpoint_group_id = endpoint_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class CreateForwardingRulesRequestForwardingRulesRuleActions(TeaModel):
    def __init__(
        self,
        forward_group_config: CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig = None,
        order: int = None,
        rule_action_type: str = None,
        rule_action_value: str = None,
    ):
        self.forward_group_config = forward_group_config
        self.order = order
        self.rule_action_type = rule_action_type
        self.rule_action_value = rule_action_value

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_action_value is not None:
            result['RuleActionValue'] = self.rule_action_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class CreateForwardingRulesRequestForwardingRulesRuleConditions(TeaModel):
    def __init__(
        self,
        host_config: CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig = None,
        path_config: CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig = None,
        rule_condition_type: str = None,
        rule_condition_value: str = None,
    ):
        self.host_config = host_config
        self.path_config = path_config
        self.rule_condition_type = rule_condition_type
        self.rule_condition_value = rule_condition_value

    def validate(self):
        if self.host_config:
            self.host_config.validate()
        if self.path_config:
            self.path_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type
        if self.rule_condition_value is not None:
            result['RuleConditionValue'] = self.rule_condition_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostConfig') is not None:
            temp_model = CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('PathConfig') is not None:
            temp_model = CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')
        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')
        return self


class CreateForwardingRulesRequestForwardingRules(TeaModel):
    def __init__(
        self,
        forwarding_rule_name: str = None,
        priority: int = None,
        rule_actions: List[CreateForwardingRulesRequestForwardingRulesRuleActions] = None,
        rule_conditions: List[CreateForwardingRulesRequestForwardingRulesRuleConditions] = None,
        rule_direction: str = None,
    ):
        self.forwarding_rule_name = forwarding_rule_name
        self.priority = priority
        self.rule_actions = rule_actions
        self.rule_conditions = rule_conditions
        self.rule_direction = rule_direction

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        if self.rule_direction is not None:
            result['RuleDirection'] = self.rule_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = CreateForwardingRulesRequestForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = CreateForwardingRulesRequestForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        if m.get('RuleDirection') is not None:
            self.rule_direction = m.get('RuleDirection')
        return self


class CreateForwardingRulesRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        forwarding_rules: List[CreateForwardingRulesRequestForwardingRules] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.forwarding_rules = forwarding_rules
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = CreateForwardingRulesRequestForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(
        self,
        forwarding_rule_id: str = None,
    ):
        self.forwarding_rule_id = forwarding_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        return self


class CreateForwardingRulesResponseBody(TeaModel):
    def __init__(
        self,
        forwarding_rules: List[CreateForwardingRulesResponseBodyForwardingRules] = None,
        request_id: str = None,
    ):
        self.forwarding_rules = forwarding_rules
        self.request_id = request_id

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = CreateForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateForwardingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateForwardingRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpSetsRequestAccelerateRegion(TeaModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        bandwidth: int = None,
        ip_version: str = None,
        isp_type: str = None,
    ):
        self.accelerate_region_id = accelerate_region_id
        self.bandwidth = bandwidth
        self.ip_version = ip_version
        self.isp_type = isp_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        return self


class CreateIpSetsRequest(TeaModel):
    def __init__(
        self,
        accelerate_region: List[CreateIpSetsRequestAccelerateRegion] = None,
        accelerator_id: str = None,
        client_token: str = None,
        region_id: str = None,
    ):
        self.accelerate_region = accelerate_region
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.region_id = region_id

    def validate(self):
        if self.accelerate_region:
            for k in self.accelerate_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccelerateRegion'] = []
        if self.accelerate_region is not None:
            for k in self.accelerate_region:
                result['AccelerateRegion'].append(k.to_map() if k else None)
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accelerate_region = []
        if m.get('AccelerateRegion') is not None:
            for k in m.get('AccelerateRegion'):
                temp_model = CreateIpSetsRequestAccelerateRegion()
                self.accelerate_region.append(temp_model.from_map(k))
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateIpSetsResponseBodyIpSets(TeaModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        bandwidth: int = None,
        ip_set_id: str = None,
        isp_type: str = None,
    ):
        self.accelerate_region_id = accelerate_region_id
        self.bandwidth = bandwidth
        self.ip_set_id = ip_set_id
        self.isp_type = isp_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        return self


class CreateIpSetsResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        ip_sets: List[CreateIpSetsResponseBodyIpSets] = None,
        request_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.ip_sets = ip_sets
        self.request_id = request_id

    def validate(self):
        if self.ip_sets:
            for k in self.ip_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k in self.ip_sets:
                result['IpSets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k in m.get('IpSets'):
                temp_model = CreateIpSetsResponseBodyIpSets()
                self.ip_sets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIpSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIpSetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateListenerRequestCertificates(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        protocols: List[str] = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.protocols = protocols
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations(TeaModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges] = None,
    ):
        self.address = address
        self.port_ranges = port_ranges

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        policy_configurations: List[CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations] = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        self.endpoint = endpoint
        self.policy_configurations = policy_configurations
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        self.type = type

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateListenerRequestCustomRoutingEndpointGroupConfigurations(TeaModel):
    def __init__(
        self,
        description: str = None,
        destination_configurations: List[CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations] = None,
        endpoint_configurations: List[CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations] = None,
        endpoint_group_region: str = None,
        name: str = None,
    ):
        self.description = description
        self.destination_configurations = destination_configurations
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_region = endpoint_group_region
        self.name = name

    def validate(self):
        if self.destination_configurations:
            for k in self.destination_configurations:
                if k:
                    k.validate()
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k in self.destination_configurations:
                result['DestinationConfigurations'].append(k.to_map() if k else None)
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k in m.get('DestinationConfigurations'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurationsDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k))
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.endpoint = endpoint
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateListenerRequestEndpointGroupConfigurationsPortOverrides(TeaModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        self.endpoint_port = endpoint_port
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class CreateListenerRequestEndpointGroupConfigurations(TeaModel):
    def __init__(
        self,
        enable_client_ippreservation_proxy_protocol: bool = None,
        enable_client_ippreservation_toa: bool = None,
        endpoint_configurations: List[CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations] = None,
        endpoint_group_description: str = None,
        endpoint_group_name: str = None,
        endpoint_group_region: str = None,
        endpoint_group_type: str = None,
        endpoint_request_protocol: str = None,
        health_check_enabled: bool = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        port_overrides: List[CreateListenerRequestEndpointGroupConfigurationsPortOverrides] = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        self.enable_client_ippreservation_proxy_protocol = enable_client_ippreservation_proxy_protocol
        self.enable_client_ippreservation_toa = enable_client_ippreservation_toa
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_description = endpoint_group_description
        self.endpoint_group_name = endpoint_group_name
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_group_type = endpoint_group_type
        self.endpoint_request_protocol = endpoint_request_protocol
        self.health_check_enabled = health_check_enabled
        self.health_check_interval_seconds = health_check_interval_seconds
        self.health_check_path = health_check_path
        self.health_check_port = health_check_port
        self.health_check_protocol = health_check_protocol
        self.port_overrides = port_overrides
        self.threshold_count = threshold_count
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation_proxy_protocol is not None:
            result['EnableClientIPPreservationProxyProtocol'] = self.enable_client_ippreservation_proxy_protocol
        if self.enable_client_ippreservation_toa is not None:
            result['EnableClientIPPreservationToa'] = self.enable_client_ippreservation_toa
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description
        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableClientIPPreservationProxyProtocol') is not None:
            self.enable_client_ippreservation_proxy_protocol = m.get('EnableClientIPPreservationProxyProtocol')
        if m.get('EnableClientIPPreservationToa') is not None:
            self.enable_client_ippreservation_toa = m.get('EnableClientIPPreservationToa')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = CreateListenerRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')
        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = CreateListenerRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class CreateListenerRequestPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class CreateListenerRequestXForwardedForConfig(TeaModel):
    def __init__(
        self,
        xforwarded_for_ga_ap_enabled: bool = None,
        xforwarded_for_ga_id_enabled: bool = None,
        xforwarded_for_port_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xreal_ip_enabled: bool = None,
    ):
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        self.xreal_ip_enabled = xreal_ip_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_ga_ap_enabled is not None:
            result['XForwardedForGaApEnabled'] = self.xforwarded_for_ga_ap_enabled
        if self.xforwarded_for_ga_id_enabled is not None:
            result['XForwardedForGaIdEnabled'] = self.xforwarded_for_ga_id_enabled
        if self.xforwarded_for_port_enabled is not None:
            result['XForwardedForPortEnabled'] = self.xforwarded_for_port_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xreal_ip_enabled is not None:
            result['XRealIpEnabled'] = self.xreal_ip_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForGaApEnabled') is not None:
            self.xforwarded_for_ga_ap_enabled = m.get('XForwardedForGaApEnabled')
        if m.get('XForwardedForGaIdEnabled') is not None:
            self.xforwarded_for_ga_id_enabled = m.get('XForwardedForGaIdEnabled')
        if m.get('XForwardedForPortEnabled') is not None:
            self.xforwarded_for_port_enabled = m.get('XForwardedForPortEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XRealIpEnabled') is not None:
            self.xreal_ip_enabled = m.get('XRealIpEnabled')
        return self


class CreateListenerRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        certificates: List[CreateListenerRequestCertificates] = None,
        client_affinity: str = None,
        client_token: str = None,
        custom_routing_endpoint_group_configurations: List[CreateListenerRequestCustomRoutingEndpointGroupConfigurations] = None,
        description: str = None,
        endpoint_group_configurations: List[CreateListenerRequestEndpointGroupConfigurations] = None,
        name: str = None,
        port_ranges: List[CreateListenerRequestPortRanges] = None,
        protocol: str = None,
        proxy_protocol: bool = None,
        region_id: str = None,
        security_policy_id: str = None,
        type: str = None,
        xforwarded_for_config: CreateListenerRequestXForwardedForConfig = None,
    ):
        self.accelerator_id = accelerator_id
        self.certificates = certificates
        self.client_affinity = client_affinity
        self.client_token = client_token
        self.custom_routing_endpoint_group_configurations = custom_routing_endpoint_group_configurations
        self.description = description
        self.endpoint_group_configurations = endpoint_group_configurations
        self.name = name
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.proxy_protocol = proxy_protocol
        self.region_id = region_id
        self.security_policy_id = security_policy_id
        self.type = type
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.custom_routing_endpoint_group_configurations:
            for k in self.custom_routing_endpoint_group_configurations:
                if k:
                    k.validate()
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['CustomRoutingEndpointGroupConfigurations'] = []
        if self.custom_routing_endpoint_group_configurations is not None:
            for k in self.custom_routing_endpoint_group_configurations:
                result['CustomRoutingEndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.type is not None:
            result['Type'] = self.type
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = CreateListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.custom_routing_endpoint_group_configurations = []
        if m.get('CustomRoutingEndpointGroupConfigurations') is not None:
            for k in m.get('CustomRoutingEndpointGroupConfigurations'):
                temp_model = CreateListenerRequestCustomRoutingEndpointGroupConfigurations()
                self.custom_routing_endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = CreateListenerRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = CreateListenerRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('XForwardedForConfig') is not None:
            temp_model = CreateListenerRequestXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class CreateListenerResponseBody(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        request_id: str = None,
    ):
        self.listener_id = listener_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpareIpsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        spare_ips: List[str] = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id
        self.spare_ips = spare_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spare_ips is not None:
            result['SpareIps'] = self.spare_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpareIps') is not None:
            self.spare_ips = m.get('SpareIps')
        return self


class CreateSpareIpsResponseBody(TeaModel):
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


class CreateSpareIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSpareIpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSpareIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        request_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAclRequest(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.acl_id = acl_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAclResponseBody(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        request_id: str = None,
    ):
        self.acl_id = acl_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationMonitorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteApplicationMonitorResponseBody(TeaModel):
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


class DeleteApplicationMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApplicationMonitorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBandwidthPackageRequest(TeaModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        client_token: str = None,
        region_id: str = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id
        self.client_token = client_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBandwidthPackageResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        request_id: str = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBandwidthPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBandwidthPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBasicAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBasicAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        request_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBasicAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBasicAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBasicAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBasicEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_group_id: str = None,
    ):
        self.client_token = client_token
        self.endpoint_group_id = endpoint_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class DeleteBasicEndpointGroupResponseBody(TeaModel):
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


class DeleteBasicEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBasicEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBasicEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBasicIpSetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        ip_set_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.ip_set_id = ip_set_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBasicIpSetResponseBody(TeaModel):
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


class DeleteBasicIpSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBasicIpSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBasicIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        destination_ids: List[str] = None,
        dry_run: bool = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.destination_ids = destination_ids
        self.dry_run = dry_run
        self.endpoint_group_id = endpoint_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination_ids is not None:
            result['DestinationIds'] = self.destination_ids
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestinationIds') is not None:
            self.destination_ids = m.get('DestinationIds')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
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


class DeleteCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomRoutingEndpointGroupDestinationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomRoutingEndpointGroupsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_group_ids: List[str] = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_group_ids = endpoint_group_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCustomRoutingEndpointGroupsResponseBody(TeaModel):
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


class DeleteCustomRoutingEndpointGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomRoutingEndpointGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCustomRoutingEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomRoutingEndpointTrafficPoliciesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_id: str = None,
        policy_ids: List[str] = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.endpoint_id = endpoint_id
        self.policy_ids = policy_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCustomRoutingEndpointTrafficPoliciesResponseBody(TeaModel):
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


class DeleteCustomRoutingEndpointTrafficPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomRoutingEndpointTrafficPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCustomRoutingEndpointTrafficPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomRoutingEndpointsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_group_id: str = None,
        endpoint_ids: List[str] = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_ids = endpoint_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCustomRoutingEndpointsResponseBody(TeaModel):
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


class DeleteCustomRoutingEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomRoutingEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCustomRoutingEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        endpoint_group_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.endpoint_group_id = endpoint_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class DeleteEndpointGroupResponseBody(TeaModel):
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


class DeleteEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEndpointGroupsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_group_ids: List[str] = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_group_ids = endpoint_group_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteEndpointGroupsResponseBody(TeaModel):
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


class DeleteEndpointGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEndpointGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteForwardingRulesRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        forwarding_rule_ids: List[str] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.forwarding_rule_ids = forwarding_rule_ids
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(
        self,
        forwarding_rule_id: str = None,
    ):
        self.forwarding_rule_id = forwarding_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        return self


class DeleteForwardingRulesResponseBody(TeaModel):
    def __init__(
        self,
        forwarding_rules: List[DeleteForwardingRulesResponseBodyForwardingRules] = None,
        request_id: str = None,
    ):
        self.forwarding_rules = forwarding_rules
        self.request_id = request_id

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = DeleteForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteForwardingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteForwardingRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpSetRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        ip_set_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.ip_set_id = ip_set_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIpSetResponseBody(TeaModel):
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


class DeleteIpSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpSetsRequest(TeaModel):
    def __init__(
        self,
        ip_set_ids: List[str] = None,
        region_id: str = None,
    ):
        self.ip_set_ids = ip_set_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_set_ids is not None:
            result['IpSetIds'] = self.ip_set_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpSetIds') is not None:
            self.ip_set_ids = m.get('IpSetIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIpSetsResponseBody(TeaModel):
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


class DeleteIpSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpSetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteListenerRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        listener_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class DeleteListenerResponseBody(TeaModel):
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


class DeleteListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpareIpsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        spare_ips: List[str] = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id
        self.spare_ips = spare_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spare_ips is not None:
            result['SpareIps'] = self.spare_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpareIps') is not None:
            self.spare_ips = m.get('SpareIps')
        return self


class DeleteSpareIpsResponseBody(TeaModel):
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


class DeleteSpareIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSpareIpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSpareIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAcceleratorResponseBodyBasicBandwidthPackage(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        bandwidth_type: str = None,
        instance_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.bandwidth_type = bandwidth_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        instance_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeAcceleratorResponseBodyIpSetConfig(TeaModel):
    def __init__(
        self,
        access_mode: str = None,
    ):
        self.access_mode = access_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class DescribeAcceleratorResponseBodyTags(TeaModel):
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


class DescribeAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth_billing_type: str = None,
        basic_bandwidth_package: DescribeAcceleratorResponseBodyBasicBandwidthPackage = None,
        cen_id: str = None,
        create_time: int = None,
        cross_domain_bandwidth_package: DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage = None,
        cross_private_state: str = None,
        ddos_id: str = None,
        description: str = None,
        dns_name: str = None,
        expired_time: int = None,
        instance_charge_type: str = None,
        ip_set_config: DescribeAcceleratorResponseBodyIpSetConfig = None,
        name: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        second_dns_name: str = None,
        spec: str = None,
        state: str = None,
        tags: List[DescribeAcceleratorResponseBodyTags] = None,
    ):
        self.accelerator_id = accelerator_id
        self.bandwidth_billing_type = bandwidth_billing_type
        self.basic_bandwidth_package = basic_bandwidth_package
        self.cen_id = cen_id
        self.create_time = create_time
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package
        self.cross_private_state = cross_private_state
        self.ddos_id = ddos_id
        self.description = description
        self.dns_name = dns_name
        self.expired_time = expired_time
        self.instance_charge_type = instance_charge_type
        self.ip_set_config = ip_set_config
        self.name = name
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.second_dns_name = second_dns_name
        self.spec = spec
        self.state = state
        self.tags = tags

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.ip_set_config:
            self.ip_set_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        if self.cross_private_state is not None:
            result['CrossPrivateState'] = self.cross_private_state
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.ip_set_config is not None:
            result['IpSetConfig'] = self.ip_set_config.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.second_dns_name is not None:
            result['SecondDnsName'] = self.second_dns_name
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = DescribeAcceleratorResponseBodyBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = DescribeAcceleratorResponseBodyCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        if m.get('CrossPrivateState') is not None:
            self.cross_private_state = m.get('CrossPrivateState')
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('IpSetConfig') is not None:
            temp_model = DescribeAcceleratorResponseBodyIpSetConfig()
            self.ip_set_config = temp_model.from_map(m['IpSetConfig'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondDnsName') is not None:
            self.second_dns_name = m.get('SecondDnsName')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeAcceleratorResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAcceleratorAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAcceleratorAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        renewal_status: str = None,
        request_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.renewal_status = renewal_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAcceleratorAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAcceleratorAutoRenewAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAcceleratorAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationMonitorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeApplicationMonitorResponseBodyIspCityList(TeaModel):
    def __init__(
        self,
        city: str = None,
        city_name: str = None,
        isp: str = None,
        isp_name: str = None,
    ):
        self.city = city
        self.city_name = city_name
        self.isp = isp
        self.isp_name = isp_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.isp_name is not None:
            result['IspName'] = self.isp_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')
        return self


class DescribeApplicationMonitorResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        address: str = None,
        detect_enable: bool = None,
        detect_threshold: int = None,
        detect_times: int = None,
        isp_city_list: List[DescribeApplicationMonitorResponseBodyIspCityList] = None,
        listener_id: str = None,
        options_json: str = None,
        region_id: str = None,
        request_id: str = None,
        silence_time: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.address = address
        self.detect_enable = detect_enable
        self.detect_threshold = detect_threshold
        self.detect_times = detect_times
        self.isp_city_list = isp_city_list
        self.listener_id = listener_id
        self.options_json = options_json
        self.region_id = region_id
        self.request_id = request_id
        self.silence_time = silence_time
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        if self.isp_city_list:
            for k in self.isp_city_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.detect_enable is not None:
            result['DetectEnable'] = self.detect_enable
        if self.detect_threshold is not None:
            result['DetectThreshold'] = self.detect_threshold
        if self.detect_times is not None:
            result['DetectTimes'] = self.detect_times
        result['IspCityList'] = []
        if self.isp_city_list is not None:
            for k in self.isp_city_list:
                result['IspCityList'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.options_json is not None:
            result['OptionsJson'] = self.options_json
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('DetectEnable') is not None:
            self.detect_enable = m.get('DetectEnable')
        if m.get('DetectThreshold') is not None:
            self.detect_threshold = m.get('DetectThreshold')
        if m.get('DetectTimes') is not None:
            self.detect_times = m.get('DetectTimes')
        self.isp_city_list = []
        if m.get('IspCityList') is not None:
            for k in m.get('IspCityList'):
                temp_model = DescribeApplicationMonitorResponseBodyIspCityList()
                self.isp_city_list.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribeApplicationMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApplicationMonitorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBandwidthPackageRequest(TeaModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        region_id: str = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBandwidthPackageResponseBodyTags(TeaModel):
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


class DescribeBandwidthPackageResponseBody(TeaModel):
    def __init__(
        self,
        accelerators: List[str] = None,
        bandwidth: int = None,
        bandwidth_package_id: str = None,
        bandwidth_type: str = None,
        billing_type: str = None,
        cbn_geographic_region_id_a: str = None,
        cbn_geographic_region_id_b: str = None,
        charge_type: str = None,
        create_time: str = None,
        description: str = None,
        expired_time: str = None,
        name: str = None,
        ratio: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[DescribeBandwidthPackageResponseBodyTags] = None,
        type: str = None,
    ):
        self.accelerators = accelerators
        self.bandwidth = bandwidth
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_type = bandwidth_type
        self.billing_type = billing_type
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b
        self.charge_type = charge_type
        self.create_time = create_time
        self.description = description
        self.expired_time = expired_time
        self.name = name
        self.ratio = ratio
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.state = state
        self.tags = tags
        self.type = type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.name is not None:
            result['Name'] = self.name
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeBandwidthPackageResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeBandwidthPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBandwidthPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBandwidthPackageAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeBandwidthPackageAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        instance_id: str = None,
        renewal_status: str = None,
        request_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.instance_id = instance_id
        self.renewal_status = renewal_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBandwidthPackageAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBandwidthPackageAutoRenewAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBandwidthPackageAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomRoutingEndPointTrafficPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        region_id: str = None,
    ):
        self.policy_id = policy_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomRoutingEndPointTrafficPolicyResponseBodyPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeCustomRoutingEndPointTrafficPolicyResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        address: str = None,
        endpoint: str = None,
        endpoint_group_id: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        policy_id: str = None,
        port_ranges: List[DescribeCustomRoutingEndPointTrafficPolicyResponseBodyPortRanges] = None,
        request_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.address = address
        self.endpoint = endpoint
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_id = endpoint_id
        self.listener_id = listener_id
        self.policy_id = policy_id
        self.port_ranges = port_ranges
        self.request_id = request_id

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = DescribeCustomRoutingEndPointTrafficPolicyResponseBodyPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCustomRoutingEndPointTrafficPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomRoutingEndPointTrafficPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomRoutingEndPointTrafficPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomRoutingEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        region_id: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomRoutingEndpointResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        endpoint: str = None,
        endpoint_group_id: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        request_id: str = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.endpoint = endpoint
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_id = endpoint_id
        self.listener_id = listener_id
        self.request_id = request_id
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCustomRoutingEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomRoutingEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomRoutingEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomRoutingEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        self.endpoint_group_id = endpoint_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomRoutingEndpointGroupResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_log_switch: str = None,
        description: str = None,
        enable_access_log: bool = None,
        endpoint_group_id: str = None,
        endpoint_group_ip_list: List[str] = None,
        endpoint_group_region: str = None,
        endpoint_group_unconfirmed_ip_list: List[str] = None,
        listener_id: str = None,
        name: str = None,
        request_id: str = None,
        sls_log_store_name: str = None,
        sls_project_name: str = None,
        sls_region: str = None,
        state: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.access_log_switch = access_log_switch
        self.description = description
        self.enable_access_log = enable_access_log
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_ip_list = endpoint_group_ip_list
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list
        self.listener_id = listener_id
        self.name = name
        self.request_id = request_id
        self.sls_log_store_name = sls_log_store_name
        self.sls_project_name = sls_project_name
        self.sls_region = sls_region
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_access_log is not None:
            result['EnableAccessLog'] = self.enable_access_log
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name
        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name
        if self.sls_region is not None:
            result['SlsRegion'] = self.sls_region
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAccessLog') is not None:
            self.enable_access_log = m.get('EnableAccessLog')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')
        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')
        if m.get('SlsRegion') is not None:
            self.sls_region = m.get('SlsRegion')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeCustomRoutingEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomRoutingEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomRoutingEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(
        self,
        destination_id: str = None,
        region_id: str = None,
    ):
        self.destination_id = destination_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        destination_id: str = None,
        endpoint_group_id: str = None,
        from_port: int = None,
        listener_id: str = None,
        protocols: List[str] = None,
        request_id: str = None,
        to_port: int = None,
    ):
        self.accelerator_id = accelerator_id
        self.destination_id = destination_id
        self.endpoint_group_id = endpoint_group_id
        self.from_port = from_port
        self.listener_id = listener_id
        self.protocols = protocols
        self.request_id = request_id
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomRoutingEndpointGroupDestinationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        self.endpoint_group_id = endpoint_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeEndpointGroupResponseBodyEndpointConfigurations(TeaModel):
    def __init__(
        self,
        enable_client_ippreservation: bool = None,
        endpoint: str = None,
        probe_port: int = None,
        probe_protocol: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.enable_client_ippreservation = enable_client_ippreservation
        self.endpoint = endpoint
        self.probe_port = probe_port
        self.probe_protocol = probe_protocol
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port
        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')
        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeEndpointGroupResponseBodyPortOverrides(TeaModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        self.endpoint_port = endpoint_port
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class DescribeEndpointGroupResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_log_switch: str = None,
        description: str = None,
        enable_access_log: bool = None,
        endpoint_configurations: List[DescribeEndpointGroupResponseBodyEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        endpoint_group_ip_list: List[str] = None,
        endpoint_group_region: str = None,
        endpoint_group_type: str = None,
        endpoint_group_unconfirmed_ip_list: List[str] = None,
        endpoint_request_protocol: str = None,
        forwarding_rule_ids: List[str] = None,
        health_check_enabled: bool = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        listener_id: str = None,
        name: str = None,
        port_overrides: List[DescribeEndpointGroupResponseBodyPortOverrides] = None,
        request_id: str = None,
        sls_log_store_name: str = None,
        sls_project_name: str = None,
        sls_region: str = None,
        state: str = None,
        threshold_count: int = None,
        total_count: int = None,
        traffic_percentage: int = None,
    ):
        self.accelerator_id = accelerator_id
        self.access_log_switch = access_log_switch
        self.description = description
        self.enable_access_log = enable_access_log
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_ip_list = endpoint_group_ip_list
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_group_type = endpoint_group_type
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list
        self.endpoint_request_protocol = endpoint_request_protocol
        self.forwarding_rule_ids = forwarding_rule_ids
        self.health_check_enabled = health_check_enabled
        self.health_check_interval_seconds = health_check_interval_seconds
        self.health_check_path = health_check_path
        self.health_check_port = health_check_port
        self.health_check_protocol = health_check_protocol
        self.listener_id = listener_id
        self.name = name
        self.port_overrides = port_overrides
        self.request_id = request_id
        self.sls_log_store_name = sls_log_store_name
        self.sls_project_name = sls_project_name
        self.sls_region = sls_region
        self.state = state
        self.threshold_count = threshold_count
        self.total_count = total_count
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_access_log is not None:
            result['EnableAccessLog'] = self.enable_access_log
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name
        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name
        if self.sls_region is not None:
            result['SlsRegion'] = self.sls_region
        if self.state is not None:
            result['State'] = self.state
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableAccessLog') is not None:
            self.enable_access_log = m.get('EnableAccessLog')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = DescribeEndpointGroupResponseBodyEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = DescribeEndpointGroupResponseBodyPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')
        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')
        if m.get('SlsRegion') is not None:
            self.sls_region = m.get('SlsRegion')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class DescribeEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpSetRequest(TeaModel):
    def __init__(
        self,
        ip_set_id: str = None,
        region_id: str = None,
    ):
        self.ip_set_id = ip_set_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeIpSetResponseBody(TeaModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        accelerator_id: str = None,
        bandwidth: int = None,
        ip_address_list: List[str] = None,
        ip_set_id: str = None,
        ip_version: str = None,
        isp_type: str = None,
        request_id: str = None,
        state: str = None,
    ):
        self.accelerate_region_id = accelerate_region_id
        self.accelerator_id = accelerator_id
        self.bandwidth = bandwidth
        self.ip_address_list = ip_address_list
        self.ip_set_id = ip_set_id
        self.ip_version = ip_version
        self.isp_type = isp_type
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_address_list is not None:
            result['IpAddressList'] = self.ip_address_list
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpAddressList') is not None:
            self.ip_address_list = m.get('IpAddressList')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeIpSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIpSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeListenerRequest(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeListenerResponseBodyBackendPorts(TeaModel):
    def __init__(
        self,
        from_port: str = None,
        to_port: str = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeListenerResponseBodyCertificates(TeaModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        self.id = id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeListenerResponseBodyPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class DescribeListenerResponseBodyRelatedAcls(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        status: str = None,
    ):
        self.acl_id = acl_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeListenerResponseBodyXForwardedForConfig(TeaModel):
    def __init__(
        self,
        xforwarded_for_ga_ap_enabled: bool = None,
        xforwarded_for_ga_id_enabled: bool = None,
        xforwarded_for_port_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xreal_ip_enabled: bool = None,
    ):
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        self.xreal_ip_enabled = xreal_ip_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_ga_ap_enabled is not None:
            result['XForwardedForGaApEnabled'] = self.xforwarded_for_ga_ap_enabled
        if self.xforwarded_for_ga_id_enabled is not None:
            result['XForwardedForGaIdEnabled'] = self.xforwarded_for_ga_id_enabled
        if self.xforwarded_for_port_enabled is not None:
            result['XForwardedForPortEnabled'] = self.xforwarded_for_port_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xreal_ip_enabled is not None:
            result['XRealIpEnabled'] = self.xreal_ip_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForGaApEnabled') is not None:
            self.xforwarded_for_ga_ap_enabled = m.get('XForwardedForGaApEnabled')
        if m.get('XForwardedForGaIdEnabled') is not None:
            self.xforwarded_for_ga_id_enabled = m.get('XForwardedForGaIdEnabled')
        if m.get('XForwardedForPortEnabled') is not None:
            self.xforwarded_for_port_enabled = m.get('XForwardedForPortEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XRealIpEnabled') is not None:
            self.xreal_ip_enabled = m.get('XRealIpEnabled')
        return self


class DescribeListenerResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        acl_type: str = None,
        backend_ports: List[DescribeListenerResponseBodyBackendPorts] = None,
        certificates: List[DescribeListenerResponseBodyCertificates] = None,
        client_affinity: str = None,
        create_time: str = None,
        description: str = None,
        listener_id: str = None,
        name: str = None,
        port_ranges: List[DescribeListenerResponseBodyPortRanges] = None,
        protocol: str = None,
        proxy_protocol: bool = None,
        related_acls: List[DescribeListenerResponseBodyRelatedAcls] = None,
        request_id: str = None,
        security_policy_id: str = None,
        state: str = None,
        type: str = None,
        xforwarded_for_config: DescribeListenerResponseBodyXForwardedForConfig = None,
    ):
        self.accelerator_id = accelerator_id
        self.acl_type = acl_type
        self.backend_ports = backend_ports
        self.certificates = certificates
        self.client_affinity = client_affinity
        self.create_time = create_time
        self.description = description
        self.listener_id = listener_id
        self.name = name
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.proxy_protocol = proxy_protocol
        self.related_acls = related_acls
        self.request_id = request_id
        self.security_policy_id = security_policy_id
        self.state = state
        self.type = type
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.backend_ports:
            for k in self.backend_ports:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.related_acls:
            for k in self.related_acls:
                if k:
                    k.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k in self.backend_ports:
                result['BackendPorts'].append(k.to_map() if k else None)
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        result['RelatedAcls'] = []
        if self.related_acls is not None:
            for k in self.related_acls:
                result['RelatedAcls'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k in m.get('BackendPorts'):
                temp_model = DescribeListenerResponseBodyBackendPorts()
                self.backend_ports.append(temp_model.from_map(k))
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = DescribeListenerResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = DescribeListenerResponseBodyPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        self.related_acls = []
        if m.get('RelatedAcls') is not None:
            for k in m.get('RelatedAcls'):
                temp_model = DescribeListenerResponseBodyRelatedAcls()
                self.related_acls.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('XForwardedForConfig') is not None:
            temp_model = DescribeListenerResponseBodyXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class DescribeListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeListenerResponseBody()
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
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachDdosFromAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachDdosFromAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        ddos_id: str = None,
        request_id: str = None,
    ):
        self.ddos_id = ddos_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachDdosFromAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachDdosFromAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachDdosFromAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachLogStoreFromEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        endpoint_group_ids: List[str] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.endpoint_group_ids = endpoint_group_ids
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachLogStoreFromEndpointGroupResponseBody(TeaModel):
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


class DetachLogStoreFromEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachLogStoreFromEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachLogStoreFromEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectApplicationMonitorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetectApplicationMonitorResponseBody(TeaModel):
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


class DetectApplicationMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetectApplicationMonitorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetectApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableApplicationMonitorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DisableApplicationMonitorResponseBody(TeaModel):
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


class DisableApplicationMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableApplicationMonitorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateAclsFromListenerRequest(TeaModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.acl_ids = acl_ids
        self.client_token = client_token
        self.dry_run = dry_run
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateAclsFromListenerResponseBody(TeaModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        listener_id: str = None,
        request_id: str = None,
    ):
        self.acl_ids = acl_ids
        self.listener_id = listener_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DissociateAclsFromListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DissociateAclsFromListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DissociateAclsFromListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateAdditionalCertificatesFromListenerRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        domains: List[str] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.domains = domains
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateAdditionalCertificatesFromListenerResponseBody(TeaModel):
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


class DissociateAdditionalCertificatesFromListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DissociateAdditionalCertificatesFromListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DissociateAdditionalCertificatesFromListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationMonitorRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class EnableApplicationMonitorResponseBody(TeaModel):
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


class EnableApplicationMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableApplicationMonitorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAclRequest(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        region_id: str = None,
    ):
        self.acl_id = acl_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAclResponseBodyAclEntries(TeaModel):
    def __init__(
        self,
        entry: str = None,
        entry_description: str = None,
    ):
        self.entry = entry
        self.entry_description = entry_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')
        return self


class GetAclResponseBodyRelatedListeners(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        acl_type: str = None,
        listener_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.acl_type = acl_type
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.acl_type is not None:
            result['AclType'] = self.acl_type
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        return self


class GetAclResponseBodyTags(TeaModel):
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


class GetAclResponseBody(TeaModel):
    def __init__(
        self,
        acl_entries: List[GetAclResponseBodyAclEntries] = None,
        acl_id: str = None,
        acl_name: str = None,
        acl_status: str = None,
        address_ipversion: str = None,
        related_listeners: List[GetAclResponseBodyRelatedListeners] = None,
        request_id: str = None,
        resource_group_id: str = None,
        tags: List[GetAclResponseBodyTags] = None,
    ):
        self.acl_entries = acl_entries
        self.acl_id = acl_id
        self.acl_name = acl_name
        self.acl_status = acl_status
        self.address_ipversion = address_ipversion
        self.related_listeners = related_listeners
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()
        if self.related_listeners:
            for k in self.related_listeners:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k in self.related_listeners:
                result['RelatedListeners'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = GetAclResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k in m.get('RelatedListeners'):
                temp_model = GetAclResponseBodyRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetAclResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBasicAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBasicAcceleratorResponseBodyBasicBandwidthPackage(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        bandwidth_type: str = None,
        instance_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.bandwidth_type = bandwidth_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        instance_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetBasicAcceleratorResponseBodyTags(TeaModel):
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


class GetBasicAcceleratorResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth_billing_type: str = None,
        basic_bandwidth_package: GetBasicAcceleratorResponseBodyBasicBandwidthPackage = None,
        basic_endpoint_group_id: str = None,
        basic_ip_set_id: str = None,
        cen_id: str = None,
        create_time: int = None,
        cross_domain_bandwidth_package: GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage = None,
        cross_private_state: str = None,
        description: str = None,
        expired_time: int = None,
        instance_charge_type: str = None,
        name: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[GetBasicAcceleratorResponseBodyTags] = None,
    ):
        self.accelerator_id = accelerator_id
        self.bandwidth_billing_type = bandwidth_billing_type
        self.basic_bandwidth_package = basic_bandwidth_package
        self.basic_endpoint_group_id = basic_endpoint_group_id
        self.basic_ip_set_id = basic_ip_set_id
        self.cen_id = cen_id
        self.create_time = create_time
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package
        self.cross_private_state = cross_private_state
        self.description = description
        self.expired_time = expired_time
        self.instance_charge_type = instance_charge_type
        self.name = name
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.state = state
        self.tags = tags

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.basic_endpoint_group_id is not None:
            result['BasicEndpointGroupId'] = self.basic_endpoint_group_id
        if self.basic_ip_set_id is not None:
            result['BasicIpSetId'] = self.basic_ip_set_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        if self.cross_private_state is not None:
            result['CrossPrivateState'] = self.cross_private_state
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = GetBasicAcceleratorResponseBodyBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('BasicEndpointGroupId') is not None:
            self.basic_endpoint_group_id = m.get('BasicEndpointGroupId')
        if m.get('BasicIpSetId') is not None:
            self.basic_ip_set_id = m.get('BasicIpSetId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = GetBasicAcceleratorResponseBodyCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        if m.get('CrossPrivateState') is not None:
            self.cross_private_state = m.get('CrossPrivateState')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetBasicAcceleratorResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetBasicAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBasicAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBasicAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBasicEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.endpoint_group_id = endpoint_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBasicEndpointGroupResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        description: str = None,
        endpoint_address: str = None,
        endpoint_group_id: str = None,
        endpoint_group_region: str = None,
        endpoint_sub_address: str = None,
        endpoint_type: str = None,
        name: str = None,
        request_id: str = None,
        state: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.description = description
        self.endpoint_address = endpoint_address
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_sub_address = endpoint_sub_address
        self.endpoint_type = endpoint_type
        self.name = name
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetBasicEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBasicEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBasicEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBasicIpSetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        ip_set_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.ip_set_id = ip_set_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetBasicIpSetResponseBody(TeaModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        accelerator_id: str = None,
        bandwidth: int = None,
        ip_address: str = None,
        ip_set_id: str = None,
        ip_version: str = None,
        isp_type: str = None,
        request_id: str = None,
        state: str = None,
    ):
        self.accelerate_region_id = accelerate_region_id
        self.accelerator_id = accelerator_id
        self.bandwidth = bandwidth
        self.ip_address = ip_address
        self.ip_set_id = ip_set_id
        self.ip_version = ip_version
        self.isp_type = isp_type
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetBasicIpSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBasicIpSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetBasicIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHealthStatusRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHealthStatusResponseBodyEndpointGroupsEndpoints(TeaModel):
    def __init__(
        self,
        address: str = None,
        endpoint_id: str = None,
        health_detail: str = None,
        health_status: str = None,
        port: int = None,
        type: str = None,
    ):
        self.address = address
        self.endpoint_id = endpoint_id
        self.health_detail = health_detail
        self.health_status = health_status
        self.port = port
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.health_detail is not None:
            result['HealthDetail'] = self.health_detail
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.port is not None:
            result['Port'] = self.port
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('HealthDetail') is not None:
            self.health_detail = m.get('HealthDetail')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetHealthStatusResponseBodyEndpointGroups(TeaModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
        endpoint_group_type: str = None,
        endpoints: List[GetHealthStatusResponseBodyEndpointGroupsEndpoints] = None,
        forwarding_rule_ids: List[str] = None,
        health_status: str = None,
    ):
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_type = endpoint_group_type
        self.endpoints = endpoints
        self.forwarding_rule_ids = forwarding_rule_ids
        self.health_status = health_status

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = GetHealthStatusResponseBodyEndpointGroupsEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        return self


class GetHealthStatusResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_groups: List[GetHealthStatusResponseBodyEndpointGroups] = None,
        health_status: str = None,
        listener_id: str = None,
        request_id: str = None,
    ):
        self.endpoint_groups = endpoint_groups
        self.health_status = health_status
        self.listener_id = listener_id
        self.request_id = request_id

    def validate(self):
        if self.endpoint_groups:
            for k in self.endpoint_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k in self.endpoint_groups:
                result['EndpointGroups'].append(k.to_map() if k else None)
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k in m.get('EndpointGroups'):
                temp_model = GetHealthStatusResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k))
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHealthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHealthStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpareIpRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        spare_ip: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id
        self.spare_ip = spare_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spare_ip is not None:
            result['SpareIp'] = self.spare_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpareIp') is not None:
            self.spare_ip = m.get('SpareIp')
        return self


class GetSpareIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state: str = None,
    ):
        self.request_id = request_id
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetSpareIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSpareIpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSpareIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccelerateAreasRequest(TeaModel):
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


class ListAccelerateAreasResponseBodyAreasRegionList(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccelerateAreasResponseBodyAreas(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        local_name: str = None,
        region_list: List[ListAccelerateAreasResponseBodyAreasRegionList] = None,
    ):
        self.area_id = area_id
        self.local_name = local_name
        self.region_list = region_list

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = ListAccelerateAreasResponseBodyAreasRegionList()
                self.region_list.append(temp_model.from_map(k))
        return self


class ListAccelerateAreasResponseBody(TeaModel):
    def __init__(
        self,
        areas: List[ListAccelerateAreasResponseBodyAreas] = None,
        request_id: str = None,
    ):
        self.areas = areas
        self.request_id = request_id

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = ListAccelerateAreasResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAccelerateAreasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccelerateAreasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccelerateAreasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAcceleratorsRequestTag(TeaModel):
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


class ListAcceleratorsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tag: List[ListAcceleratorsRequestTag] = None,
    ):
        self.accelerator_id = accelerator_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.state = state
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
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAcceleratorsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        bandwidth_type: str = None,
        instance_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.bandwidth_type = bandwidth_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        instance_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAcceleratorsResponseBodyAcceleratorsIpSetConfig(TeaModel):
    def __init__(
        self,
        access_mode: str = None,
    ):
        self.access_mode = access_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        return self


class ListAcceleratorsResponseBodyAcceleratorsTags(TeaModel):
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


class ListAcceleratorsResponseBodyAccelerators(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth: int = None,
        bandwidth_billing_type: str = None,
        basic_bandwidth_package: ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage = None,
        cen_id: str = None,
        create_time: int = None,
        cross_domain_bandwidth_package: ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage = None,
        ddos_id: str = None,
        description: str = None,
        dns_name: str = None,
        expired_time: int = None,
        instance_charge_type: str = None,
        ip_set_config: ListAcceleratorsResponseBodyAcceleratorsIpSetConfig = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        second_dns_name: str = None,
        spec: str = None,
        state: str = None,
        tags: List[ListAcceleratorsResponseBodyAcceleratorsTags] = None,
        type: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.bandwidth = bandwidth
        self.bandwidth_billing_type = bandwidth_billing_type
        self.basic_bandwidth_package = basic_bandwidth_package
        self.cen_id = cen_id
        self.create_time = create_time
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package
        self.ddos_id = ddos_id
        self.description = description
        self.dns_name = dns_name
        self.expired_time = expired_time
        self.instance_charge_type = instance_charge_type
        self.ip_set_config = ip_set_config
        self.name = name
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.second_dns_name = second_dns_name
        self.spec = spec
        self.state = state
        self.tags = tags
        self.type = type

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.ip_set_config:
            self.ip_set_config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        if self.ddos_id is not None:
            result['DdosId'] = self.ddos_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dns_name is not None:
            result['DnsName'] = self.dns_name
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.ip_set_config is not None:
            result['IpSetConfig'] = self.ip_set_config.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.second_dns_name is not None:
            result['SecondDnsName'] = self.second_dns_name
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = ListAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = ListAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        if m.get('DdosId') is not None:
            self.ddos_id = m.get('DdosId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DnsName') is not None:
            self.dns_name = m.get('DnsName')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('IpSetConfig') is not None:
            temp_model = ListAcceleratorsResponseBodyAcceleratorsIpSetConfig()
            self.ip_set_config = temp_model.from_map(m['IpSetConfig'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecondDnsName') is not None:
            self.second_dns_name = m.get('SecondDnsName')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListAcceleratorsResponseBodyAcceleratorsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAcceleratorsResponseBody(TeaModel):
    def __init__(
        self,
        accelerators: List[ListAcceleratorsResponseBodyAccelerators] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.accelerators = accelerators
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.accelerators:
            for k in self.accelerators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accelerators'] = []
        if self.accelerators is not None:
            for k in self.accelerators:
                result['Accelerators'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accelerators = []
        if m.get('Accelerators') is not None:
            for k in m.get('Accelerators'):
                temp_model = ListAcceleratorsResponseBodyAccelerators()
                self.accelerators.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAcceleratorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAcceleratorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAcceleratorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclsRequestTag(TeaModel):
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


class ListAclsRequest(TeaModel):
    def __init__(
        self,
        acl_ids: List[str] = None,
        acl_name: str = None,
        client_token: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[ListAclsRequestTag] = None,
    ):
        self.acl_ids = acl_ids
        self.acl_name = acl_name
        self.client_token = client_token
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.resource_group_id = resource_group_id
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
        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListAclsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListAclsResponseBodyAclsTags(TeaModel):
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


class ListAclsResponseBodyAcls(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_name: str = None,
        acl_status: str = None,
        address_ipversion: str = None,
        resource_group_id: str = None,
        tags: List[ListAclsResponseBodyAclsTags] = None,
    ):
        self.acl_id = acl_id
        self.acl_name = acl_name
        self.acl_status = acl_status
        self.address_ipversion = address_ipversion
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListAclsResponseBodyAclsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListAclsResponseBody(TeaModel):
    def __init__(
        self,
        acls: List[ListAclsResponseBodyAcls] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.acls = acls
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.acls:
            for k in self.acls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Acls'] = []
        if self.acls is not None:
            for k in self.acls:
                result['Acls'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acls = []
        if m.get('Acls') is not None:
            for k in m.get('Acls'):
                temp_model = ListAclsResponseBodyAcls()
                self.acls.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAclsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAclsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAclsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationMonitorRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        search_value: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.search_value = search_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        return self


class ListApplicationMonitorResponseBodyApplicationMonitors(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        address: str = None,
        detect_enable: bool = None,
        detect_threshold: int = None,
        detect_times: int = None,
        listener_id: str = None,
        options_json: str = None,
        silence_time: int = None,
        state: str = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.address = address
        self.detect_enable = detect_enable
        self.detect_threshold = detect_threshold
        self.detect_times = detect_times
        self.listener_id = listener_id
        self.options_json = options_json
        self.silence_time = silence_time
        self.state = state
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.detect_enable is not None:
            result['DetectEnable'] = self.detect_enable
        if self.detect_threshold is not None:
            result['DetectThreshold'] = self.detect_threshold
        if self.detect_times is not None:
            result['DetectTimes'] = self.detect_times
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.options_json is not None:
            result['OptionsJson'] = self.options_json
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.state is not None:
            result['State'] = self.state
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('DetectEnable') is not None:
            self.detect_enable = m.get('DetectEnable')
        if m.get('DetectThreshold') is not None:
            self.detect_threshold = m.get('DetectThreshold')
        if m.get('DetectTimes') is not None:
            self.detect_times = m.get('DetectTimes')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListApplicationMonitorResponseBody(TeaModel):
    def __init__(
        self,
        application_monitors: List[ListApplicationMonitorResponseBodyApplicationMonitors] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.application_monitors = application_monitors
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.application_monitors:
            for k in self.application_monitors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationMonitors'] = []
        if self.application_monitors is not None:
            for k in self.application_monitors:
                result['ApplicationMonitors'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_monitors = []
        if m.get('ApplicationMonitors') is not None:
            for k in m.get('ApplicationMonitors'):
                temp_model = ListApplicationMonitorResponseBodyApplicationMonitors()
                self.application_monitors.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationMonitorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationMonitorDetectResultRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        task_id: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        content: str = None,
        detail: str = None,
        detect_time: str = None,
        diag_status: str = None,
        listener_id: str = None,
        port: str = None,
        protocol: str = None,
        status_code: str = None,
        task_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.content = content
        self.detail = detail
        self.detect_time = detect_time
        self.diag_status = diag_status
        self.listener_id = listener_id
        self.port = port
        self.protocol = protocol
        self.status_code = status_code
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.content is not None:
            result['Content'] = self.content
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.detect_time is not None:
            result['DetectTime'] = self.detect_time
        if self.diag_status is not None:
            result['DiagStatus'] = self.diag_status
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DetectTime') is not None:
            self.detect_time = m.get('DetectTime')
        if m.get('DiagStatus') is not None:
            self.diag_status = m.get('DiagStatus')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListApplicationMonitorDetectResultResponseBody(TeaModel):
    def __init__(
        self,
        application_monitor_detect_result_list: List[ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.application_monitor_detect_result_list = application_monitor_detect_result_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.application_monitor_detect_result_list:
            for k in self.application_monitor_detect_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationMonitorDetectResultList'] = []
        if self.application_monitor_detect_result_list is not None:
            for k in self.application_monitor_detect_result_list:
                result['ApplicationMonitorDetectResultList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_monitor_detect_result_list = []
        if m.get('ApplicationMonitorDetectResultList') is not None:
            for k in m.get('ApplicationMonitorDetectResultList'):
                temp_model = ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList()
                self.application_monitor_detect_result_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationMonitorDetectResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationMonitorDetectResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListApplicationMonitorDetectResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableAccelerateAreasRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAvailableAccelerateAreasResponseBodyAreasRegionList(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAvailableAccelerateAreasResponseBodyAreas(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        local_name: str = None,
        region_list: List[ListAvailableAccelerateAreasResponseBodyAreasRegionList] = None,
    ):
        self.area_id = area_id
        self.local_name = local_name
        self.region_list = region_list

    def validate(self):
        if self.region_list:
            for k in self.region_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        result['RegionList'] = []
        if self.region_list is not None:
            for k in self.region_list:
                result['RegionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        self.region_list = []
        if m.get('RegionList') is not None:
            for k in m.get('RegionList'):
                temp_model = ListAvailableAccelerateAreasResponseBodyAreasRegionList()
                self.region_list.append(temp_model.from_map(k))
        return self


class ListAvailableAccelerateAreasResponseBody(TeaModel):
    def __init__(
        self,
        areas: List[ListAvailableAccelerateAreasResponseBodyAreas] = None,
        request_id: str = None,
    ):
        self.areas = areas
        self.request_id = request_id

    def validate(self):
        if self.areas:
            for k in self.areas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Areas'] = []
        if self.areas is not None:
            for k in self.areas:
                result['Areas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.areas = []
        if m.get('Areas') is not None:
            for k in m.get('Areas'):
                temp_model = ListAvailableAccelerateAreasResponseBodyAreas()
                self.areas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAvailableAccelerateAreasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAvailableAccelerateAreasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAvailableAccelerateAreasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableBusiRegionsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAvailableBusiRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        pop: bool = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.pop = pop
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.pop is not None:
            result['Pop'] = self.pop
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('Pop') is not None:
            self.pop = m.get('Pop')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAvailableBusiRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[ListAvailableBusiRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListAvailableBusiRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAvailableBusiRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAvailableBusiRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAvailableBusiRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBandwidthPackagesRequestTag(TeaModel):
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


class ListBandwidthPackagesRequest(TeaModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tag: List[ListBandwidthPackagesRequestTag] = None,
        type: str = None,
    ):
        self.bandwidth_package_id = bandwidth_package_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.state = state
        self.tag = tag
        self.type = type

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
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListBandwidthPackagesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBandwidthPackagesResponseBodyBandwidthPackagesTags(TeaModel):
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


class ListBandwidthPackagesResponseBodyBandwidthPackages(TeaModel):
    def __init__(
        self,
        accelerators: List[str] = None,
        bandwidth: int = None,
        bandwidth_package_id: str = None,
        bandwidth_type: str = None,
        billing_type: str = None,
        cbn_geographic_region_id_a: str = None,
        cbn_geographic_region_id_b: str = None,
        charge_type: str = None,
        create_time: str = None,
        description: str = None,
        expired_time: str = None,
        name: str = None,
        ratio: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[ListBandwidthPackagesResponseBodyBandwidthPackagesTags] = None,
        type: str = None,
    ):
        self.accelerators = accelerators
        self.bandwidth = bandwidth
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_type = bandwidth_type
        self.billing_type = billing_type
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b
        self.charge_type = charge_type
        self.create_time = create_time
        self.description = description
        self.expired_time = expired_time
        self.name = name
        self.ratio = ratio
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.state = state
        self.tags = tags
        self.type = type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a
        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.name is not None:
            result['Name'] = self.name
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')
        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListBandwidthPackagesResponseBodyBandwidthPackagesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBandwidthPackagesResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_packages: List[ListBandwidthPackagesResponseBodyBandwidthPackages] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.bandwidth_packages = bandwidth_packages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.bandwidth_packages:
            for k in self.bandwidth_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BandwidthPackages'] = []
        if self.bandwidth_packages is not None:
            for k in self.bandwidth_packages:
                result['BandwidthPackages'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bandwidth_packages = []
        if m.get('BandwidthPackages') is not None:
            for k in m.get('BandwidthPackages'):
                temp_model = ListBandwidthPackagesResponseBodyBandwidthPackages()
                self.bandwidth_packages.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBandwidthPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBandwidthPackagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBandwidthPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBandwidthackagesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBandwidthackagesResponseBodyBandwidthPackagesTags(TeaModel):
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


class ListBandwidthackagesResponseBodyBandwidthPackages(TeaModel):
    def __init__(
        self,
        accelerators: List[str] = None,
        bandwidth: int = None,
        bandwidth_package_id: str = None,
        charge_type: str = None,
        create_time: str = None,
        description: str = None,
        expired_time: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[ListBandwidthackagesResponseBodyBandwidthPackagesTags] = None,
    ):
        self.accelerators = accelerators
        self.bandwidth = bandwidth
        self.bandwidth_package_id = bandwidth_package_id
        self.charge_type = charge_type
        self.create_time = create_time
        self.description = description
        self.expired_time = expired_time
        self.name = name
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.state = state
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerators is not None:
            result['Accelerators'] = self.accelerators
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerators') is not None:
            self.accelerators = m.get('Accelerators')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListBandwidthackagesResponseBodyBandwidthPackagesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListBandwidthackagesResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_packages: List[ListBandwidthackagesResponseBodyBandwidthPackages] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.bandwidth_packages = bandwidth_packages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.bandwidth_packages:
            for k in self.bandwidth_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BandwidthPackages'] = []
        if self.bandwidth_packages is not None:
            for k in self.bandwidth_packages:
                result['BandwidthPackages'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bandwidth_packages = []
        if m.get('BandwidthPackages') is not None:
            for k in m.get('BandwidthPackages'):
                temp_model = ListBandwidthackagesResponseBodyBandwidthPackages()
                self.bandwidth_packages.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBandwidthackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBandwidthackagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBandwidthackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBasicAcceleratorsRequestTag(TeaModel):
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


class ListBasicAcceleratorsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tag: List[ListBasicAcceleratorsRequestTag] = None,
    ):
        self.accelerator_id = accelerator_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.state = state
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
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListBasicAcceleratorsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListBasicAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        bandwidth_type: str = None,
        instance_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.bandwidth_type = bandwidth_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListBasicAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        instance_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListBasicAcceleratorsResponseBodyAcceleratorsTags(TeaModel):
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


class ListBasicAcceleratorsResponseBodyAccelerators(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth_billing_type: str = None,
        basic_bandwidth_package: ListBasicAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage = None,
        basic_endpoint_group_id: str = None,
        basic_ip_set_id: str = None,
        create_time: int = None,
        cross_domain_bandwidth_package: ListBasicAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage = None,
        description: str = None,
        expired_time: int = None,
        instance_charge_type: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[ListBasicAcceleratorsResponseBodyAcceleratorsTags] = None,
        type: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.bandwidth_billing_type = bandwidth_billing_type
        self.basic_bandwidth_package = basic_bandwidth_package
        self.basic_endpoint_group_id = basic_endpoint_group_id
        self.basic_ip_set_id = basic_ip_set_id
        self.create_time = create_time
        self.cross_domain_bandwidth_package = cross_domain_bandwidth_package
        self.description = description
        self.expired_time = expired_time
        self.instance_charge_type = instance_charge_type
        self.name = name
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.state = state
        self.tags = tags
        self.type = type

    def validate(self):
        if self.basic_bandwidth_package:
            self.basic_bandwidth_package.validate()
        if self.cross_domain_bandwidth_package:
            self.cross_domain_bandwidth_package.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type
        if self.basic_bandwidth_package is not None:
            result['BasicBandwidthPackage'] = self.basic_bandwidth_package.to_map()
        if self.basic_endpoint_group_id is not None:
            result['BasicEndpointGroupId'] = self.basic_endpoint_group_id
        if self.basic_ip_set_id is not None:
            result['BasicIpSetId'] = self.basic_ip_set_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_domain_bandwidth_package is not None:
            result['CrossDomainBandwidthPackage'] = self.cross_domain_bandwidth_package.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')
        if m.get('BasicBandwidthPackage') is not None:
            temp_model = ListBasicAcceleratorsResponseBodyAcceleratorsBasicBandwidthPackage()
            self.basic_bandwidth_package = temp_model.from_map(m['BasicBandwidthPackage'])
        if m.get('BasicEndpointGroupId') is not None:
            self.basic_endpoint_group_id = m.get('BasicEndpointGroupId')
        if m.get('BasicIpSetId') is not None:
            self.basic_ip_set_id = m.get('BasicIpSetId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossDomainBandwidthPackage') is not None:
            temp_model = ListBasicAcceleratorsResponseBodyAcceleratorsCrossDomainBandwidthPackage()
            self.cross_domain_bandwidth_package = temp_model.from_map(m['CrossDomainBandwidthPackage'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListBasicAcceleratorsResponseBodyAcceleratorsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBasicAcceleratorsResponseBody(TeaModel):
    def __init__(
        self,
        accelerators: List[ListBasicAcceleratorsResponseBodyAccelerators] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.accelerators = accelerators
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.accelerators:
            for k in self.accelerators:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Accelerators'] = []
        if self.accelerators is not None:
            for k in self.accelerators:
                result['Accelerators'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accelerators = []
        if m.get('Accelerators') is not None:
            for k in m.get('Accelerators'):
                temp_model = ListBasicAcceleratorsResponseBodyAccelerators()
                self.accelerators.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBasicAcceleratorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBasicAcceleratorsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBasicAcceleratorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBusiRegionsRequest(TeaModel):
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


class ListBusiRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListBusiRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[ListBusiRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListBusiRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBusiRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBusiRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBusiRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        endpoint_group_id: str = None,
        from_port: int = None,
        listener_id: str = None,
        page_number: str = None,
        page_size: str = None,
        protocols: List[str] = None,
        region_id: str = None,
        to_port: int = None,
    ):
        self.accelerator_id = accelerator_id
        self.endpoint_group_id = endpoint_group_id
        self.from_port = from_port
        self.listener_id = listener_id
        self.page_number = page_number
        self.page_size = page_size
        self.protocols = protocols
        self.region_id = region_id
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        destination_id: str = None,
        endpoint_group_id: str = None,
        from_port: int = None,
        listener_id: str = None,
        protocols: List[str] = None,
        to_port: int = None,
    ):
        self.accelerator_id = accelerator_id
        self.destination_id = destination_id
        self.endpoint_group_id = endpoint_group_id
        self.from_port = from_port
        self.listener_id = listener_id
        self.protocols = protocols
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
    def __init__(
        self,
        destinations: List[ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.destinations = destinations
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.destinations:
            for k in self.destinations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Destinations'] = []
        if self.destinations is not None:
            for k in self.destinations:
                result['Destinations'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.destinations = []
        if m.get('Destinations') is not None:
            for k in m.get('Destinations'):
                temp_model = ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations()
                self.destinations.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomRoutingEndpointGroupDestinationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingEndpointGroupsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        endpoint_group_id: str = None,
        listener_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.endpoint_group_id = endpoint_group_id
        self.listener_id = listener_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        description: str = None,
        endpoint_group_id: str = None,
        endpoint_group_ip_list: List[str] = None,
        endpoint_group_region: str = None,
        endpoint_group_unconfirmed_ip_list: List[str] = None,
        listener_id: str = None,
        name: str = None,
        state: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.description = description
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_ip_list = endpoint_group_ip_list
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list
        self.listener_id = listener_id
        self.name = name
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListCustomRoutingEndpointGroupsResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_groups: List[ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.endpoint_groups = endpoint_groups
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.endpoint_groups:
            for k in self.endpoint_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k in self.endpoint_groups:
                result['EndpointGroups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k in m.get('EndpointGroups'):
                temp_model = ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingEndpointGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomRoutingEndpointGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomRoutingEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingEndpointTrafficPoliciesRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        address: str = None,
        endpoint_group_id: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.address = address
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_id = endpoint_id
        self.listener_id = listener_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        address: str = None,
        endpoint_group_id: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        policy_id: str = None,
        port_ranges: List[ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges] = None,
    ):
        self.accelerator_id = accelerator_id
        self.address = address
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_id = endpoint_id
        self.listener_id = listener_id
        self.policy_id = policy_id
        self.port_ranges = port_ranges

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.address is not None:
            result['Address'] = self.address
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class ListCustomRoutingEndpointTrafficPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policies: List[ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.policies = policies
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingEndpointTrafficPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomRoutingEndpointTrafficPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomRoutingEndpointTrafficPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingEndpointsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        endpoint_group_id: str = None,
        listener_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.endpoint_group_id = endpoint_group_id
        self.listener_id = listener_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingEndpointsResponseBodyEndpoints(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        endpoint: str = None,
        endpoint_group_id: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.endpoint = endpoint
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_id = endpoint_id
        self.listener_id = listener_id
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCustomRoutingEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        endpoints: List[ListCustomRoutingEndpointsResponseBodyEndpoints] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.endpoints = endpoints
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListCustomRoutingEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomRoutingEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomRoutingEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingPortMappingsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        endpoint_group_id: str = None,
        listener_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.endpoint_group_id = endpoint_group_id
        self.listener_id = listener_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingPortMappingsResponseBodyPortMappingsDestinationSocketAddress(TeaModel):
    def __init__(
        self,
        ip_address: str = None,
        port: int = None,
    ):
        self.ip_address = ip_address
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ListCustomRoutingPortMappingsResponseBodyPortMappings(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        accelerator_port: int = None,
        destination_socket_address: ListCustomRoutingPortMappingsResponseBodyPortMappingsDestinationSocketAddress = None,
        destination_traffic_state: str = None,
        endpoint_group_id: str = None,
        endpoint_group_region: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        protocols: List[str] = None,
        vswitch: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.accelerator_port = accelerator_port
        self.destination_socket_address = destination_socket_address
        self.destination_traffic_state = destination_traffic_state
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_id = endpoint_id
        self.listener_id = listener_id
        self.protocols = protocols
        self.vswitch = vswitch

    def validate(self):
        if self.destination_socket_address:
            self.destination_socket_address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.accelerator_port is not None:
            result['AcceleratorPort'] = self.accelerator_port
        if self.destination_socket_address is not None:
            result['DestinationSocketAddress'] = self.destination_socket_address.to_map()
        if self.destination_traffic_state is not None:
            result['DestinationTrafficState'] = self.destination_traffic_state
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AcceleratorPort') is not None:
            self.accelerator_port = m.get('AcceleratorPort')
        if m.get('DestinationSocketAddress') is not None:
            temp_model = ListCustomRoutingPortMappingsResponseBodyPortMappingsDestinationSocketAddress()
            self.destination_socket_address = temp_model.from_map(m['DestinationSocketAddress'])
        if m.get('DestinationTrafficState') is not None:
            self.destination_traffic_state = m.get('DestinationTrafficState')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class ListCustomRoutingPortMappingsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        port_mappings: List[ListCustomRoutingPortMappingsResponseBodyPortMappings] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.port_mappings = port_mappings
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.port_mappings:
            for k in self.port_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k in self.port_mappings:
                result['PortMappings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k in m.get('PortMappings'):
                temp_model = ListCustomRoutingPortMappingsResponseBodyPortMappings()
                self.port_mappings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingPortMappingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomRoutingPortMappingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomRoutingPortMappingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomRoutingPortMappingsByDestinationRequest(TeaModel):
    def __init__(
        self,
        destination_address: str = None,
        endpoint_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.destination_address = destination_address
        self.endpoint_id = endpoint_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_address is not None:
            result['DestinationAddress'] = self.destination_address
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationAddress') is not None:
            self.destination_address = m.get('DestinationAddress')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress(TeaModel):
    def __init__(
        self,
        ip_address: str = None,
        port: int = None,
    ):
        self.ip_address = ip_address
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        accelerator_port: int = None,
        destination_socket_address: ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress = None,
        destination_traffic_state: str = None,
        endpoint_group_id: str = None,
        endpoint_group_region: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        protocols: List[str] = None,
        vswitch: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.accelerator_port = accelerator_port
        self.destination_socket_address = destination_socket_address
        self.destination_traffic_state = destination_traffic_state
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_id = endpoint_id
        self.listener_id = listener_id
        self.protocols = protocols
        self.vswitch = vswitch

    def validate(self):
        if self.destination_socket_address:
            self.destination_socket_address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.accelerator_port is not None:
            result['AcceleratorPort'] = self.accelerator_port
        if self.destination_socket_address is not None:
            result['DestinationSocketAddress'] = self.destination_socket_address.to_map()
        if self.destination_traffic_state is not None:
            result['DestinationTrafficState'] = self.destination_traffic_state
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AcceleratorPort') is not None:
            self.accelerator_port = m.get('AcceleratorPort')
        if m.get('DestinationSocketAddress') is not None:
            temp_model = ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress()
            self.destination_socket_address = temp_model.from_map(m['DestinationSocketAddress'])
        if m.get('DestinationTrafficState') is not None:
            self.destination_traffic_state = m.get('DestinationTrafficState')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')
        return self


class ListCustomRoutingPortMappingsByDestinationResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        port_mappings: List[ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.port_mappings = port_mappings
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.port_mappings:
            for k in self.port_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k in self.port_mappings:
                result['PortMappings'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k in m.get('PortMappings'):
                temp_model = ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings()
                self.port_mappings.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomRoutingPortMappingsByDestinationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomRoutingPortMappingsByDestinationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCustomRoutingPortMappingsByDestinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEndpointGroupsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_log_switch: str = None,
        endpoint_group_id: str = None,
        endpoint_group_type: str = None,
        listener_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.access_log_switch = access_log_switch
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_type = endpoint_group_type
        self.listener_id = listener_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations(TeaModel):
    def __init__(
        self,
        enable_client_ippreservation: bool = None,
        endpoint: str = None,
        endpoint_id: str = None,
        probe_port: int = None,
        probe_protocol: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.enable_client_ippreservation = enable_client_ippreservation
        self.endpoint = endpoint
        self.endpoint_id = endpoint_id
        self.probe_port = probe_port
        self.probe_protocol = probe_protocol
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port
        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')
        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides(TeaModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        self.endpoint_port = endpoint_port
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class ListEndpointGroupsResponseBodyEndpointGroups(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        description: str = None,
        endpoint_configurations: List[ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        endpoint_group_ip_list: List[str] = None,
        endpoint_group_region: str = None,
        endpoint_group_type: str = None,
        endpoint_group_unconfirmed_ip_list: List[str] = None,
        endpoint_request_protocol: str = None,
        forwarding_rule_ids: List[str] = None,
        health_check_enabled: bool = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        listener_id: str = None,
        name: str = None,
        port_overrides: List[ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides] = None,
        state: str = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        self.accelerator_id = accelerator_id
        self.description = description
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_ip_list = endpoint_group_ip_list
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_group_type = endpoint_group_type
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list
        self.endpoint_request_protocol = endpoint_request_protocol
        self.forwarding_rule_ids = forwarding_rule_ids
        self.health_check_enabled = health_check_enabled
        self.health_check_interval_seconds = health_check_interval_seconds
        self.health_check_path = health_check_path
        self.health_check_port = health_check_port
        self.health_check_protocol = health_check_protocol
        self.listener_id = listener_id
        self.name = name
        self.port_overrides = port_overrides
        self.state = state
        self.threshold_count = threshold_count
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.description is not None:
            result['Description'] = self.description
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type
        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.state is not None:
            result['State'] = self.state
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')
        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class ListEndpointGroupsResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_groups: List[ListEndpointGroupsResponseBodyEndpointGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.endpoint_groups = endpoint_groups
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.endpoint_groups:
            for k in self.endpoint_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k in self.endpoint_groups:
                result['EndpointGroups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k in m.get('EndpointGroups'):
                temp_model = ListEndpointGroupsResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEndpointGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEndpointGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListForwardingRulesRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        forwarding_rule_id: str = None,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.forwarding_rule_id = forwarding_rule_id
        self.listener_id = listener_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
    ):
        self.endpoint_group_id = endpoint_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleActions(TeaModel):
    def __init__(
        self,
        forward_group_config: ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig = None,
        order: int = None,
        rule_action_type: str = None,
        rule_action_value: str = None,
    ):
        self.forward_group_config = forward_group_config
        self.order = order
        self.rule_action_type = rule_action_type
        self.rule_action_value = rule_action_value

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_action_value is not None:
            result['RuleActionValue'] = self.rule_action_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListForwardingRulesResponseBodyForwardingRulesRuleConditions(TeaModel):
    def __init__(
        self,
        host_config: ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig = None,
        path_config: ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig = None,
        rule_condition_type: str = None,
        rule_condition_value: str = None,
    ):
        self.host_config = host_config
        self.path_config = path_config
        self.rule_condition_type = rule_condition_type
        self.rule_condition_value = rule_condition_value

    def validate(self):
        if self.host_config:
            self.host_config.validate()
        if self.path_config:
            self.path_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type
        if self.rule_condition_value is not None:
            result['RuleConditionValue'] = self.rule_condition_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostConfig') is not None:
            temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('PathConfig') is not None:
            temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')
        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')
        return self


class ListForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(
        self,
        forwarding_rule_direction: str = None,
        forwarding_rule_id: str = None,
        forwarding_rule_name: str = None,
        forwarding_rule_status: str = None,
        listener_id: str = None,
        priority: int = None,
        rule_actions: List[ListForwardingRulesResponseBodyForwardingRulesRuleActions] = None,
        rule_conditions: List[ListForwardingRulesResponseBodyForwardingRulesRuleConditions] = None,
    ):
        self.forwarding_rule_direction = forwarding_rule_direction
        self.forwarding_rule_id = forwarding_rule_id
        self.forwarding_rule_name = forwarding_rule_name
        self.forwarding_rule_status = forwarding_rule_status
        self.listener_id = listener_id
        self.priority = priority
        self.rule_actions = rule_actions
        self.rule_conditions = rule_conditions

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_direction is not None:
            result['ForwardingRuleDirection'] = self.forwarding_rule_direction
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name
        if self.forwarding_rule_status is not None:
            result['ForwardingRuleStatus'] = self.forwarding_rule_status
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleDirection') is not None:
            self.forwarding_rule_direction = m.get('ForwardingRuleDirection')
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')
        if m.get('ForwardingRuleStatus') is not None:
            self.forwarding_rule_status = m.get('ForwardingRuleStatus')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = ListForwardingRulesResponseBodyForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        return self


class ListForwardingRulesResponseBody(TeaModel):
    def __init__(
        self,
        forwarding_rules: List[ListForwardingRulesResponseBodyForwardingRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.forwarding_rules = forwarding_rules
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = ListForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListForwardingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListForwardingRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIpSetsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIpSetsResponseBodyIpSets(TeaModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        bandwidth: int = None,
        ip_address_list: List[str] = None,
        ip_set_id: str = None,
        ip_version: str = None,
        isp_type: str = None,
        state: str = None,
    ):
        self.accelerate_region_id = accelerate_region_id
        self.bandwidth = bandwidth
        self.ip_address_list = ip_address_list
        self.ip_set_id = ip_set_id
        self.ip_version = ip_version
        self.isp_type = isp_type
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_address_list is not None:
            result['IpAddressList'] = self.ip_address_list
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.isp_type is not None:
            result['IspType'] = self.isp_type
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpAddressList') is not None:
            self.ip_address_list = m.get('IpAddressList')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListIpSetsResponseBody(TeaModel):
    def __init__(
        self,
        ip_sets: List[ListIpSetsResponseBodyIpSets] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.ip_sets = ip_sets
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ip_sets:
            for k in self.ip_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k in self.ip_sets:
                result['IpSets'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k in m.get('IpSets'):
                temp_model = ListIpSetsResponseBodyIpSets()
                self.ip_sets.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIpSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIpSetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenerCertificatesRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.listener_id = listener_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListListenerCertificatesResponseBodyCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        domain: str = None,
        is_default: bool = None,
        state: str = None,
    ):
        self.certificate_id = certificate_id
        self.domain = domain
        self.is_default = is_default
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListListenerCertificatesResponseBody(TeaModel):
    def __init__(
        self,
        certificates: List[ListListenerCertificatesResponseBodyCertificates] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.certificates = certificates
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = ListListenerCertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenerCertificatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListListenerCertificatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListListenerCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListListenersResponseBodyListenersBackendPorts(TeaModel):
    def __init__(
        self,
        from_port: str = None,
        to_port: str = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListListenersResponseBodyListenersCertificates(TeaModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        self.id = id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListListenersResponseBodyListenersPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class ListListenersResponseBodyListenersXForwardedForConfig(TeaModel):
    def __init__(
        self,
        xforwarded_for_ga_ap_enabled: bool = None,
        xforwarded_for_ga_id_enabled: bool = None,
        xforwarded_for_port_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xreal_ip_enabled: bool = None,
    ):
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        self.xreal_ip_enabled = xreal_ip_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_ga_ap_enabled is not None:
            result['XForwardedForGaApEnabled'] = self.xforwarded_for_ga_ap_enabled
        if self.xforwarded_for_ga_id_enabled is not None:
            result['XForwardedForGaIdEnabled'] = self.xforwarded_for_ga_id_enabled
        if self.xforwarded_for_port_enabled is not None:
            result['XForwardedForPortEnabled'] = self.xforwarded_for_port_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xreal_ip_enabled is not None:
            result['XRealIpEnabled'] = self.xreal_ip_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForGaApEnabled') is not None:
            self.xforwarded_for_ga_ap_enabled = m.get('XForwardedForGaApEnabled')
        if m.get('XForwardedForGaIdEnabled') is not None:
            self.xforwarded_for_ga_id_enabled = m.get('XForwardedForGaIdEnabled')
        if m.get('XForwardedForPortEnabled') is not None:
            self.xforwarded_for_port_enabled = m.get('XForwardedForPortEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XRealIpEnabled') is not None:
            self.xreal_ip_enabled = m.get('XRealIpEnabled')
        return self


class ListListenersResponseBodyListeners(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        backend_ports: List[ListListenersResponseBodyListenersBackendPorts] = None,
        certificates: List[ListListenersResponseBodyListenersCertificates] = None,
        client_affinity: str = None,
        create_time: int = None,
        description: str = None,
        listener_id: str = None,
        name: str = None,
        port_ranges: List[ListListenersResponseBodyListenersPortRanges] = None,
        protocol: str = None,
        proxy_protocol: bool = None,
        security_policy_id: str = None,
        state: str = None,
        type: str = None,
        xforwarded_for_config: ListListenersResponseBodyListenersXForwardedForConfig = None,
    ):
        self.accelerator_id = accelerator_id
        self.backend_ports = backend_ports
        self.certificates = certificates
        self.client_affinity = client_affinity
        self.create_time = create_time
        self.description = description
        self.listener_id = listener_id
        self.name = name
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.proxy_protocol = proxy_protocol
        self.security_policy_id = security_policy_id
        self.state = state
        self.type = type
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.backend_ports:
            for k in self.backend_ports:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k in self.backend_ports:
                result['BackendPorts'].append(k.to_map() if k else None)
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.state is not None:
            result['State'] = self.state
        if self.type is not None:
            result['Type'] = self.type
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k in m.get('BackendPorts'):
                temp_model = ListListenersResponseBodyListenersBackendPorts()
                self.backend_ports.append(temp_model.from_map(k))
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = ListListenersResponseBodyListenersCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = ListListenersResponseBodyListenersPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('XForwardedForConfig') is not None:
            temp_model = ListListenersResponseBodyListenersXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class ListListenersResponseBody(TeaModel):
    def __init__(
        self,
        listeners: List[ListListenersResponseBodyListeners] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.listeners = listeners
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListListenersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListListenersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpareIpsRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListSpareIpsResponseBodySpareIps(TeaModel):
    def __init__(
        self,
        spare_ip: str = None,
        state: str = None,
    ):
        self.spare_ip = spare_ip
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spare_ip is not None:
            result['SpareIp'] = self.spare_ip
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpareIp') is not None:
            self.spare_ip = m.get('SpareIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListSpareIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        spare_ips: List[ListSpareIpsResponseBodySpareIps] = None,
    ):
        self.request_id = request_id
        self.spare_ips = spare_ips

    def validate(self):
        if self.spare_ips:
            for k in self.spare_ips:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SpareIps'] = []
        if self.spare_ips is not None:
            for k in self.spare_ips:
                result['SpareIps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spare_ips = []
        if m.get('SpareIps') is not None:
            for k in m.get('SpareIps'):
                temp_model = ListSpareIpsResponseBodySpareIps()
                self.spare_ips.append(temp_model.from_map(k))
        return self


class ListSpareIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSpareIpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSpareIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemSecurityPoliciesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListSystemSecurityPoliciesResponseBodySecurityPolicies(TeaModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        security_policy_id: str = None,
        tls_versions: List[str] = None,
    ):
        self.ciphers = ciphers
        self.security_policy_id = security_policy_id
        self.tls_versions = tls_versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.tls_versions is not None:
            result['TlsVersions'] = self.tls_versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('TlsVersions') is not None:
            self.tls_versions = m.get('TlsVersions')
        return self


class ListSystemSecurityPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        security_policies: List[ListSystemSecurityPoliciesResponseBodySecurityPolicies] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.security_policies = security_policies
        self.total_count = total_count

    def validate(self):
        if self.security_policies:
            for k in self.security_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k in self.security_policies:
                result['SecurityPolicies'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k in m.get('SecurityPolicies'):
                temp_model = ListSystemSecurityPoliciesResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSystemSecurityPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSystemSecurityPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSystemSecurityPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveEntriesFromAclRequestAclEntries(TeaModel):
    def __init__(
        self,
        entry: str = None,
    ):
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class RemoveEntriesFromAclRequest(TeaModel):
    def __init__(
        self,
        acl_entries: List[RemoveEntriesFromAclRequestAclEntries] = None,
        acl_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.acl_entries = acl_entries
        self.acl_id = acl_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = RemoveEntriesFromAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveEntriesFromAclResponseBody(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        request_id: str = None,
    ):
        self.acl_id = acl_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveEntriesFromAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveEntriesFromAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveEntriesFromAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceBandwidthPackageRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        bandwidth_package_id: str = None,
        region_id: str = None,
        target_bandwidth_package_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.bandwidth_package_id = bandwidth_package_id
        self.region_id = region_id
        self.target_bandwidth_package_id = target_bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.target_bandwidth_package_id is not None:
            result['TargetBandwidthPackageId'] = self.target_bandwidth_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TargetBandwidthPackageId') is not None:
            self.target_bandwidth_package_id = m.get('TargetBandwidthPackageId')
        return self


class ReplaceBandwidthPackageResponseBody(TeaModel):
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


class ReplaceBandwidthPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReplaceBandwidthPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReplaceBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        spec: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.auto_pay = auto_pay
        self.auto_use_coupon = auto_use_coupon
        self.client_token = client_token
        self.description = description
        self.name = name
        self.region_id = region_id
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class UpdateAcceleratorResponseBody(TeaModel):
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


class UpdateAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAcceleratorAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        client_token: str = None,
        name: str = None,
        region_id: str = None,
        renewal_status: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.client_token = client_token
        self.name = name
        self.region_id = region_id
        self.renewal_status = renewal_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class UpdateAcceleratorAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        request_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAcceleratorAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAcceleratorAutoRenewAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAcceleratorAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAcceleratorConfirmRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAcceleratorConfirmResponseBody(TeaModel):
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


class UpdateAcceleratorConfirmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAcceleratorConfirmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAcceleratorConfirmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAclAttributeRequest(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_name: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.acl_id = acl_id
        self.acl_name = acl_name
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.acl_name is not None:
            result['AclName'] = self.acl_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAclAttributeResponseBody(TeaModel):
    def __init__(
        self,
        acl_id: str = None,
        request_id: str = None,
    ):
        self.acl_id = acl_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_id is not None:
            result['AclId'] = self.acl_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAclAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAclAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAclAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationMonitorRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        client_token: str = None,
        detect_enable: bool = None,
        detect_threshold: int = None,
        detect_times: int = None,
        listener_id: str = None,
        options_json: str = None,
        region_id: str = None,
        silence_time: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.address = address
        self.client_token = client_token
        self.detect_enable = detect_enable
        self.detect_threshold = detect_threshold
        self.detect_times = detect_times
        self.listener_id = listener_id
        self.options_json = options_json
        self.region_id = region_id
        self.silence_time = silence_time
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.detect_enable is not None:
            result['DetectEnable'] = self.detect_enable
        if self.detect_threshold is not None:
            result['DetectThreshold'] = self.detect_threshold
        if self.detect_times is not None:
            result['DetectTimes'] = self.detect_times
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.options_json is not None:
            result['OptionsJson'] = self.options_json
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DetectEnable') is not None:
            self.detect_enable = m.get('DetectEnable')
        if m.get('DetectThreshold') is not None:
            self.detect_threshold = m.get('DetectThreshold')
        if m.get('DetectTimes') is not None:
            self.detect_times = m.get('DetectTimes')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('OptionsJson') is not None:
            self.options_json = m.get('OptionsJson')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UpdateApplicationMonitorResponseBody(TeaModel):
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


class UpdateApplicationMonitorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApplicationMonitorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateApplicationMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBandwidthPackagaAutoRenewAttributeRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        client_token: str = None,
        instance_id: str = None,
        name: str = None,
        region_id: str = None,
        renewal_status: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration
        self.client_token = client_token
        self.instance_id = instance_id
        self.name = name
        self.region_id = region_id
        self.renewal_status = renewal_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class UpdateBandwidthPackagaAutoRenewAttributeResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBandwidthPackagaAutoRenewAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBandwidthPackagaAutoRenewAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBandwidthPackagaAutoRenewAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBandwidthPackageRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        bandwidth: int = None,
        bandwidth_package_id: str = None,
        bandwidth_type: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.auto_use_coupon = auto_use_coupon
        self.bandwidth = bandwidth
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_type = bandwidth_type
        self.description = description
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateBandwidthPackageResponseBody(TeaModel):
    def __init__(
        self,
        bandwidth_package: str = None,
        description: str = None,
        name: str = None,
        request_id: str = None,
    ):
        self.bandwidth_package = bandwidth_package
        self.description = description
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package is not None:
            result['BandwidthPackage'] = self.bandwidth_package
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackage') is not None:
            self.bandwidth_package = m.get('BandwidthPackage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBandwidthPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBandwidthPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBasicAcceleratorRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.description = description
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateBasicAcceleratorResponseBody(TeaModel):
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


class UpdateBasicAcceleratorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBasicAcceleratorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBasicAcceleratorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBasicEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        endpoint_address: str = None,
        endpoint_group_id: str = None,
        endpoint_sub_address: str = None,
        endpoint_type: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.endpoint_address = endpoint_address
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_sub_address = endpoint_sub_address
        self.endpoint_type = endpoint_type
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_address is not None:
            result['EndpointAddress'] = self.endpoint_address
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_sub_address is not None:
            result['EndpointSubAddress'] = self.endpoint_sub_address
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointAddress') is not None:
            self.endpoint_address = m.get('EndpointAddress')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointSubAddress') is not None:
            self.endpoint_sub_address = m.get('EndpointSubAddress')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateBasicEndpointGroupResponseBody(TeaModel):
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


class UpdateBasicEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBasicEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBasicEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBasicIpSetRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        ip_set_id: str = None,
        region_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.client_token = client_token
        self.ip_set_id = ip_set_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateBasicIpSetResponseBody(TeaModel):
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


class UpdateBasicIpSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBasicIpSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBasicIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomRoutingEndpointGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        endpoint_group_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.endpoint_group_id = endpoint_group_id
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCustomRoutingEndpointGroupAttributeResponseBody(TeaModel):
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


class UpdateCustomRoutingEndpointGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomRoutingEndpointGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCustomRoutingEndpointGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations(TeaModel):
    def __init__(
        self,
        destination_id: str = None,
        from_port: int = None,
        protocols: List[str] = None,
        to_port: int = None,
    ):
        self.destination_id = destination_id
        self.from_port = from_port
        self.protocols = protocols
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.protocols is not None:
            result['Protocols'] = self.protocols
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateCustomRoutingEndpointGroupDestinationsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        destination_configurations: List[UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations] = None,
        dry_run: bool = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.destination_configurations = destination_configurations
        self.dry_run = dry_run
        self.endpoint_group_id = endpoint_group_id
        self.region_id = region_id

    def validate(self):
        if self.destination_configurations:
            for k in self.destination_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['DestinationConfigurations'] = []
        if self.destination_configurations is not None:
            for k in self.destination_configurations:
                result['DestinationConfigurations'].append(k.to_map() if k else None)
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.destination_configurations = []
        if m.get('DestinationConfigurations') is not None:
            for k in m.get('DestinationConfigurations'):
                temp_model = UpdateCustomRoutingEndpointGroupDestinationsRequestDestinationConfigurations()
                self.destination_configurations.append(temp_model.from_map(k))
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCustomRoutingEndpointGroupDestinationsResponseBody(TeaModel):
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


class UpdateCustomRoutingEndpointGroupDestinationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomRoutingEndpointGroupDestinationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCustomRoutingEndpointGroupDestinationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations(TeaModel):
    def __init__(
        self,
        address: str = None,
        policy_id: str = None,
        port_ranges: List[UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges] = None,
    ):
        self.address = address
        self.policy_id = policy_id
        self.port_ranges = port_ranges

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_id: str = None,
        policy_configurations: List[UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations] = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.endpoint_id = endpoint_id
        self.policy_configurations = policy_configurations
        self.region_id = region_id

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = UpdateCustomRoutingEndpointTrafficPoliciesRequestPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        request_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCustomRoutingEndpointTrafficPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomRoutingEndpointTrafficPoliciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCustomRoutingEndpointTrafficPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges(TeaModel):
    def __init__(
        self,
        from_port: str = None,
        to_port: str = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations(TeaModel):
    def __init__(
        self,
        address: str = None,
        port_ranges: List[UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges] = None,
    ):
        self.address = address
        self.port_ranges = port_ranges

    def validate(self):
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurationsPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        return self


class UpdateCustomRoutingEndpointsRequestEndpointConfigurations(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        policy_configurations: List[UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations] = None,
        traffic_to_endpoint_policy: str = None,
    ):
        self.endpoint_id = endpoint_id
        self.policy_configurations = policy_configurations
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy

    def validate(self):
        if self.policy_configurations:
            for k in self.policy_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['PolicyConfigurations'] = []
        if self.policy_configurations is not None:
            for k in self.policy_configurations:
                result['PolicyConfigurations'].append(k.to_map() if k else None)
        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.policy_configurations = []
        if m.get('PolicyConfigurations') is not None:
            for k in m.get('PolicyConfigurations'):
                temp_model = UpdateCustomRoutingEndpointsRequestEndpointConfigurationsPolicyConfigurations()
                self.policy_configurations.append(temp_model.from_map(k))
        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')
        return self


class UpdateCustomRoutingEndpointsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        endpoint_configurations: List[UpdateCustomRoutingEndpointsRequestEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_id = endpoint_group_id
        self.region_id = region_id

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = UpdateCustomRoutingEndpointsRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateCustomRoutingEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_ids: List[str] = None,
        request_id: str = None,
    ):
        self.endpoint_ids = endpoint_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCustomRoutingEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomRoutingEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateCustomRoutingEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointGroupRequestEndpointConfigurations(TeaModel):
    def __init__(
        self,
        enable_client_ippreservation: bool = None,
        endpoint: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.enable_client_ippreservation = enable_client_ippreservation
        self.endpoint = endpoint
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateEndpointGroupRequestPortOverrides(TeaModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        self.endpoint_port = endpoint_port
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class UpdateEndpointGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        endpoint_configurations: List[UpdateEndpointGroupRequestEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        endpoint_group_region: str = None,
        endpoint_request_protocol: str = None,
        health_check_enabled: bool = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        name: str = None,
        port_overrides: List[UpdateEndpointGroupRequestPortOverrides] = None,
        region_id: str = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        self.client_token = client_token
        self.description = description
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_region = endpoint_group_region
        self.endpoint_request_protocol = endpoint_request_protocol
        self.health_check_enabled = health_check_enabled
        self.health_check_interval_seconds = health_check_interval_seconds
        self.health_check_path = health_check_path
        self.health_check_port = health_check_port
        self.health_check_protocol = health_check_protocol
        self.name = name
        self.port_overrides = port_overrides
        self.region_id = region_id
        self.threshold_count = threshold_count
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        if self.name is not None:
            result['Name'] = self.name
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = UpdateEndpointGroupRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = UpdateEndpointGroupRequestPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class UpdateEndpointGroupResponseBody(TeaModel):
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


class UpdateEndpointGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEndpointGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEndpointGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        endpoint_group_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.endpoint_group_id = endpoint_group_id
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateEndpointGroupAttributeResponseBody(TeaModel):
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


class UpdateEndpointGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEndpointGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEndpointGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        type: str = None,
        weight: int = None,
    ):
        self.endpoint = endpoint
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.type is not None:
            result['Type'] = self.type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides(TeaModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        self.endpoint_port = endpoint_port
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        return self


class UpdateEndpointGroupsRequestEndpointGroupConfigurations(TeaModel):
    def __init__(
        self,
        enable_client_ippreservation_proxy_protocol: bool = None,
        enable_client_ippreservation_toa: bool = None,
        endpoint_configurations: List[UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations] = None,
        endpoint_group_description: str = None,
        endpoint_group_id: str = None,
        endpoint_group_name: str = None,
        endpoint_request_protocol: str = None,
        health_check_enabled: bool = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        port_overrides: List[UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides] = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        self.enable_client_ippreservation_proxy_protocol = enable_client_ippreservation_proxy_protocol
        self.enable_client_ippreservation_toa = enable_client_ippreservation_toa
        self.endpoint_configurations = endpoint_configurations
        self.endpoint_group_description = endpoint_group_description
        self.endpoint_group_id = endpoint_group_id
        self.endpoint_group_name = endpoint_group_name
        self.endpoint_request_protocol = endpoint_request_protocol
        self.health_check_enabled = health_check_enabled
        self.health_check_interval_seconds = health_check_interval_seconds
        self.health_check_path = health_check_path
        self.health_check_port = health_check_port
        self.health_check_protocol = health_check_protocol
        self.port_overrides = port_overrides
        self.threshold_count = threshold_count
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for k in self.endpoint_configurations:
                if k:
                    k.validate()
        if self.port_overrides:
            for k in self.port_overrides:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_client_ippreservation_proxy_protocol is not None:
            result['EnableClientIPPreservationProxyProtocol'] = self.enable_client_ippreservation_proxy_protocol
        if self.enable_client_ippreservation_toa is not None:
            result['EnableClientIPPreservationToa'] = self.enable_client_ippreservation_toa
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k.to_map() if k else None)
        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name
        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds
        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path
        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port
        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol
        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k in self.port_overrides:
                result['PortOverrides'].append(k.to_map() if k else None)
        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count
        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableClientIPPreservationProxyProtocol') is not None:
            self.enable_client_ippreservation_proxy_protocol = m.get('EnableClientIPPreservationProxyProtocol')
        if m.get('EnableClientIPPreservationToa') is not None:
            self.enable_client_ippreservation_toa = m.get('EnableClientIPPreservationToa')
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k in m.get('EndpointConfigurations'):
                temp_model = UpdateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k))
        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')
        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')
        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')
        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')
        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')
        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k in m.get('PortOverrides'):
                temp_model = UpdateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k))
        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')
        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')
        return self


class UpdateEndpointGroupsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_group_configurations: List[UpdateEndpointGroupsRequestEndpointGroupConfigurations] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.endpoint_group_configurations = endpoint_group_configurations
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        if self.endpoint_group_configurations:
            for k in self.endpoint_group_configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k in m.get('EndpointGroupConfigurations'):
                temp_model = UpdateEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateEndpointGroupsResponseBody(TeaModel):
    def __init__(
        self,
        endpoint_group_ids: List[str] = None,
        request_id: str = None,
    ):
        self.endpoint_group_ids = endpoint_group_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateEndpointGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEndpointGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEndpointGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(TeaModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
    ):
        self.endpoint_group_id = endpoint_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig(TeaModel):
    def __init__(
        self,
        server_group_tuples: List[UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for k in self.server_group_tuples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k in self.server_group_tuples:
                result['ServerGroupTuples'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k in m.get('ServerGroupTuples'):
                temp_model = UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k))
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleActions(TeaModel):
    def __init__(
        self,
        forward_group_config: UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig = None,
        order: int = None,
        rule_action_type: str = None,
        rule_action_value: str = None,
    ):
        self.forward_group_config = forward_group_config
        self.order = order
        self.rule_action_type = rule_action_type
        self.rule_action_value = rule_action_value

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()
        if self.order is not None:
            result['Order'] = self.order
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_action_value is not None:
            result['RuleActionValue'] = self.rule_action_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = UpdateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m['ForwardGroupConfig'])
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class UpdateForwardingRulesRequestForwardingRulesRuleConditions(TeaModel):
    def __init__(
        self,
        host_config: UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig = None,
        path_config: UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig = None,
        rule_condition_type: str = None,
        rule_condition_value: str = None,
    ):
        self.host_config = host_config
        self.path_config = path_config
        self.rule_condition_type = rule_condition_type
        self.rule_condition_value = rule_condition_value

    def validate(self):
        if self.host_config:
            self.host_config.validate()
        if self.path_config:
            self.path_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()
        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()
        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type
        if self.rule_condition_value is not None:
            result['RuleConditionValue'] = self.rule_condition_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostConfig') is not None:
            temp_model = UpdateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m['HostConfig'])
        if m.get('PathConfig') is not None:
            temp_model = UpdateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m['PathConfig'])
        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')
        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')
        return self


class UpdateForwardingRulesRequestForwardingRules(TeaModel):
    def __init__(
        self,
        forwarding_rule_id: str = None,
        forwarding_rule_name: str = None,
        priority: int = None,
        rule_actions: List[UpdateForwardingRulesRequestForwardingRulesRuleActions] = None,
        rule_conditions: List[UpdateForwardingRulesRequestForwardingRulesRuleConditions] = None,
        rule_direction: str = None,
    ):
        self.forwarding_rule_id = forwarding_rule_id
        self.forwarding_rule_name = forwarding_rule_name
        self.priority = priority
        self.rule_actions = rule_actions
        self.rule_conditions = rule_conditions
        self.rule_direction = rule_direction

    def validate(self):
        if self.rule_actions:
            for k in self.rule_actions:
                if k:
                    k.validate()
        if self.rule_conditions:
            for k in self.rule_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name
        if self.priority is not None:
            result['Priority'] = self.priority
        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k in self.rule_actions:
                result['RuleActions'].append(k.to_map() if k else None)
        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k in self.rule_conditions:
                result['RuleConditions'].append(k.to_map() if k else None)
        if self.rule_direction is not None:
            result['RuleDirection'] = self.rule_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k in m.get('RuleActions'):
                temp_model = UpdateForwardingRulesRequestForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k))
        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k in m.get('RuleConditions'):
                temp_model = UpdateForwardingRulesRequestForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k))
        if m.get('RuleDirection') is not None:
            self.rule_direction = m.get('RuleDirection')
        return self


class UpdateForwardingRulesRequest(TeaModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        forwarding_rules: List[UpdateForwardingRulesRequestForwardingRules] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.accelerator_id = accelerator_id
        self.client_token = client_token
        self.forwarding_rules = forwarding_rules
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = UpdateForwardingRulesRequestForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateForwardingRulesResponseBodyForwardingRules(TeaModel):
    def __init__(
        self,
        forwarding_rule_id: str = None,
    ):
        self.forwarding_rule_id = forwarding_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forwarding_rule_id is not None:
            result['ForwardingRuleId'] = self.forwarding_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleId') is not None:
            self.forwarding_rule_id = m.get('ForwardingRuleId')
        return self


class UpdateForwardingRulesResponseBody(TeaModel):
    def __init__(
        self,
        forwarding_rules: List[UpdateForwardingRulesResponseBodyForwardingRules] = None,
        request_id: str = None,
    ):
        self.forwarding_rules = forwarding_rules
        self.request_id = request_id

    def validate(self):
        if self.forwarding_rules:
            for k in self.forwarding_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k in self.forwarding_rules:
                result['ForwardingRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k in m.get('ForwardingRules'):
                temp_model = UpdateForwardingRulesResponseBodyForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateForwardingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateForwardingRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateForwardingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpSetRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        ip_set_id: str = None,
        region_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.client_token = client_token
        self.ip_set_id = ip_set_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateIpSetResponseBody(TeaModel):
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


class UpdateIpSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIpSetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateIpSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIpSetsRequestIpSets(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        ip_set_id: str = None,
    ):
        self.bandwidth = bandwidth
        self.ip_set_id = ip_set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')
        return self


class UpdateIpSetsRequest(TeaModel):
    def __init__(
        self,
        ip_sets: List[UpdateIpSetsRequestIpSets] = None,
        region_id: str = None,
    ):
        self.ip_sets = ip_sets
        self.region_id = region_id

    def validate(self):
        if self.ip_sets:
            for k in self.ip_sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpSets'] = []
        if self.ip_sets is not None:
            for k in self.ip_sets:
                result['IpSets'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_sets = []
        if m.get('IpSets') is not None:
            for k in m.get('IpSets'):
                temp_model = UpdateIpSetsRequestIpSets()
                self.ip_sets.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateIpSetsResponseBody(TeaModel):
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


class UpdateIpSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIpSetsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateIpSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateListenerRequestBackendPorts(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateListenerRequestCertificates(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateListenerRequestPortRanges(TeaModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        self.from_port = from_port
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_port is not None:
            result['FromPort'] = self.from_port
        if self.to_port is not None:
            result['ToPort'] = self.to_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')
        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')
        return self


class UpdateListenerRequestXForwardedForConfig(TeaModel):
    def __init__(
        self,
        xforwarded_for_ga_ap_enabled: bool = None,
        xforwarded_for_ga_id_enabled: bool = None,
        xforwarded_for_port_enabled: bool = None,
        xforwarded_for_proto_enabled: bool = None,
        xreal_ip_enabled: bool = None,
    ):
        self.xforwarded_for_ga_ap_enabled = xforwarded_for_ga_ap_enabled
        self.xforwarded_for_ga_id_enabled = xforwarded_for_ga_id_enabled
        self.xforwarded_for_port_enabled = xforwarded_for_port_enabled
        self.xforwarded_for_proto_enabled = xforwarded_for_proto_enabled
        self.xreal_ip_enabled = xreal_ip_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.xforwarded_for_ga_ap_enabled is not None:
            result['XForwardedForGaApEnabled'] = self.xforwarded_for_ga_ap_enabled
        if self.xforwarded_for_ga_id_enabled is not None:
            result['XForwardedForGaIdEnabled'] = self.xforwarded_for_ga_id_enabled
        if self.xforwarded_for_port_enabled is not None:
            result['XForwardedForPortEnabled'] = self.xforwarded_for_port_enabled
        if self.xforwarded_for_proto_enabled is not None:
            result['XForwardedForProtoEnabled'] = self.xforwarded_for_proto_enabled
        if self.xreal_ip_enabled is not None:
            result['XRealIpEnabled'] = self.xreal_ip_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('XForwardedForGaApEnabled') is not None:
            self.xforwarded_for_ga_ap_enabled = m.get('XForwardedForGaApEnabled')
        if m.get('XForwardedForGaIdEnabled') is not None:
            self.xforwarded_for_ga_id_enabled = m.get('XForwardedForGaIdEnabled')
        if m.get('XForwardedForPortEnabled') is not None:
            self.xforwarded_for_port_enabled = m.get('XForwardedForPortEnabled')
        if m.get('XForwardedForProtoEnabled') is not None:
            self.xforwarded_for_proto_enabled = m.get('XForwardedForProtoEnabled')
        if m.get('XRealIpEnabled') is not None:
            self.xreal_ip_enabled = m.get('XRealIpEnabled')
        return self


class UpdateListenerRequest(TeaModel):
    def __init__(
        self,
        backend_ports: List[UpdateListenerRequestBackendPorts] = None,
        certificates: List[UpdateListenerRequestCertificates] = None,
        client_affinity: str = None,
        client_token: str = None,
        description: str = None,
        listener_id: str = None,
        name: str = None,
        port_ranges: List[UpdateListenerRequestPortRanges] = None,
        protocol: str = None,
        proxy_protocol: str = None,
        region_id: str = None,
        security_policy_id: str = None,
        xforwarded_for_config: UpdateListenerRequestXForwardedForConfig = None,
    ):
        self.backend_ports = backend_ports
        self.certificates = certificates
        self.client_affinity = client_affinity
        self.client_token = client_token
        self.description = description
        self.listener_id = listener_id
        self.name = name
        self.port_ranges = port_ranges
        self.protocol = protocol
        self.proxy_protocol = proxy_protocol
        self.region_id = region_id
        self.security_policy_id = security_policy_id
        self.xforwarded_for_config = xforwarded_for_config

    def validate(self):
        if self.backend_ports:
            for k in self.backend_ports:
                if k:
                    k.validate()
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()
        if self.port_ranges:
            for k in self.port_ranges:
                if k:
                    k.validate()
        if self.xforwarded_for_config:
            self.xforwarded_for_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BackendPorts'] = []
        if self.backend_ports is not None:
            for k in self.backend_ports:
                result['BackendPorts'].append(k.to_map() if k else None)
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
        if self.client_affinity is not None:
            result['ClientAffinity'] = self.client_affinity
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.name is not None:
            result['Name'] = self.name
        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k in self.port_ranges:
                result['PortRanges'].append(k.to_map() if k else None)
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_protocol is not None:
            result['ProxyProtocol'] = self.proxy_protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.xforwarded_for_config is not None:
            result['XForwardedForConfig'] = self.xforwarded_for_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_ports = []
        if m.get('BackendPorts') is not None:
            for k in m.get('BackendPorts'):
                temp_model = UpdateListenerRequestBackendPorts()
                self.backend_ports.append(temp_model.from_map(k))
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = UpdateListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('ClientAffinity') is not None:
            self.client_affinity = m.get('ClientAffinity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k in m.get('PortRanges'):
                temp_model = UpdateListenerRequestPortRanges()
                self.port_ranges.append(temp_model.from_map(k))
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyProtocol') is not None:
            self.proxy_protocol = m.get('ProxyProtocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('XForwardedForConfig') is not None:
            temp_model = UpdateListenerRequestXForwardedForConfig()
            self.xforwarded_for_config = temp_model.from_map(m['XForwardedForConfig'])
        return self


class UpdateListenerResponseBody(TeaModel):
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


class UpdateListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


