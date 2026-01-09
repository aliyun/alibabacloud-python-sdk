# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class ImportTaskNumberDatasRequest(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        oss_file_name: str = None,
        owner_id: int = None,
        phone_number_list: List[Dict[str, Any]] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.data_type = data_type
        self.oss_file_name = oss_file_name
        self.owner_id = owner_id
        self.phone_number_list = phone_number_list
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
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.oss_file_name is not None:
            result['OssFileName'] = self.oss_file_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number_list is not None:
            result['PhoneNumberList'] = self.phone_number_list

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('OssFileName') is not None:
            self.oss_file_name = m.get('OssFileName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumberList') is not None:
            self.phone_number_list = m.get('PhoneNumberList')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

