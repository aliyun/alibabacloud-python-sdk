# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyGtmConfigRequest(DaraModel):
    def __init__(
        self,
        copy_type: str = None,
        lang: str = None,
        source_id: str = None,
        target_id: str = None,
    ):
        # The type of the object that is copied. Only the INSTANCE type is supported.
        # 
        # This parameter is required.
        self.copy_type = copy_type
        # The language.
        self.lang = lang
        # The ID of the source object. Only instance IDs are supported.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The ID of the target object. Only instance IDs are supported.
        # 
        # This parameter is required.
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copy_type is not None:
            result['CopyType'] = self.copy_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopyType') is not None:
            self.copy_type = m.get('CopyType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        return self

