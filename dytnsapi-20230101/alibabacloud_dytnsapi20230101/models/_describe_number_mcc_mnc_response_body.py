# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20230101 import models as main_models
from darabonba.model import DaraModel

class DescribeNumberMccMncResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.DescribeNumberMccMncResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = main_models.DescribeNumberMccMncResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNumberMccMncResponseBodyData(DaraModel):
    def __init__(
        self,
        country_iso_3: str = None,
        mcc: str = None,
        mnc: str = None,
        ported: bool = None,
    ):
        self.country_iso_3 = country_iso_3
        self.mcc = mcc
        self.mnc = mnc
        self.ported = ported

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.country_iso_3 is not None:
            result['CountryIso3'] = self.country_iso_3

        if self.mcc is not None:
            result['Mcc'] = self.mcc

        if self.mnc is not None:
            result['Mnc'] = self.mnc

        if self.ported is not None:
            result['Ported'] = self.ported

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountryIso3') is not None:
            self.country_iso_3 = m.get('CountryIso3')

        if m.get('Mcc') is not None:
            self.mcc = m.get('Mcc')

        if m.get('Mnc') is not None:
            self.mnc = m.get('Mnc')

        if m.get('Ported') is not None:
            self.ported = m.get('Ported')

        return self

