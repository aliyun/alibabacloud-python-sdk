# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class MemberApiKeyDTO(DaraModel):
    def __init__(
        self,
        client: main_models.ClientDTO = None,
        client_id: int = None,
        delete_tag: int = None,
        expire_at: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        key: str = None,
        key_preview: str = None,
        member_user_id: int = None,
        member_user_name: str = None,
        name: str = None,
        status: str = None,
    ):
        # The parent department information.
        self.client = client
        # The ID of the parent department. Member keys are mapped to their parent departments.
        self.client_id = client_id
        # The deletion tag. A value of 0 indicates that the key is enabled, and a non-zero value indicates that the key is disabled.
        self.delete_tag = delete_tag
        # The expiration time. A null value indicates that the key never expires.
        self.expire_at = expire_at
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The API key ID. This ID can be used to query the bound group by API key.
        self.id = id
        # The full key. This field is not returned in the member list and is always empty.
        self.key = key
        # The masked preview of the API key.
        self.key_preview = key_preview
        # The ID of the department member to whom the key belongs.
        self.member_user_id = member_user_id
        # The member name.
        self.member_user_name = member_user_name
        # The API key name.
        self.name = name
        # The status. Valid values: active: Enabled. disabled: Disabled.
        self.status = status

    def validate(self):
        if self.client:
            self.client.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client is not None:
            result['client'] = self.client.to_map()

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.delete_tag is not None:
            result['deleteTag'] = self.delete_tag

        if self.expire_at is not None:
            result['expireAt'] = self.expire_at

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.key is not None:
            result['key'] = self.key

        if self.key_preview is not None:
            result['keyPreview'] = self.key_preview

        if self.member_user_id is not None:
            result['memberUserId'] = self.member_user_id

        if self.member_user_name is not None:
            result['memberUserName'] = self.member_user_name

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client') is not None:
            temp_model = main_models.ClientDTO()
            self.client = temp_model.from_map(m.get('client'))

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('deleteTag') is not None:
            self.delete_tag = m.get('deleteTag')

        if m.get('expireAt') is not None:
            self.expire_at = m.get('expireAt')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('keyPreview') is not None:
            self.key_preview = m.get('keyPreview')

        if m.get('memberUserId') is not None:
            self.member_user_id = m.get('memberUserId')

        if m.get('memberUserName') is not None:
            self.member_user_name = m.get('memberUserName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

