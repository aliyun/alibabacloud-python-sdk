# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetK8sApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        from_: str = None,
    ):
        # The ID of the application. You can call the [ListApplication](https://help.aliyun.com/document_detail/149390.html) operation to obtain the application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The source of the query.
        # 
        # - If this parameter is empty, a regular query is performed.
        # 
        # - deploy: The query is initiated from the deployment page.
        self.from_ = from_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.from_ is not None:
            result['From'] = self.from_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        return self

