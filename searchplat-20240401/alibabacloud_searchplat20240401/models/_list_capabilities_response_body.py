# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class ListCapabilitiesResponseBody(DaraModel):
    def __init__(
        self,
        http_code: int = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        result: List[main_models.ListCapabilitiesResponseBodyResult] = None,
        status: str = None,
        total_count: int = None,
    ):
        # The HTTP status code.
        self.http_code = http_code
        # The number of returned entries.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The returned result.
        self.result = result
        # The request status.
        self.status = status
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListCapabilitiesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListCapabilitiesResponseBodyResult(DaraModel):
    def __init__(
        self,
        created: int = None,
        is_default: bool = None,
        item_category: str = None,
        item_desc: str = None,
        item_name: str = None,
        item_value: Dict[str, Any] = None,
        status: str = None,
        updated: int = None,
    ):
        # The creation time.
        self.created = created
        # Indicates whether the configuration is the default configuration.
        self.is_default = is_default
        # The configuration category.
        self.item_category = item_category
        # The configuration description.
        self.item_desc = item_desc
        # The configuration name.
        self.item_name = item_name
        # itemValue
        self.item_value = item_value
        # status
        self.status = status
        # updated
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['created'] = self.created

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        if self.item_category is not None:
            result['itemCategory'] = self.item_category

        if self.item_desc is not None:
            result['itemDesc'] = self.item_desc

        if self.item_name is not None:
            result['itemName'] = self.item_name

        if self.item_value is not None:
            result['itemValue'] = self.item_value

        if self.status is not None:
            result['status'] = self.status

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        if m.get('itemCategory') is not None:
            self.item_category = m.get('itemCategory')

        if m.get('itemDesc') is not None:
            self.item_desc = m.get('itemDesc')

        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')

        if m.get('itemValue') is not None:
            self.item_value = m.get('itemValue')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

