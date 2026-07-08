# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class CertNoThreeElementVerificationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CertNoThreeElementVerificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about why access was denied.
        self.access_denied_detail = access_denied_detail
        # The request status code. Valid values:
        # - OK: The request is successful.
        # - For other error codes, see the error code list below.
        self.code = code
        # The returned result.
        self.data = data
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CertNoThreeElementVerificationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self



class CertNoThreeElementVerificationResponseBodyData(DaraModel):
    def __init__(
        self,
        is_consistent: str = None,
    ):
        # Indicates whether the verification result is consistent. Returned values:
        # 
        # - 0: The name matches the ID card number, but they are recognized as not the same person.
        # 
        # - 1: The name matches the ID card number, and they are recognized as the same person.
        # 
        # - 2: The name matches the ID card number, and they are suspected to be the same person.
        # 
        # - 3: The name matches the ID card number, but no portrait information is found in the database.
        # 
        # - 4: Invalid identity information (the name does not match the ID card number).
        # 
        # - 5: The photo quality is unqualified.
        self.is_consistent = is_consistent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_consistent is not None:
            result['IsConsistent'] = self.is_consistent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsConsistent') is not None:
            self.is_consistent = m.get('IsConsistent')

        return self

