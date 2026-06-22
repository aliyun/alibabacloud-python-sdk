# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListApplicationsResponseBodyApplications] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The applications.
        self.applications = applications
        # The number of entries per page.
        self.max_results = max_results
        # The page number of the next page returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of pages.
        self.total_count = total_count

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

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
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationsResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        application_state: str = None,
        application_version: str = None,
        community_version: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The status of the applications. Valid values:
        # 
        # *   STOPPED: At least one application is in the Stopped state.
        # *   RUNNING: All applications are in the Running state.
        # 
        # This parameter is returned only for DataLake, OLAP, Dataflow, DataServing, and custom clusters. For other types of clusters, no value is returned for this parameter.
        self.application_state = application_state
        # The version of the application.
        self.application_version = application_version
        # The community edition.
        self.community_version = community_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.application_state is not None:
            result['ApplicationState'] = self.application_state

        if self.application_version is not None:
            result['ApplicationVersion'] = self.application_version

        if self.community_version is not None:
            result['CommunityVersion'] = self.community_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ApplicationState') is not None:
            self.application_state = m.get('ApplicationState')

        if m.get('ApplicationVersion') is not None:
            self.application_version = m.get('ApplicationVersion')

        if m.get('CommunityVersion') is not None:
            self.community_version = m.get('CommunityVersion')

        return self

