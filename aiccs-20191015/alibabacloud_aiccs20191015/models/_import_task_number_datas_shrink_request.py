# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportTaskNumberDatasShrinkRequest(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        encryption_type: int = None,
        oss_file_name: str = None,
        owner_id: int = None,
        phone_number_list_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        # The data type. Valid values:
        # 
        # - EXCEL
        # 
        # - JSON
        # 
        # 
        #   >Notice: 
        # 
        #   API calls currently support only the JSON data type.
        # 
        # This parameter is required.
        self.data_type = data_type
        self.encryption_type = encryption_type
        # The OSS file path. This parameter is optional.
        # 
        # > Importing data by specifying an OSS file path is not available because API calls currently support only the JSON data type.
        self.oss_file_name = oss_file_name
        self.owner_id = owner_id
        # If `DataType` is set to `JSON`, you must use this parameter to upload the data. You can import up to 1,000 records per request.
        self.phone_number_list_shrink = phone_number_list_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the call task.
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
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type

        if self.oss_file_name is not None:
            result['OssFileName'] = self.oss_file_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number_list_shrink is not None:
            result['PhoneNumberList'] = self.phone_number_list_shrink

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

        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')

        if m.get('OssFileName') is not None:
            self.oss_file_name = m.get('OssFileName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumberList') is not None:
            self.phone_number_list_shrink = m.get('PhoneNumberList')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

