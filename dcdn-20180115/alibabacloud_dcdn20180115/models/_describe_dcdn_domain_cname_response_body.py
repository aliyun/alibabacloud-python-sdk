# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainCnameResponseBody(DaraModel):
    def __init__(
        self,
        cname_datas: main_models.DescribeDcdnDomainCnameResponseBodyCnameDatas = None,
        request_id: str = None,
    ):
        # The CNAME information.
        self.cname_datas = cname_datas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cname_datas:
            self.cname_datas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname_datas is not None:
            result['CnameDatas'] = self.cname_datas.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnameDatas') is not None:
            temp_model = main_models.DescribeDcdnDomainCnameResponseBodyCnameDatas()
            self.cname_datas = temp_model.from_map(m.get('CnameDatas'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnDomainCnameResponseBodyCnameDatas(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeDcdnDomainCnameResponseBodyCnameDatasData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeDcdnDomainCnameResponseBodyCnameDatasData()
                self.data.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainCnameResponseBodyCnameDatasData(DaraModel):
    def __init__(
        self,
        cname: str = None,
        domain: str = None,
        err_msg: str = None,
        passed: str = None,
        status: int = None,
    ):
        # The CNAME assigned to the domain name.
        self.cname = cname
        # The accelerated domain name.
        self.domain = domain
        self.err_msg = err_msg
        self.passed = passed
        # The configuration status of the CNAME record. If the operation returns 0 for the parameter, the configuration was successful. Otherwise, the configuration failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

