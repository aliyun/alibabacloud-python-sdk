# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ImportKeyPairResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ImportKeyPairResponseBodyData = None,
        request_id: str = None,
    ):
        # The object that is returned.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ImportKeyPairResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ImportKeyPairResponseBodyData(DaraModel):
    def __init__(
        self,
        gmt_created: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
    ):
        # The time when the ADB key pair was created.
        self.gmt_created = gmt_created
        # The ID of the ADB key pair.
        self.key_pair_id = key_pair_id
        # The name of the ADB key pair.
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        return self

