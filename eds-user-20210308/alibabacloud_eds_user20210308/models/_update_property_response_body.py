# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class UpdatePropertyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        update_result: main_models.UpdatePropertyResponseBodyUpdateResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The result of the modification.
        self.update_result = update_result

    def validate(self):
        if self.update_result:
            self.update_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.update_result is not None:
            result['UpdateResult'] = self.update_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpdateResult') is not None:
            temp_model = main_models.UpdatePropertyResponseBodyUpdateResult()
            self.update_result = temp_model.from_map(m.get('UpdateResult'))

        return self

class UpdatePropertyResponseBodyUpdateResult(DaraModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        save_property_value_model: main_models.UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel = None,
    ):
        # The ID of the property.
        self.property_id = property_id
        # The name of the property.
        self.property_key = property_key
        # The result of the property value modification.
        self.save_property_value_model = save_property_value_model

    def validate(self):
        if self.save_property_value_model:
            self.save_property_value_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_id is not None:
            result['PropertyId'] = self.property_id

        if self.property_key is not None:
            result['PropertyKey'] = self.property_key

        if self.save_property_value_model is not None:
            result['SavePropertyValueModel'] = self.save_property_value_model.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')

        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')

        if m.get('SavePropertyValueModel') is not None:
            temp_model = main_models.UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel()
            self.save_property_value_model = temp_model.from_map(m.get('SavePropertyValueModel'))

        return self

class UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel(DaraModel):
    def __init__(
        self,
        failed_property_values: List[main_models.UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues] = None,
        save_property_values: List[main_models.UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues] = None,
    ):
        # The property values that failed to be modified.
        self.failed_property_values = failed_property_values
        # The property values that were modified.
        self.save_property_values = save_property_values

    def validate(self):
        if self.failed_property_values:
            for v1 in self.failed_property_values:
                 if v1:
                    v1.validate()
        if self.save_property_values:
            for v1 in self.save_property_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedPropertyValues'] = []
        if self.failed_property_values is not None:
            for k1 in self.failed_property_values:
                result['FailedPropertyValues'].append(k1.to_map() if k1 else None)

        result['SavePropertyValues'] = []
        if self.save_property_values is not None:
            for k1 in self.save_property_values:
                result['SavePropertyValues'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_property_values = []
        if m.get('FailedPropertyValues') is not None:
            for k1 in m.get('FailedPropertyValues'):
                temp_model = main_models.UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues()
                self.failed_property_values.append(temp_model.from_map(k1))

        self.save_property_values = []
        if m.get('SavePropertyValues') is not None:
            for k1 in m.get('SavePropertyValues'):
                temp_model = main_models.UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues()
                self.save_property_values.append(temp_model.from_map(k1))

        return self

class UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues(DaraModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The value of the property.
        self.property_value = property_value
        # The ID of the property value.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')

        return self

class UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        property_id: int = None,
        property_value: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the property.
        self.property_id = property_id
        # The value of the property.
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.property_id is not None:
            result['PropertyId'] = self.property_id

        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')

        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        return self

