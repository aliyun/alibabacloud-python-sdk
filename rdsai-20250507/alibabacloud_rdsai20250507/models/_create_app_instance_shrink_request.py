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
        dbinstance_config_shrink: str = None,
        dbinstance_name: str = None,
        dashboard_password: str = None,
        dashboard_username: str = None,
        database_password: str = None,
        instance_class: str = None,
        public_endpoint_enabled: bool = None,
        public_network_access_enabled: bool = None,
        ragenabled: bool = None,
        region_id: str = None,
        v_switch_id: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.client_token = client_token
        self.dbinstance_config_shrink = dbinstance_config_shrink
        self.dbinstance_name = dbinstance_name
        self.dashboard_password = dashboard_password
        self.dashboard_username = dashboard_username
        self.database_password = database_password
        self.instance_class = instance_class
        self.public_endpoint_enabled = public_endpoint_enabled
        self.public_network_access_enabled = public_network_access_enabled
        self.ragenabled = ragenabled
        self.region_id = region_id
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

        if self.dbinstance_config_shrink is not None:
            result['DBInstanceConfig'] = self.dbinstance_config_shrink

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password

        if self.dashboard_username is not None:
            result['DashboardUsername'] = self.dashboard_username

        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password

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

        if m.get('DBInstanceConfig') is not None:
            self.dbinstance_config_shrink = m.get('DBInstanceConfig')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')

        if m.get('DashboardUsername') is not None:
            self.dashboard_username = m.get('DashboardUsername')

        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')

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

