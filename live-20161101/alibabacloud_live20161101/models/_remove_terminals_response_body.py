# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class RemoveTerminalsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        terminals: List[main_models.RemoveTerminalsResponseBodyTerminals] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the users.
        self.terminals = terminals

    def validate(self):
        if self.terminals:
            for v1 in self.terminals:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Terminals'] = []
        if self.terminals is not None:
            for k1 in self.terminals:
                result['Terminals'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.terminals = []
        if m.get('Terminals') is not None:
            for k1 in m.get('Terminals'):
                temp_model = main_models.RemoveTerminalsResponseBodyTerminals()
                self.terminals.append(temp_model.from_map(k1))

        return self

class RemoveTerminalsResponseBodyTerminals(DaraModel):
    def __init__(
        self,
        code: int = None,
        id: str = None,
        message: str = None,
    ):
        # The returned status code. A value of 0 indicates that the request is successful. If the request fails, an error message is returned.
        self.code = code
        # The ID of the user.
        self.id = id
        # The result of removing the specified users from the channel. Valid values:
        # 
        # *   Success
        # *   Failed
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

