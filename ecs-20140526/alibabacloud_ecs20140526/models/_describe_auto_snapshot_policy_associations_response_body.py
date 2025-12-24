# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoSnapshotPolicyAssociationsResponseBody(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_associations: main_models.DescribeAutoSnapshotPolicyAssociationsResponseBodyAutoSnapshotPolicyAssociations = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The association of automatic snapshot policies.
        self.auto_snapshot_policy_associations = auto_snapshot_policy_associations
        # The returned pagination token which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.auto_snapshot_policy_associations:
            self.auto_snapshot_policy_associations.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_associations is not None:
            result['AutoSnapshotPolicyAssociations'] = self.auto_snapshot_policy_associations.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyAssociations') is not None:
            temp_model = main_models.DescribeAutoSnapshotPolicyAssociationsResponseBodyAutoSnapshotPolicyAssociations()
            self.auto_snapshot_policy_associations = temp_model.from_map(m.get('AutoSnapshotPolicyAssociations'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAutoSnapshotPolicyAssociationsResponseBodyAutoSnapshotPolicyAssociations(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_association: List[main_models.DescribeAutoSnapshotPolicyAssociationsResponseBodyAutoSnapshotPolicyAssociationsAutoSnapshotPolicyAssociation] = None,
    ):
        self.auto_snapshot_policy_association = auto_snapshot_policy_association

    def validate(self):
        if self.auto_snapshot_policy_association:
            for v1 in self.auto_snapshot_policy_association:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoSnapshotPolicyAssociation'] = []
        if self.auto_snapshot_policy_association is not None:
            for k1 in self.auto_snapshot_policy_association:
                result['AutoSnapshotPolicyAssociation'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_snapshot_policy_association = []
        if m.get('AutoSnapshotPolicyAssociation') is not None:
            for k1 in m.get('AutoSnapshotPolicyAssociation'):
                temp_model = main_models.DescribeAutoSnapshotPolicyAssociationsResponseBodyAutoSnapshotPolicyAssociationsAutoSnapshotPolicyAssociation()
                self.auto_snapshot_policy_association.append(temp_model.from_map(k1))

        return self

class DescribeAutoSnapshotPolicyAssociationsResponseBodyAutoSnapshotPolicyAssociationsAutoSnapshotPolicyAssociation(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        disk_id: str = None,
    ):
        # The ID of the automatic snapshot policy.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The ID of the cloud disk.
        self.disk_id = disk_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        return self

