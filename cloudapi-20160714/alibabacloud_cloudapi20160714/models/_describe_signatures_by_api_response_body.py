# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeSignaturesByApiResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        signatures: main_models.DescribeSignaturesByApiResponseBodySignatures = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned signature key information. It is an array consisting of SignatureItem data.
        self.signatures = signatures

    def validate(self):
        if self.signatures:
            self.signatures.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signatures is not None:
            result['Signatures'] = self.signatures.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Signatures') is not None:
            temp_model = main_models.DescribeSignaturesByApiResponseBodySignatures()
            self.signatures = temp_model.from_map(m.get('Signatures'))

        return self

class DescribeSignaturesByApiResponseBodySignatures(DaraModel):
    def __init__(
        self,
        signature_item: List[main_models.DescribeSignaturesByApiResponseBodySignaturesSignatureItem] = None,
    ):
        self.signature_item = signature_item

    def validate(self):
        if self.signature_item:
            for v1 in self.signature_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SignatureItem'] = []
        if self.signature_item is not None:
            for k1 in self.signature_item:
                result['SignatureItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.signature_item = []
        if m.get('SignatureItem') is not None:
            for k1 in m.get('SignatureItem'):
                temp_model = main_models.DescribeSignaturesByApiResponseBodySignaturesSignatureItem()
                self.signature_item.append(temp_model.from_map(k1))

        return self

class DescribeSignaturesByApiResponseBodySignaturesSignatureItem(DaraModel):
    def __init__(
        self,
        bound_time: str = None,
        signature_id: str = None,
        signature_name: str = None,
    ):
        # The time when the key was bound.
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
        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time

        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id

        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')

        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')

        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')

        return self

