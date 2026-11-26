# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AICoachScriptHotWordItem(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        creator_name: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hot_word: str = None,
        hot_word_id: str = None,
        modifier_id: str = None,
        modifier_name: str = None,
        script_record_id: str = None,
    ):
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.description = description
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hot_word = hot_word
        self.hot_word_id = hot_word_id
        self.modifier_id = modifier_id
        self.modifier_name = modifier_name
        self.script_record_id = script_record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.hot_word is not None:
            result['hotWord'] = self.hot_word

        if self.hot_word_id is not None:
            result['hotWordId'] = self.hot_word_id

        if self.modifier_id is not None:
            result['modifierId'] = self.modifier_id

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('hotWord') is not None:
            self.hot_word = m.get('hotWord')

        if m.get('hotWordId') is not None:
            self.hot_word_id = m.get('hotWordId')

        if m.get('modifierId') is not None:
            self.modifier_id = m.get('modifierId')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        return self

