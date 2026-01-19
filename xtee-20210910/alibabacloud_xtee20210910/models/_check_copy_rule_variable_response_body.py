# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class CheckCopyRuleVariableResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.CheckCopyRuleVariableResponseBodyResultObject = None,
    ):
        # ID of the request
        self.request_id = request_id
        # Returned result information
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.CheckCopyRuleVariableResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class CheckCopyRuleVariableResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        message: List[main_models.CheckCopyRuleVariableResponseBodyResultObjectMessage] = None,
    ):
        # Information.
        self.message = message

    def validate(self):
        if self.message:
            for v1 in self.message:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Message'] = []
        if self.message is not None:
            for k1 in self.message:
                result['Message'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message = []
        if m.get('Message') is not None:
            for k1 in m.get('Message'):
                temp_model = main_models.CheckCopyRuleVariableResponseBodyResultObjectMessage()
                self.message.append(temp_model.from_map(k1))

        return self



class CheckCopyRuleVariableResponseBodyResultObjectMessage(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        title: str = None,
        type: str = None,
    ):
        # Primary key ID of the variable
        self.id = id
        # Name of the variable
        self.name = name
        # Title of the variable
        self.title = title
        # Type of the variable
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.title is not None:
            result['Title'] = self.title

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

