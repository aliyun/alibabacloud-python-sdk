# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class DescribeCapabilityResponseBody(DaraModel):
    def __init__(
        self,
        http_code: int = None,
        request_id: str = None,
        result: main_models.DescribeCapabilityResponseBodyResult = None,
        status: str = None,
    ):
        # HTTP status code
        self.http_code = http_code
        # Request ID
        self.request_id = request_id
        # Response result
        self.result = result
        # Request status
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.DescribeCapabilityResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class DescribeCapabilityResponseBodyResult(DaraModel):
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
        # Timestamp of creation time
        self.created = created
        # Whether it is the default configuration
        self.is_default = is_default
        # Configuration category
        self.item_category = item_category
        # Configuration description
        self.item_desc = item_desc
        # Configuration name
        self.item_name = item_name
        # An object containing information such as endpoint and function, which describes the detailed configuration of the knowledge base.
        self.item_value = item_value
        # Status
        self.status = status
        # Update timestamp
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

