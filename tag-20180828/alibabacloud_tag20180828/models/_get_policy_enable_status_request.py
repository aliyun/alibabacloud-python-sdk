# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPolicyEnableStatusRequest(DaraModel):
    def __init__(
        self,
        open_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        user_type: str = None,
    ):
        # The enabling type. Valid values:
        # 
        # *   TAG_POLICY: the Tag Policy feature.
        # *   VERIFY_NO_TAG: the strong verification feature.
        # *   TAG_POLICY_NOTIFY: the notification feature that sends notifications for resources found to be non-compliant with the tag policy.
        self.open_type = open_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. Set the value to cn-shanghai.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The mode of the Tag Policy feature. This parameter specifies a filter condition for the query. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        # 
        # >  The value of this parameter is not case-sensitive.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_type is not None:
            result['OpenType'] = self.open_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenType') is not None:
            self.open_type = m.get('OpenType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

