# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class BatchIntrudeDomainsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.BatchIntrudeDomainsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.BatchIntrudeDomainsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchIntrudeDomainsResponseBodyData(DaraModel):
    def __init__(
        self,
        failure_count: int = None,
        failure_list: List[main_models.BatchIntrudeDomainsResponseBodyDataFailureList] = None,
        success_count: int = None,
        success_list: List[main_models.BatchIntrudeDomainsResponseBodyDataSuccessList] = None,
    ):
        self.failure_count = failure_count
        self.failure_list = failure_list
        self.success_count = success_count
        self.success_list = success_list

    def validate(self):
        if self.failure_list:
            for v1 in self.failure_list:
                 if v1:
                    v1.validate()
        if self.success_list:
            for v1 in self.success_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count

        result['FailureList'] = []
        if self.failure_list is not None:
            for k1 in self.failure_list:
                result['FailureList'].append(k1.to_map() if k1 else None)

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        result['SuccessList'] = []
        if self.success_list is not None:
            for k1 in self.success_list:
                result['SuccessList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')

        self.failure_list = []
        if m.get('FailureList') is not None:
            for k1 in m.get('FailureList'):
                temp_model = main_models.BatchIntrudeDomainsResponseBodyDataFailureList()
                self.failure_list.append(temp_model.from_map(k1))

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        self.success_list = []
        if m.get('SuccessList') is not None:
            for k1 in m.get('SuccessList'):
                temp_model = main_models.BatchIntrudeDomainsResponseBodyDataSuccessList()
                self.success_list.append(temp_model.from_map(k1))

        return self

class BatchIntrudeDomainsResponseBodyDataSuccessList(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        self.domain_name = domain_name
        self.error_code = error_code
        self.error_msg = error_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class BatchIntrudeDomainsResponseBodyDataFailureList(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        error_code: str = None,
        error_msg: str = None,
        success: bool = None,
    ):
        self.domain_name = domain_name
        self.error_code = error_code
        self.error_msg = error_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

