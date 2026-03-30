# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportVocabularyRequest(DaraModel):
    def __init__(
        self,
        file_key: str = None,
        instance_id: str = None,
    ):
        self.file_key = file_key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

