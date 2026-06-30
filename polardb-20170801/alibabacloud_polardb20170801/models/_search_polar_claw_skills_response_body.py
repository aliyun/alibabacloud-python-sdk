# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class SearchPolarClawSkillsResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
        results: List[main_models.SearchPolarClawSkillsResponseBodyResults] = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The list of search results.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.SearchPolarClawSkillsResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class SearchPolarClawSkillsResponseBodyResults(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        score: float = None,
        slug: str = None,
        summary: str = None,
        updated_at: int = None,
        version: str = None,
    ):
        # The display name.
        self.display_name = display_name
        # The relevance score.
        self.score = score
        # The skill identifier.
        self.slug = slug
        # The brief description.
        self.summary = summary
        # The UNIX timestamp of the last update, in seconds.
        self.updated_at = updated_at
        # The latest version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.score is not None:
            result['Score'] = self.score

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

