# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelAiCallDetailsShrinkRequest(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        detail_id_list_shrink: str = None,
        owner_id: int = None,
        phone_numbers_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        self.batch_id = batch_id
        self.detail_id_list_shrink = detail_id_list_shrink
        self.owner_id = owner_id
        self.phone_numbers_shrink = phone_numbers_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.detail_id_list_shrink is not None:
            result['DetailIdList'] = self.detail_id_list_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_numbers_shrink is not None:
            result['PhoneNumbers'] = self.phone_numbers_shrink

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('DetailIdList') is not None:
            self.detail_id_list_shrink = m.get('DetailIdList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumbers') is not None:
            self.phone_numbers_shrink = m.get('PhoneNumbers')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

