# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ims20190815 import models as main_models
from darabonba.model import DaraModel

class ListPasskeysResponseBody(DaraModel):
    def __init__(
        self,
        passkeys: List[main_models.ListPasskeysResponseBodyPasskeys] = None,
        request_id: str = None,
    ):
        # The information about the passkeys.
        self.passkeys = passkeys
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.passkeys:
            for v1 in self.passkeys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Passkeys'] = []
        if self.passkeys is not None:
            for k1 in self.passkeys:
                result['Passkeys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.passkeys = []
        if m.get('Passkeys') is not None:
            for k1 in m.get('Passkeys'):
                temp_model = main_models.ListPasskeysResponseBodyPasskeys()
                self.passkeys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPasskeysResponseBodyPasskeys(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        last_use_date: str = None,
        passkey_id: str = None,
        passkey_name: str = None,
    ):
        # The time when the passkey was created. The value is a timestamp.
        self.create_date = create_date
        # The time when the passkey was last used. The value is a timestamp.
        self.last_use_date = last_use_date
        # The ID of the passkey.
        self.passkey_id = passkey_id
        # The name of the passkey.
        self.passkey_name = passkey_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.last_use_date is not None:
            result['LastUseDate'] = self.last_use_date

        if self.passkey_id is not None:
            result['PasskeyId'] = self.passkey_id

        if self.passkey_name is not None:
            result['PasskeyName'] = self.passkey_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('LastUseDate') is not None:
            self.last_use_date = m.get('LastUseDate')

        if m.get('PasskeyId') is not None:
            self.passkey_id = m.get('PasskeyId')

        if m.get('PasskeyName') is not None:
            self.passkey_name = m.get('PasskeyName')

        return self

