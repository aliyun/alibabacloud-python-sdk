# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class SimilarImageCluster(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        custom_labels: Dict[str, Any] = None,
        files: List[main_models.SimilarImage] = None,
        object_id: str = None,
        update_time: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The custom tag.
        self.custom_labels = custom_labels
        # The similar images.
        self.files = files
        # The ID of the cluster.
        self.object_id = object_id
        # The time when the cluster was updated.
        self.update_time = update_time

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_labels is not None:
            result['CustomLabels'] = self.custom_labels

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomLabels') is not None:
            self.custom_labels = m.get('CustomLabels')

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.SimilarImage()
                self.files.append(temp_model.from_map(k1))

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

