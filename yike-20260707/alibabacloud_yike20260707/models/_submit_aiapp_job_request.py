# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAIAppJobRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        inputs: str = None,
        user_data: str = None,
    ):
        # The template ID.
        self.app_id = app_id
        # Ensures the idempotence of the request. Generate a parameter value from your client to ensure that the value is unique across different requests. The ClientToken parameter supports only ASCII characters and can be up to 64 characters in length.
        self.client_token = client_token
        # The task inputs.
        self.inputs = inputs
        # The custom fields.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.inputs is not None:
            result['Inputs'] = self.inputs

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

