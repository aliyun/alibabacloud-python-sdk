# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribePhoneTwiceTelVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribePhoneTwiceTelVerifyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The request status code. Valid values:
        # 
        # - **OK**: The request was successful.
        # 
        # - **PortabilityNumberNotSupported**: Queries for this ported number are not supported.
        # 
        # - **RequestNumberNotSupported**: Queries are not supported for numbers from China Broadnet (starting with 192), mobile virtual network operators, and other unsupported carriers.
        # 
        # - **RequestFrequencyLimit**: Carriers limit frequent queries for the same number. If you receive this error code, try again later.
        # 
        # > A charge applies when the value of `Code` is `OK` and the value of `VerifyResult` is not `0`. For more information, see [Phone Number Service pricing](https://help.aliyun.com/document_detail/154751.html).
        self.code = code
        # A data structure that contains the verification results.
        self.data = data
        # A description of the returned status code.
        self.message = message
        # The unique ID of the request. This common parameter is returned with each request. Use this ID to troubleshoot issues.
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
            temp_model = main_models.DescribePhoneTwiceTelVerifyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePhoneTwiceTelVerifyResponseBodyData(DaraModel):
    def __init__(
        self,
        carrier: str = None,
        verify_result: str = None,
    ):
        # The carrier that provides service for the number. Valid values:
        # 
        # - **CMCC**: China Mobile.
        # 
        # - **CUCC**: China Unicom.
        # 
        # - **CTCC**: China Telecom.
        # 
        # > The carrier that currently provides service for the number. For a ported number, this is the destination carrier.
        self.carrier = carrier
        # The verification result. Valid values:
        # 
        # - **0**: Cannot be determined.
        # 
        # - **1**: The number is a recycled number.
        # 
        # - **2**: The number is not a recycled number.
        # 
        # - **3**: The number has been deactivated.
        # 
        # - **4**: Unknown: The number was transferred to a new owner.
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carrier is not None:
            result['Carrier'] = self.carrier

        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')

        return self

