# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListImagesRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        name: str = None,
        official: bool = None,
        page_number: int = None,
        page_size: int = None,
        project_ids: List[int] = None,
        provider_types: List[str] = None,
        search_all: bool = None,
        sort_by: str = None,
        stages: List[str] = None,
        statuses: List[str] = None,
        supported_modules: List[str] = None,
        supported_task_types: List[str] = None,
    ):
        self.accessibility = accessibility
        self.name = name
        self.official = official
        self.page_number = page_number
        self.page_size = page_size
        self.project_ids = project_ids
        self.provider_types = provider_types
        self.search_all = search_all
        self.sort_by = sort_by
        self.stages = stages
        self.statuses = statuses
        self.supported_modules = supported_modules
        self.supported_task_types = supported_task_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.name is not None:
            result['Name'] = self.name

        if self.official is not None:
            result['Official'] = self.official

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.provider_types is not None:
            result['ProviderTypes'] = self.provider_types

        if self.search_all is not None:
            result['SearchAll'] = self.search_all

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.stages is not None:
            result['Stages'] = self.stages

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        if self.supported_modules is not None:
            result['SupportedModules'] = self.supported_modules

        if self.supported_task_types is not None:
            result['SupportedTaskTypes'] = self.supported_task_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Official') is not None:
            self.official = m.get('Official')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('ProviderTypes') is not None:
            self.provider_types = m.get('ProviderTypes')

        if m.get('SearchAll') is not None:
            self.search_all = m.get('SearchAll')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Stages') is not None:
            self.stages = m.get('Stages')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        if m.get('SupportedModules') is not None:
            self.supported_modules = m.get('SupportedModules')

        if m.get('SupportedTaskTypes') is not None:
            self.supported_task_types = m.get('SupportedTaskTypes')

        return self

