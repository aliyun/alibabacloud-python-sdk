# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ListApplicationGroupsResponseBody(DaraModel):
    def __init__(
        self,
        application_groups: List[main_models.ListApplicationGroupsResponseBodyApplicationGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of the application group.
        self.application_groups = application_groups
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_groups:
            for v1 in self.application_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationGroups'] = []
        if self.application_groups is not None:
            for k1 in self.application_groups:
                result['ApplicationGroups'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_groups = []
        if m.get('ApplicationGroups') is not None:
            for k1 in m.get('ApplicationGroups'):
                temp_model = main_models.ListApplicationGroupsResponseBodyApplicationGroups()
                self.application_groups.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListApplicationGroupsResponseBodyApplicationGroups(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        cms_group_id: str = None,
        create_date: str = None,
        deploy_parameters: str = None,
        deploy_region_id: str = None,
        deployed_revision_ids: str = None,
        description: str = None,
        error_detail: str = None,
        error_type: str = None,
        execution_id: str = None,
        import_tag_key: str = None,
        import_tag_value: str = None,
        name: str = None,
        status: str = None,
        status_reason: str = None,
        update_date: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id
        # The time when the application group was created.
        self.create_date = create_date
        # The configuration information of the application group.
        self.deploy_parameters = deploy_parameters
        # The ID of the region in which the related resources reside.
        self.deploy_region_id = deploy_region_id
        self.deployed_revision_ids = deployed_revision_ids
        # The description of the application group.
        self.description = description
        self.error_detail = error_detail
        self.error_type = error_type
        self.execution_id = execution_id
        # The tag key.
        self.import_tag_key = import_tag_key
        # The tag value.
        self.import_tag_value = import_tag_value
        # The name of the application group.
        self.name = name
        # The state of the application group.
        self.status = status
        # The state information of the application group.
        self.status_reason = status_reason
        # The time when the application group was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters

        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id

        if self.deployed_revision_ids is not None:
            result['DeployedRevisionIds'] = self.deployed_revision_ids

        if self.description is not None:
            result['Description'] = self.description

        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail

        if self.error_type is not None:
            result['ErrorType'] = self.error_type

        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key

        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')

        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')

        if m.get('DeployedRevisionIds') is not None:
            self.deployed_revision_ids = m.get('DeployedRevisionIds')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')

        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')

        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')

        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

