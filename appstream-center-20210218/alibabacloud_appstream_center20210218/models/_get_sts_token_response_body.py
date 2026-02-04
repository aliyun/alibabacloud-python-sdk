# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210218 import models as main_models
from darabonba.model import DaraModel

class GetStsTokenResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sts_token_model: main_models.GetStsTokenResponseBodyStsTokenModel = None,
    ):
        self.request_id = request_id
        self.sts_token_model = sts_token_model

    def validate(self):
        if self.sts_token_model:
            self.sts_token_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sts_token_model is not None:
            result['StsTokenModel'] = self.sts_token_model.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StsTokenModel') is not None:
            temp_model = main_models.GetStsTokenResponseBodyStsTokenModel()
            self.sts_token_model = temp_model.from_map(m.get('StsTokenModel'))

        return self

class GetStsTokenResponseBodyStsTokenModel(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        session_id: str = None,
        sts_token: str = None,
        tenant_id: int = None,
    ):
        self.ali_uid = ali_uid
        self.session_id = session_id
        self.sts_token = sts_token
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.sts_token is not None:
            result['StsToken'] = self.sts_token

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

