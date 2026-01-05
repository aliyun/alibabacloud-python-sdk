# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateIdentifyCredentialRequest(DaraModel):
    def __init__(
        self,
        identify_credential: main_models.IdentifyCredential = None,
    ):
        # The user credential object.
        self.identify_credential = identify_credential

    def validate(self):
        if self.identify_credential:
            self.identify_credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identify_credential is not None:
            result['IdentifyCredential'] = self.identify_credential.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyCredential') is not None:
            temp_model = main_models.IdentifyCredential()
            self.identify_credential = temp_model.from_map(m.get('IdentifyCredential'))

        return self

