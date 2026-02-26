# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Row(DaraModel):
    def __init__(
        self,
        custom_labels: List[main_models.KeyValuePair] = None,
        uri: str = None,
    ):
        # The custom labels.
        self.custom_labels = custom_labels
        # The OSS URI of the file.
        # 
        # The OSS URI is in the `oss://${bucketname}/${objectname}` format, where `${bucketname}` is the name of the OSS bucket that is in the same region as the current project and `${objectname}` is the path of the file.
        self.uri = uri

    def validate(self):
        if self.custom_labels:
            for v1 in self.custom_labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomLabels'] = []
        if self.custom_labels is not None:
            for k1 in self.custom_labels:
                result['CustomLabels'].append(k1.to_map() if k1 else None)

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_labels = []
        if m.get('CustomLabels') is not None:
            for k1 in m.get('CustomLabels'):
                temp_model = main_models.KeyValuePair()
                self.custom_labels.append(temp_model.from_map(k1))

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

