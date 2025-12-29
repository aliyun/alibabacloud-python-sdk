# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class GetAirflowResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        root: main_models.GetAirflowResponseBodyRoot = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.error_code = error_code
        self.http_status_code = http_status_code
        self.message = message
        # Reuqest ID。
        self.request_id = request_id
        self.root = root
        self.success = success

    def validate(self):
        if self.root:
            self.root.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root is not None:
            result['Root'] = self.root.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Root') is not None:
            temp_model = main_models.GetAirflowResponseBodyRoot()
            self.root = temp_model.from_map(m.get('Root'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAirflowResponseBodyRoot(DaraModel):
    def __init__(
        self,
        airflow_id: str = None,
        airflow_name: str = None,
        app_spec: str = None,
        app_type: str = None,
        custom_airflow_cfg: List[str] = None,
        dags_dir: str = None,
        deploy_error_msg: str = None,
        description: str = None,
        gmt_created: str = None,
        oss_bucket_name: str = None,
        oss_path: str = None,
        plugins_dir: str = None,
        region_id: str = None,
        requirement_file: str = None,
        security_group_id: str = None,
        startup_file: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        self.airflow_id = airflow_id
        self.airflow_name = airflow_name
        self.app_spec = app_spec
        self.app_type = app_type
        self.custom_airflow_cfg = custom_airflow_cfg
        self.dags_dir = dags_dir
        self.deploy_error_msg = deploy_error_msg
        self.description = description
        self.gmt_created = gmt_created
        self.oss_bucket_name = oss_bucket_name
        self.oss_path = oss_path
        self.plugins_dir = plugins_dir
        self.region_id = region_id
        self.requirement_file = requirement_file
        self.security_group_id = security_group_id
        self.startup_file = startup_file
        self.status = status
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id
        self.worker_serverless_replicas = worker_serverless_replicas
        self.workspace_id = workspace_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airflow_id is not None:
            result['AirflowId'] = self.airflow_id

        if self.airflow_name is not None:
            result['AirflowName'] = self.airflow_name

        if self.app_spec is not None:
            result['AppSpec'] = self.app_spec

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.custom_airflow_cfg is not None:
            result['CustomAirflowCfg'] = self.custom_airflow_cfg

        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir

        if self.deploy_error_msg is not None:
            result['DeployErrorMsg'] = self.deploy_error_msg

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.worker_serverless_replicas is not None:
            result['WorkerServerlessReplicas'] = self.worker_serverless_replicas

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AirflowId') is not None:
            self.airflow_id = m.get('AirflowId')

        if m.get('AirflowName') is not None:
            self.airflow_name = m.get('AirflowName')

        if m.get('AppSpec') is not None:
            self.app_spec = m.get('AppSpec')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CustomAirflowCfg') is not None:
            self.custom_airflow_cfg = m.get('CustomAirflowCfg')

        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')

        if m.get('DeployErrorMsg') is not None:
            self.deploy_error_msg = m.get('DeployErrorMsg')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WorkerServerlessReplicas') is not None:
            self.worker_serverless_replicas = m.get('WorkerServerlessReplicas')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

