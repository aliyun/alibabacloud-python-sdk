# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DataAgentApplication(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        app_name: str = None,
        app_url: str = None,
        application_extra_info: str = None,
        application_revision: int = None,
        availability_error_code: str = None,
        availability_error_message: str = None,
        creator_name: str = None,
        creator_uid: str = None,
        description: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        last_request: main_models.DataAgentApplicationLastRequest = None,
        main_uid: str = None,
        observation_stale: bool = None,
        ready: bool = None,
        region: str = None,
        session_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        workspace_id: str = None,
    ):
        # The ID of the currently associated Data Agent.
        self.agent_id = agent_id
        # The stable identifier of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The access URL of the application. This URL is generated and returned as-is by RM when the deployment snapshot ready=true, and is not filtered again based on Status or ObservationStale. If not provided, this parameter is empty or omitted.
        self.app_url = app_url
        # The extended information of the application.
        self.application_extra_info = application_extra_info
        # The control revision number of the application. The initial value is 0. This number increments after a control request is accepted and can be passed as ExpectedRevision.
        self.application_revision = application_revision
        # The error code for the current service unavailability, which is expressed separately from the error code of the most recent control request. If no error occurs, this parameter is empty.
        self.availability_error_code = availability_error_code
        # The summary of the cause for the current service unavailability. If no error occurs, this parameter is empty.
        self.availability_error_message = availability_error_message
        # The name of the application creator.
        self.creator_name = creator_name
        # The UID of the application owner.
        self.creator_uid = creator_uid
        # The description of the application, which can be up to 250 characters in length.
        self.description = description
        # The time when the application was created.
        self.gmt_created = gmt_created
        # The time when the application was last modified.
        self.gmt_modified = gmt_modified
        # The most recent user control request. If no control request has been made, this parameter is empty.
        self.last_request = last_request
        # The UID of the Alibaba Cloud account.
        self.main_uid = main_uid
        # Specifies whether the runtime or service observation is missing or stale. If this parameter is set to true, the availability information may be outdated.
        self.observation_stale = observation_stale
        # Specifies whether the current platform service is available. This does not indicate whether the most recent control request succeeded or whether the business components are healthy.
        self.ready = ready
        # The region.
        self.region = region
        # The ID of the current or most recently associated session.
        self.session_id = session_id
        # The status of the application. Valid values:
        # - REGISTERED
        # - PREPARING
        # - WAITING_AGREEMENT: Indicates that the system is waiting for the owner of the target workspace to sign a valid agreement. The original deployment or restart request is still being executed. After the agreement is signed, RM automatically resumes the original request.
        # - SEALING
        # - REVIEWING
        # - DEPLOYING
        # - DEPLOYED
        # - DEPLOY_FAILED
        # - STOPPING
        # - STOPPED
        # - STOP_FAILED
        # - RECOVERING
        # - UNAVAILABLE
        # - DELETING
        # - DELETE_FAILED
        # - DELETED: The logical deletion terminal state. The application no longer appears in List or Describe operations.
        self.status = status
        # The ID of the vSwitch used for the actual deployment of the currently running application. If no resources are currently running, this parameter is empty.
        self.v_switch_id = v_switch_id
        # The ID of the VPC used for the actual deployment of the currently running application. If no resources are currently running, this parameter is empty.
        self.vpc_id = vpc_id
        # The ID of the workspace.
        self.workspace_id = workspace_id

    def validate(self):
        if self.last_request:
            self.last_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_url is not None:
            result['AppUrl'] = self.app_url

        if self.application_extra_info is not None:
            result['ApplicationExtraInfo'] = self.application_extra_info

        if self.application_revision is not None:
            result['ApplicationRevision'] = self.application_revision

        if self.availability_error_code is not None:
            result['AvailabilityErrorCode'] = self.availability_error_code

        if self.availability_error_message is not None:
            result['AvailabilityErrorMessage'] = self.availability_error_message

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.creator_uid is not None:
            result['CreatorUid'] = self.creator_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.last_request is not None:
            result['LastRequest'] = self.last_request.to_map()

        if self.main_uid is not None:
            result['MainUid'] = self.main_uid

        if self.observation_stale is not None:
            result['ObservationStale'] = self.observation_stale

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.region is not None:
            result['Region'] = self.region

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppUrl') is not None:
            self.app_url = m.get('AppUrl')

        if m.get('ApplicationExtraInfo') is not None:
            self.application_extra_info = m.get('ApplicationExtraInfo')

        if m.get('ApplicationRevision') is not None:
            self.application_revision = m.get('ApplicationRevision')

        if m.get('AvailabilityErrorCode') is not None:
            self.availability_error_code = m.get('AvailabilityErrorCode')

        if m.get('AvailabilityErrorMessage') is not None:
            self.availability_error_message = m.get('AvailabilityErrorMessage')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('CreatorUid') is not None:
            self.creator_uid = m.get('CreatorUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LastRequest') is not None:
            temp_model = main_models.DataAgentApplicationLastRequest()
            self.last_request = temp_model.from_map(m.get('LastRequest'))

        if m.get('MainUid') is not None:
            self.main_uid = m.get('MainUid')

        if m.get('ObservationStale') is not None:
            self.observation_stale = m.get('ObservationStale')

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class DataAgentApplicationLastRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The control action. Valid values:
        # - DEPLOY
        # - STOP
        # - RESTART
        # - DELETE
        self.action = action
        # The error code for the failure of the most recent user control request. If no error occurs, this parameter is empty.
        self.error_code = error_code
        # The summary of the failure cause for the most recent user control request. If no error occurs, this parameter is empty.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

