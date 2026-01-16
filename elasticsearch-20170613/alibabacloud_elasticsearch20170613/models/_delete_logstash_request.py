# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLogstashRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        delete_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The type of the release operation. Valid values:
        # 
        # *   immediate: The cluster is immediately deleted when it is released. After the cluster is deleted, the data stored in the cluster is deleted, and the system removes the cluster from the Logstash cluster list.
        # *   protective: The cluster is released 24 hours later. During the period of 24 hours, you can still find the cluster in the Logstash cluster list, and [restore the cluster](https://help.aliyun.com/document_detail/202205.html) or [immediately release the cluster](https://help.aliyun.com/document_detail/160591.html). After 24 hours elapse, the data stored in the cluster is deleted.
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

