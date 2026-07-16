# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CancelAiCallDetailsRequest(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        detail_id_list: List[str] = None,
        encryption_type: int = None,
        owner_id: int = None,
        phone_numbers: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        # The batch ID. This ID is returned when you import callee data. You can find the task batch ID on the **Call Task Management**>**Details**>**Execution Record** page, or use the import batch ID that is returned by the [ImportTaskNumberDatas](https://help.aliyun.com/document_detail/2926815.html) API operation. If DetailIdList is specified, this parameter is invalid.
        self.batch_id = batch_id
        # A list of detail IDs. If you specify this parameter, `BatchId` and `PhoneNumbers` are ignored.
        self.detail_id_list = detail_id_list
        self.encryption_type = encryption_type
        self.owner_id = owner_id
        # A list of phone numbers. This parameter takes effect only when `BatchId` is also specified.
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task ID. You can view the task ID on the **Call Task Management** page or obtain it by calling the [QueryAiCallTaskPage](https://help.aliyun.com/document_detail/2926799.html) operation.
        # 
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

        if self.detail_id_list is not None:
            result['DetailIdList'] = self.detail_id_list

        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers

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
            self.detail_id_list = m.get('DetailIdList')

        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

