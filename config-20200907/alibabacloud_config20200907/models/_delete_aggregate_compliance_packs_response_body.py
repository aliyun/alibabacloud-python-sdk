# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class DeleteAggregateCompliancePacksResponseBody(DaraModel):
    def __init__(
        self,
        operate_compliance_packs_result: main_models.DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResult = None,
        request_id: str = None,
    ):
        # The results of the delete operations.
        self.operate_compliance_packs_result = operate_compliance_packs_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.operate_compliance_packs_result:
            self.operate_compliance_packs_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_compliance_packs_result is not None:
            result['OperateCompliancePacksResult'] = self.operate_compliance_packs_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateCompliancePacksResult') is not None:
            temp_model = main_models.DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResult()
            self.operate_compliance_packs_result = temp_model.from_map(m.get('OperateCompliancePacksResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResult(DaraModel):
    def __init__(
        self,
        operate_compliance_packs: List[main_models.DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks] = None,
    ):
        # An array that contains the deleted compliance packages.
        self.operate_compliance_packs = operate_compliance_packs

    def validate(self):
        if self.operate_compliance_packs:
            for v1 in self.operate_compliance_packs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OperateCompliancePacks'] = []
        if self.operate_compliance_packs is not None:
            for k1 in self.operate_compliance_packs:
                result['OperateCompliancePacks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operate_compliance_packs = []
        if m.get('OperateCompliancePacks') is not None:
            for k1 in m.get('OperateCompliancePacks'):
                temp_model = main_models.DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks()
                self.operate_compliance_packs.append(temp_model.from_map(k1))

        return self

class DeleteAggregateCompliancePacksResponseBodyOperateCompliancePacksResultOperateCompliancePacks(DaraModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        error_code: str = None,
        success: bool = None,
    ):
        # The ID of the compliance package.
        self.compliance_pack_id = compliance_pack_id
        # The error code returned.
        # 
        # *   If the compliance package is deleted, no error code is returned.
        # *   If the compliance package fails to be deleted, an error code is returned. For more information about error codes, see [Error codes](https://error-center.alibabacloud.com/status/product/Config).
        self.error_code = error_code
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

