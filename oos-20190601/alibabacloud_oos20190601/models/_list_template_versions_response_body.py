# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListTemplateVersionsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        template_versions: List[main_models.ListTemplateVersionsResponseBodyTemplateVersions] = None,
    ):
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The versions of the template.
        self.template_versions = template_versions

    def validate(self):
        if self.template_versions:
            for v1 in self.template_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TemplateVersions'] = []
        if self.template_versions is not None:
            for k1 in self.template_versions:
                result['TemplateVersions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.template_versions = []
        if m.get('TemplateVersions') is not None:
            for k1 in m.get('TemplateVersions'):
                temp_model = main_models.ListTemplateVersionsResponseBodyTemplateVersions()
                self.template_versions.append(temp_model.from_map(k1))

        return self

class ListTemplateVersionsResponseBodyTemplateVersions(DaraModel):
    def __init__(
        self,
        description: str = None,
        template_format: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
        version_name: str = None,
    ):
        # The description of the version.
        self.description = description
        # The format of the template content. Valid values: YAML and JSON.
        self.template_format = template_format
        # The number of the version.
        self.template_version = template_version
        # The user who last updated the version.
        self.updated_by = updated_by
        # The time when the version was last updated.
        self.updated_date = updated_date
        # The name of the version.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by

        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

