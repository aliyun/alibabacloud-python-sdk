# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class ThreeElementsVerificationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ThreeElementsVerificationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   **OK**: The request is successful.
        # *   For more information, see Error codes in this documentation.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # The response parameters.
        self.data = data
        # The returned message.
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ThreeElementsVerificationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ThreeElementsVerificationResponseBodyData(DaraModel):
    def __init__(
        self,
        basic_carrier: str = None,
        is_consistent: int = None,
    ):
        # The basic carrier. Valid values:
        # 
        # *   **China Mobile**
        # *   **China Unicom**
        # *   **China Telecom**
        self.basic_carrier = basic_carrier
        # Indicates whether the specified name, phone number, and ID card number belong to the same user. Valid values:
        # 
        # * **1**: The specified name, phone number, and ID card number belong to the same user.
        # * **0**: The specified name, phone number, and ID card number do not belong to the same user.
        # * **2**: The specified name, phone number, and ID card number cannot be found.
        # 
        # **Note** The phone number registration data of a user is usually updated one or three days after registration. The registration data can be queried only after the update. The following table shows the verification results under different phone number states.
        # 
        # |Carrier/Phone number state|Out-of-service|Nonexistent|Canceled|
        # |---|---|---|---|
        # |China Mobile|Verifications can be carried out normally.|The specified name, phone number, and ID card number cannot be found.|The specified name, phone number, and ID card number cannot be found.|
        # |China Unicom|Verifications can be carried out normally.|The specified name, phone number, and ID card number do not belong to the same user.|The specified name, phone number, and ID card number do not belong to the same user.|
        # |China Telecom|Verifications can be carried out normally.|The specified name, phone number, and ID card number cannot be found.|The specified name, phone number, and ID card number cannot be found.|
        self.is_consistent = is_consistent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_carrier is not None:
            result['BasicCarrier'] = self.basic_carrier

        if self.is_consistent is not None:
            result['IsConsistent'] = self.is_consistent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicCarrier') is not None:
            self.basic_carrier = m.get('BasicCarrier')

        if m.get('IsConsistent') is not None:
            self.is_consistent = m.get('IsConsistent')

        return self

