# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolicyRequest(DaraModel):
    def __init__(
        self,
        cascading_delete: bool = None,
        policy_name: str = None,
    ):
        # Specifies whether to delete all versions of the policy. Valid values:
        # 
        # *   true: deletes all versions of the policy.
        # *   false: does not delete all versions of the policy. If you set the parameter to false, the non-default versions of the policy are not deleted. Before you delete the policy, you must manually delete all non-default versions of the policy.
        self.cascading_delete = cascading_delete
        # The name of the policy.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cascading_delete is not None:
            result['CascadingDelete'] = self.cascading_delete

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CascadingDelete') is not None:
            self.cascading_delete = m.get('CascadingDelete')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

