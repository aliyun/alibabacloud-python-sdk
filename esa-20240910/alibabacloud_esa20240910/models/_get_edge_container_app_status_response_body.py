# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetEdgeContainerAppStatusResponseBody(DaraModel):
    def __init__(
        self,
        app_status: main_models.GetEdgeContainerAppStatusResponseBodyAppStatus = None,
        request_id: str = None,
    ):
        # The status of the application.
        self.app_status = app_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.app_status:
            self.app_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_status is not None:
            result['AppStatus'] = self.app_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppStatus') is not None:
            temp_model = main_models.GetEdgeContainerAppStatusResponseBodyAppStatus()
            self.app_status = temp_model.from_map(m.get('AppStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEdgeContainerAppStatusResponseBodyAppStatus(DaraModel):
    def __init__(
        self,
        base_line_version: str = None,
        deploy_status: str = None,
        deploy_time: str = None,
        deployed_version: str = None,
        expect_percentage: int = None,
        full_release: bool = None,
        publish_env: str = None,
        publish_percentage: int = None,
        publish_status: str = None,
        publish_time: str = None,
        publish_type: str = None,
        publishing_version: str = None,
        regions: main_models.GetEdgeContainerAppStatusResponseBodyAppStatusRegions = None,
        rollback_time: str = None,
        un_deploy_time: str = None,
    ):
        # The base version of the application.
        self.base_line_version = base_line_version
        # The deployment status of the application.
        # 
        # *   **undeploy**: The application is not deployed.
        # *   **deploying**: The application is being deployed.
        # *   **deployed**: The application is deployed.
        # *   **undeploying**: The deployment is being canceled.
        self.deploy_status = deploy_status
        # The time when the application was deployed. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.deploy_time = deploy_time
        # The release version of the application.
        self.deployed_version = deployed_version
        # The expected release percentage of the application.
        self.expect_percentage = expect_percentage
        # Specifies whether to fully release the version. This parameter takes effect only when PublishType is set to region.
        self.full_release = full_release
        # The environment to which the application was released. Valid values:
        # 
        # *   **prod**: the production environment.
        # *   **staging**: the staging environment.
        self.publish_env = publish_env
        # The release percentage of the application.
        self.publish_percentage = publish_percentage
        # The release status of the application. Valid values:
        # 
        # *   **publishing**
        # *   **published**
        # *   **rollbacking**
        # *   **rollbacked**
        self.publish_status = publish_status
        # The time when the application was released. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.publish_time = publish_time
        # Specifies how the version is released. Valid values:
        # 
        # *   percentage: releases the version by percentage.
        # *   region: releases the version by region.
        # 
        # If you do not specify this parameter, the version is released by percentage by default.
        self.publish_type = publish_type
        # The release version of the application.
        self.publishing_version = publishing_version
        # The regions to which the version is released.
        self.regions = regions
        # The time when the last rollback was performed.
        self.rollback_time = rollback_time
        # The time when the application deployment was canceled. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.un_deploy_time = un_deploy_time

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_line_version is not None:
            result['BaseLineVersion'] = self.base_line_version

        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status

        if self.deploy_time is not None:
            result['DeployTime'] = self.deploy_time

        if self.deployed_version is not None:
            result['DeployedVersion'] = self.deployed_version

        if self.expect_percentage is not None:
            result['ExpectPercentage'] = self.expect_percentage

        if self.full_release is not None:
            result['FullRelease'] = self.full_release

        if self.publish_env is not None:
            result['PublishEnv'] = self.publish_env

        if self.publish_percentage is not None:
            result['PublishPercentage'] = self.publish_percentage

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.publishing_version is not None:
            result['PublishingVersion'] = self.publishing_version

        if self.regions is not None:
            result['Regions'] = self.regions.to_map()

        if self.rollback_time is not None:
            result['RollbackTime'] = self.rollback_time

        if self.un_deploy_time is not None:
            result['UnDeployTime'] = self.un_deploy_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseLineVersion') is not None:
            self.base_line_version = m.get('BaseLineVersion')

        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')

        if m.get('DeployTime') is not None:
            self.deploy_time = m.get('DeployTime')

        if m.get('DeployedVersion') is not None:
            self.deployed_version = m.get('DeployedVersion')

        if m.get('ExpectPercentage') is not None:
            self.expect_percentage = m.get('ExpectPercentage')

        if m.get('FullRelease') is not None:
            self.full_release = m.get('FullRelease')

        if m.get('PublishEnv') is not None:
            self.publish_env = m.get('PublishEnv')

        if m.get('PublishPercentage') is not None:
            self.publish_percentage = m.get('PublishPercentage')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('PublishingVersion') is not None:
            self.publishing_version = m.get('PublishingVersion')

        if m.get('Regions') is not None:
            temp_model = main_models.GetEdgeContainerAppStatusResponseBodyAppStatusRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        if m.get('RollbackTime') is not None:
            self.rollback_time = m.get('RollbackTime')

        if m.get('UnDeployTime') is not None:
            self.un_deploy_time = m.get('UnDeployTime')

        return self

class GetEdgeContainerAppStatusResponseBodyAppStatusRegions(DaraModel):
    def __init__(
        self,
        region: List[str] = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

