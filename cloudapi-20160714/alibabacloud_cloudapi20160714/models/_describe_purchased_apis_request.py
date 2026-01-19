# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePurchasedApisRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The name of the API.
        self.api_name = api_name
        # The ID of the API group.
        self.group_id = group_id
        # The page number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        self.security_token = security_token
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **PRE**
        # *   **TEST**
        self.stage_name = stage_name
        # Specifies whether the API is public. Valid values:
        # 
        # *   **PUBLIC**: indicates that the API is public. If you set this parameter to PUBLIC, this API is displayed on the API List page in the console for all users after the API is published to the production environment.
        # *   **PRIVATE**: indicates that the API is private. If you set this parameter to PRIVATE, this API is not displayed in Alibaba Cloud Marketplace after the API group to which this API belongs is made available.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

