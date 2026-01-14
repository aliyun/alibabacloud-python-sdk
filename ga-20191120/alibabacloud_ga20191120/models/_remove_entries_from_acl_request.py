# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class RemoveEntriesFromAclRequest(DaraModel):
    def __init__(
        self,
        acl_entries: List[main_models.RemoveEntriesFromAclRequestAclEntries] = None,
        acl_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        # The entries that you want to delete. You can delete up to 50 entries at a time.
        # 
        # This parameter is required.
        self.acl_entries = acl_entries
        # The ACL ID.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k1 in m.get('AclEntries'):
                temp_model = main_models.RemoveEntriesFromAclRequestAclEntries()
                self.acl_entries.append(temp_model.from_map(k1))

        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class RemoveEntriesFromAclRequestAclEntries(DaraModel):
    def __init__(
        self,
        entry: str = None,
    ):
        # The entry (IP address or CIDR block) that you want to delete. You can delete up to 50 entries at a time.
        # 
        # >  This parameter is required.
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

