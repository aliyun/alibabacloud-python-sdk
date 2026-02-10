# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAttestorRequest(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        key_region_id: str = None,
        key_version_id: str = None,
        name: str = None,
        remark: str = None,
        resource_owner_id: int = None,
        source_ip: str = None,
    ):
        # The ID of the KMS key.
        self.key_id = key_id
        # The region ID of the Key Management Service (KMS) key.
        self.key_region_id = key_region_id
        # The version ID of the KMS key.
        self.key_version_id = key_version_id
        # The name of the witness.
        self.name = name
        # The description.
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_region_id is not None:
            result['KeyRegionId'] = self.key_region_id

        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyRegionId') is not None:
            self.key_region_id = m.get('KeyRegionId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

