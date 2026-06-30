# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class AddEntriesToAclRequest(DaraModel):
    def __init__(
        self,
        acl_entries: List[main_models.AddEntriesToAclRequestAclEntries] = None,
        acl_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        # The access control policy group entries to add. An entry can be an IP address or a CIDR block.
        # 
        # You can add up to 50 entries at a time.
        # 
        # This parameter is required.
        self.acl_entries = acl_entries
        # The ID of the access control policy group.
        # 
        # This parameter is required.
        self.acl_id = acl_id
        # The client token that is used to ensure the idempotence of a request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** value as the **ClientToken** value. The **RequestId** value is different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run. The system checks the required parameters, request format, and business limitations without actually adding IP entries to the access control policy group. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # - **false** (default): sends a normal request. If the check succeeds, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The region ID of the Global Accelerator (GA) instance. Set the value to **cn-hangzhou**.
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
                temp_model = main_models.AddEntriesToAclRequestAclEntries()
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



class AddEntriesToAclRequestAclEntries(DaraModel):
    def __init__(
        self,
        entry: str = None,
        entry_description: str = None,
    ):
        # The access control policy group entry to add. An entry can be an IP address or a CIDR block. You can add up to 50 entries at a time.
        # 
        # > This parameter is required.
        self.entry = entry
        # The description of the access control policy group entry.
        # 
        # You can add descriptions for up to 50 entries at a time.
        # 
        # The description must be 1 to 256 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_). Chinese characters are supported.
        self.entry_description = entry_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

