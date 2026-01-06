# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class AddImageLabelsRequest(DaraModel):
    def __init__(
        self,
        labels: List[main_models.AddImageLabelsRequestLabels] = None,
    ):
        # The list of image tags.
        # 
        # This parameter is required.
        self.labels = labels

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.AddImageLabelsRequestLabels()
                self.labels.append(temp_model.from_map(k1))

        return self

class AddImageLabelsRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The following keys can be added:
        # 
        # *   system.chipType
        # *   system.dsw.cudaVersion
        # *   system.dsw.fromImageId
        # *   system.dsw.fromInstanceId
        # *   system.dsw.id
        # *   system.dsw.os
        # *   system.dsw.osVersion
        # *   system.dsw.resourceType
        # *   system.dsw.rootImageId
        # *   system.dsw.stage
        # *   system.dsw.tag
        # *   system.dsw.type
        # *   system.framework
        # *   system.origin
        # *   system.pythonVersion
        # *   system.source
        # *   system.supported.dlc
        # *   system.supported.dsw
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

