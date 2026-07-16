# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class UpdateAirflowResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        root: main_models.UpdateAirflowResponseBodyRoot = None,
        success: bool = None,
    ):
        # Details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.error_code = error_code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Details of the updated Airflow instance.
        self.root = root
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
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
            temp_model = main_models.UpdateAirflowResponseBodyRoot()
            self.root = temp_model.from_map(m.get('Root'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateAirflowResponseBodyRoot(DaraModel):
    def __init__(
        self,
        airflow_name: str = None,
        airflow_version: str = None,
        app_spec: str = None,
        app_type: str = None,
        custom_airflow_cfg: List[str] = None,
        dags_dir: str = None,
        data_mount_info_list: List[main_models.DataMountInfo] = None,
        deploy_error_msg: str = None,
        description: str = None,
        enable_serverless: bool = None,
        environments: str = None,
        gmt_created: str = None,
        graceful_shutdown_timeout: int = None,
        oss_bucket_name: str = None,
        oss_path: str = None,
        plugins_dir: str = None,
        requirement_file: str = None,
        requirements: str = None,
        security_group_id: str = None,
        startup_file: str = None,
        status: str = None,
        uuid: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        # The name of the Airflow instance.
        self.airflow_name = airflow_name
        # The version of Airflow.
        self.airflow_version = airflow_version
        # The instance specification.
        self.app_spec = app_spec
        # The instance type.
        self.app_type = app_type
        # A list of custom configuration items.
        self.custom_airflow_cfg = custom_airflow_cfg
        # The directory where DAGs are scanned.
        self.dags_dir = dags_dir
        # A data mount item.
        self.data_mount_info_list = data_mount_info_list
        # The error message returned upon deployment failure.
        self.deploy_error_msg = deploy_error_msg
        # The description of the Airflow instance.
        self.description = description
        # Indicates whether serverless mode is enabled.
        self.enable_serverless = enable_serverless
        # The environment variables.
        self.environments = environments
        # The time when the instance was created.
        self.gmt_created = gmt_created
        # The graceful shutdown timeout, in seconds.
        self.graceful_shutdown_timeout = graceful_shutdown_timeout
        # The name of the Object Storage Service (OSS) bucket.
        self.oss_bucket_name = oss_bucket_name
        # The path in OSS where logs are stored.
        self.oss_path = oss_path
        # The directory where Airflow plugins are scanned.
        self.plugins_dir = plugins_dir
        # The path to the Python requirements file.
        self.requirement_file = requirement_file
        # The Python package requirements.
        self.requirements = requirements
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The startup script for the Airflow container.
        self.startup_file = startup_file
        # The instance status.
        self.status = status
        # The Airflow instance ID.
        self.uuid = uuid
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The number of worker node replicas.
        self.worker_serverless_replicas = worker_serverless_replicas
        # The workspace ID.
        self.workspace_id = workspace_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.data_mount_info_list:
            for v1 in self.data_mount_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airflow_name is not None:
            result['AirflowName'] = self.airflow_name

        if self.airflow_version is not None:
            result['AirflowVersion'] = self.airflow_version

        if self.app_spec is not None:
            result['AppSpec'] = self.app_spec

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.custom_airflow_cfg is not None:
            result['CustomAirflowCfg'] = self.custom_airflow_cfg

        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir

        result['DataMountInfoList'] = []
        if self.data_mount_info_list is not None:
            for k1 in self.data_mount_info_list:
                result['DataMountInfoList'].append(k1.to_map() if k1 else None)

        if self.deploy_error_msg is not None:
            result['DeployErrorMsg'] = self.deploy_error_msg

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_serverless is not None:
            result['EnableServerless'] = self.enable_serverless

        if self.environments is not None:
            result['Environments'] = self.environments

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.graceful_shutdown_timeout is not None:
            result['GracefulShutdownTimeout'] = self.graceful_shutdown_timeout

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir

        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file

        if self.requirements is not None:
            result['Requirements'] = self.requirements

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

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
        if m.get('AirflowName') is not None:
            self.airflow_name = m.get('AirflowName')

        if m.get('AirflowVersion') is not None:
            self.airflow_version = m.get('AirflowVersion')

        if m.get('AppSpec') is not None:
            self.app_spec = m.get('AppSpec')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CustomAirflowCfg') is not None:
            self.custom_airflow_cfg = m.get('CustomAirflowCfg')

        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')

        self.data_mount_info_list = []
        if m.get('DataMountInfoList') is not None:
            for k1 in m.get('DataMountInfoList'):
                temp_model = main_models.DataMountInfo()
                self.data_mount_info_list.append(temp_model.from_map(k1))

        if m.get('DeployErrorMsg') is not None:
            self.deploy_error_msg = m.get('DeployErrorMsg')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableServerless') is not None:
            self.enable_serverless = m.get('EnableServerless')

        if m.get('Environments') is not None:
            self.environments = m.get('Environments')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GracefulShutdownTimeout') is not None:
            self.graceful_shutdown_timeout = m.get('GracefulShutdownTimeout')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')

        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')

        if m.get('Requirements') is not None:
            self.requirements = m.get('Requirements')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

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

