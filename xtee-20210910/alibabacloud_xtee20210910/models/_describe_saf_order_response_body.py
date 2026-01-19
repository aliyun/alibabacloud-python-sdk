# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSafOrderResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeSafOrderResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned object.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeSafOrderResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeSafOrderResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        expiration_date: int = None,
    ):
        # Expiration date (timestamp).
        self.expiration_date = expiration_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_date is not None:
            result['expirationDate'] = self.expiration_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationDate') is not None:
            self.expiration_date = m.get('expirationDate')

        return self

