# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFileByBizRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        file_type: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        save_oss_file_name: str = None,
        user_view_file_name: str = None,
    ):
        self.biz_id = biz_id
        # This parameter is required.
        self.biz_type = biz_type
        self.file_type = file_type
        self.owner_id = owner_id
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.save_oss_file_name = save_oss_file_name
        # This parameter is required.
        self.user_view_file_name = user_view_file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.save_oss_file_name is not None:
            result['SaveOssFileName'] = self.save_oss_file_name

        if self.user_view_file_name is not None:
            result['UserViewFileName'] = self.user_view_file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SaveOssFileName') is not None:
            self.save_oss_file_name = m.get('SaveOssFileName')

        if m.get('UserViewFileName') is not None:
            self.user_view_file_name = m.get('UserViewFileName')

        return self

