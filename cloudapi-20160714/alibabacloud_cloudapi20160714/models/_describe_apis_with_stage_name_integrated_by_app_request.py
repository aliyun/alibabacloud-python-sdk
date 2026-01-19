# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApisWithStageNameIntegratedByAppRequest(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_uid: str = None,
        app_id: int = None,
        description: str = None,
        method: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
        security_token: str = None,
    ):
        # The API name.
        self.api_name = api_name
        # The API ID.
        self.api_uid = api_uid
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The API description. The description can be up to 200 characters in length.
        self.description = description
        # The request HTTP method of the API.
        self.method = method
        # The page number of the page to return.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request path of the API.
        self.path = path
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.description is not None:
            result['Description'] = self.description

        if self.method is not None:
            result['Method'] = self.method

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

