# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateApplicationEnvironmentVariablesResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        restarted: bool = None,
        total_variables: int = None,
        updated_keys: List[str] = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The response message.
        self.message = message
        # Indicates whether the operation succeeded.
        self.ok = ok
        # The request ID.
        self.request_id = request_id
        # Indicates whether the gateway was restarted.
        self.restarted = restarted
        # The total number of environment variables for the application after the update.
        self.total_variables = total_variables
        # A list of the environment variable names that were added or updated.
        self.updated_keys = updated_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restarted is not None:
            result['Restarted'] = self.restarted

        if self.total_variables is not None:
            result['TotalVariables'] = self.total_variables

        if self.updated_keys is not None:
            result['UpdatedKeys'] = self.updated_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Restarted') is not None:
            self.restarted = m.get('Restarted')

        if m.get('TotalVariables') is not None:
            self.total_variables = m.get('TotalVariables')

        if m.get('UpdatedKeys') is not None:
            self.updated_keys = m.get('UpdatedKeys')

        return self

