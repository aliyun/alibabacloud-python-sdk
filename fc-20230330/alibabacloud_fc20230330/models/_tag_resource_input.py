# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class TagResourceInput(DaraModel):
    def __init__(
        self,
        resource_arn: str = None,
        tags: Dict[str, str] = None,
    ):
        # This parameter is required.
        self.resource_arn = resource_arn
        # This parameter is required.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

