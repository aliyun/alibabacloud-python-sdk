# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ModifyAppGroupQuotaRequest(DaraModel):
    def __init__(
        self,
        body: main_models.Quota = None,
        client_token: str = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # A client token that is used to ensure the idempotence of the request. The client generates this value to make sure that it is unique among different requests. The value can be up to 64 ASCII characters in length.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Default value: false.
        # 
        # Valid values:
        # 
        # - **true**: Validates the request parameters without creating the attribution configuration.
        # 
        # - **false**: Validates the request parameters and creates the attribution configuration.
        self.dry_run = dry_run

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.Quota()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

