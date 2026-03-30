# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class GetAccessKeyInfoInRecycleBinResponseBody(DaraModel):
    def __init__(
        self,
        access_key: main_models.GetAccessKeyInfoInRecycleBinResponseBodyAccessKey = None,
        request_id: str = None,
    ):
        # The information about the AccessKey pair.
        self.access_key = access_key
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_key:
            self.access_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            temp_model = main_models.GetAccessKeyInfoInRecycleBinResponseBodyAccessKey()
            self.access_key = temp_model.from_map(m.get('AccessKey'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccessKeyInfoInRecycleBinResponseBodyAccessKey(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        create_date: str = None,
        delete_date: str = None,
        recycle_date: str = None,
        user_id: str = None,
        user_principal_name: str = None,
        user_recycled: bool = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The time when the AccessKey pair was created.
        self.create_date = create_date
        # The time when the AccessKey pair will be permanently deleted from the recycle bin.
        self.delete_date = delete_date
        # The time when the AccessKey pair was deleted and moved to the recycle bin.
        self.recycle_date = recycle_date
        # The ID of the RAM user.
        self.user_id = user_id
        # The logon name of the RAM user.
        self.user_principal_name = user_principal_name
        # Indicates whether the RAM user to which the AccessKey pair belongs is in the recycle bin. Valid values:
        # 
        # *   true
        # *   false
        self.user_recycled = user_recycled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date

        if self.recycle_date is not None:
            result['RecycleDate'] = self.recycle_date

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        if self.user_recycled is not None:
            result['UserRecycled'] = self.user_recycled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')

        if m.get('RecycleDate') is not None:
            self.recycle_date = m.get('RecycleDate')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        if m.get('UserRecycled') is not None:
            self.user_recycled = m.get('UserRecycled')

        return self

