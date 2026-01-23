# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetInstanceEndpointResponseBody(DaraModel):
    def __init__(
        self,
        acl_enable: bool = None,
        acl_entries: List[main_models.GetInstanceEndpointResponseBodyAclEntries] = None,
        code: str = None,
        domains: List[main_models.GetInstanceEndpointResponseBodyDomains] = None,
        enable: bool = None,
        is_success: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        # Indicates whether the access control list (ACL) feature is enabled.
        self.acl_enable = acl_enable
        # The ACLs.
        self.acl_entries = acl_entries
        # The return value.
        self.code = code
        # Domain names.
        self.domains = domains
        # Indicates whether the ACL feature is enabled.
        self.enable = enable
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The status of the instance.
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

        if self.code is not None:
            result['Code'] = self.code

        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
                temp_model = main_models.GetInstanceEndpointResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.GetInstanceEndpointResponseBodyDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetInstanceEndpointResponseBodyDomains(DaraModel):
    def __init__(
        self,
        domain: str = None,
        type: str = None,
    ):
        # The domain name that is used to access the Container Registry Enterprise Edition instance.
        self.domain = domain
        # The type of the domain name. Valid values:
        # 
        # *   `SYSTEM`: a system domain name.
        # *   `USER`: a user domain name.
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

class GetInstanceEndpointResponseBodyAclEntries(DaraModel):
    def __init__(
        self,
        comment: str = None,
        entry: str = None,
    ):
        # Remarks for public IP address whitelists.
        self.comment = comment
        # The public IP address whitelist.
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.entry is not None:
            result['Entry'] = self.entry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        return self

