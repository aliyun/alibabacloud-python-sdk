# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AttachLogStoreToEndpointGroupRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_log_record_customized_header_list: List[str] = None,
        access_log_record_customized_headers_enabled: bool = None,
        client_token: str = None,
        endpoint_group_ids: List[str] = None,
        listener_id: str = None,
        region_id: str = None,
        sls_log_store_name: str = None,
        sls_project_name: str = None,
        sls_region_id: str = None,
    ):
        # The ID of the GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        self.access_log_record_customized_header_list = access_log_record_customized_header_list
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token
        # The IDs of the endpoint groups.
        # 
        # This parameter is required.
        self.endpoint_group_ids = endpoint_group_ids
        # The ID of the listener.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.sls_log_store_name = sls_log_store_name
        # The name of the Log Service project.
        # 
        # This parameter is required.
        self.sls_project_name = sls_project_name
        # The region ID of the Log Service project.
        # 
        # This parameter is required.
        self.sls_region_id = sls_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.access_log_record_customized_header_list is not None:
            result['AccessLogRecordCustomizedHeaderList'] = self.access_log_record_customized_header_list

        if self.access_log_record_customized_headers_enabled is not None:
            result['AccessLogRecordCustomizedHeadersEnabled'] = self.access_log_record_customized_headers_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.endpoint_group_ids is not None:
            result['EndpointGroupIds'] = self.endpoint_group_ids

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name

        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AccessLogRecordCustomizedHeaderList') is not None:
            self.access_log_record_customized_header_list = m.get('AccessLogRecordCustomizedHeaderList')

        if m.get('AccessLogRecordCustomizedHeadersEnabled') is not None:
            self.access_log_record_customized_headers_enabled = m.get('AccessLogRecordCustomizedHeadersEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EndpointGroupIds') is not None:
            self.endpoint_group_ids = m.get('EndpointGroupIds')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')

        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        return self

