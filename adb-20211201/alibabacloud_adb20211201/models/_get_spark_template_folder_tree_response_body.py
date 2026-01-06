# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSparkTemplateFolderTreeResponseBody(DaraModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The directory structure of Spark applications, which is in the tree format. Fields in the response parameter:
        # 
        # *   **Uid**: the UID of the Alibaba Cloud account.
        # 
        # *   **Type**: the application template type. Valid values: **FOLDER**
        # 
        # *   **Parent**: indicates whether a child directory exists. Valid values:
        # 
        #     *   **0**: no.
        #     *   **-1**: yes.
        # 
        # *   **Children**: the child directory.
        # 
        # *   **LastModified**: the time when applications in the directory are last modified. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # *   **Name**: the name of the directory.
        # 
        # *   **Id**: the directory ID.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

