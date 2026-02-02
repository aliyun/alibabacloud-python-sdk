# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20221125 import models as main_models
from darabonba.model import DaraModel

class EntRiskQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.EntRiskQueryResponseBodyResult = None,
    ):
        # Error code. For details about error codes, see **[Error Codes](https://help.aliyun.com/document_detail/215420.html)**.
        self.code = code
        # Response message for the request information.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Result
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.EntRiskQueryResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class EntRiskQueryResponseBodyResult(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        risk_list: List[main_models.EntRiskQueryResponseBodyResultRiskList] = None,
        status: str = None,
    ):
        # Query result
        # 0: Normal business operation
        # 1: Abnormal business operation
        # 2: Not found
        self.biz_code = biz_code
        # List of abnormal information
        self.risk_list = risk_list
        # Business operation status.
        # - 1: In operation (open)
        # - 2: Relocated
        # - 3: Deregistered
        # - 4: Revoked
        # - 5: Canceled
        # - 6: Suspended
        # - 0: Other
        self.status = status

    def validate(self):
        if self.risk_list:
            for v1 in self.risk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        result['RiskList'] = []
        if self.risk_list is not None:
            for k1 in self.risk_list:
                result['RiskList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        self.risk_list = []
        if m.get('RiskList') is not None:
            for k1 in m.get('RiskList'):
                temp_model = main_models.EntRiskQueryResponseBodyResultRiskList()
                self.risk_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class EntRiskQueryResponseBodyResultRiskList(DaraModel):
    def __init__(
        self,
        credit_code: str = None,
        ent_name: str = None,
        listed_date: str = None,
        listed_reason: str = None,
        operation_org: str = None,
        reg_no: str = None,
        removed_date: str = None,
        removed_org: str = None,
        removed_reason: str = None,
    ):
        # Unified Social Credit Code
        self.credit_code = credit_code
        # Company name.
        self.ent_name = ent_name
        # Date listed as abnormal
        # Example: 2023-02-03
        self.listed_date = listed_date
        # Reason for being listed as abnormal
        self.listed_reason = listed_reason
        # Authority that handled the inclusion
        self.operation_org = operation_org
        # Business registration number
        self.reg_no = reg_no
        # Date removed from the abnormal list
        # Example: 2023-02-03
        self.removed_date = removed_date
        # Authority that handled the removal
        self.removed_org = removed_org
        # Reason for being removed from the abnormal list
        self.removed_reason = removed_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_code is not None:
            result['CreditCode'] = self.credit_code

        if self.ent_name is not None:
            result['EntName'] = self.ent_name

        if self.listed_date is not None:
            result['ListedDate'] = self.listed_date

        if self.listed_reason is not None:
            result['ListedReason'] = self.listed_reason

        if self.operation_org is not None:
            result['OperationOrg'] = self.operation_org

        if self.reg_no is not None:
            result['RegNo'] = self.reg_no

        if self.removed_date is not None:
            result['RemovedDate'] = self.removed_date

        if self.removed_org is not None:
            result['RemovedOrg'] = self.removed_org

        if self.removed_reason is not None:
            result['RemovedReason'] = self.removed_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditCode') is not None:
            self.credit_code = m.get('CreditCode')

        if m.get('EntName') is not None:
            self.ent_name = m.get('EntName')

        if m.get('ListedDate') is not None:
            self.listed_date = m.get('ListedDate')

        if m.get('ListedReason') is not None:
            self.listed_reason = m.get('ListedReason')

        if m.get('OperationOrg') is not None:
            self.operation_org = m.get('OperationOrg')

        if m.get('RegNo') is not None:
            self.reg_no = m.get('RegNo')

        if m.get('RemovedDate') is not None:
            self.removed_date = m.get('RemovedDate')

        if m.get('RemovedOrg') is not None:
            self.removed_org = m.get('RemovedOrg')

        if m.get('RemovedReason') is not None:
            self.removed_reason = m.get('RemovedReason')

        return self

