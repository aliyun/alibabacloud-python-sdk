# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCrossProjectPipelineRunsRequest(DaraModel):
    def __init__(
        self,
        create_time_from: int = None,
        create_time_to: int = None,
        creator: str = None,
        deployment_environment_id: int = None,
        executor: str = None,
        object_id: str = None,
        object_type: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        status: str = None,
    ):
        # The start of the creation time range. This value is a UNIX timestamp in milliseconds.
        self.create_time_from = create_time_from
        # The end of the creation time range. This value is a UNIX timestamp in milliseconds.
        self.create_time_to = create_time_to
        # The creator.
        self.creator = creator
        # The cross-workspace publish environment ID.
        self.deployment_environment_id = deployment_environment_id
        # The executor.
        self.executor = executor
        # The publish object ID.
        self.object_id = object_id
        # The publish object type.
        self.object_type = object_type
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The publish flow status. Valid values:
        # - Building: Building.
        # - Ready: Ready and waiting for execution.
        # - Running: Running.
        # - Termination: Terminated.
        # - Success: Succeeded.
        # - Fail: Failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time_from is not None:
            result['CreateTimeFrom'] = self.create_time_from

        if self.create_time_to is not None:
            result['CreateTimeTo'] = self.create_time_to

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.deployment_environment_id is not None:
            result['DeploymentEnvironmentId'] = self.deployment_environment_id

        if self.executor is not None:
            result['Executor'] = self.executor

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimeFrom') is not None:
            self.create_time_from = m.get('CreateTimeFrom')

        if m.get('CreateTimeTo') is not None:
            self.create_time_to = m.get('CreateTimeTo')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeploymentEnvironmentId') is not None:
            self.deployment_environment_id = m.get('DeploymentEnvironmentId')

        if m.get('Executor') is not None:
            self.executor = m.get('Executor')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

