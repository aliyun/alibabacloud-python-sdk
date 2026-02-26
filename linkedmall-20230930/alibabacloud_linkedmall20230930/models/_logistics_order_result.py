# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class LogisticsOrderResult(DaraModel):
    def __init__(
        self,
        data_provider: str = None,
        data_provider_title: str = None,
        goods: List[main_models.Good] = None,
        logistics_company_code: str = None,
        logistics_company_name: str = None,
        logistics_detail_list: List[main_models.LogisticsDetail] = None,
        mail_no: str = None,
    ):
        self.data_provider = data_provider
        self.data_provider_title = data_provider_title
        self.goods = goods
        self.logistics_company_code = logistics_company_code
        self.logistics_company_name = logistics_company_name
        self.logistics_detail_list = logistics_detail_list
        self.mail_no = mail_no

    def validate(self):
        if self.goods:
            for v1 in self.goods:
                 if v1:
                    v1.validate()
        if self.logistics_detail_list:
            for v1 in self.logistics_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_provider is not None:
            result['dataProvider'] = self.data_provider

        if self.data_provider_title is not None:
            result['dataProviderTitle'] = self.data_provider_title

        result['goods'] = []
        if self.goods is not None:
            for k1 in self.goods:
                result['goods'].append(k1.to_map() if k1 else None)

        if self.logistics_company_code is not None:
            result['logisticsCompanyCode'] = self.logistics_company_code

        if self.logistics_company_name is not None:
            result['logisticsCompanyName'] = self.logistics_company_name

        result['logisticsDetailList'] = []
        if self.logistics_detail_list is not None:
            for k1 in self.logistics_detail_list:
                result['logisticsDetailList'].append(k1.to_map() if k1 else None)

        if self.mail_no is not None:
            result['mailNo'] = self.mail_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataProvider') is not None:
            self.data_provider = m.get('dataProvider')

        if m.get('dataProviderTitle') is not None:
            self.data_provider_title = m.get('dataProviderTitle')

        self.goods = []
        if m.get('goods') is not None:
            for k1 in m.get('goods'):
                temp_model = main_models.Good()
                self.goods.append(temp_model.from_map(k1))

        if m.get('logisticsCompanyCode') is not None:
            self.logistics_company_code = m.get('logisticsCompanyCode')

        if m.get('logisticsCompanyName') is not None:
            self.logistics_company_name = m.get('logisticsCompanyName')

        self.logistics_detail_list = []
        if m.get('logisticsDetailList') is not None:
            for k1 in m.get('logisticsDetailList'):
                temp_model = main_models.LogisticsDetail()
                self.logistics_detail_list.append(temp_model.from_map(k1))

        if m.get('mailNo') is not None:
            self.mail_no = m.get('mailNo')

        return self

