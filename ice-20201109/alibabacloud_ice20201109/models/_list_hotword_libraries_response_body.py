# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListHotwordLibrariesResponseBody(DaraModel):
    def __init__(
        self,
        hotword_library_list: List[main_models.ListHotwordLibrariesResponseBodyHotwordLibraryList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The hotword libraries.
        self.hotword_library_list = hotword_library_list
        # The maximum number of hotword libraries that can be returned.
        self.max_results = max_results
        # A pagination token that can be used in the next request to retrieve a new page of results. If it is empty, all results are returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of hotword libraries.
        self.total_count = total_count

    def validate(self):
        if self.hotword_library_list:
            for v1 in self.hotword_library_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HotwordLibraryList'] = []
        if self.hotword_library_list is not None:
            for k1 in self.hotword_library_list:
                result['HotwordLibraryList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hotword_library_list = []
        if m.get('HotwordLibraryList') is not None:
            for k1 in m.get('HotwordLibraryList'):
                temp_model = main_models.ListHotwordLibrariesResponseBodyHotwordLibraryList()
                self.hotword_library_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHotwordLibrariesResponseBodyHotwordLibraryList(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        hotword_library_id: str = None,
        modified_time: str = None,
        name: str = None,
        usage_scenario: str = None,
    ):
        # The time when the hotword library was created.
        self.creation_time = creation_time
        # The description of the hotword library. It can be up to 200 characters in length.
        self.description = description
        # The ID of the hotword library.
        self.hotword_library_id = hotword_library_id
        # The time when the hotword library was last modified.
        self.modified_time = modified_time
        # The name of the hotword library.
        self.name = name
        # The usage scenario of the hotword library. Valid values:
        # 
        # *   ASR: Automatic Speech Recognition
        # *   StructuredMediaAssets: structured media analysis
        # *   VideoTranslation: Video translation This field cannot be modified after the hotword library is created.
        self.usage_scenario = usage_scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.hotword_library_id is not None:
            result['HotwordLibraryId'] = self.hotword_library_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.usage_scenario is not None:
            result['UsageScenario'] = self.usage_scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HotwordLibraryId') is not None:
            self.hotword_library_id = m.get('HotwordLibraryId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UsageScenario') is not None:
            self.usage_scenario = m.get('UsageScenario')

        return self

