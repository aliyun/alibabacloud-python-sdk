# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApiSignaturesResponseBody(DaraModel):
    def __init__(
        self,
        api_signatures: main_models.DescribeApiSignaturesResponseBodyApiSignatures = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned signature key information. It is an array consisting of ApiSignatureItem data.
        self.api_signatures = api_signatures
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.api_signatures:
            self.api_signatures.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_signatures is not None:
            result['ApiSignatures'] = self.api_signatures.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiSignatures') is not None:
            temp_model = main_models.DescribeApiSignaturesResponseBodyApiSignatures()
            self.api_signatures = temp_model.from_map(m.get('ApiSignatures'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApiSignaturesResponseBodyApiSignatures(DaraModel):
    def __init__(
        self,
        api_signature_item: List[main_models.DescribeApiSignaturesResponseBodyApiSignaturesApiSignatureItem] = None,
    ):
        self.api_signature_item = api_signature_item

    def validate(self):
        if self.api_signature_item:
            for v1 in self.api_signature_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiSignatureItem'] = []
        if self.api_signature_item is not None:
            for k1 in self.api_signature_item:
                result['ApiSignatureItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_signature_item = []
        if m.get('ApiSignatureItem') is not None:
            for k1 in m.get('ApiSignatureItem'):
                temp_model = main_models.DescribeApiSignaturesResponseBodyApiSignaturesApiSignatureItem()
                self.api_signature_item.append(temp_model.from_map(k1))

        return self

class DescribeApiSignaturesResponseBodyApiSignaturesApiSignatureItem(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        bound_time: str = None,
        signature_id: str = None,
        signature_name: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The name of the API.
        self.api_name = api_name
        # The time when the backend signature key was bound.
        self.bound_time = bound_time
        # The ID of the backend signature key.
        self.signature_id = signature_id
        # The name of the backend signature key.
        self.signature_name = signature_name

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

        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time

        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id

        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')

        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')

        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')

        return self

