# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class AddEntriesToAclRequest(DaraModel):
    def __init__(
        self,
        acl_entries: List[main_models.AddEntriesToAclRequestAclEntries] = None,
        acl_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
    ):
        # The ACL entries that you want to add. You can add at most 20 entries in each call.
        # 
        # This parameter is required.
        self.acl_entries = acl_entries
        # The ID of the ACL.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run

    def validate(self):
        if self.acl_entries:
            for v1 in self.acl_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k1 in self.acl_entries:
                result['AclEntries'].append(k1.to_map() if k1 else None)

        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k1 in m.get('AclEntries'):
                temp_model = main_models.AddEntriesToAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k1))

        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        return self



class AddEntriesToAclRequestAclEntries(DaraModel):
    def __init__(
        self,
        description: str = None,
        entry: str = None,
    ):
        # The description of the ACL entry. The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        # 
        # You can add at most 20 entries in each call.
        self.description = description
        # The CIDR block in the ACL entry.
        # 
        # This parameter is required.
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.entry is not None:
            result['Entry'] = self.entry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        return self

