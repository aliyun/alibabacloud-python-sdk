# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListEventMetaCacheAllKeysDataResult(DaraModel):
    def __init__(
        self,
        annotation: List[str] = None,
        label: List[str] = None,
        resource_tag: List[str] = None,
    ):
        # annotation类型的Key列表
        self.annotation = annotation
        # label类型的Key列表
        self.label = label
        # resource.tag类型的Key列表
        self.resource_tag = resource_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation is not None:
            result['annotation'] = self.annotation

        if self.label is not None:
            result['label'] = self.label

        if self.resource_tag is not None:
            result['resourceTag'] = self.resource_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotation') is not None:
            self.annotation = m.get('annotation')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('resourceTag') is not None:
            self.resource_tag = m.get('resourceTag')

        return self

