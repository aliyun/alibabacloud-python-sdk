# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetEncryptionConfigResponseBody(DaraModel):
    def __init__(
        self,
        config: main_models.GetEncryptionConfigResponseBodyConfig = None,
        request_id: str = None,
    ):
        # The object key.
        self.config = config
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.GetEncryptionConfigResponseBodyConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetEncryptionConfigResponseBodyConfig(DaraModel):
    def __init__(
        self,
        alias: str = None,
        creator: str = None,
        key_arn: str = None,
        key_id: str = None,
        status: str = None,
    ):
        # The key alias.
        self.alias = alias
        # The creator ID.
        self.creator = creator
        # The key ARN.
        self.key_arn = key_arn
        # The key ID.
        self.key_id = key_id
        # The key status. Valid values:
        # - Enabled
        # - Disabled
        # - PendingDeletion
        # - PendingImport
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.creator is not None:
            result['creator'] = self.creator

        if self.key_arn is not None:
            result['keyArn'] = self.key_arn

        if self.key_id is not None:
            result['keyId'] = self.key_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('keyArn') is not None:
            self.key_arn = m.get('keyArn')

        if m.get('keyId') is not None:
            self.key_id = m.get('keyId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

