# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataConnectorRequest(DaraModel):
    def __init__(
        self,
        auth_config_id: str = None,
        auth_config_product: str = None,
        auth_config_vendor: str = None,
        data_connector_config: str = None,
        data_connector_id: str = None,
        data_connector_status: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The configuration item ID of the collector access object in the multi-cloud configuration.
        self.auth_config_id = auth_config_id
        # The cloud service to which the authentication configuration belongs.
        self.auth_config_product = auth_config_product
        # The authentication vendor name.
        self.auth_config_vendor = auth_config_vendor
        # The configuration information of the collector.
        self.data_connector_config = data_connector_config
        # The collector ID.
        # 
        # This parameter is required.
        self.data_connector_id = data_connector_id
        # The status of the collector. Valid values:
        # - enabled: enabled.
        # - disabled: disabled.
        self.data_connector_status = data_connector_status
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The data management center of the threat analysis feature. Specify this parameter based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Your assets belong to the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Your assets belong to regions outside China.
        self.region_id = region_id
        # The ID of the member account that the administrator switches to.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config_id is not None:
            result['AuthConfigId'] = self.auth_config_id

        if self.auth_config_product is not None:
            result['AuthConfigProduct'] = self.auth_config_product

        if self.auth_config_vendor is not None:
            result['AuthConfigVendor'] = self.auth_config_vendor

        if self.data_connector_config is not None:
            result['DataConnectorConfig'] = self.data_connector_config

        if self.data_connector_id is not None:
            result['DataConnectorId'] = self.data_connector_id

        if self.data_connector_status is not None:
            result['DataConnectorStatus'] = self.data_connector_status

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConfigId') is not None:
            self.auth_config_id = m.get('AuthConfigId')

        if m.get('AuthConfigProduct') is not None:
            self.auth_config_product = m.get('AuthConfigProduct')

        if m.get('AuthConfigVendor') is not None:
            self.auth_config_vendor = m.get('AuthConfigVendor')

        if m.get('DataConnectorConfig') is not None:
            self.data_connector_config = m.get('DataConnectorConfig')

        if m.get('DataConnectorId') is not None:
            self.data_connector_id = m.get('DataConnectorId')

        if m.get('DataConnectorStatus') is not None:
            self.data_connector_status = m.get('DataConnectorStatus')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

