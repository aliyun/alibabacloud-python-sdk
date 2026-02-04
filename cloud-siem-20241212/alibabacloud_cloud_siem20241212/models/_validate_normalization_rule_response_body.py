# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ValidateNormalizationRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        validate_result: List[main_models.ValidateNormalizationRuleResponseBodyValidateResult] = None,
    ):
        self.request_id = request_id
        self.validate_result = validate_result

    def validate(self):
        if self.validate_result:
            for v1 in self.validate_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ValidateResult'] = []
        if self.validate_result is not None:
            for k1 in self.validate_result:
                result['ValidateResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.validate_result = []
        if m.get('ValidateResult') is not None:
            for k1 in m.get('ValidateResult'):
                temp_model = main_models.ValidateNormalizationRuleResponseBodyValidateResult()
                self.validate_result.append(temp_model.from_map(k1))

        return self

class ValidateNormalizationRuleResponseBodyValidateResult(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
        log_field_name: str = None,
        log_field_value: str = None,
        message: str = None,
        normalization_field_from: str = None,
        normalization_field_name: str = None,
        normalization_field_required: bool = None,
        normalization_field_reserved: bool = None,
        normalization_field_type: str = None,
        normalization_field_validation_reason: str = None,
        normalization_field_validation_status: str = None,
        result: int = None,
    ):
        self.field_name = field_name
        self.field_value = field_value
        self.log_field_name = log_field_name
        self.log_field_value = log_field_value
        self.message = message
        self.normalization_field_from = normalization_field_from
        self.normalization_field_name = normalization_field_name
        self.normalization_field_required = normalization_field_required
        self.normalization_field_reserved = normalization_field_reserved
        self.normalization_field_type = normalization_field_type
        self.normalization_field_validation_reason = normalization_field_validation_reason
        self.normalization_field_validation_status = normalization_field_validation_status
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        if self.log_field_name is not None:
            result['LogFieldName'] = self.log_field_name

        if self.log_field_value is not None:
            result['LogFieldValue'] = self.log_field_value

        if self.message is not None:
            result['Message'] = self.message

        if self.normalization_field_from is not None:
            result['NormalizationFieldFrom'] = self.normalization_field_from

        if self.normalization_field_name is not None:
            result['NormalizationFieldName'] = self.normalization_field_name

        if self.normalization_field_required is not None:
            result['NormalizationFieldRequired'] = self.normalization_field_required

        if self.normalization_field_reserved is not None:
            result['NormalizationFieldReserved'] = self.normalization_field_reserved

        if self.normalization_field_type is not None:
            result['NormalizationFieldType'] = self.normalization_field_type

        if self.normalization_field_validation_reason is not None:
            result['NormalizationFieldValidationReason'] = self.normalization_field_validation_reason

        if self.normalization_field_validation_status is not None:
            result['NormalizationFieldValidationStatus'] = self.normalization_field_validation_status

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        if m.get('LogFieldName') is not None:
            self.log_field_name = m.get('LogFieldName')

        if m.get('LogFieldValue') is not None:
            self.log_field_value = m.get('LogFieldValue')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NormalizationFieldFrom') is not None:
            self.normalization_field_from = m.get('NormalizationFieldFrom')

        if m.get('NormalizationFieldName') is not None:
            self.normalization_field_name = m.get('NormalizationFieldName')

        if m.get('NormalizationFieldRequired') is not None:
            self.normalization_field_required = m.get('NormalizationFieldRequired')

        if m.get('NormalizationFieldReserved') is not None:
            self.normalization_field_reserved = m.get('NormalizationFieldReserved')

        if m.get('NormalizationFieldType') is not None:
            self.normalization_field_type = m.get('NormalizationFieldType')

        if m.get('NormalizationFieldValidationReason') is not None:
            self.normalization_field_validation_reason = m.get('NormalizationFieldValidationReason')

        if m.get('NormalizationFieldValidationStatus') is not None:
            self.normalization_field_validation_status = m.get('NormalizationFieldValidationStatus')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

