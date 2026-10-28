# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListInstanceCatalogRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        only_custom: bool = None,
        region_id: str = None,
        requirement_ids: List[int] = None,
        standard_ids: List[int] = None,
        task_sources: List[str] = None,
        types: List[str] = None,
    ):
        # The language type of the request and response messages. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # Specifies whether to filter assets that support custom checks. Valid values:
        # 
        # - **true**: Filters assets that support custom checks.
        # - **false**: All check assets. This is the default value.
        self.only_custom = only_custom
        # The ID of the region where the instance to be queried is located. Valid values:
        # 
        # - **cn-hangzhou**: Center.
        # - **ap-southeast-1**: Singapore.
        self.region_id = region_id
        # The list of requirement IDs.
        self.requirement_ids = requirement_ids
        # The list of standard IDs.
        self.standard_ids = standard_ids
        # The list of task sources.
        self.task_sources = task_sources
        # The list of types to which the check standards belong.
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.only_custom is not None:
            result['OnlyCustom'] = self.only_custom

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.requirement_ids is not None:
            result['RequirementIds'] = self.requirement_ids

        if self.standard_ids is not None:
            result['StandardIds'] = self.standard_ids

        if self.task_sources is not None:
            result['TaskSources'] = self.task_sources

        if self.types is not None:
            result['Types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OnlyCustom') is not None:
            self.only_custom = m.get('OnlyCustom')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequirementIds') is not None:
            self.requirement_ids = m.get('RequirementIds')

        if m.get('StandardIds') is not None:
            self.standard_ids = m.get('StandardIds')

        if m.get('TaskSources') is not None:
            self.task_sources = m.get('TaskSources')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

