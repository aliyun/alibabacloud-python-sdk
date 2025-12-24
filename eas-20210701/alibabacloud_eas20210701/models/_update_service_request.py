# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceRequest(DaraModel):
    def __init__(
        self,
        member_to_update: str = None,
        update_type: str = None,
        body: str = None,
    ):
        self.member_to_update = member_to_update
        # The type of the service update. Valid values: merge and replace. By default, merge is used if you do not specify this parameter.
        # 
        # *   merge: If the JSON string configured for the existing service is `{"a":"b"}` and the JSON string specified in the body parameter is `{"c":"d"}`, the JSON string is `{"a":"b","c":"d"}` after the service update.
        # *   replace: If the JSON string configured for the existing service is `{"a":"b"}` and the JSON string specified in the body parameter is `{"c":"d"}`, the JSON string is `{"c":"d"}` after the service update.
        self.update_type = update_type
        # The request body. The body includes the request parameters that you want to update. For more information about the request parameters, see [CreateService](https://help.aliyun.com/document_detail/412086.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_to_update is not None:
            result['MemberToUpdate'] = self.member_to_update

        if self.update_type is not None:
            result['UpdateType'] = self.update_type

        if self.body is not None:
            result['body'] = self.body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberToUpdate') is not None:
            self.member_to_update = m.get('MemberToUpdate')

        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')

        if m.get('body') is not None:
            self.body = m.get('body')

        return self

