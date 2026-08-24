# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetConnectorResponseBody(DaraModel):
    def __init__(
        self,
        connector: main_models.GetConnectorResponseBodyConnector = None,
        request_id: str = None,
    ):
        # Connector。
        self.connector = connector
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.connector:
            self.connector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector is not None:
            result['Connector'] = self.connector.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connector') is not None:
            temp_model = main_models.GetConnectorResponseBodyConnector()
            self.connector = temp_model.from_map(m.get('Connector'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetConnectorResponseBodyConnector(DaraModel):
    def __init__(
        self,
        connector_id: str = None,
        create_time: str = None,
        name: str = None,
        region_id: str = None,
        status: str = None,
        switch_status: str = None,
        upgrade_time: main_models.GetConnectorResponseBodyConnectorUpgradeTime = None,
        vip_cidr: str = None,
    ):
        # ConnectorID。
        self.connector_id = connector_id
        # The connector creation time.
        self.create_time = create_time
        # The connector name.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The connector connection status. Valid values:
        # - **Online**: Online.
        # - **Offline**: Offline.
        self.status = status
        # The connector instance status. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.switch_status = switch_status
        # The connector upgrade time.
        self.upgrade_time = upgrade_time
        # The virtual IP address range.
        self.vip_cidr = vip_cidr

    def validate(self):
        if self.upgrade_time:
            self.upgrade_time.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        if self.upgrade_time is not None:
            result['UpgradeTime'] = self.upgrade_time.to_map()

        if self.vip_cidr is not None:
            result['VipCidr'] = self.vip_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        if m.get('UpgradeTime') is not None:
            temp_model = main_models.GetConnectorResponseBodyConnectorUpgradeTime()
            self.upgrade_time = temp_model.from_map(m.get('UpgradeTime'))

        if m.get('VipCidr') is not None:
            self.vip_cidr = m.get('VipCidr')

        return self

class GetConnectorResponseBodyConnectorUpgradeTime(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The end time.
        self.end = end
        # The start time.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

