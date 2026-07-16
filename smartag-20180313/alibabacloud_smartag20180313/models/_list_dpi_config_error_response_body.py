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
        # A list of DPI configuration errors.
        self.dpi_config_error = dpi_config_error
        # The maximum number of configuration errors to return on each page.
        self.max_results = max_results
        # The token for the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of DPI configuration errors.
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
        # The type of the configuration error.
        # 
        # - DeviceNotSupported: The Smart Access Gateway device does not support the DPI feature.
        # - VersionNotSupported: The DPI version of the Smart Access Gateway device is too old.
        # - **NotEnable**: The DPI feature is disabled for the Smart Access Gateway device.
        self.error_type = error_type
        # A list of rule configuration errors.
        self.rule_config_error_list = rule_config_error_list
        # The serial number of the Smart Access Gateway device.
        self.sn = sn
        # The ID of the Smart Access Gateway instance.
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
        # A list of IDs of application groups that have configuration errors.
        self.dpi_group_ids = dpi_group_ids
        # A list of IDs of applications that have configuration errors.
        self.dpi_signature_ids = dpi_signature_ids
        # The ID of the rule that is associated with the application that has a configuration error.
        # 
        # - If you query DPI configuration errors for Resource Access Management, this parameter indicates the ID of the Resource Access Management rule instance that has a configuration error.
        # - If you query DPI configuration errors for a QoS policy, this parameter indicates the ID of the quintuple rule instance that has a configuration error.
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

