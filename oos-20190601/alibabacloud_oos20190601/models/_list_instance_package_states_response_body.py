# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListInstancePackageStatesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        package_states: List[main_models.ListInstancePackageStatesResponseBodyPackageStates] = None,
        request_id: str = None,
    ):
        # Page size.
        self.max_results = max_results
        # Token string for pagination.
        self.next_token = next_token
        # List of extensions
        self.package_states = package_states
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.package_states:
            for v1 in self.package_states:
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

        result['PackageStates'] = []
        if self.package_states is not None:
            for k1 in self.package_states:
                result['PackageStates'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.package_states = []
        if m.get('PackageStates') is not None:
            for k1 in m.get('PackageStates'):
                temp_model = main_models.ListInstancePackageStatesResponseBodyPackageStates()
                self.package_states.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstancePackageStatesResponseBodyPackageStates(DaraModel):
    def __init__(
        self,
        configuration_info: str = None,
        description: str = None,
        parameters: str = None,
        publisher: str = None,
        template_category: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        template_version_name: str = None,
        update_time: str = None,
    ):
        self.configuration_info = configuration_info
        # Description
        self.description = description
        # Parameters
        self.parameters = parameters
        # Publisher
        self.publisher = publisher
        # Template type
        self.template_category = template_category
        # Template ID
        self.template_id = template_id
        # Template name.
        self.template_name = template_name
        # Template version number
        self.template_version = template_version
        # Template version name
        self.template_version_name = template_version_name
        # Update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_info is not None:
            result['ConfigurationInfo'] = self.configuration_info

        if self.description is not None:
            result['Description'] = self.description

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.publisher is not None:
            result['Publisher'] = self.publisher

        if self.template_category is not None:
            result['TemplateCategory'] = self.template_category

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.template_version_name is not None:
            result['TemplateVersionName'] = self.template_version_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationInfo') is not None:
            self.configuration_info = m.get('ConfigurationInfo')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Publisher') is not None:
            self.publisher = m.get('Publisher')

        if m.get('TemplateCategory') is not None:
            self.template_category = m.get('TemplateCategory')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('TemplateVersionName') is not None:
            self.template_version_name = m.get('TemplateVersionName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

