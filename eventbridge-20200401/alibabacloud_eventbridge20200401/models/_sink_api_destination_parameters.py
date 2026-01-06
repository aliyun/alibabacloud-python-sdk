# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class SinkApiDestinationParameters(DaraModel):
    def __init__(
        self,
        body_parameters: main_models.SinkApiDestinationParametersBodyParameters = None,
        header_parameters: main_models.SinkApiDestinationParametersHeaderParameters = None,
        name: str = None,
        query_string_parameters: main_models.SinkApiDestinationParametersQueryStringParameters = None,
    ):
        self.body_parameters = body_parameters
        self.header_parameters = header_parameters
        self.name = name
        self.query_string_parameters = query_string_parameters

    def validate(self):
        if self.body_parameters:
            self.body_parameters.validate()
        if self.header_parameters:
            self.header_parameters.validate()
        if self.query_string_parameters:
            self.query_string_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_parameters is not None:
            result['BodyParameters'] = self.body_parameters.to_map()

        if self.header_parameters is not None:
            result['HeaderParameters'] = self.header_parameters.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.query_string_parameters is not None:
            result['QueryStringParameters'] = self.query_string_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyParameters') is not None:
            temp_model = main_models.SinkApiDestinationParametersBodyParameters()
            self.body_parameters = temp_model.from_map(m.get('BodyParameters'))

        if m.get('HeaderParameters') is not None:
            temp_model = main_models.SinkApiDestinationParametersHeaderParameters()
            self.header_parameters = temp_model.from_map(m.get('HeaderParameters'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QueryStringParameters') is not None:
            temp_model = main_models.SinkApiDestinationParametersQueryStringParameters()
            self.query_string_parameters = temp_model.from_map(m.get('QueryStringParameters'))

        return self

class SinkApiDestinationParametersQueryStringParameters(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SinkApiDestinationParametersHeaderParameters(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SinkApiDestinationParametersBodyParameters(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

