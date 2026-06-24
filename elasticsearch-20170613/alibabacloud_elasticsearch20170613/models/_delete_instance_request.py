# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        delete_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The release type. Valid values:
        # 
        # - immediate: The instance is immediately deleted. After deletion, the system permanently clears all data, and the instance no longer appears in the instance list.
        # - protective: The instance is frozen for 24 hours before the data is permanently cleared. During this period, the instance still appears in the instance list, and you can choose to [restore the instance](https://help.aliyun.com/document_detail/202195.html) or [immediately release it](https://help.aliyun.com/document_detail/202195.html).
        self.delete_type = delete_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.delete_type is not None:
            result['deleteType'] = self.delete_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('deleteType') is not None:
            self.delete_type = m.get('deleteType')

        return self

