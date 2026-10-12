# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListImagesShrinkRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        name: str = None,
        official: bool = None,
        page_number: int = None,
        page_size: int = None,
        project_ids_shrink: str = None,
        provider_types_shrink: str = None,
        search_all: bool = None,
        sort_by: str = None,
        stages_shrink: str = None,
        statuses_shrink: str = None,
        supported_modules_shrink: str = None,
        supported_task_types_shrink: str = None,
    ):
        # The accessibility of the image. Valid values:
        # - Public: The image is visible to all users.
        # - Private: The image is visible only to the creator.
        self.accessibility = accessibility
        # The image name used for fuzzy match.
        self.name = name
        # Specifies whether the image is an official image.
        self.official = official
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of workspace IDs.
        self.project_ids_shrink = project_ids_shrink
        # The list of image reference data types.
        self.provider_types_shrink = provider_types_shrink
        # Specifies whether to search for all images.
        self.search_all = search_all
        # The list of sort fields. Fields such as scheduled time and start time are supported. The format is "sort field + sort order (Desc/Asc)". Asc can be omitted. Valid values for sort fields:
        # - CreateTime (Desc/Asc): creation time.
        # - Name (Desc/Asc): image name.
        # Default value: CreateTime Asc.
        self.sort_by = sort_by
        # The list of image publishing stages to query.
        self.stages_shrink = stages_shrink
        # The list of image statuses to query.
        self.statuses_shrink = statuses_shrink
        # The list of supported modules.
        self.supported_modules_shrink = supported_modules_shrink
        # The list of supported task types.
        self.supported_task_types_shrink = supported_task_types_shrink

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

        if self.project_ids_shrink is not None:
            result['ProjectIds'] = self.project_ids_shrink

        if self.provider_types_shrink is not None:
            result['ProviderTypes'] = self.provider_types_shrink

        if self.search_all is not None:
            result['SearchAll'] = self.search_all

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.stages_shrink is not None:
            result['Stages'] = self.stages_shrink

        if self.statuses_shrink is not None:
            result['Statuses'] = self.statuses_shrink

        if self.supported_modules_shrink is not None:
            result['SupportedModules'] = self.supported_modules_shrink

        if self.supported_task_types_shrink is not None:
            result['SupportedTaskTypes'] = self.supported_task_types_shrink

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
            self.project_ids_shrink = m.get('ProjectIds')

        if m.get('ProviderTypes') is not None:
            self.provider_types_shrink = m.get('ProviderTypes')

        if m.get('SearchAll') is not None:
            self.search_all = m.get('SearchAll')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Stages') is not None:
            self.stages_shrink = m.get('Stages')

        if m.get('Statuses') is not None:
            self.statuses_shrink = m.get('Statuses')

        if m.get('SupportedModules') is not None:
            self.supported_modules_shrink = m.get('SupportedModules')

        if m.get('SupportedTaskTypes') is not None:
            self.supported_task_types_shrink = m.get('SupportedTaskTypes')

        return self

