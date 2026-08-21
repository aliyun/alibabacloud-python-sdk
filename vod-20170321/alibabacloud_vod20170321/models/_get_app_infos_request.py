# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppInfosRequest(DaraModel):
    def __init__(
        self,
        app_ids: str = None,
    ):
        # The list of application IDs. The list consists of one or more application IDs. An application ID is the value of the AppId parameter returned by the [CreateAppInfo](https://help.aliyun.com/document_detail/113266.html) or [GetAppInfos](https://help.aliyun.com/document_detail/114000.html) operation.
        # - A maximum of 10 IDs are supported.
        # - Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.app_ids = app_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        return self

