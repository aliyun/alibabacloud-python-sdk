# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitFactAuditUrlRequest(DaraModel):
    def __init__(
        self,
        url: str = None,
        workspace_id: str = None,
    ):
        # The URL of the information source you want to use for factuality audit. After you add a source URL using this operation, MiaoBi retrieves audit information only from your configured list of URLs. If you do not add any URL, MiaoBi searches the entire web for audit information. You can configure up to 10 source URLs.
        # 
        # This parameter is required.
        self.url = url
        # Unique identifier of the Alibaba Cloud Model Studio workspace. To get the workspace ID, see [Get the workspace ID](https://help.aliyun.com/document_detail/2782167.html).
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['Url'] = self.url

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

