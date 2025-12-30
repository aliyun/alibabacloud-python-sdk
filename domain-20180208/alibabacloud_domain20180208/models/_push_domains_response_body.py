# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class PushDomainsResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.PushDomainsResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            temp_model = main_models.PushDomainsResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PushDomainsResponseBodyModule(DaraModel):
    def __init__(
        self,
        failed_results: List[main_models.PushDomainsResponseBodyModuleFailedResults] = None,
        out_biz_id: str = None,
        push_no: str = None,
        success: bool = None,
        success_domains: List[str] = None,
    ):
        self.failed_results = failed_results
        self.out_biz_id = out_biz_id
        self.push_no = push_no
        self.success = success
        self.success_domains = success_domains

    def validate(self):
        if self.failed_results:
            for v1 in self.failed_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedResults'] = []
        if self.failed_results is not None:
            for k1 in self.failed_results:
                result['FailedResults'].append(k1.to_map() if k1 else None)

        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.push_no is not None:
            result['PushNo'] = self.push_no

        if self.success is not None:
            result['Success'] = self.success

        if self.success_domains is not None:
            result['SuccessDomains'] = self.success_domains

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_results = []
        if m.get('FailedResults') is not None:
            for k1 in m.get('FailedResults'):
                temp_model = main_models.PushDomainsResponseBodyModuleFailedResults()
                self.failed_results.append(temp_model.from_map(k1))

        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('PushNo') is not None:
            self.push_no = m.get('PushNo')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('SuccessDomains') is not None:
            self.success_domains = m.get('SuccessDomains')

        return self

class PushDomainsResponseBodyModuleFailedResults(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        error_code: str = None,
        error_msg: str = None,
    ):
        self.domain_name = domain_name
        self.error_code = error_code
        self.error_msg = error_msg

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        return self

