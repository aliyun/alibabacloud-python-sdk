# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DatasetFileMetaResponse(DaraModel):
    def __init__(
        self,
        dataset_file_meta_id: str = None,
        result: str = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.dataset_file_meta_id = dataset_file_meta_id
        # This parameter is required.
        self.result = result
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_file_meta_id is not None:
            result['DatasetFileMetaId'] = self.dataset_file_meta_id

        if self.result is not None:
            result['Result'] = self.result

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetFileMetaId') is not None:
            self.dataset_file_meta_id = m.get('DatasetFileMetaId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

