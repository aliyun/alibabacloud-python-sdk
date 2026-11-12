# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CmsV1MigrationAdmission(DaraModel):
    def __init__(
        self,
        new_migration_allowed: bool = None,
        policy_revision: str = None,
        reason: str = None,
    ):
        # The real-time new migration eligibility evaluated for the current target primary account, which does not replace RAM, account ownership, or workspace validations.
        self.new_migration_allowed = new_migration_allowed
        # The summary of the normalized policy, which excludes the UID list and is not an authorization credential.
        self.policy_revision = policy_revision
        # The reason why the new migration is denied. CMSV1_MIGRATION_NOT_ADMITTED indicates that the migration is not admitted, and CMSV1_MIGRATION_POLICY_UNAVAILABLE indicates that the policy is unavailable. Historical tasks remain queryable.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_migration_allowed is not None:
            result['newMigrationAllowed'] = self.new_migration_allowed

        if self.policy_revision is not None:
            result['policyRevision'] = self.policy_revision

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newMigrationAllowed') is not None:
            self.new_migration_allowed = m.get('newMigrationAllowed')

        if m.get('policyRevision') is not None:
            self.policy_revision = m.get('policyRevision')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

