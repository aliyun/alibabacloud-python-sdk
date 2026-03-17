# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ListDpiConfigErrorResponseBody(DaraModel):
    def __init__(
        self,
        dpi_config_error: List[main_models.ListDpiConfigErrorResponseBodyDpiConfigError] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The information about the configuration errors.
        self.dpi_config_error = dpi_config_error
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The token that was used to query the next page.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.dpi_config_error:
            for v1 in self.dpi_config_error:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DpiConfigError'] = []
        if self.dpi_config_error is not None:
            for k1 in self.dpi_config_error:
                result['DpiConfigError'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dpi_config_error = []
        if m.get('DpiConfigError') is not None:
            for k1 in m.get('DpiConfigError'):
                temp_model = main_models.ListDpiConfigErrorResponseBodyDpiConfigError()
                self.dpi_config_error.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListDpiConfigErrorResponseBodyDpiConfigError(DaraModel):
    def __init__(
        self,
        error_type: str = None,
        rule_config_error_list: List[main_models.ListDpiConfigErrorResponseBodyDpiConfigErrorRuleConfigErrorList] = None,
        sn: str = None,
        smart_agid: str = None,
    ):
        # The type of the configuration error. Valid values:
        # 
        # *   **DeviceNotSupported**: The SAG instance does not support the DPI feature.
        # *   **VersionNotSupported**: The version of the DPI feature is outdated.
        # *   **NotEnable**: The DPI feature is disabled on the SAG instance.
        self.error_type = error_type
        # The information about the configuration errors.
        self.rule_config_error_list = rule_config_error_list
        # The serial number of the SAG instance.
        self.sn = sn
        # The ID of the SAG instance.
        self.smart_agid = smart_agid

    def validate(self):
        if self.rule_config_error_list:
            for v1 in self.rule_config_error_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_type is not None:
            result['ErrorType'] = self.error_type

        result['RuleConfigErrorList'] = []
        if self.rule_config_error_list is not None:
            for k1 in self.rule_config_error_list:
                result['RuleConfigErrorList'].append(k1.to_map() if k1 else None)

        if self.sn is not None:
            result['SN'] = self.sn

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')

        self.rule_config_error_list = []
        if m.get('RuleConfigErrorList') is not None:
            for k1 in m.get('RuleConfigErrorList'):
                temp_model = main_models.ListDpiConfigErrorResponseBodyDpiConfigErrorRuleConfigErrorList()
                self.rule_config_error_list.append(temp_model.from_map(k1))

        if m.get('SN') is not None:
            self.sn = m.get('SN')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

class ListDpiConfigErrorResponseBodyDpiConfigErrorRuleConfigErrorList(DaraModel):
    def __init__(
        self,
        dpi_group_ids: List[str] = None,
        dpi_signature_ids: List[str] = None,
        rule_id: str = None,
    ):
        # The IDs of the application groups that have configuration errors.
        # 
        # You can call the [ListDpiGroups](https://help.aliyun.com/document_detail/196754.html) operation to query application group IDs and information about the applications.
        self.dpi_group_ids = dpi_group_ids
        # The IDs of applications that have configuration errors.
        # 
        # You can call the [ListDpiSignatures](https://help.aliyun.com/document_detail/196630.html) operation to query application IDs and information about the applications.
        self.dpi_signature_ids = dpi_signature_ids
        # The IDs of rules that are applied to applications with configuration errors.
        # 
        # *   If you make the request to query configuration errors of ACLs, the IDs of ACL rules that have configuration errors are returned.
        # *   If you make the request to query configuration errors of QoS polices, the IDs of the 5-tuples in the QoS polices that have configuration errors are returned.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_group_ids is not None:
            result['DpiGroupIds'] = self.dpi_group_ids

        if self.dpi_signature_ids is not None:
            result['DpiSignatureIds'] = self.dpi_signature_ids

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiGroupIds') is not None:
            self.dpi_group_ids = m.get('DpiGroupIds')

        if m.get('DpiSignatureIds') is not None:
            self.dpi_signature_ids = m.get('DpiSignatureIds')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

