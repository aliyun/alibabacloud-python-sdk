# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListInstanceEndpointResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        endpoints: List[main_models.ListInstanceEndpointResponseBodyEndpoints] = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The return value.
        self.code = code
        # The endpoints of the instance.
        self.endpoints = endpoints
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.ListInstanceEndpointResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstanceEndpointResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        acl_enable: bool = None,
        acl_entries: List[main_models.ListInstanceEndpointResponseBodyEndpointsAclEntries] = None,
        domains: List[main_models.ListInstanceEndpointResponseBodyEndpointsDomains] = None,
        enable: bool = None,
        endpoint_type: str = None,
        linked_vpcs: List[main_models.ListInstanceEndpointResponseBodyEndpointsLinkedVpcs] = None,
        status: str = None,
    ):
        # Indicates whether the endpoint is added to an access control list (ACL).
        self.acl_enable = acl_enable
        # The ACLs that are configured for the instance.
        self.acl_entries = acl_entries
        # The list of domain names of the Container Registry instance.
        self.domains = domains
        # Indicates whether the endpoint is added to an ACL.
        self.enable = enable
        # The type of the endpoint.
        self.endpoint_type = endpoint_type
        # The VPCs associated with the instance.
        self.linked_vpcs = linked_vpcs
        # The status of the endpoint.
        self.status = status

    def validate(self):
        if self.acl_entries:
            for v1 in self.acl_entries:
                 if v1:
                    v1.validate()
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()
        if self.linked_vpcs:
            for v1 in self.linked_vpcs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_enable is not None:
            result['AclEnable'] = self.acl_enable

        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k1 in self.acl_entries:
                result['AclEntries'].append(k1.to_map() if k1 else None)

        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        result['LinkedVpcs'] = []
        if self.linked_vpcs is not None:
            for k1 in self.linked_vpcs:
                result['LinkedVpcs'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEnable') is not None:
            self.acl_enable = m.get('AclEnable')

        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k1 in m.get('AclEntries'):
                temp_model = main_models.ListInstanceEndpointResponseBodyEndpointsAclEntries()
                self.acl_entries.append(temp_model.from_map(k1))

        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.ListInstanceEndpointResponseBodyEndpointsDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        self.linked_vpcs = []
        if m.get('LinkedVpcs') is not None:
            for k1 in m.get('LinkedVpcs'):
                temp_model = main_models.ListInstanceEndpointResponseBodyEndpointsLinkedVpcs()
                self.linked_vpcs.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstanceEndpointResponseBodyEndpointsLinkedVpcs(DaraModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListInstanceEndpointResponseBodyEndpointsDomains(DaraModel):
    def __init__(
        self,
        domain: str = None,
        type: str = None,
    ):
        # The domain name of the Container Registry instance.
        self.domain = domain
        # The type of the domain name. Valid values:
        # 
        # *   SYSTEM: system domain name.
        # *   USER: user domain name.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListInstanceEndpointResponseBodyEndpointsAclEntries(DaraModel):
    def __init__(
        self,
        entry: str = None,
    ):
        # The information about the ACL.
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry is not None:
            result['Entry'] = self.entry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        return self

