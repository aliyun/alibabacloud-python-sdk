# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIpamResponseBody(DaraModel):
    def __init__(
        self,
        default_resource_discovery_association_id: str = None,
        default_resource_discovery_id: str = None,
        ipam_id: str = None,
        private_default_scope_id: str = None,
        public_default_scope_id: str = None,
        request_id: str = None,
        resource_discovery_association_count: int = None,
    ):
        # The ID of the default resource discovery association.
        self.default_resource_discovery_association_id = default_resource_discovery_association_id
        # The ID of the default resource discovery instance.
        self.default_resource_discovery_id = default_resource_discovery_id
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The default private scope created by the system after the IPAM is created.
        self.private_default_scope_id = private_default_scope_id
        # The default public scope created by the system after the IPAM is created.
        self.public_default_scope_id = public_default_scope_id
        # The request ID.
        self.request_id = request_id
        # The number of discovered resources.
        self.resource_discovery_association_count = resource_discovery_association_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_resource_discovery_association_id is not None:
            result['DefaultResourceDiscoveryAssociationId'] = self.default_resource_discovery_association_id

        if self.default_resource_discovery_id is not None:
            result['DefaultResourceDiscoveryId'] = self.default_resource_discovery_id

        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id

        if self.private_default_scope_id is not None:
            result['PrivateDefaultScopeId'] = self.private_default_scope_id

        if self.public_default_scope_id is not None:
            result['PublicDefaultScopeId'] = self.public_default_scope_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_discovery_association_count is not None:
            result['ResourceDiscoveryAssociationCount'] = self.resource_discovery_association_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResourceDiscoveryAssociationId') is not None:
            self.default_resource_discovery_association_id = m.get('DefaultResourceDiscoveryAssociationId')

        if m.get('DefaultResourceDiscoveryId') is not None:
            self.default_resource_discovery_id = m.get('DefaultResourceDiscoveryId')

        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')

        if m.get('PrivateDefaultScopeId') is not None:
            self.private_default_scope_id = m.get('PrivateDefaultScopeId')

        if m.get('PublicDefaultScopeId') is not None:
            self.public_default_scope_id = m.get('PublicDefaultScopeId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceDiscoveryAssociationCount') is not None:
            self.resource_discovery_association_count = m.get('ResourceDiscoveryAssociationCount')

        return self

