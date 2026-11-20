# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySecretNoDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_no_info_dto: main_models.QuerySecretNoDetailResponseBodySecretNoInfoDTO = None,
    ):
        # The request status code.
        # 
        # - OK indicates that the request was successful.
        # - For other error codes, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The number properties.
        self.secret_no_info_dto = secret_no_info_dto

    def validate(self):
        if self.secret_no_info_dto:
            self.secret_no_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.secret_no_info_dto is not None:
            result['SecretNoInfoDTO'] = self.secret_no_info_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecretNoInfoDTO') is not None:
            temp_model = main_models.QuerySecretNoDetailResponseBodySecretNoInfoDTO()
            self.secret_no_info_dto = temp_model.from_map(m.get('SecretNoInfoDTO'))

        return self

class QuerySecretNoDetailResponseBodySecretNoInfoDTO(DaraModel):
    def __init__(
        self,
        certify_status: int = None,
        city: str = None,
        province: str = None,
        purchase_time: str = None,
        secret_status: int = None,
        vendor: int = None,
    ):
        # The number verification status. Valid values:
        # 
        # - **0**: Unverified.
        # - **1**: Verified.
        self.certify_status = certify_status
        # The city.
        self.city = city
        # The province.
        self.province = province
        # The purchase time of the number, in the format of YYYY-MM-DD HH:mm:ss.
        self.purchase_time = purchase_time
        # The number status. Valid values:
        # 
        # - **0**: Unbound.
        # - **1**: Bound.
        # - **2**: Locked.
        # - **3**: Frozen.
        self.secret_status = secret_status
        # The carrier. Valid values:
        # 
        # - **1**: China Mobile
        # - **2**: China Unicom
        # - **3**: China Telecom
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status

        if self.city is not None:
            result['City'] = self.city

        if self.province is not None:
            result['Province'] = self.province

        if self.purchase_time is not None:
            result['PurchaseTime'] = self.purchase_time

        if self.secret_status is not None:
            result['SecretStatus'] = self.secret_status

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('PurchaseTime') is not None:
            self.purchase_time = m.get('PurchaseTime')

        if m.get('SecretStatus') is not None:
            self.secret_status = m.get('SecretStatus')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

