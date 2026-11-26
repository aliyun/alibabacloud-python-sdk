# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class CreateAirflowRequest(DaraModel):
    def __init__(
        self,
        airflow_name: str = None,
        airflow_version: str = None,
        app_spec: str = None,
        client_token: str = None,
        dags_dir: str = None,
        data_mount_info_list: List[main_models.DataMountInfo] = None,
        description: str = None,
        enable_lineage: bool = None,
        enable_serverless: bool = None,
        graceful_shutdown_timeout: int = None,
        lineage_replicas: int = None,
        lineage_spec: str = None,
        oss_bucket_name: str = None,
        oss_path: str = None,
        plugins_dir: str = None,
        requirement_file: str = None,
        security_group_id: str = None,
        startup_file: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        worker_serverless_replicas: int = None,
        workspace_id: str = None,
        zone_id: str = None,
    ):
        # The name of the Airflow instance.
        # 
        # This parameter is required.
        self.airflow_name = airflow_name
        # The Airflow version. Valid values: "3.2.2", "3.1.0", "2.10.4", and "3.0.6".
        self.airflow_version = airflow_version
        # The specification of the Airflow instance. Valid values: **SMALL**, **MEDIUM**, **LARGE**, **XLARGE**, and **X2LARGE**.
        # 
        # This parameter is required.
        self.app_spec = app_spec
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The directory scanned by Airflow for DAGs.
        self.dags_dir = dags_dir
        # The list of data mount information.
        self.data_mount_info_list = data_mount_info_list
        # The description of the Airflow instance.
        self.description = description
        # Specifies whether to enable data lineage. For Airflow 2.x, this feature is always disabled, and the lineage specification and number of replicas are ignored.
        self.enable_lineage = enable_lineage
        # Specifies whether to enable elasticity for workers.
        self.enable_serverless = enable_serverless
        # The timeout period for a worker to gracefully shut down.
        self.graceful_shutdown_timeout = graceful_shutdown_timeout
        # The number of replicas for the lineage service. The default value is 1 when enabled. If omitted during an update, the original value is retained.
        self.lineage_replicas = lineage_replicas
        # The specification of the lineage service. It uses the same tier as the Airflow instance specification.
        self.lineage_spec = lineage_spec
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.oss_bucket_name = oss_bucket_name
        # The OSS path for storing logs.
        # 
        # This parameter is required.
        self.oss_path = oss_path
        # The directory scanned by the Airflow instance for plugins.
        self.plugins_dir = plugins_dir
        # The path to the installation package.
        self.requirement_file = requirement_file
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The startup script for the Airflow container.
        self.startup_file = startup_file
        # The ID of the vSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The number of worker node extensions.
        # 
        # This parameter is required.
        self.worker_serverless_replicas = worker_serverless_replicas
        # The DMS workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id
        # The zone ID in the region.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dags_dir is not None:
            result['DagsDir'] = self.dags_dir

        result['DataMountInfoList'] = []
        if self.data_mount_info_list is not None:
            for k1 in self.data_mount_info_list:
                result['DataMountInfoList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_lineage is not None:
            result['EnableLineage'] = self.enable_lineage

        if self.enable_serverless is not None:
            result['EnableServerless'] = self.enable_serverless

        if self.graceful_shutdown_timeout is not None:
            result['GracefulShutdownTimeout'] = self.graceful_shutdown_timeout

        if self.lineage_replicas is not None:
            result['LineageReplicas'] = self.lineage_replicas

        if self.lineage_spec is not None:
            result['LineageSpec'] = self.lineage_spec

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_path is not None:
            result['OssPath'] = self.oss_path

        if self.plugins_dir is not None:
            result['PluginsDir'] = self.plugins_dir

        if self.requirement_file is not None:
            result['RequirementFile'] = self.requirement_file

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.startup_file is not None:
            result['StartupFile'] = self.startup_file

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DagsDir') is not None:
            self.dags_dir = m.get('DagsDir')

        self.data_mount_info_list = []
        if m.get('DataMountInfoList') is not None:
            for k1 in m.get('DataMountInfoList'):
                temp_model = main_models.DataMountInfo()
                self.data_mount_info_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableLineage') is not None:
            self.enable_lineage = m.get('EnableLineage')

        if m.get('EnableServerless') is not None:
            self.enable_serverless = m.get('EnableServerless')

        if m.get('GracefulShutdownTimeout') is not None:
            self.graceful_shutdown_timeout = m.get('GracefulShutdownTimeout')

        if m.get('LineageReplicas') is not None:
            self.lineage_replicas = m.get('LineageReplicas')

        if m.get('LineageSpec') is not None:
            self.lineage_spec = m.get('LineageSpec')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')

        if m.get('PluginsDir') is not None:
            self.plugins_dir = m.get('PluginsDir')

        if m.get('RequirementFile') is not None:
            self.requirement_file = m.get('RequirementFile')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('StartupFile') is not None:
            self.startup_file = m.get('StartupFile')

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

