# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryAgRelationCountAndQuotaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryAgRelationCountAndQuotaResponseBodyData = None,
        http_code: str = None,
        message: str = None,
        null_object: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_code = http_code
        self.message = message
        self.null_object = null_object
        self.request_id = request_id
        self.success = success

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

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.null_object is not None:
            result['NullObject'] = self.null_object

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryAgRelationCountAndQuotaResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NullObject') is not None:
            self.null_object = m.get('NullObject')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAgRelationCountAndQuotaResponseBodyData(DaraModel):
    def __init__(
        self,
        account_count: int = None,
        mpk: str = None,
        null_object: bool = None,
        quota: int = None,
    ):
        self.account_count = account_count
        self.mpk = mpk
        self.null_object = null_object
        self.quota = quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_count is not None:
            result['AccountCount'] = self.account_count

        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.null_object is not None:
            result['NullObject'] = self.null_object

        if self.quota is not None:
            result['Quota'] = self.quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountCount') is not None:
            self.account_count = m.get('AccountCount')

        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('NullObject') is not None:
            self.null_object = m.get('NullObject')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        return self

