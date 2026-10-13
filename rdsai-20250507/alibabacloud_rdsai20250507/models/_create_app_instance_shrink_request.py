# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        client_token: str = None,
        components_shrink: str = None,
        dbinstance_config_shrink: str = None,
        dbinstance_name: str = None,
        dashboard_password: str = None,
        dashboard_username: str = None,
        database: str = None,
        database_password: str = None,
        initialize_with_existing_data: bool = None,
        instance_class: str = None,
        public_endpoint_enabled: bool = None,
        public_network_access_enabled: bool = None,
        ragenabled: bool = None,
        region_id: str = None,
        v_switch_id: str = None,
    ):
        # The name of the AI application to create.
        self.app_name = app_name
        # The application type. Currently, only **supabase** is supported.
        self.app_type = app_type
        # The client token that is used to ensure the idempotence of the request. The client generates the value of this parameter to prevent duplicate requests from being submitted.
        self.client_token = client_token
        # The list of components.
        self.components_shrink = components_shrink
        # The database instance configuration.
        self.dbinstance_config_shrink = dbinstance_config_shrink
        # The instance ID of the RDS PostgreSQL database instance to which the AI application connects.
        # 
        # <notice>Only **newly purchased empty RDS PostgreSQL instances** are supported. The major engine version must be **17**, and the minor engine version must be **20250630 or later**.
        self.dbinstance_name = dbinstance_name
        # The password for the Supabase Dashboard.
        # 
        # The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and underscores (_).
        self.dashboard_password = dashboard_password
        # The username for the Supabase Dashboard.
        self.dashboard_username = dashboard_username
        # The database name.
        self.database = database
        # The password for accessing the RDS database.
        # 
        # The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and underscores (_).
        self.database_password = database_password
        # Specifies whether to restore from existing PostgreSQL data. Valid values:
        # 
        # - true: restores from existing data.
        # 
        # - false (default): does not restore from existing data.
        self.initialize_with_existing_data = initialize_with_existing_data
        # The instance type. Currently, only **rdsai.supabase.basic** is supported.
        self.instance_class = instance_class
        # Specifies whether to enable the public network connection endpoint. Valid values:
        # 
        # - true (default): Enabled.
        # 
        # - false: Disabled.
        self.public_endpoint_enabled = public_endpoint_enabled
        # Specifies whether to enable the Internet NAT gateway. Valid values:
        # 
        # - **true**: enables the Internet NAT gateway.
        # - **false** (default): does not enable the Internet NAT gateway.
        # 
        # >Notice: If an Internet NAT gateway is already enabled for the vSwitch specified by the **VSwitchId** parameter settings, set this parameter to **false**.
        self.public_network_access_enabled = public_network_access_enabled
        # Reserved parameter.
        self.ragenabled = ragenabled
        # The region ID.
        self.region_id = region_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.components_shrink is not None:
            result['Components'] = self.components_shrink

        if self.dbinstance_config_shrink is not None:
            result['DBInstanceConfig'] = self.dbinstance_config_shrink

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password

        if self.dashboard_username is not None:
            result['DashboardUsername'] = self.dashboard_username

        if self.database is not None:
            result['Database'] = self.database

        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password

        if self.initialize_with_existing_data is not None:
            result['InitializeWithExistingData'] = self.initialize_with_existing_data

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.public_endpoint_enabled is not None:
            result['PublicEndpointEnabled'] = self.public_endpoint_enabled

        if self.public_network_access_enabled is not None:
            result['PublicNetworkAccessEnabled'] = self.public_network_access_enabled

        if self.ragenabled is not None:
            result['RAGEnabled'] = self.ragenabled

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')

        if m.get('DBInstanceConfig') is not None:
            self.dbinstance_config_shrink = m.get('DBInstanceConfig')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')

        if m.get('DashboardUsername') is not None:
            self.dashboard_username = m.get('DashboardUsername')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')

        if m.get('InitializeWithExistingData') is not None:
            self.initialize_with_existing_data = m.get('InitializeWithExistingData')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('PublicEndpointEnabled') is not None:
            self.public_endpoint_enabled = m.get('PublicEndpointEnabled')

        if m.get('PublicNetworkAccessEnabled') is not None:
            self.public_network_access_enabled = m.get('PublicNetworkAccessEnabled')

        if m.get('RAGEnabled') is not None:
            self.ragenabled = m.get('RAGEnabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

