# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class ListHotlineTransferRegisterFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListHotlineTransferRegisterFileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [API error codes](https://help.aliyun.com/document_detail/112502.html).
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
            temp_model = main_models.ListHotlineTransferRegisterFileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListHotlineTransferRegisterFileResponseBodyData(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
        values: List[main_models.ListHotlineTransferRegisterFileResponseBodyDataValues] = None,
    ):
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total
        # The registration file.
        self.values = values

    def validate(self):
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.ListHotlineTransferRegisterFileResponseBodyDataValues()
                self.values.append(temp_model.from_map(k1))

        return self

class ListHotlineTransferRegisterFileResponseBodyDataValues(DaraModel):
    def __init__(
        self,
        agree: str = None,
        corp_name: str = None,
        hotline_number: str = None,
        mng_op_identity_card: str = None,
        mng_op_mail: str = None,
        mng_op_mobile: str = None,
        mng_op_name: str = None,
        qualification_id: str = None,
        res_unique_code: int = None,
    ):
        # The authenticity of the commitment.
        self.agree = agree
        # The enterprise name.
        self.corp_name = corp_name
        # The China 400 number.
        self.hotline_number = hotline_number
        # The ID card number of the handler.
        self.mng_op_identity_card = mng_op_identity_card
        # The email address of the handler.
        self.mng_op_mail = mng_op_mail
        # The mobile phone number of the handler.
        self.mng_op_mobile = mng_op_mobile
        # The name of the handler.
        self.mng_op_name = mng_op_name
        # The qualification ID.
        self.qualification_id = qualification_id
        # The unique code of the query operation.
        self.res_unique_code = res_unique_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agree is not None:
            result['Agree'] = self.agree

        if self.corp_name is not None:
            result['CorpName'] = self.corp_name

        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number

        if self.mng_op_identity_card is not None:
            result['MngOpIdentityCard'] = self.mng_op_identity_card

        if self.mng_op_mail is not None:
            result['MngOpMail'] = self.mng_op_mail

        if self.mng_op_mobile is not None:
            result['MngOpMobile'] = self.mng_op_mobile

        if self.mng_op_name is not None:
            result['MngOpName'] = self.mng_op_name

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.res_unique_code is not None:
            result['ResUniqueCode'] = self.res_unique_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agree') is not None:
            self.agree = m.get('Agree')

        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')

        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')

        if m.get('MngOpIdentityCard') is not None:
            self.mng_op_identity_card = m.get('MngOpIdentityCard')

        if m.get('MngOpMail') is not None:
            self.mng_op_mail = m.get('MngOpMail')

        if m.get('MngOpMobile') is not None:
            self.mng_op_mobile = m.get('MngOpMobile')

        if m.get('MngOpName') is not None:
            self.mng_op_name = m.get('MngOpName')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('ResUniqueCode') is not None:
            self.res_unique_code = m.get('ResUniqueCode')

        return self

