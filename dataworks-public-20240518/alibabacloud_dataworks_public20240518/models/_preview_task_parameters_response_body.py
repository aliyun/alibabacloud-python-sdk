# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class PreviewTaskParametersResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.PreviewTaskParametersResponseBodyItems] = None,
        request_id: str = None,
    ):
        # The parameter preview results for each cycle.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.PreviewTaskParametersResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PreviewTaskParametersResponseBodyItems(DaraModel):
    def __init__(
        self,
        bizdate: int = None,
        error_message: str = None,
        parameters: str = None,
        success: bool = None,
        trigger_time: int = None,
    ):
        # The business date of the cycle. The value is a 13-digit UNIX timestamp in milliseconds.
        self.bizdate = bizdate
        # The error message returned when the parsing for the cycle fails. This parameter is returned when Success is false and is not returned when Success is true.
        self.error_message = error_message
        # The complete script parameter string parsed for the cycle. Multiple parameters are separated by spaces. This parameter is returned when Success is true.
        self.parameters = parameters
        # Specifies whether the scheduling parameters for the cycle are parsed successfully. Valid values:
        # - true: The parsing is successful.
        # - false: The parsing fails.
        self.success = success
        # The simulated scheduled trigger time. The value is a 13-digit UNIX timestamp in milliseconds.
        self.trigger_time = trigger_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.success is not None:
            result['Success'] = self.success

        if self.trigger_time is not None:
            result['TriggerTime'] = self.trigger_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TriggerTime') is not None:
            self.trigger_time = m.get('TriggerTime')

        return self

