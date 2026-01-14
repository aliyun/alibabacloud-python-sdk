# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateLogStoreConfigRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_log_record_customized_header_list: List[str] = None,
        access_log_record_customized_headers_enabled: bool = None,
        client_token: str = None,
        endpoint_group_id: str = None,
        listener_id: str = None,
        region_id: str = None,
        sls_log_store_name: str = None,
        sls_project_name: str = None,
    ):
        # This parameter is required.
        self.accelerator_id = accelerator_id
        self.access_log_record_customized_header_list = access_log_record_customized_header_list
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        self.client_token = client_token
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # This parameter is required.
        self.listener_id = listener_id
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.sls_log_store_name = sls_log_store_name
        # This parameter is required.
        self.sls_project_name = sls_project_name

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

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name

        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name

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

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')

        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')

        return self

