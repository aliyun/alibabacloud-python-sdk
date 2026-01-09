# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class S3IngestionConfiguration(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        source: main_models.S3IngestionConfigurationSource = None,
    ):
        self.logstore = logstore
        self.source = source

    def validate(self):
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.source is not None:
            result['source'] = self.source.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('source') is not None:
            temp_model = main_models.S3IngestionConfigurationSource()
            self.source = temp_model.from_map(m.get('source'))

        return self

