# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRumAppRequest(DaraModel):
    def __init__(
        self,
        app_config: str = None,
        auto_restart: bool = None,
        backend_service_trace_region: str = None,
        bonree_sdkconfig_json: str = None,
        description: str = None,
        is_subscribe: bool = None,
        nickname: str = None,
        pid: str = None,
        real_region_id: str = None,
        region_id: str = None,
        restart: bool = None,
        service_domain_operation_json: str = None,
        stop: bool = None,
        web_sdkconfig_json: str = None,
    ):
        # The application configurations in the JSON format. This parameter is deprecated.
        self.app_config = app_config
        # Specifies whether to restart the application the next day. Valid values: true and false.
        self.auto_restart = auto_restart
        # The region where the backend application is deployed. This parameter is used in end-to-end tracing scenarios.
        self.backend_service_trace_region = backend_service_trace_region
        # The collection configurations of the mobile SDK. You can enable or disable collection configurations based on the app version.
        self.bonree_sdkconfig_json = bonree_sdkconfig_json
        # The description of the application.
        self.description = description
        # Specifies whether you want to subscribe to the application. Valid values: true and false.
        self.is_subscribe = is_subscribe
        # The alias of the application.
        self.nickname = nickname
        # The application ID.
        # 
        # This parameter is required.
        self.pid = pid
        # The region where the application resides. You can leave this parameter empty or set it to China East 2 Finance.
        self.real_region_id = real_region_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to restart the application. Valid values: true and false.
        self.restart = restart
        # The service domain name of the application. You can create, modify, and delete service domain name configurations.
        self.service_domain_operation_json = service_domain_operation_json
        # Specifies whether to stop the application. Valid values: true and false.
        self.stop = stop
        self.web_sdkconfig_json = web_sdkconfig_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_config is not None:
            result['AppConfig'] = self.app_config

        if self.auto_restart is not None:
            result['AutoRestart'] = self.auto_restart

        if self.backend_service_trace_region is not None:
            result['BackendServiceTraceRegion'] = self.backend_service_trace_region

        if self.bonree_sdkconfig_json is not None:
            result['BonreeSDKConfigJson'] = self.bonree_sdkconfig_json

        if self.description is not None:
            result['Description'] = self.description

        if self.is_subscribe is not None:
            result['IsSubscribe'] = self.is_subscribe

        if self.nickname is not None:
            result['Nickname'] = self.nickname

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.real_region_id is not None:
            result['RealRegionId'] = self.real_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.restart is not None:
            result['Restart'] = self.restart

        if self.service_domain_operation_json is not None:
            result['ServiceDomainOperationJson'] = self.service_domain_operation_json

        if self.stop is not None:
            result['Stop'] = self.stop

        if self.web_sdkconfig_json is not None:
            result['WebSDKConfigJson'] = self.web_sdkconfig_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConfig') is not None:
            self.app_config = m.get('AppConfig')

        if m.get('AutoRestart') is not None:
            self.auto_restart = m.get('AutoRestart')

        if m.get('BackendServiceTraceRegion') is not None:
            self.backend_service_trace_region = m.get('BackendServiceTraceRegion')

        if m.get('BonreeSDKConfigJson') is not None:
            self.bonree_sdkconfig_json = m.get('BonreeSDKConfigJson')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsSubscribe') is not None:
            self.is_subscribe = m.get('IsSubscribe')

        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RealRegionId') is not None:
            self.real_region_id = m.get('RealRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('ServiceDomainOperationJson') is not None:
            self.service_domain_operation_json = m.get('ServiceDomainOperationJson')

        if m.get('Stop') is not None:
            self.stop = m.get('Stop')

        if m.get('WebSDKConfigJson') is not None:
            self.web_sdkconfig_json = m.get('WebSDKConfigJson')

        return self

